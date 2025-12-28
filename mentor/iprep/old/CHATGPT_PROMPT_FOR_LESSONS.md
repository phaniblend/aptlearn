# ChatGPT Prompt for Creating Algorithm Lessons

Copy and paste this prompt into ChatGPT to generate algorithm lessons:

---

**You are creating algorithm lessons for the INPACT LEARN platform. Your task is to create a complete, production-ready JSON lesson file following the Gold+ standard.**

## CONTEXT
- Platform: INPACT LEARN (interactive algorithm learning)
- Format: JSON file with structured flow
- Gold Standard Reference: `three-sum.json` (use as quality benchmark)
- Target: 900-1300+ lines per file, 90-140 unique stepIds

## LESSON TO CREATE
Create a lesson for: **[INSERT ALGORITHM NAME HERE]**
- Pattern: **[INSERT PATTERN: two-pointers, sliding-window, binary-search, linked-list, etc.]**
- Difficulty: **[INSERT: easy, medium, or hard]**
- LeetCode Problem: **[INSERT PROBLEM NUMBER IF APPLICABLE]**

## NON-NEGOTIABLE QUALITY BAR (Gold+ Standard)

### A) Beginner-Friendly Concept Gates
For EACH of the 5 languages (JavaScript, Python, Java, C++, TypeScript), include:
- `variable-check-{lang}` → Yes/No choice → explanation if No
- `function-check-{lang}` → Yes/No choice → explanation if No
- `parameter-check-{lang}` → Yes/No choice → explanation if No
- `array-check-{lang}` or `linked-list-check-{lang}` (as appropriate) → Yes/No choice → explanation if No
- `loop-check-{lang}` → Yes/No choice → explanation if No

Each explanation must include:
- `mentorSays`: Conversational explanation
- `example`: Algorithm-specific code example (not generic)
- `action: "continue"`
- `next`: Points to next step

### B) Problem Illustration (MUST BE CONCRETE)
- At least 2 concrete examples with real inputs/outputs
- Step-by-step walkthrough for the main example
- Explanation of what makes it tricky
- Common pitfalls
- Clear output format
- NO placeholder phrases like "Example input and output for..."

### C) Approach Exploration (REAL CHOICES)
- Provide 2-3 distinct approaches:
  - Brute force / naive approach
  - Optimized approach (the intended pattern)
  - Alternative approach (if applicable)
- Each choice MUST lead to different content
- Each approach needs a mini-walkthrough
- If one approach is inferior, teach it briefly then transition to optimized

### D) Incremental Code Building (6-10 STEPS PER LANGUAGE)
For EACH language, break coding into 6-10 micro-steps:
- Each step adds ONE concept
- Each step includes:
  - `mentorSays`: Explaining WHY this step exists
  - `example`: Working code snippet (compilable/runnable by final step)
- Pattern: `coding-start` → `coding-init-vars` → `coding-{main-logic-step-1}` → `coding-{main-logic-step-2}` → ... → `coding-return`
- Code must be algorithm-specific, not generic templates

### E) Test Cases (4-6 RIGOROUS TESTS)
- Include edge cases: empty, minimal, duplicates, boundary conditions
- Each test case must have expected output
- Tests must match the algorithm exactly

### F) Navigation Integrity
- All `next` pointers must exist
- No orphan/unreachable steps
- All language paths converge to shared `final` step
- Consistent flow: `title` → `problem-illustration` → `thinking-challenge` → `approach-exploration` → `language-selection` → `concept-gates` → `coding-steps` → `test-code` → `final`

### G) Final Step
Must include:
- Time complexity
- Space complexity
- Key takeaways (3-5 bullet points)
- Related practice problems (1-2 suggestions)

## STYLE RULES
- Mentor voice: Conversational, confident, minimal fluff, no corporate tone
- Use concrete variable names and arrays
- Explicitly describe pointer/window movement in plain English
- Repeat the "why" behind each move
- Avoid generic phrases unless followed by concrete example
- Never use placeholders like "[problem]", "[X]", "Example input and expected output for"

## JSON STRUCTURE TEMPLATE

