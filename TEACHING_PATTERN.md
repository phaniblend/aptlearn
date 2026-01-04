# APT Learn Teaching Pattern - Instruction Set

## Core Philosophy
**Beginner-first, mentor-led, interactive learning.** Never assume prior knowledge. Every new concept must be introduced with a knowledge check.

## Fundamental Blocks vs Advanced Lessons

### Fundamental Blocks (Level 1 - First 10 Algorithms)
These lessons are the foundation. They include **FULL knowledge checks** for:
- Arrays & indexing
- Variables
- Functions/methods
- Parameters (how values are passed to functions)
- Loops
- Function calls (showing how to call functions with actual values)

**Purpose**: Build complete understanding from scratch. No assumptions.

### Advanced Lessons (Level 2+)
These lessons assume knowledge of fundamental concepts. They only check for **NEW concepts** that haven't been introduced yet:
- If a new data structure is introduced (e.g., hash map, stack) → check for it
- If a new pattern is introduced (e.g., recursion, backtracking) → check for it
- If a new concept is introduced (e.g., pointers, references) → check for it

**Purpose**: Focus on the new pattern/concept, not re-teaching basics.

---

## 1. PREREQUISITE KNOWLEDGE CHECKS (MANDATORY)

### Rule 1.1: Check Before Teaching
- **Every new concept** must have a knowledge check BEFORE it's used
- Examples: arrays, indices, functions, loops, hash maps, etc.
- Format: "Do you know what [concept] is?"
- Options: "Yes, I know [concept]" / "No, explain [concept]"

### Rule 1.2: Explanation Structure
If learner says "No":
- Provide a simple, beginner-friendly explanation
- Use a concrete example (not abstract)
- Keep it short (2-3 sentences max)
- Show a code example if applicable
- Then continue to the main flow

### Rule 1.3: Order of Checks
Check prerequisites in this order:
1. Arrays & indexing (if working with arrays)
2. Variables (if using variables/parameters)
3. Functions/methods (if writing code)
4. Parameters (if function has parameters - explain how values are passed)
5. Loops (if using loops)
6. Data structures (if using hash maps, etc.)

### Rule 1.4: Variable Knowledge Check
- **Before introducing parameters**, check if learner knows what variables are
- If "No": Explain variables as labeled boxes that store values
- Show example: `let numbers = [5, 10, 15, 20]` where 'numbers' is a variable storing an array

### Rule 1.5: Parameter Explanation
- **After function explanation**, if function has parameters, explain:
  - Parameters are like variables that receive values when you call the function
  - Show how to call the function with actual values
  - Demonstrate: `function printArray(arr)` → `printArray([5, 10, 15, 20])` where the array goes into 'arr'
  - Never show function code without showing how to call it

---

## 2. LESSON STRUCTURE (MANDATORY ORDER)

### Rule 2.1: Title/Welcome
- Brief welcome message
- Set expectations
- No technical jargon

### Rule 2.2: Prerequisite Check
- Start with array/index knowledge check
- Only proceed after confirming understanding

### Rule 2.3: Problem Illustration
- **BEFORE any challenge**, clearly explain what the problem is asking
- Use a concrete example: `[2, 6, 7, 9]` with `target = 9`
- Show the answer: `[0, 2]` and explain WHY
- This is NOT the solution process, just clarification of the problem

### Rule 2.4: Thinking Challenge
- Ask: "How would YOU try to find these indices?"
- Provide 2-3 approach options
- Do NOT indicate which is "correct"
- Let learner choose their approach

### Rule 2.5: Explore Chosen Approach
- Validate their choice positively
- Walk through their approach step-by-step
- Use the same concrete example throughout
- Show the thinking process, not just the answer

### Rule 2.6: Language Selection
- After exploring the approach, ask: "Which programming language?"
- Options: JavaScript, Python, Java, C++, TypeScript
- Each language path is independent

### Rule 2.7: Function Knowledge Check
- Before showing any code, check: "Do you know what a function is?"
- Language-specific terminology (method for Java, function for others)

### Rule 2.8: Loop Knowledge Check (if using loops)
- Before showing loops, check: "Do you know what a loop is?"
- Explain if needed with simple example

### Rule 2.9: Step-by-Step Coding
Break coding into clear steps:
1. **Variable check** (if using variables/parameters)
   - Check if learner knows what variables are
   - Explain variables as labeled boxes that store values
2. **Function check** (if writing functions)
   - Check if learner knows what functions are
   - Explain functions as reusable blocks of code
3. **Parameter check** (if function has parameters)
   - Check if learner knows what parameters are
   - Explain parameters receive values when function is called
   - Show how to call the function with actual values
   - NEVER show function code without showing how to call it
4. **Outer loop explanation** (if applicable)
   - Map pseudocode to syntax
   - Show what happens with concrete example: "When i=0, picks 2; when i=1, picks 6..."
5. **Inner loop explanation** (if applicable)
   - Map pseudocode to syntax
   - Show relationship: "When outer picks 2, inner picks 6, 7, 9 one by one"
6. **Complete solution**
   - Show final code
   - **ALWAYS show function call with example values**
   - Include trace example showing execution

### Rule 2.10: Test Step
- Ask learner to test with the example
- Show expected input/output
- Encourage trying in IDE

### Rule 2.11: Recommendation (if applicable)
- If learner chose a less efficient approach (e.g., brute force)
- After completion, recommend: "There's a more efficient method..."
- Give choice: "Would you like to learn it?" / "No, I'm done"
- If "Yes", redirect to the efficient approach

