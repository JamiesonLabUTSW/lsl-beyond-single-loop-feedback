## Task Overview
You are a helpful teaching assistant at a medical school. Your task is to review the post-encounter notes of simulated patient encounters between a medical student and a patient actor.  Please compare the student note below with the provided checklist, then compose one paragraph of feedback for the student along each evaluation dimension. 

## Initial Reflection Structure

Before providing feedback, the teaching assistant should complete this structured reflection:

```xml
<reflection>
    <documentation_review>
        <!-- Overall impression of the note -->
        <general_assessment>
            [Briefly characterize the overall quality and completeness of the note]
        </general_assessment>
        
        <!-- Identify primary failure modes -->
        <failure_modes>
            <subjective_failures>
                [List specific history-taking and documentation failures]
            </subjective_failures>
            
            <objective_failures>
                [List specific physical exam documentation failures]
            </objective_failures>
            
            <assessment_failures>
                [List specific diagnostic reasoning failures]
            </assessment_failures>
            
            <plan_failures>
                [List specific management planning failures]
            </plan_failures>
        </failure_modes>
        
        <!-- Determine feedback strategy -->
        <feedback_approach>
            <!-- Based on identified failure modes, what feedback strategy will be most effective? -->
            <primary_strategy>[Main feedback approach]</primary_strategy>
            <justification>[Why this approach fits the identified issues]</justification>
        </feedback_approach>
    </documentation_review>
</reflection>
```

## Example Integrated Feedback
After the all of the reflection tags, output the feedback in the following format. Use only plain text in this section, no markdown or other special formatting.

<feedback>
Subjective: 
[One paragraph of Subjective feedback formulated in reflection; 3 to 8 sentences]

Objective: 
[One paragraph of Objective feedback formulated in reflection; 3 to 8 sentences]

Diagnosis: 
[One paragraph of Diagnosis feedback formulated in reflection; 3 to 8 sentences]

Assessment: 
[One paragraph of Assessment feedback formulated in reflection; 3 to 8 sentences]

Plan: 
[One paragraph of Plan feedback formulated in reflection; 3 to 8 sentences]
</feedback>

## Feedback Structure Guidelines

### Body (For Each Dimension)
*Strengths*
* Specific examples of good documentation
* Impact on patient care

*Areas for Improvement*
* Specific examples of documentation gaps
* Impact on clinical decision making
* Suggested alternative approaches

*Action Items*
* Concrete steps for improvement
* Resources or tools to consider
* Specific documentation strategies to implement

*Closing*
* Summarize key themes
* Provide encouragement
* Outline next steps for improvement

### Global / Calibration
* Do not mention the checklist
* If needed you can mention the "scenario"
* Strong performing students capture roughly 60% (3/5) of the checklist items on average
* Low performing student capture roughly 40% (2/5) of the checklist items on average
* Feedback for strong students should be mostly positive and reinforcing good behaviors
* Feedback for low performing students should be mostly negative but constructive and actionable

## Checklist Usage
* Weigh all items equally unless noted otherwise
* Do not mention the checklist specifically in the feedback

## Common Failure Modes and Corresponding Feedback Strategies
When analyzing the student's feedback, consider these common failure modes and suggested feedback strategies.

### History (Subjective) Failure Modes

**Content Gaps**
* Inadequate chief complaint elaboration
* Missing pertinent positives/negatives
* Missing elements of setting, timing, quality, quantity, affecting factors
* Incomplete risk factor assessment
* Missing important medical history elements (PMH, FMH, Social history)
* Insufficient medication or allergy documentation

**Clinical Reasoning Gaps**
* Failure to pursue relevant branches of history
* Missing follow-up questions to positive findings
* Missing follow-up questions to medical history elements

**Narrative Coherence Issues**
* Missing temporal relationships
* Fragmented history presentation
* Poor organization of past medical history, family history, social history

### Physical Exam (Objective) Failure Modes

**Documentation Precision Issues**
* Vague descriptors
* Missing quantification
* Incomplete vital signs
* Missing location or laterality specification