```json
{
  "id": "algorithm-name",
  "title": "Algorithm Title",
  "pattern": "two-pointers",
  "difficulty": "medium",
  "language": "javascript",
  "status": "draft",
  "flow": [
    {
      "stepId": "title",
      "mentorSays": "At the end of this lesson, you will be able to:\n\n1. [Learning objective 1]\n2. [Learning objective 2]\n3. [Learning objective 3]\n4. [Learning objective 4]\n5. [Learning objective 5]",
      "action": "continue",
      "next": "problem-illustration"
    },
    {
      "stepId": "problem-illustration",
      "mentorSays": "[Detailed problem explanation with 2+ concrete examples, step-by-step walkthrough, what makes it tricky, common pitfalls]",
      "example": "[Visual representation of examples]",
      "action": "continue",
      "next": "thinking-challenge"
    },
    {
      "stepId": "thinking-challenge",
      "mentorSays": "Now that you understand what the problem wants, here's the real question:\n\nHow would YOU solve this?\n\nThink about it for a moment. What approach feels natural to you?",
      "choices": [
        {
          "label": "[Approach 1 description]",
          "next": "explore-approach-1"
        },
        {
          "label": "[Approach 2 description]",
          "next": "explore-approach-2"
        },
        {
          "label": "[Approach 3 description]",
          "next": "explore-approach-3"
        }
      ]
    },
    {
      "stepId": "explore-approach-1",
      "mentorSays": "[Explain approach, show it works, mention complexity, transition to optimized]",
      "action": "continue",
      "next": "explore-approach-2"
    },
    {
      "stepId": "explore-approach-2",
      "mentorSays": "[Detailed explanation of optimized approach with algorithm, why it works, step-by-step trace]",
      "action": "continue",
      "next": "language-selection"
    },
    {
      "stepId": "language-selection",
      "mentorSays": "Great! Now let's code this solution. Which programming language would you like to use?",
      "choices": [
        {
          "label": "JavaScript",
          "next": "variable-check-js"
        },
        {
          "label": "Python",
          "next": "variable-check-python"
        },
        {
          "label": "Java",
          "next": "variable-check-java"
        },
        {
          "label": "C++",
          "next": "variable-check-cpp"
        },
        {
          "label": "TypeScript",
          "next": "variable-check-ts"
        }
      ]
    },
    // For EACH language, include:
    // - variable-check-{lang} (with Yes/No choice)
    // - variable-explanation-{lang} (if No chosen)
    // - function-check-{lang}
    // - function-explanation-{lang} (if No chosen)
    // - parameter-check-{lang}
    // - parameter-explanation-{lang} (if No chosen)
    // - array-check-{lang} or linked-list-check-{lang}
    // - array-explanation-{lang} or linked-list-explanation-{lang} (if No chosen)
    // - loop-check-{lang}
    // - loop-explanation-{lang} (if No chosen)
    // - coding-start-{lang}
    // - coding-init-vars-{lang}
    // - coding-{step-1}-{lang}
    // - coding-{step-2}-{lang}
    // - ... (6-10 total coding steps)
    // - coding-return-{lang}
    // - test-code-{lang}
    {
      "stepId": "final",
      "mentorSays": "🎉 Well done! [Recap with key takeaways, time/space complexity, related problems]",
      "action": "continue"
    }
  ]
}
```

## OUTPUT REQUIREMENTS
1. Output ONLY valid JSON (no markdown, no explanations outside JSON)
2. Do NOT truncate - include complete file
3. Ensure all `next` pointers are valid
4. Validate JSON structure before outputting
5. Target 900-1300+ lines for complex algorithms, 800+ for simpler ones

## EXAMPLE QUALITY CHECKLIST
- [ ] 2+ concrete examples in problem-illustration
- [ ] Step-by-step walkthrough included
- [ ] 2-3 approach choices (not fake choices)
- [ ] All 5 languages have concept gates (variable, function, parameter, array/list, loop)
- [ ] Each language has 6-10 incremental coding steps
- [ ] Each coding step has `mentorSays` explaining WHY
- [ ] Code is algorithm-specific, not generic
- [ ] 4-6 test cases with expected outputs
- [ ] Final step includes complexity analysis
- [ ] All navigation paths converge to `final`
- [ ] No placeholder phrases
- [ ] Conversational mentor tone throughout

## ALGORITHM-SPECIFIC NOTES
**[INSERT ANY ALGORITHM-SPECIFIC REQUIREMENTS HERE]**

For example:
- If it's a two-pointer problem: Explain why moving the smaller pointer is optimal
- If it's a sliding window: Explain window expansion/shrinking logic
- If it's binary search: Explain the comparison and pointer movement
- If it's a linked list: Explain pointer manipulation and null handling

---

**Now create the complete JSON lesson file for [ALGORITHM NAME]. Output ONLY the JSON, no explanations or markdown.**