### Rule 2.12: Final Completion
- Celebration message
- Reinforce learning
- Encourage practice

---

## 3. CONTENT GUIDELINES

### Rule 3.1: No Assumptions
- Never assume learner knows arrays, indices, functions, loops
- Never assume they understand Big-O notation
- Never assume they know data structures

### Rule 3.2: No Big-O Discussion
- **NEVER mention**: Big-O, O(n), O(n²), time complexity, space complexity
- If need to justify efficiency, say: "This works but can get slow on large inputs"
- Use plain language only

### Rule 3.3: No External Links
- All explanations must be self-contained
- No w3schools, no documentation links
- Keep everything inside the lesson

### Rule 3.4: Concrete Examples
- Always use the same concrete example throughout: `[2, 6, 7, 9]` with `target = 9`
- Show step-by-step execution
- Map each line of code to what happens with the example

### Rule 3.5: Pseudocode to Syntax Mapping
- When teaching code, map pseudocode to actual syntax
- Example: "Use a for loop to pick the first element" → Show `for (let i = 0; i < nums.length; i++)`
- Explain what each part does with the concrete example

### Rule 3.6: One Concept at a Time
- Don't introduce multiple new concepts in one step
- Break complex ideas into smaller steps
- Each step should teach ONE thing

---

## 4. TONE & STYLE

### Rule 4.1: Conversational Mentor
- Use "you" and "we"
- Friendly, encouraging tone
- "Let's build this step by step"
- "Great thinking!"
- "Perfect!"

### Rule 4.2: Short Instructions
- One instruction per step
- Keep `mentorSays` concise (2-4 sentences max)
- Break long explanations into multiple steps

### Rule 4.3: Directive, Not Passive
- "Let's build this step by step"
- "Now we need to..."
- "For each element picked by the outer loop..."
- Active, guiding language

### Rule 4.4: Positive Reinforcement
- Validate learner's choices: "That's a solid approach!"
- "Excellent thinking!"
- "Great job!"
- Never criticize their approach choice

---

## 5. INTERACTIVE ELEMENTS

### Rule 5.1: Choices, Not Lectures
- Present options, let learner choose
- Don't tell them which is "best" upfront
- Guide them through their chosen path

### Rule 5.2: Branching Paths
- Different approaches lead to different coding paths
- All paths should eventually converge or offer next steps
- Never dead-end a path

### Rule 5.3: Recommendations, Not Forced
- After less efficient approach, recommend better one
- Give choice: learn it now or finish
- Don't force them to learn everything

---

## 6. CODE PRESENTATION

### Rule 6.1: Progressive Disclosure
- Start with function skeleton
- Add outer loop
- Add inner loop (if needed)
- Add condition/check
- Show complete solution last

### Rule 6.2: Inline Comments
- Use comments to explain what each part does
- Show concrete values: "When i=0, nums[i] = 2"
- Map execution to example array

### Rule 6.3: Trace Examples
- In final solution, include execution trace
- Show: "When i=0, j=1: 2+6=8 (not 9)"
- Show: "When i=0, j=2: 2+7=9 ✓ Return [0,2]"

---

## 7. ERROR HANDLING

### Rule 7.1: No Wrong Choices
- Every approach choice is valid
- Guide them through their choice
- If approach has issues, explain gently and redirect

### Rule 7.2: Alternative Paths
- If learner chooses problematic approach (e.g., sorting)
- Explain the issue
- Offer alternative approaches to choose from
- Don't force a specific path

---

## 8. COMPLETION

### Rule 8.1: Celebration
- Always end with positive message
- "🎉 Well done!"
- Reinforce what they learned

### Rule 8.2: Next Steps
- If they completed less efficient approach, recommend efficient one
- If they completed efficient approach, celebrate and finish
- Give clear choices

---

## 9. LANGUAGE-SPECIFIC CONSIDERATIONS

### Rule 9.1: Terminology
- Java: "method" not "function"
- Python: "function" or "def"
- Others: "function"

### Rule 9.2: Syntax Differences
- Adapt explanations to language syntax
- Show language-specific examples
- Keep the same teaching pattern across languages

---

## 10. VALIDATION CHECKLIST

Before finalizing a lesson, verify:

- [ ] Prerequisite checks for arrays/indices
- [ ] Prerequisite checks for functions
- [ ] Prerequisite checks for loops (if used)
- [ ] Problem illustration BEFORE challenge
- [ ] Thinking challenge with choices
- [ ] Step-by-step exploration of chosen approach
- [ ] Language selection
- [ ] Function knowledge check
- [ ] Loop knowledge check (if needed)
- [ ] Progressive code disclosure
- [ ] Pseudocode-to-syntax mapping
- [ ] Concrete example throughout
- [ ] Test step
- [ ] Recommendation (if applicable)
- [ ] Final celebration

---

## Example Flow Summary

```
1. Welcome
2. Array knowledge check → Array explanation (if needed)
3. Problem illustration (what problem asks)
4. Thinking challenge (choose approach)
5. Explore chosen approach
6. Language selection
7. Function knowledge check → Function explanation (if needed)
8. Loop knowledge check → Loop explanation (if needed)
9. Outer loop coding step
10. Inner loop coding step (if applicable)
11. Complete solution
12. Test step
13. Recommendation (if brute force) → Hashmap path OR Final
14. Final celebration
```

---

**Remember: The goal is to teach thinking, not just solutions. Every step should build understanding, not just show code.**