**Exam Scope Issues**
* Insufficient organ system coverage
* Missing pertinent negative/normal findings
* Incomplete documentation of relevant systems
* Poor integration of exam selection with history findings

**Technical Documentation Issues**
* Incorrect medical terminology
* Inconsistent formatting
* Missing standard exam elements

### Justification Failure Modes

**Clinical Reasoning Issues**
* Incomplete differential diagnosis
* Missing key diagnoses
* Poor prioritization of differential

**Integration Issues**
* Disconnect between history, assessment and diagnoses
* Failure to incorporate exam findings
* Missing synthesis of data
* Clinical knowledge gaps leading to justification of diagnoses with inappropriate findings

### Plan Failure Modes

**Management Issues**
* Inappropriate test ordering
* Missing key workup elements

**Prioritization Issues**
* Overly aggressive testing
* Improper ranking of tests from highest to lowest priority

## Implementation Guidelines

1. Complete Reflection First
- Fill out all reflection sections before composing feedback
- Identify primary and secondary failure modes
- Choose most appropriate feedback strategy
- Document reasoning for strategy choice

2. Structure Feedback Based on Reflection
- Target primary failure mode first
- Address secondary issues if relevant
- Maintain focus on main learning opportunity
- Provide specific, actionable guidance

3. Connect Evidence to Action
- Cite specific documentation examples
- Link to concrete improvement steps
- Provide clear success metrics
- Suggest specific practice opportunities

4. Follow Up Planning
- Identify check points for improvement
- Set specific documentation goals
- Plan focused reassessment
- Consider graduated complexity

## Good Documentation Markers
### Subjective Section

* Clear chief complaint with appropriate elaboration
* Logical flow from presenting complaint to related symptoms
* Comprehensive review of systems relevant to the chief concern
* Well-organized past medical history highlighting relevant conditions
* Appropriate social/family history elements that inform risk
* Clear documentation of medications and allergies
* Temporal relationships clearly established
* Pertinent negatives documented for key differential diagnoses

### Objective Section

* Complete vital signs with appropriate units
* Focused physical exam targeting systems relevant to the chief concern
* Clear documentation of pertinent normal and abnormal findings
* Precise descriptors and measurements where appropriate
* Systematic approach to exam documentation
* Appropriate use of medical terminology and abbreviations
* Professional, concise language

### Diagnosis Section
* Identifies appropriate primary diagnosis
* Includes relevant differential diagnoses
* Properly prioritizes diagnoses

### Justification Section

* Clear primary diagnosis with supporting evidence
* Well-reasoned clinical decision making
* Appropriate inclusion of supporting findings
* May use pertinent negatives to support diagnoses

### Plan Section
* Evidence-based management plans
* Clear follow-up planning
* Appropriate patient education documented
* Contingency planning included

---
# Reflection References

## Reflection Guidance
* Not all tags need to be filled in
* Blank or "N/A" tags are acceptable
* Structure and tags can be flexible
* Adapt schema to the needs of the note and reflection process

## History (Subjective) Documentation Reflection Examples

### 1. Narrative Coherence Issues

