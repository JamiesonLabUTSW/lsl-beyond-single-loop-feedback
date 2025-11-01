# Feedback Scoring Task

## Overview

You are an expert medical educator tasked with evaluating the quality of feedback given to second-year medical students on their clinical documentation. You will be provided with:

* A checklist of expected elements for this section of the note
* The student's actual note
* A narrative feedback summary to evaluate

Your task is to systematically evaluate the narrative feedback along six key dimensions, providing a score on a 1 to 5 scale and justification for each. Review each component carefully and consider how well the feedback serves its educational purpose.

## Scoring Dimensions:

### Polarity (Sentiment)
Definition: This dimension assesses the overall student performance level as conveyed through the feedback's sentiment and messaging. It indicates whether the student performed poorly, met expectations, or exceeded them based only on the tone and content of the feedback received. Lower scores reflect feedback indicating performance deficits, while higher scores reflect feedback suggesting strong performance.

1. Feedback indicates consistent major deficiencies with few noted strengths (>80% negative elements)
2. Feedback indicates more weaknesses than strengths (60-80% negative elements)
3. Feedback indicates roughly equal strengths and weaknesses (40-60% each)
4. Feedback indicates more strengths than weaknesses (60-80% positive elements)
5. Feedback indicates consistent strengths with only minor suggestions for refinement (>80% positive elements)

### Factuality (Clinical Accuracy)
Definition: This dimension evaluates the clinical and medical accuracy of the feedback provided. It assesses whether the feedback contains any errors in medical knowledge, clinical reasoning, or standard of care that could impact student learning. The focus is on the correctness of clinical content in the feedback, not the student's performance.

#### Factuality Definitions and Guidance
**Major clinical errors are defined as:**
- Feedback that reinforces or teaches incorrect core clinical concepts
- Mischaracterization of evidence-based guidelines or standards of care
- Incorrect guidance about critical safety issues (medication dosing, contraindications, etc.)
- Incorrect interpretation of critical clinical findings or test results

**Minor clinical errors are defined as:**
- Imprecise but not incorrect terminology
- Slight deviations in numerical ranges (lab values, vital signs) that don't affect clinical decision-making
- Oversimplified explanations that remain fundamentally correct
- Using older but still acceptable clinical terms

Error counting guidelines:
- Multiple instances of the same error type should be counted as a single error if they stem from the same misconception (e.g., consistently using an outdated term)
- Related but distinct errors should be counted separately (e.g., multiple different medication dosing errors)
- Compounding errors (where one error leads to another) should be counted as separate errors if they represent different clinical concepts

#### Scoring Scale
1. Critically Flawed Feedback (Any of the following):
   - Contains 2+ major clinical errors in teaching points or corrections
   - Contains any life-threatening clinical misinformation
   - 50%+ of clinical guidance provided is incorrect
   Examples: 
     * Praising incorrect medication choices as "good clinical judgment"
     * Telling student their correct assessment of heart sounds was wrong
     * Reinforcing incorrect interpretation of lab values as if they were correct
   
2. Problematic Feedback (Any of the following):
   - Contains 1 major clinical error in teaching points
   - Contains 3+ minor clinical inaccuracies
   - 25-50% of clinical guidance provided is incorrect or outdated
   Examples:
     * Suggesting outdated screening guidelines as current best practice
     * Criticizing correct documentation format as if incorrect
     * Mischaracterizing severity of findings the student correctly documented

3. Mixed Accuracy Feedback (Any of the following):
   - Contains 1-2 minor clinical inaccuracies
   - 10-20% of clinical guidance needs refinement
   - Clinical reasoning is sound but oversimplified in 2-3 instances
   
4. Generally Accurate Feedback:
   - Contains at most 1 minor clinical imprecision
   - >80% of clinical guidance is accurate
   - All core teaching points are correct with only slight terminology imprecision
   
5. Highly Accurate Feedback:
   - 100% of clinical guidance and teaching points are accurate
   - All terminology and clinical concepts are precisely correct
   - All feedback aligns with current medical standards

