#!/usr/bin/env python3
"""
LLM-as-a-Judge Feedback Evaluation Script

Evaluates narrative feedback quality using Claude as a judge across six dimensions:
Polarity, Factuality, Evidence, Actionability, Connectivity, and Developmental Alignment.

Copyright (c) 2025 The University of Texas Southwestern Medical Center.
All rights reserved.

This software is licensed for academic research use only.
Commercial use is expressly prohibited.
See LICENSE file for full terms and conditions.
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional

try:
    from anthropic import Anthropic
    from dotenv import load_dotenv
    from rich.console import Console
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich.table import Table
    from rich.text import Text
except ImportError:
    print("Error: Required packages not installed.")
    print("Please run: pip install -r requirements.txt")
    sys.exit(1)

# Load environment variables from .env file if it exists
load_dotenv()


# Initialize rich console for beautiful output
console = Console()


class FeedbackJudge:
    """Handles the evaluation of feedback using Claude as a judge."""

    DIMENSIONS = [
        "Polarity",
        "Factuality",
        "Evidence",
        "Actionability",
        "Connectivity",
        "Developmental Alignment"
    ]

    def __init__(self, api_key: Optional[str] = None, model: str = "claude-sonnet-4-5-20250929"):
        """Initialize the judge with API credentials and model selection."""
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        if not self.api_key:
            console.print("[bold red]Error:[/] ANTHROPIC_API_KEY not found.")
            console.print("Please set it using one of these methods:")
            console.print("  1. Create a .env file: echo 'ANTHROPIC_API_KEY=your-key-here' > .env")
            console.print("  2. Export as environment variable: export ANTHROPIC_API_KEY='your-key-here'")
            sys.exit(1)

        self.client = Anthropic(api_key=self.api_key)
        self.model = model

    def load_file(self, path: str) -> str:
        """Load and return file contents."""
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            console.print(f"[bold red]Error:[/] File not found: {path}")
            sys.exit(1)
        except Exception as e:
            console.print(f"[bold red]Error reading {path}:[/] {e}")
            sys.exit(1)

    def construct_prompt(self, checklist: str, student_note: str, feedback: str, judge_template: str) -> str:
        """Construct the evaluation prompt by filling in the template."""
        prompt = judge_template.replace("{checklist}", checklist)
        prompt = prompt.replace("{note}", student_note)
        prompt = prompt.replace("{feedback}", feedback)
        return prompt

    def evaluate(self, prompt: str) -> str:
        """Send the prompt to Claude and get the evaluation response."""
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=4096,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response.content[0].text
        except Exception as e:
            console.print(f"[bold red]Error calling Anthropic API:[/] {e}")
            sys.exit(1)

    def parse_evaluation(self, response: str) -> Dict:
        """Parse the structured evaluation response into scores and analyses."""
        results = {}

        # Extract content between <feedback> tags
        feedback_match = re.search(r'<feedback>(.*?)</feedback>', response, re.DOTALL)
        if feedback_match:
            feedback_content = feedback_match.group(1)
        else:
            feedback_content = response

        for dimension in self.DIMENSIONS:
            # Create pattern to match dimension section
            # Handle both "Analysis" and "Anaysis" (typo in prompt template)
            pattern = rf'{dimension}:\s*(?:Analysis|Anaysis):\s*(.*?)\s*{dimension} Score:\s*(\d+)/5'

            match = re.search(pattern, feedback_content, re.DOTALL | re.IGNORECASE)

            if match:
                analysis = match.group(1).strip()
                score = int(match.group(2))
                results[dimension] = {
                    "score": score,
                    "analysis": analysis
                }
            else:
                # Fallback: try to find just the score
                score_pattern = rf'{dimension} Score:\s*(\d+)/5'
                score_match = re.search(score_pattern, feedback_content, re.IGNORECASE)
                if score_match:
                    results[dimension] = {
                        "score": int(score_match.group(1)),
                        "analysis": "[Unable to parse analysis]"
                    }
                else:
                    results[dimension] = {
                        "score": None,
                        "analysis": "[Unable to parse]"
                    }

        return results


def display_results(results: Dict, checklist_path: str, note_path: str, feedback_path: str, model: str):
    """Display evaluation results in an attractive terminal format."""

    # Header
    console.print()
    console.print(Panel.fit(
        "[bold cyan]LLM-as-a-Judge Feedback Evaluation[/]\n"
        f"[dim]Model: {model}[/]",
        border_style="cyan"
    ))

    # Input files
    console.print("\n[bold]Input Files:[/]")
    console.print(f"  📋 Checklist: [cyan]{checklist_path}[/]")
    console.print(f"  📝 Student Note: [cyan]{note_path}[/]")
    console.print(f"  💬 Feedback: [cyan]{feedback_path}[/]")

    # Results table
    console.print("\n[bold]Evaluation Results:[/]")
    table = Table(show_header=True, header_style="bold magenta", box=None, padding=(0, 2))
    table.add_column("Dimension", style="cyan", width=22)
    table.add_column("Score", justify="center", style="bold")
    table.add_column("Analysis", style="white")

    # Calculate average score
    scores = [r["score"] for r in results.values() if r["score"] is not None]
    avg_score = sum(scores) / len(scores) if scores else 0

    for dimension, data in results.items():
        score = data["score"]
        analysis = data["analysis"]

        # Color code the score
        if score is None:
            score_text = "[red]N/A[/]"
        elif score >= 4:
            score_text = f"[green]{score}/5[/]"
        elif score >= 3:
            score_text = f"[yellow]{score}/5[/]"
        else:
            score_text = f"[red]{score}/5[/]"

        # Truncate long analyses for table display
        display_analysis = analysis[:100] + "..." if len(analysis) > 100 else analysis

        table.add_row(dimension, score_text, display_analysis)

    console.print(table)

    # Summary
    console.print()
    if avg_score >= 4:
        avg_color = "green"
    elif avg_score >= 3:
        avg_color = "yellow"
    else:
        avg_color = "red"

    console.print(Panel(
        f"[bold]Average Score:[/] [{avg_color}]{avg_score:.2f}/5.00[/]",
        border_style=avg_color
    ))
    console.print()


def save_results(results: Dict, checklist_path: str, note_path: str,
                feedback_path: str, model: str, output_path: str, raw_response: str):
    """Save evaluation results to JSON file."""
    output_data = {
        "metadata": {
            "timestamp": datetime.now().isoformat(),
            "model": model,
            "inputs": {
                "checklist_path": str(Path(checklist_path).absolute()),
                "student_note_path": str(Path(note_path).absolute()),
                "feedback_path": str(Path(feedback_path).absolute())
            }
        },
        "evaluation": {
            "dimensions": results,
            "average_score": sum(r["score"] for r in results.values() if r["score"] is not None) /
                           len([r for r in results.values() if r["score"] is not None])
        },
        "raw_response": raw_response
    }

    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        console.print(f"[bold green]✓[/] Results saved to: [cyan]{output_path}[/]")
    except Exception as e:
        console.print(f"[bold red]Error saving results:[/] {e}")
        sys.exit(1)


def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(
        description="Evaluate narrative feedback quality using Claude as a judge.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s examples/checklist.md examples/student_note1.md examples/feedback/student_note1_simple.md
  %(prog)s -o results.json examples/checklist.md examples/student_note2.md examples/feedback/student_note2_mega.md
  %(prog)s --model claude-3-opus-20240229 examples/checklist.md examples/student_note1.md examples/feedback/student_note1_simple.md
        """
    )

    parser.add_argument(
        "checklist",
        help="Path to the checklist file (markdown format)"
    )
    parser.add_argument(
        "student_note",
        help="Path to the student note file (markdown format)"
    )
    parser.add_argument(
        "feedback",
        help="Path to the feedback file to evaluate (plain text)"
    )
    parser.add_argument(
        "-o", "--output",
        default="output.json",
        help="Output JSON file path (default: output.json)"
    )
    parser.add_argument(
        "-m", "--model",
        default="claude-sonnet-4-5-20250929",
        help="Claude model to use (default: claude-sonnet-4-5-20250929)"
    )
    parser.add_argument(
        "--judge-prompt",
        default="prompts/judge/judge.md",
        help="Path to judge prompt template (default: prompts/judge/judge.md)"
    )

    args = parser.parse_args()

    # Display header
    console.print()
    console.print(Panel.fit(
        "[bold cyan]LLM-as-a-Judge Feedback Evaluation[/]\n"
        "[dim]Evaluating narrative feedback quality using Claude[/]",
        border_style="cyan"
    ))
    console.print()

    # Initialize judge
    with console.status("[bold green]Initializing judge...", spinner="dots"):
        judge = FeedbackJudge(model=args.model)

    # Load files
    console.print("[bold]Loading input files...[/]")
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console
    ) as progress:
        task1 = progress.add_task("  Loading checklist...", total=1)
        checklist = judge.load_file(args.checklist)
        progress.update(task1, completed=1)

        task2 = progress.add_task("  Loading student note...", total=1)
        student_note = judge.load_file(args.student_note)
        progress.update(task2, completed=1)

        task3 = progress.add_task("  Loading feedback...", total=1)
        feedback = judge.load_file(args.feedback)
        progress.update(task3, completed=1)

        task4 = progress.add_task("  Loading judge prompt template...", total=1)
        judge_template = judge.load_file(args.judge_prompt)
        progress.update(task4, completed=1)

    console.print("[bold green]✓[/] All files loaded successfully\n")

    # Construct prompt
    with console.status("[bold yellow]Constructing evaluation prompt...", spinner="dots"):
        prompt = judge.construct_prompt(checklist, student_note, feedback, judge_template)
    console.print("[bold green]✓[/] Prompt constructed\n")

    # Evaluate
    console.print("[bold yellow]Sending to Claude for evaluation...[/]")
    console.print("[dim]This may take 30-60 seconds...[/]\n")

    with console.status("[bold yellow]Awaiting Claude's evaluation...", spinner="bouncingBar"):
        response = judge.evaluate(prompt)

    console.print("[bold green]✓[/] Evaluation complete\n")

    # Parse results
    with console.status("[bold cyan]Parsing evaluation results...", spinner="dots"):
        results = judge.parse_evaluation(response)
    console.print("[bold green]✓[/] Results parsed\n")

    # Display results
    display_results(results, args.checklist, args.student_note, args.feedback, args.model)

    # Save results
    save_results(results, args.checklist, args.student_note, args.feedback,
                args.model, args.output, response)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[bold red]Interrupted by user[/]")
        sys.exit(1)