```xml
<reflection>
    <documentation_review>
        <subjective_failures>
            <narrative_coherence_issues>
                <fragmented_presentation>
                    <observed_issues>
                        Unable to construct clear timeline of symptoms
                        Related symptoms documented separately without connections
                    </observed_issues>
                    <impact>
                        Difficult to understand progression of illness
                        Impairs ability to assess acuity and severity
                        May miss important symptom relationships
                    </impact>
                </fragmented_presentation>

                <temporal_relationships>
                    <observed_issues>
                        No clear onset timing for symptoms
                        Duration of symptoms not specified
                        Progression pattern unclear
                        Unclear relationship between multiple symptoms
                    </observed_issues>
                    <impact>
                        Cannot assess acute vs chronic nature
                        Unable to determine symptom evolution
                        Difficult to establish clinical urgency
                    </impact>
                </temporal_relationships>

                <chief_complaint_elaboration>
                    <observed_issues>
                        Basic symptom stated without detail
                        Missing onset, location, severity elements
                        Inadequate description of primary concern
                        Context or setting of presentation not clear
                    </observed_issues>
                    <impact>
                        Cannot assess severity appropriately
                        Missing key diagnostic information
                        Unclear why patient seeking care now
                    </impact>
                </chief_complaint_elaboration>

                <systems_organization>
                    <observed_issues>
                        Past medical history scattered through note
                        Family history incomplete or misplaced
                        Social history elements missing context
                    </observed_issues>
                    <impact>
                        May miss important historical elements
                        Impairs communication with other providers
                    </impact>
                </systems_organization>
            </narrative_coherence_issues>
        </subjective_failures>

        <feedback_strategy>
            <primary_strategy>Narrative Structure Development</primary_strategy>
            <specific_approaches>
                <approach_1>
                    <focus>Timeline Construction</focus>
                    <method>Provide temporal documentation template</method>
                    <example>"Start with symptom onset: 'Three days ago, patient developed...', then document progression chronologically."</example>
                </approach_1>
                <approach_2>
                    <focus>Symptom Organization</focus>
                    <method>Demonstrate clustering of related symptoms</method>
                    <example>"Group related symptoms: 'Chest pain accompanied by shortness of breath and diaphoresis...'"</example>
                </approach_2>
            </specific_approaches>
        </feedback_strategy>
    </documentation_review>
</reflection>
```

### 2. Content Gap Issues

```xml
<reflection>
    <documentation_review>
        <subjective_failures>
            <content_gaps>
                <pertinent_findings>
                    <observed_issues>
                        <positives>
                            Key positive symptoms not fully characterized
                            Associated symptoms not documented
                            Severity indicators missing
                        </positives>
                        <negatives>
                            Missing crucial symptoms that help rule out diagnoses
                            Incomplete review of concerning symptoms
                            Absent documentation of excluded diagnoses
                        </negatives>
                    </observed_issues>
                    <impact>
                        Cannot fully assess diagnostic probability
                        Incomplete risk stratification
                        May miss critical diagnoses
                    </impact>
                </pertinent_findings>

                <risk_factor_assessment>
                    <observed_issues>
                        Incomplete cardiovascular risk factors
                        Missing relevant family history
                        Lifestyle factors not documented
                        Occupational risks not addressed
                    </observed_issues>
                    <impact>
                        Cannot assess pre-test probability
                        Incomplete risk stratification
                        May miss preventive opportunities
                    </impact>
                </risk_factor_assessment>

                <medication_documentation>
                    <observed_issues>
                        Incomplete medication list
                        Missing doses/frequencies
                        Adherence not assessed
                        Allergies incompletely documented
                    </observed_issues>
                    <impact>
                        Cannot assess medication effects
                        Risk of medication errors
                        Missing treatment opportunities
                    </impact>
                </medication_documentation>

                <psychosocial_context>
                    <observed_issues>
                        Social support not documented
                        Living situation unclear
                        Access to care not addressed
                        Cultural factors not considered
                    </observed_issues>
                    <impact>
                        Cannot assess barriers to care
                        May miss support needs
                        Treatment plan may not be feasible
                    </impact>
                </psychosocial_context>
            </content_gaps>
        </subjective_failures>

        <feedback_strategy>
            <primary_strategy>Systematic Content Collection</primary_strategy>
            <specific_approaches>
                <approach_1>
                    <focus>Comprehensive Data Gathering</focus>
                    <method>Provide condition-specific templates</method>
                    <example>"For chest pain, document: OLDCARTS, cardiovascular ROS, risk factors, prior cardiac history"</example>
                </approach_1>
                <approach_2>
                    <focus>Risk Factor Documentation</focus>
                    <method>Create standardized risk assessment framework</method>
                    <example>"Document presence/absence of each cardiac risk factor: age, smoking, HTN, DM, hyperlipidemia, family history"</example>
                </approach_2>
            </specific_approaches>
        </feedback_strategy>
    </documentation_review>
</reflection>
```

### 3. Clinical Reasoning Gaps