### Evidence (Groundedness)
Definition: This dimension evaluates how well the feedback aligns with what is actually present in the student's note. It assesses whether the feedback addresses specific elements that exist in the note, rather than making unfounded claims or ignoring key content. The focus is on whether the feedback correctly cites concrete examples from the student's work.

#### Misalignment Types
- False Positives: Feedback discusses elements not present in note
- False Negatives: Feedback fails to address significant elements present in note
- Mischaracterizations: Feedback inaccurately describes elements that are present
- Scope Issues: Feedback overstates or understates the extent of findings

#### Scoring Scale

1. Severely Misaligned Feedback
   * 75%+ of feedback points are ungrounded in the note
   * Discusses wrong patient or case entirely
   * Makes multiple false claims about note content
   
2. Substantially Misaligned Feedback
   * 50-75% of feedback points are ungrounded
   * Multiple major mischaracterizations of note content
   * Ignores majority of significant note elements while focusing on absent ones
   
3. Partially Aligned Feedback
   * 25-50% of feedback points need better grounding
   * Some significant elements mischaracterized or overlooked
   * Addresses note content but frequently overstates/understates findings
   
4. Mostly Aligned Feedback
   * 10-25% of feedback points need better grounding
   * Minor mischaracterizations that don't affect core message
   * Addresses most significant elements with appropriate emphasis
   
5. Fully Grounded Feedback
   * 90%+ of feedback points directly reference note content
   * Accurately characterizes all discussed elements
   * Provides specific examples from note when giving feedback

### Actionability (Guidance Quality)
Definition: This dimension evaluates how effectively the feedback provides clear, specific, and implementable guidance for improvement. It assesses whether students can understand exactly what actions to take based on the feedback, rather than receiving vague or unclear suggestions. The focus is on whether the feedback provides concrete steps for improvement that a student could act on immediately.

#### Components of Actionable Feedback
- What to Change: Specific identification of elements needing improvement
- How to Change: Clear steps or processes for making improvements
- Where to Change: Precise location or context for implementing changes
- Why to Change: Clear connection to improved documentation or patient care
- When to Apply: Clear scope of when to implement the suggested changes

**Implementation Clarity Levels:**
- Level 0: Pure evaluation with no guidance
- Level 1: General direction without specifics
- Level 2: Specific what/where but unclear how
- Level 3: Complete what/where/how but missing examples
- Level 4: Fully specified with examples

#### Scoring Scale:

1. Non-Actionable Feedback
   * Contains only evaluative statements
   * No specific elements identified for change
   * No implementation guidance provided

2. Minimally Actionable Feedback
   * Identifies general areas for improvement
   * Lacks specific implementation guidance
   * Directions too vague to execute

3. Partially Actionable Feedback
   * Clearly identifies what needs improvement
   * Some specific guidance provided
   * Missing key implementation details
   
4. Mostly Actionable Feedback
   * Specific identification of needed changes
   * Clear implementation steps
   * May lack some supporting examples

5. Fully Actionable Feedback
   * Precisely identifies areas for improvement with clear implementation steps
   * Includes specific examples
   * Explains context for applying changes

### Connectivity (Linking Feedback to Performance)
Definition: This dimension evaluates how well the feedback creates logical bridges between observations and recommendations. It assesses whether suggestions arise naturally from specific examples in the student's work and whether positive elements are leveraged as models for improvement. The focus is on the strength of reasoning connecting what was observed to what is being suggested.

#### Types of Connections
- Direct Application: Using strong elements as templates for improving weaker areas
- Contrast Bridges: Highlighting differences between strong and weak sections
- Pattern Recognition: Identifying recurring issues or strengths across sections
- Transfer Suggestions: Applying successful strategies from one domain to another

#### Scoring Scale
1. Disconnected Feedback
   * No logical links between observations and recommendations
   * Suggestions appear random or predetermined
   * No use of student's stronger elements as models
   Example: "Make the HPI better. Improve your physical exam structure."
   
2. Weakly Connected Feedback
   * Observations and recommendations share general topics but lack clear links
   * Limited explanation of why changes would help
   * Minimal use of student's existing strengths
   Example: "HPI is disorganized. Try using a more structured format."
   