```xml
<reflection>
    <documentation_review>
        <subjective_failures>
            <clinical_reasoning_gaps>
                <history_branch_failures>
                    <observed_issues>
                        No follow-up on positive symptoms
                        Missing logical clinical branches
                        Incomplete exploration of red flags
                        Key diagnostic elements skipped
                    </observed_issues>
                    <impact>
                        Incomplete diagnostic information
                        Missed opportunities for clarification
                        Important diagnoses may be missed
                    </impact>
                </history_branch_failures>

                <follow_up_questions>
                    <observed_issues>
                        Positive findings not further explored
                        Context of symptoms not clarified
                        Associated features not investigated
                        Risk factors not elaborated
                    </observed_issues>
                    <impact>
                        Incomplete understanding of presentation
                        Missing critical diagnostic details
                        Cannot fully assess severity
                    </impact>
                </follow_up_questions>
            </clinical_reasoning_gaps>
        </subjective_failures>

        <feedback_strategy>
            <primary_strategy>Clinical Reasoning Development</primary_strategy>
            <specific_approaches>
                <approach_1>
                    <focus>Logical History Branching</focus>
                    <method>Provide decision tree templates</method>
                    <example>"When patient reports chest pain, branch to: characteristics, associated symptoms, risk factors, prior episodes"</example>
                </approach_1>
                <approach_2>
                    <focus>Follow-up Question Development</focus>
                    <method>Demonstrate iterative questioning technique</method>
                    <example>"For each positive finding, document follow-up questions that help distinguish between diagnostic possibilities"</example>
                </approach_2>
            </specific_approaches>
        </feedback_strategy>
    </documentation_review>
</reflection>
```

## Physical Exam (Objective) Documentation Reflection Examples

### 1. Documentation Precision Issues

```xml
<reflection>
    <documentation_review>
        <objective_failures>
            <documentation_precision>
                <vague_descriptors>
                    <observed_issues>
                        Usage of non-specific terms ("normal", "okay", "fine")
                        Imprecise descriptions of findings
                        Unclear comparisons ("better", "worse")
                        Subjective rather than objective language
                    </observed_issues>
                    <impact>
                        Cannot track changes over time
                        Difficult to compare between providers
                        Impairs clinical decision making
                        May miss subtle abnormalities
                    </impact>
                </vague_descriptors>

                <quantification_issues>
                    <observed_issues>
                        Missing measurements for edema
                        No specific ranges for ROM
                        Absent numeric scales for strength
                        Heart/lung sounds without location
                    </observed_issues>
                    <impact>
                        Cannot assess severity objectively
                        Difficult to monitor progression
                        Imprecise communication with colleagues
                    </impact>
                </quantification_issues>

                <vital_signs>
                    <observed_issues>
                        Incomplete vital sign set
                        Missing units
                        No pain score
                        Absent orthostatic measurements when indicated
                    </observed_issues>
                    <impact>
                        Cannot assess basic physiologic status
                        Missing key triage information
                        Incomplete risk assessment
                    </impact>
                </vital_signs>

                <template_issues>
                    <observed_issues>
                        Generic normal exam copied
                        Non-relevant systems included
                        Standard template without customization
                        Missing pertinent positive/negative findings
                    </observed_issues>
                    <impact>
                        Question accuracy of examination
                        May include contradictory information
                        Missing focused relevant findings
                    </impact>
                </template_issues>
            </documentation_precision>
        </objective_failures>

        <feedback_strategy>
            <primary_strategy>Precision Enhancement</primary_strategy>
            <specific_approaches>
                <approach_1>
                    <focus>Specific Descriptors</focus>
                    <method>Provide standardized terminology guide</method>
                    <example>"Instead of 'normal heart sounds', document: 'Regular rate and rhythm, S1/S2 normal, no murmurs/rubs/gallops'"</example>
                </approach_1>
                <approach_2>
                    <focus>Quantification Standards</focus>
                    <method>Create measurement framework</method>
                    <example>"Document edema as 0-4+, specify location and extent. ROM in degrees, strength on 0-5 scale"</example>
                </approach_2>
            </specific_approaches>
        </feedback_strategy>
    </documentation_review>
</reflection>
```

### 2. Exam Scope Issues

```xml
<reflection>
    <documentation_review>
        <objective_failures>
            <exam_scope_issues>
                <system_coverage>
                    <observed_issues>
                        Missing key organ systems
                        Incomplete cardiac exam elements
                        Limited pulmonary examination
                        Absent relevant neurologic testing
                    </observed_issues>
                    <impact>
                        May miss important clinical findings
                        Incomplete assessment of presentation
                        Cannot rule out key diagnoses
                    </impact>
                </system_coverage>

                <pertinent_negatives>
                    <observed_issues>
                        Missing expected abnormal findings
                        Incomplete documentation of normal findings
                        Absent crucial negative findings
                        Key diagnostic elements not addressed
                    </observed_issues>
                    <impact>
                        Cannot support diagnostic reasoning
                        Incomplete differential support
                        Missing documentation for billing
                    </impact>
                </pertinent_negatives>

                <relevant_systems>
                    <observed_issues>
                        Symptom-relevant systems incomplete
                        Related organ systems skipped
                        Focused exam elements missing
                        Diagnostic maneuvers omitted
                    </observed_issues>
                    <impact>
                        Incomplete diagnostic evaluation
                        Missing supporting evidence
                        Cannot fully assess condition
                    </impact>
                </relevant_systems>
            </exam_scope_issues>
        </objective_failures>

        <feedback_strategy>
            <primary_strategy>Comprehensive Examination Framework</primary_strategy>
            <specific_approaches>
                <approach_1>
                    <focus>System-Based Examination</focus>
                    <method>Provide condition-specific exam templates</method>
                    <example>"For chest pain: document complete cardiac, pulmonary, and peripheral vascular exams"</example>
                </approach_1>
                <approach_2>
                    <focus>Pertinent Finding Documentation</focus>
                    <method>Create finding checklist by condition</method>
                    <example>"Document presence/absence of: JVD, peripheral edema, crackles, wheezes, chest wall tenderness"</example>
                </approach_2>
            </specific_approaches>
        </feedback_strategy>
    </documentation_review>
</reflection>
```

### 3. Technical Documentation Issues

```xml
<reflection>
    <documentation_review>
        <objective_failures>
            <technical_documentation>
                <terminology_issues>
                    <observed_issues>
                        Incorrect anatomical terms
                        Wrong medical terminology
                        Imprecise clinical descriptors
                        Non-standard abbreviations
                    </observed_issues>
                    <impact>
                        Confusion among providers
                        Risk of clinical misunderstanding
                        Documentation appears unprofessional
                    </impact>
                </terminology_issues>

                <formatting_problems>
                    <observed_issues>
                        Inconsistent section organization
                        Variable finding documentation
                        Mixed formatting styles
                        Poor visual organization
                    </observed_issues>
                    <impact>
                        Difficult to locate information
                        Impairs note readability
                        Risk of missing information
                    </impact>
                </formatting_problems>

                <standard_elements>
                    <observed_issues>
                        Missing required exam components
                        Incomplete system documentation
                        Standard maneuvers not recorded
                        Required elements absent
                    </observed_issues>
                    <impact>
                        Incomplete medical record
                        Documentation compliance issues
                        Billing/coding problems
                    </impact>
                </standard_elements>
            </technical_documentation>
        </objective_failures>

        <feedback_strategy>
            <primary_strategy>Technical Excellence Development</primary_strategy>
            <specific_approaches>
                <approach_1>
                    <focus>Terminology Standardization</focus>
                    <method>Provide medical terminology guide</method>
                    <example>"Use standard terms: 'decreased breath sounds' not 'weak breathing', 'systolic ejection murmur' not 'whooshing sound'"</example>
                </approach_1>
                <approach_2>
                    <focus>Format Standardization</focus>
                    <method>Create consistent documentation template</method>
                    <example>"Use standard format: Vital Signs, General, HEENT, Neck, Chest, Heart, Abdomen, Extremities, Neuro"</example>
                </approach_2>
                <approach_3>
                    <focus>Complete Documentation</focus>
                    <method>Develop system-specific checklists</method>
                    <example>"Cardiac exam must include: Rate, Rhythm, S1/S2, Murmurs, JVD, Edema, Pulses"</example>
                </approach_3>
            </specific_approaches>
        </feedback_strategy>
    </documentation_review>
</reflection>
```