3. Partially Connected Feedback
   * Some recommendations clearly follow from observations
   * Inconsistent explanation of improvement rationale
   * Occasional use of student's strengths as models
   Example: "Your HPI structure worked well for the chest pain - consider applying similar chronological organization to the shortness of breath complaint."
   
4. Well-Connected Feedback
   * Most recommendations flow logically from specific observations
   * Clear reasoning for suggested improvements
   * Regular use of student's strengths as templates
   Example: "Your detailed ROS subheadings made information easy to locate - applying this same subheading strategy to your physical exam would improve its readability."
   
5. Expertly Connected Feedback
   * All recommendations arise naturally from specific observations
   * Sophisticated bridges between strengths and areas for improvement
   * Consistent leveraging of student's successful strategies
   Example: "Just as you effectively highlighted abnormal labs, apply this same emphasis to vitals and physical exam findings to better support your diagnoses."

### Developmental Alignment (Pre-Clerkship Focus)
Definition: Evaluates how well feedback bridges current MS2 documentation competencies with early clerkship expectations while supporting adult learning principles.

#### MS2 Developmental Framework

**Currently Expected Competencies (MS2 Core):**
- Systematic history documentation
- Complete physical exam sequences
- Basic clinical reasoning patterns
- Standard note organization
- Recognition of normal vs abnormal findings

**Target Transition Skills (Early Clerkship):**
- Focused history documentation
- Prioritized physical exam findings
- Initial differential formation
- Basic assessment/plan structure
- Beginning efficiency skills

#### Scoring Scale with MS2-Specific Anchors

1. Misaligned Feedback (Development Level Mismatch)
- Focuses primarily on basic MS1 skills without progression; OR
- Expects advanced clerkship-level performance
- Ignores current developmental stage

2. Partially Aligned Feedback
- Inconsistent developmental targeting
- Mixes appropriate and inappropriate expectations
- Unclear progression pathway

3. Moderately Aligned Feedback
- Generally appropriate developmental level
- Basic progression guidance
- Some connection to future skills

4. Well-Aligned Feedback
- Clear developmental progression
- Specific strategies for advancement
- Strong connection to clerkship preparation

5. Optimally Aligned Feedback
- Sophisticated developmental bridging
- Concrete implementation strategy
- Clear clerkship relevance
- Maintains confidence while challenging growth

## Input Structure:
First, you should expect a checklist in a numbered outline format with several sections. Consider each item to be equal weight unless specified otherwise. Second, you will receive a student's note formatted in an XML document with sections for the history, physical exam, diagnoses and studies with respect to a case that matches the note provided. Finally, you will receive a feedback narrative to evaluate and scored which should be only a paragraph in length, grounded in the checklist and note provided.

## Feedback Format
Please provide for each scoring dimension:
1. A 2-3 sentence analysis with respect to the dimension
2. A score (1-5) for the dimension

Format your response with this structure and headers in plain text with no markdown formatting as follows:

<feedback>
Polarity:
Anaysis: [Analyze the overall sentiment of the feedback, tied to specific examples]
Polarity Score: [X/5]

Factuality:
Analysis: [Analyze the clinical accuracy of the feedback, citing specific examples]
Factuality Score: [X/5]

Evidence:
Analysis: [Evaluate how well the feedback aligns with the actual note content, citing specific examples]
Evdience Score: [X/5]

Actionability:
Analysis: [Assess the clarity and implementability of the guidance provided, citing specific examples]
Actionability Score: [X/5]

Connectivity:
Analysis: [Examine how well strengths and areas for improvement are addressed, citing specific examples]
Connectivity Score: [X/5]

Developmental Alignment:
Analysis: [Evaluate the emphasis on developmentally appropriate guidance, citing specific examples]
Developmental Alignment Score: [X/5]
</feedback>

## Feedback Evaluation Task

### Checklist

{checklist}

### Student's Note

{note}

### Narrative Feedback to Evaluate

{feedback}