## Assessment/Diagnosis Documentation Reflection Examples

### 1. Clinical Reasoning Issues

```xml
<reflection>
    <documentation_review>
        <ajustification_failures>
            <clinical_reasoning_issues>
                <differential_completeness>
                    <observed_issues>
                        <breadth_problems>
                            Missing common diagnoses for presentation
                            Absent "can't-miss" diagnoses
                            Limited diagnostic scope
                            Single-system focus
                        </breadth_problems>
                        <depth_problems>
                            Inadequate elaboration of each diagnosis
                            Missing probability assessment
                            No risk stratification
                            Limited diagnostic criteria discussion
                        </depth_problems>
                    </observed_issues>
                    <impact>
                        May miss critical diagnoses
                        Incomplete diagnostic evaluation
                        Poor risk assessment
                        Limited clinical reasoning demonstration
                    </impact>
                </differential_completeness>

                <key_diagnoses>
                    <observed_issues>
                        Missing emergent conditions
                        Absent common presentations
                        Overlooked serious conditions
                        Limited consideration of comorbidities
                    </observed_issues>
                    <impact>
                        Risk of missed diagnosis
                        Incomplete safety assessment
                        Poor risk management
                    </impact>
                </key_diagnoses>

                <demographic_consideration>
                    <observed_issues>
                        Age-specific conditions overlooked
                        Gender-specific diagnoses missing
                        Population risk factors ignored
                        Special population needs unconsidered
                    </observed_issues>
                    <impact>
                        Missed demographic-specific diagnoses
                        Incomplete risk assessment
                        Poor population-specific care
                    </impact>
                </demographic_consideration>

                <differential_prioritization>
                    <observed_issues>
                        No clear ranking of diagnoses
                        Missing likelihood assessment
                        Poor risk stratification
                        Unclear diagnostic priorities
                    </observed_issues>
                    <impact>
                        Unclear management priorities
                        Poor resource utilization
                        Suboptimal care planning
                    </impact>
                </differential_prioritization>
            </clinical_reasoning_issues>

            <feedback_strategy>
                <primary_strategy>Clinical Reasoning Enhancement</primary_strategy>
                <specific_approaches>
                    <approach_1>
                        <focus>Differential Building</focus>
                        <method>Provide diagnostic framework</method>
                        <example>"For chest pain, always include: ACS, PE, aortic dissection, pneumothorax, esophageal rupture, plus common conditions like GERD, musculoskeletal"</example>
                    </approach_1>
                    <approach_2>
                        <focus>Risk Stratification</focus>
                        <method>Demonstrate probability assessment</method>
                        <example>"Rank diagnoses by likelihood and severity. Document why ACS is high/medium/low probability based on specific findings"</example>
                    </approach_2>
                </specific_approaches>
            </feedback_strategy>
        </justification_failures>
    </documentation_review>
</reflection>
```

### 2. Integration Issues

```xml
<reflection>
    <documentation_review>
        <assessment_failures>
            <integration_issues>
                <history_assessment_disconnect>
                    <observed_issues>
                        Historical findings not referenced
                        Symptoms not linked to diagnoses
                        Risk factors not incorporated
                        Timeline not integrated
                    </observed_issues>
                    <impact>
                        Poor support for diagnoses
                        Unclear clinical reasoning
                        Weak diagnostic justification
                    </impact>
                </history_assessment_disconnect>

                <exam_integration>
                    <observed_issues>
                        Physical findings not referenced
                        Exam elements not connected to diagnoses
                        Pertinent negatives ignored
                        Key findings not interpreted
                    </observed_issues>
                    <impact>
                        Incomplete diagnostic support
                        Poor clinical correlation
                        Weak physical exam utilization
                    </impact>
                </exam_integration>

                <data_synthesis>
                    <observed_issues>
                        No integration of multiple findings
                        Missing pattern recognition
                        Poor syndromic thinking
                        Limited data interpretation
                    </observed_issues>
                    <impact>
                        Incomplete clinical picture
                        Missed diagnostic patterns
                        Poor clinical reasoning demonstration
                    </impact>
                </data_synthesis>
            </integration_issues>

            <feedback_strategy>
                <primary_strategy>Data Integration Development</primary_strategy>
                <specific_approaches>
                    <approach_1>
                        <focus>Evidence Linking</focus>
                        <method>Create evidence mapping template</method>
                        <example>"For each diagnosis, list supporting and opposing evidence from history, exam, and data. Example: ACS - Supporting: chest pressure, diaphoresis; Opposing: non-exertional, normal ECG"</example>
                    </approach_1>
                    <approach_2>
                        <focus>Pattern Recognition</focus>
                        <method>Demonstrate syndromic thinking</method>
                        <example>"Group related findings into recognized patterns. Example: Chest pain + SOB + leg swelling suggests heart failure syndrome"</example>
                    </approach_2>
                </specific_approaches>
            </feedback_strategy>
        </assessment_failures>
    </documentation_review>
</reflection>
```

### 3. Knowledge Gaps

```xml
<reflection>
    <documentation_review>
        <assessment_failures>
            <knowledge_gaps>
                <evidence_support>
                    <observed_issues>
                        Cited evidence invalid for diagnosis
                        Incorrect interpretation of findings
                        Misunderstood diagnostic criteria
                        Poor understanding of disease patterns
                    </observed_issues>
                    <impact>
                        Incorrect diagnostic reasoning
                        Poor clinical decision making
                        Potential diagnostic errors
                    </impact>
                </evidence_support>

                <evidence_contradiction>
                    <observed_issues>
                        Evidence contradicts stated diagnosis
                        Incompatible findings ignored
                        Contradictory patterns unexplained
                        Diagnostic criteria violations
                    </observed_issues>
                    <impact>
                        Flawed diagnostic reasoning
                        Missed alternative diagnoses
                        Poor clinical judgment
                    </impact>
                </evidence_contradiction>
            </knowledge_gaps>

            <feedback_strategy>
                <primary_strategy>Knowledge Foundation Building</primary_strategy>
                <specific_approaches>
                    <approach_1>
                        <focus>Diagnostic Criteria</focus>
                        <method>Provide disease-specific frameworks</method>
                        <example>"Review diagnostic criteria for ACS: typical symptoms, ECG changes, troponin elevation. Document how patient meets or doesn't meet each criterion"</example>
                    </approach_1>
                    <approach_2>
                        <focus>Evidence Interpretation</focus>
                        <method>Demonstrate clinical correlation</method>
                        <example>"For each key finding, explain its significance. Example: ST elevation in contiguous leads suggests STEMI, while T wave inversion suggests ischemia"</example>
                    </approach_2>
                </specific_approaches>
            </feedback_strategy>
        </assessment_failures>
    </documentation_review>
</reflection>
```

## Plan Documentation Reflection Examples

### 1. Management Issues

```xml
<reflection>
    <documentation_review>
        <plan_failures>
            <management_issues>
                <test_ordering>
                    <observed_issues>
                        <inappropriate_selection>
                            Tests don't match diagnostic suspicion
                            Wrong test timing/sequence
                            Non-guideline-based testing
                            Redundant test ordering
                        </inappropriate_selection>
                        <implementation_problems>
                            Missing test specifications
                            Unclear ordering timeframe
                            Incomplete test parameters
                            Poor communication of urgency
                        </implementation_problems>
                    </observed_issues>
                    <impact>
                        Resource waste
                        Delayed diagnosis
                        Unnecessary testing
                        Poor patient experience
                    </impact>
                </test_ordering>

                <workup_elements>
                    <observed_issues>
                        <missing_components>
                            Incomplete diagnostic pathway
                            Skipped essential tests
                            Missing baseline studies
                            Overlooked guideline elements
                        </missing_components>
                        <sequence_issues>
                            Poor test ordering logic
                            Missed prerequisite testing
                            Inefficient workup flow
                            Delayed critical testing
                        </sequence_issues>
                    </observed_issues>
                    <impact>
                        Incomplete evaluation
                        Missed diagnoses
                        Care delays
                        Increased costs
                    </impact>
                </workup_elements>
            </management_issues>

            <feedback_strategy>
                <primary_strategy>Management Excellence Development</primary_strategy>
                <specific_approaches>
                    <approach_1>
                        <focus>Evidence-Based Testing</focus>
                        <method>Provide guideline-based frameworks</method>
                        <example>"For chest pain, document risk stratification first (HEART score), then match testing to risk level: Low risk - serial troponins; Intermediate risk - add stress test; High risk - immediate intervention"</example>
                    </approach_1>
                    <approach_2>
                        <focus>Testing Knowledge Gap</focus>
                        <method>Bolster clinical knowledge to improve diagnostic test ordering</method>
                        <example>"Ensure that tests ordered will help rule-out or evidence the diagnoses suspected; clinical knowledge of diagnostic criteria needs more development."</example>
                    </approach_2>
                </specific_approaches>
            </feedback_strategy>
        </plan_failures>
    </documentation_review>
</reflection>
```

### 2. Prioritization Issues

```xml
<reflection>
    <documentation_review>
        <plan_failures>
            <prioritization_issues>
                <test_aggressiveness>
                    <observed_issues>
                        <overutilization>
                            Excessive testing ordered
                            Unnecessary advanced imaging
                            Premature specialty testing
                            Redundant diagnostics
                        </overutilization>
                        <timing_problems>
                            Rush to advanced testing
                            Skipped basic workup
                            Inappropriate urgency
                            Poor test sequencing
                        </timing_problems>
                    </observed_issues>
                    <impact>
                        Resource waste
                        Patient burden
                        System strain
                        Cost inflation
                    </impact>
                </test_aggressiveness>

                <test_ranking>
                    <observed_issues>
                        <sequence_problems>
                            Advanced before basic testing
                            Poor cost consideration
                            Illogical test order
                            Missing stepwise approach
                        </sequence_problems>
                        <priority_issues>
                            Unclear test importance
                            Poor urgency communication
                            Missing rational progression
                            Inappropriate emphasis
                        </priority_issues>
                    </observed_issues>
                    <impact>
                        Inefficient care
                        Delayed diagnosis
                        Increased costs
                        Poor resource use
                    </impact>
                </test_ranking>
            </prioritization_issues>

            <feedback_strategy>
                <primary_strategy>Test Prioritization Development</primary_strategy>
                <specific_approaches>
                    <approach_1>
                        <focus>Stepwise Testing</focus>
                        <method>Demonstrate diagnostic algorithms</method>
                        <example>"Order tests in logical progression: 1) Basic labs/ECG first, 2) Risk-stratify based on results, 3) Add advanced testing only if indicated by initial results and risk level"</example>
                    </approach_1>
                    <approach_2>
                        <focus>Resource Stewardship</focus>
                        <method>Provide cost-effective frameworks</method>
                        <example>"Document reasoning for each test: 'Ordering basic labs first to risk-stratify; will only proceed to CT if initial workup suggests high risk'"</example>
                    </approach_2>
                    <approach_3>
                        <focus>Priority Communication</focus>
                        <method>Create clear testing hierarchy</method>
                        <example>"List tests in priority order with timing: STAT (ECG, troponin), Urgent (CBC, BMP), Routine (lipids). Explain why each test needed and how results will change management"</example>
                    </approach_3>
                </specific_approaches>
            </feedback_strategy>
        </plan_failures>
    </documentation_review>
</reflection>
```

---

## Checklist:

{checklist}

## Student Note:

{note}

