# APTLEARN Development Continuation Guide

**Last Updated:** December 2024  
**Purpose:** Complete guide for continuing APTLEARN development on a new machine

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [System Architecture](#system-architecture)
3. [Lesson Structure & JSON Format](#lesson-structure--json-format)
4. [Lesson Creation Process](#lesson-creation-process)
5. [Quality Standards](#quality-standards)
6. [Current Development Status](#current-development-status)
7. [How to Continue Development](#how-to-continue-development)
8. [Common Patterns & Examples](#common-patterns--examples)
9. [Troubleshooting](#troubleshooting)

---

## Project Overview

**APTLEARN** is an interactive algorithm learning platform that teaches 125+ algorithms through step-by-step, mentor-led lessons. The system uses a JSON-based architecture with a Node.js backend and static HTML/JS frontend.

### Key Features

- **125+ Algorithm Lessons**: Covering sorting, searching, dynamic programming, two pointers, sliding window, etc.
- **5 Language Support**: JavaScript, Python, Java, C++, TypeScript
- **Progressive Learning**: Step-by-step incremental coding with explanations
- **Prerequisite System**: Knowledge checks before lessons
- **Level System**: Progressive difficulty levels with level-up messages
- **Interactive Code Lessons (ICLs)**: Main algorithm teaching system
- **Knowledge Check Questions (KCQs)**: Verify understanding of concepts

### Tech Stack

- **Backend**: Node.js/Express
- **Frontend**: Static HTML/CSS/JavaScript
- **Data**: JSON files for lessons, prerequisites, concepts
- **No Database**: All data stored in JSON files

---

## System Architecture

### Directory Structure

```
APTLEARN/
├── mentor-backend/                    # Backend Server
│   ├── src/
│   │   ├── server.js                  # Main Express server
│   │   ├── mentor/
│   │   │   ├── lesson-engine.js       # Lesson loading & navigation
│   │   │   ├── prerequisite-engine.js # Prerequisites & levels
│   │   │   ├── mentor-router.js       # API endpoints
│   │   │   ├── ai-helper.js           # AI question answering
│   │   │   └── question-cache.js       # Question caching
│   │   └── ide/
│   │       ├── file-api.js            # File operations
│   │       └── execute-api.js         # Code execution
│   │
│   └── mentor/                        # Data Files
│       ├── lessons/                   # Individual lesson files
│       │   ├── index.json             # Lesson metadata index
│       │   ├── two-sum.json           # Lesson: Two Sum
│       │   ├── bubble-sort.json       # Lesson: Bubble Sort
│       │   └── ... (152 total files)
│       │
│       ├── prerequisites.json         # Concepts + Levels + Mappings
│       │   ├── concepts: {...}        # Concept definitions
│       │   ├── levels: {...}          # Level definitions
│       │   ├── lessonLevels: {...}    # Lesson → Level mapping
│       │   └── lessonPrerequisites: {...}  # Lesson → Concepts mapping
│       │
│       └── questions-cache.json       # AI question cache
│
├── ide-frontend/                      # Frontend
│   ├── learn.html                     # Main lesson page
│   ├── algos.html                     # Algorithm listing page
│   ├── assets/
│   │   ├── app.js                     # Navigation utilities
│   │   ├── concept-explainer.js       # ICL Tool component
│   │   └── styles.css                 # Main styles
│
└── scripts/                           # Development scripts
    └── (various Python scripts for lesson generation)
```

### Data Flow

```
User Browser
    ↓
Frontend (learn.html, algos.html)
    ↓
Express API Server (server.js)
    ↓
Lesson Engine / Prerequisite Engine
    ↓
JSON Files (lessons/*.json, prerequisites.json)
```

### API Endpoints

- `GET /api/mentor/lesson?lessonId={id}` - Get lesson data
- `GET /api/mentor/lesson/step?lessonId={id}&stepId={step}` - Get specific step
- `GET /api/mentor/prerequisites?lessonId={id}` - Get prerequisites
- `POST /api/mentor/test/validate` - Validate knowledge check
- `GET /api/mentor/level?level={n}` - Get level information
- `GET /api/mentor/level/kc?level={n}&language={lang}` - Get level knowledge check

---

## Lesson Structure & JSON Format

### Basic Lesson File Structure

Each lesson is a JSON file in `mentor-backend/mentor/lessons/` with the following structure:

```json
{
  "id": "bubble-sort",
  "title": "Bubble sort",
  "pattern": "sorting",
  "difficulty": "easy",
  "language": "javascript",
  "status": "draft",
  "flow": [
    // Array of step objects
  ]
}
```

### Metadata Fields

- **id**: Unique identifier (kebab-case, e.g., "bubble-sort", "two-sum")
- **title**: Display name (e.g., "Bubble sort", "Two Sum")
- **pattern**: Algorithm pattern (e.g., "sorting", "hash-map", "two-pointers", "sliding-window")
- **difficulty**: "easy", "medium", "hard"
- **language**: Default language ("javascript")
- **status**: "draft" or "complete"

### Step Types

#### 1. Continue Step (Single Action)

```json
{
  "stepId": "title",
  "mentorSays": "At the end of this lesson, you will be able to:\n\n1. Understand...\n2. Implement...",
  "action": "continue",
  "next": "problem-illustration"
}
```

#### 2. Choice Step (User Selection)

```json
{
  "stepId": "thinking-challenge",
  "mentorSays": "How would YOU implement this?",
  "choices": [
    {
      "label": "Use nested loops",
      "next": "explore-nested-loops"
    },
    {
      "label": "Use recursion",
      "next": "explore-recursion"
    }
  ]
}
```

#### 3. Knowledge Check Step

```json
{
  "stepId": "variable-check-js",
  "mentorSays": "Before we start coding, let me ask: Do you know what a variable is in JavaScript?",
  "choices": [
    {
      "label": "Yes, I know variables",
      "next": "function-check-js"
    },
    {
      "label": "No, explain variables",
      "next": "variable-explanation-js"
    }
  ]
}
```

#### 4. Explanation Step

```json
{
  "stepId": "variable-explanation-js",
  "mentorSays": "A variable is like a labeled box where you can store a value...",
  "example": "let temp = 0;\n\n// Later use:\ntemp = 5;",
  "action": "continue",
  "next": "function-check-js"
}
```

#### 5. Coding Step (Incremental)

```json
{
  "stepId": "coding-start-js",
  "mentorSays": "Perfect! Let's implement bubble sort in JavaScript. We'll use nested loops...",
  "example": "function bubbleSort(arr) {\n    // Your code here\n}",
  "action": "continue",
  "next": "coding-outer-loop-js"
}
```

#### 6. Test Code Step

```json
{
  "stepId": "test-code-js",
  "mentorSays": "Perfect! Now test your code with the example we used earlier:\n\narr = [5, 2, 8, 1, 9]...",
  "example": "Test input:\narr = [5, 2, 8, 1, 9]\n\nAfter bubbleSort(arr):\n[1, 2, 5, 8, 9]",
  "action": "continue",
  "next": "final"
}
```

#### 7. Final Step

```json
{
  "stepId": "final",
  "mentorSays": "🎉 Congratulations! You've completed the Bubble Sort lesson...",
  "action": "complete"
}
```

### Standard Lesson Flow

```
1. title
   ↓
2. problem-illustration
   ↓
3. thinking-challenge (choices: approach selection)
   ↓
4. explore-{approach} (explanation of chosen approach)
   ↓
5. language-selection (choices: JavaScript, Python, Java, C++, TypeScript)
   ↓
6. {concept}-check-{lang} (knowledge checks for prerequisites)
   ↓
7. {concept}-explanation-{lang} (if user doesn't know)
   ↓
8. coding-start-{lang}
   ↓
9. coding-{step1}-{lang}
   ↓
10. coding-{step2}-{lang}
   ↓
11. ... (more incremental coding steps)
   ↓
12. test-code-{lang}
   ↓
13. final
```

---

## Lesson Creation Process

### Step-by-Step Process

1. **Choose Algorithm**: Identify which algorithm to create (check `mentor-backend/mentor/lessons/index.json` for existing lessons)

2. **Create JSON File**: Create `{algorithm-id}.json` in `mentor-backend/mentor/lessons/`

3. **Set Metadata**: Fill in id, title, pattern, difficulty, language, status

4. **Create Title Step**: Learning goals for the lesson

5. **Create Problem Illustration**: 
   - Explain what the problem asks
   - Use a concrete example (same example throughout lesson)
   - Show step-by-step trace if applicable
   - Include visual representation in `example` field

6. **Create Thinking Challenge**: 
   - Ask "How would YOU solve this?"
   - Provide 2-3 approach choices
   - Each choice leads to an exploration step

7. **Create Approach Exploration Steps**:
   - For each approach, explain how it works
   - Walk through the example step-by-step
   - Discuss time/space complexity
   - Explain when it's applicable
   - Guide to language selection

8. **Create Language Selection**: 
   - Choices for all 5 languages
   - Each leads to language-specific path

9. **Create Knowledge Check Steps** (for each language):
   - Check prerequisites: variable, function, parameter, array, loop
   - Use format: `{concept}-check-{lang}`
   - Provide explanation steps: `{concept}-explanation-{lang}`

10. **Create Coding Steps** (for each language):
    - Start with `coding-start-{lang}`
    - Break solution into 5-8 incremental steps
    - Each step builds on previous
    - Use descriptive step IDs: `coding-{action}-{lang}`
    - Examples:
      - `coding-outer-loop-js`
      - `coding-inner-loop-js`
      - `coding-swap-js`
      - `coding-base-case-js`
      - `coding-find-mid-js`
      - `coding-split-js`
      - `coding-merge-js`

11. **Create Test Code Step**: 
    - Use same example from problem illustration
    - Show expected output
    - Format: `test-code-{lang}`

12. **Create Final Step**: 
    - Congratulatory message
    - Summary of what was learned
    - `stepId: "final"`, `action: "complete"`

### Language-Specific Paths

Each language must have:
- Knowledge checks (variable, function, parameter, array, loop)
- Coding steps (5-8 incremental steps)
- Test code step
- All paths converge to `final` step

### Naming Conventions

- **Step IDs**: `{category}-{description}-{lang}`
  - Examples: `coding-start-js`, `variable-check-python`, `explore-nested-loops`
- **Language Suffixes**: `js`, `python`, `java`, `cpp`, `ts`
- **Approach IDs**: `explore-{approach-name}` (e.g., `explore-nested-loops`, `explore-recursion`)

---

## Quality Standards

### Required Elements

1. **Problem Illustration**:
   - ✅ Clear explanation of what the problem asks
   - ✅ Concrete example (same throughout lesson)
   - ✅ Step-by-step trace showing how algorithm works
   - ✅ Visual representation in `example` field

2. **Approach Exploration**:
   - ✅ Explain HOW the approach works (not just "this is better")
   - ✅ Walk through example step-by-step
   - ✅ Time/space complexity analysis
   - ✅ When to use this approach
   - ✅ For alternative approaches: explain why they're less suitable (not dismissive)

3. **Incremental Coding Steps**:
   - ✅ **5-8 steps per language** (not just 3)
   - ✅ Each step builds understanding incrementally
   - ✅ Start with function skeleton
   - ✅ Add variables/pointers
   - ✅ Add loops/conditions
   - ✅ Add logic
   - ✅ Show complete solution gradually

4. **Language-Specific Content**:
   - ✅ Correct syntax for each language
   - ✅ Language-appropriate explanations
   - ✅ Proper variable naming conventions
   - ✅ Language-specific examples

5. **Knowledge Checks**:
   - ✅ Check all relevant prerequisites
   - ✅ Provide explanations if user doesn't know
   - ✅ Use specific check IDs (e.g., `main-variables-check-js` not `variable-check-js`)

6. **Navigation**:
   - ✅ All `next` fields point to valid step IDs
   - ✅ All paths eventually reach `final`
   - ✅ No orphaned steps
   - ✅ Language paths converge correctly

### Common Mistakes to Avoid

❌ **Too Few Coding Steps**: Only 3 steps instead of 5-8
❌ **Dismissive Approach Explanations**: "This doesn't work" instead of explaining why
❌ **Generic Knowledge Checks**: Using generic IDs instead of specific ones
❌ **Incorrect Syntax**: Wrong syntax examples for languages
❌ **Broken Navigation**: `next` fields pointing to non-existent steps
❌ **Missing Language Paths**: Not all 5 languages have complete paths
❌ **Duplicate Steps**: Same step ID appearing multiple times
❌ **Wrong Step Order**: Steps in reverse order in JSON (works but confusing)

### Quality Checklist

Before marking a lesson as complete:

- [ ] All 5 languages have complete paths
- [ ] Each language has 5-8 incremental coding steps
- [ ] Problem illustration uses concrete example
- [ ] Approach exploration explains HOW, not just WHAT
- [ ] All knowledge checks have corresponding explanations
- [ ] All `next` fields are valid
- [ ] Test code step uses same example
- [ ] Final step exists and is reachable
- [ ] No duplicate step IDs
- [ ] Syntax is correct for all languages
- [ ] JSON is valid (no syntax errors)

---

## Current Development Status

### Completed Lessons

As of December 2024, **32+ lessons are fully complete** with all 5 language paths. Examples:
- `two-sum.json`
- `bubble-sort.json`
- `move-zeros-to-end.json`
- `smallest-subarray-sum-s.json`
- `selection-sort.json`
- `insertion-sort.json`
- `merge-sort.json` (recently fixed - duplicate Python steps removed)
- `quick-sort.json`
- `heap-sort.json`

### Recently Completed

- **Sorting Algorithms**: Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort, Heap Sort
- **Sliding Window**: Smallest Subarray Sum S, Count Subarrays Size K (redone for quality)
- **Two Pointers**: Move Zeros to End

### In Progress / Needs Work

- Some lessons may have incomplete language paths
- Some lessons may need quality improvements (more coding steps, better approach exploration)
- Check `mentor-backend/mentor/lessons/index.json` for status of all 152 lessons

### Lesson Files Location

- **Main Directory**: `mentor-backend/mentor/lessons/`
- **Completed Backup**: `mentor-backend/mentor/lessons/completed/` (some completed lessons are backed up here)

---

## How to Continue Development

### Setup on New Machine

1. **Clone Repository**:
   ```bash
   git clone <repository-url>
   cd APTLEARN
   ```

2. **Install Dependencies**:
   ```bash
   cd mentor-backend
   npm install
   ```

3. **Verify Structure**:
   - Check `mentor-backend/mentor/lessons/` has all lesson files
   - Check `mentor-backend/mentor/prerequisites.json` exists
   - Check `mentor-backend/src/server.js` exists

4. **Start Server** (if needed for testing):
   ```bash
   cd mentor-backend
   node src/server.js
   ```

### Creating a New Lesson

1. **Choose Algorithm**: Check `mentor-backend/mentor/lessons/index.json` to see what's missing

2. **Use Template**: Copy `bubble-sort.json` or `two-sum.json` as a template

3. **Follow Process**: Use the "Lesson Creation Process" section above

4. **Test Navigation**: Ensure all `next` fields are valid

5. **Validate JSON**: Use a JSON validator to check syntax

6. **Quality Check**: Use the quality checklist above

### Completing Incomplete Lessons

1. **Identify Incomplete Lesson**: Check lesson file for missing language paths

2. **Check Pattern**: Look at similar completed lessons (e.g., for sorting algorithms, use `bubble-sort.json`)

3. **Add Missing Paths**: 
   - Add knowledge checks
   - Add coding steps (5-8 steps)
   - Add test code step
   - Ensure navigation converges to `final`

4. **Verify**: Check all `next` fields, test JSON validity

### Fixing Quality Issues

Common fixes needed:

1. **Add More Coding Steps**: Break down solution into smaller increments
2. **Improve Approach Exploration**: Add detailed explanations, complexity analysis
3. **Fix Navigation**: Ensure all `next` fields point to valid steps
4. **Fix Syntax**: Correct language-specific syntax errors
5. **Remove Duplicates**: Check for duplicate step IDs

### Using Scripts

There are Python scripts in `mentor-backend/scripts/` for:
- Generating lesson templates
- Completing language paths
- Checking lesson quality

**Note**: Scripts may need manual adjustment. Always review generated content.

---

## Common Patterns & Examples

### Pattern 1: Sorting Algorithms

**Template**: `bubble-sort.json`

**Structure**:
1. Title → Problem Illustration (trace through sorting)
2. Thinking Challenge → Approach choices (nested loops, single loop, recursion)
3. Explore chosen approach → Language selection
4. Knowledge checks → Coding steps → Test → Final

**Coding Steps Pattern**:
- `coding-start-{lang}`: Function skeleton
- `coding-outer-loop-{lang}`: Outer loop for passes
- `coding-inner-loop-{lang}`: Inner loop for comparisons
- `coding-swap-{lang}`: Swap logic
- `coding-optimization-{lang}`: Optional optimization
- `test-code-{lang}`: Test with example
- `final`: Complete

### Pattern 2: Two Pointers

**Template**: `move-zeros-to-end.json`

**Structure**:
1. Title → Problem Illustration
2. Thinking Challenge → Approach choices
3. Explore approach → Language selection
4. Knowledge checks → Coding steps → Test → Final

**Coding Steps Pattern**:
- `coding-start-{lang}`: Function skeleton
- `coding-initialize-pointers-{lang}`: Initialize two pointers
- `coding-traverse-{lang}`: Traverse array
- `coding-swap-{lang}`: Swap when condition met
- `coding-return-{lang}`: Return result
- `test-code-{lang}`: Test
- `final`: Complete

### Pattern 3: Sliding Window

**Template**: `smallest-subarray-sum-s.json`

**Structure**:
1. Title → Problem Illustration
2. Thinking Challenge → Approach choices (formula, loop, sliding window)
3. Explore each approach in detail → Language selection
4. Knowledge checks → Coding steps → Test → Final

**Coding Steps Pattern** (for sliding window):
- `coding-start-{lang}`: Function skeleton
- `coding-initialize-variables-{lang}`: Window start, end, sum, min
- `coding-expand-window-{lang}`: Expand window (add elements)
- `coding-shrink-window-{lang}`: Shrink window (remove elements)
- `coding-update-result-{lang}`: Update minimum length
- `coding-return-{lang}`: Return result
- `test-code-{lang}`: Test
- `final`: Complete

### Pattern 4: Divide and Conquer (Merge Sort, Quick Sort)

**Template**: `merge-sort.json`, `quick-sort.json`

**Structure**:
1. Title → Problem Illustration (show divide, conquer, combine)
2. Thinking Challenge → Approach choices (recursion, iteration)
3. Explore recursive approach → Language selection
4. Knowledge checks → Coding steps (main function + helper) → Test → Final

**Coding Steps Pattern**:
- `coding-start-{lang}`: Function skeleton
- `coding-base-case-{lang}`: Base case (0 or 1 element)
- `coding-find-mid-{lang}`: Find middle index
- `coding-split-{lang}`: Split into halves
- `coding-recursive-sort-{lang}`: Recursive calls
- `coding-merge-call-{lang}` or `coding-partition-call-{lang}`: Call helper
- `coding-merge-start-{lang}` or `coding-partition-start-{lang}`: Helper function
- `coding-merge-init-{lang}` or `coding-partition-init-{lang}`: Initialize
- `coding-merge-compare-{lang}` or `coding-partition-loop-{lang}`: Main logic
- `coding-merge-remaining-{lang}` or `coding-partition-place-{lang}`: Handle remaining
- `test-code-{lang}`: Test
- `final`: Complete

### Knowledge Check Pattern

For each language, check prerequisites:

```json
{
  "stepId": "variable-check-js",
  "mentorSays": "Before we start coding, let me ask: Do you know what a variable is in JavaScript?",
  "choices": [
    { "label": "Yes, I know variables", "next": "function-check-js" },
    { "label": "No, explain variables", "next": "variable-explanation-js" }
  ]
},
{
  "stepId": "variable-explanation-js",
  "mentorSays": "A variable is like a labeled box...",
  "example": "let temp = 0;",
  "action": "continue",
  "next": "function-check-js"
}
```

Repeat for: variable, function, parameter, array, loop (as needed for the algorithm).

---

## Troubleshooting

### Issue: JSON Syntax Error

**Symptoms**: File won't load, JSON parser error

**Solution**:
1. Use JSON validator (online or VS Code extension)
2. Check for:
   - Missing commas
   - Trailing commas
   - Unclosed brackets/braces
   - Unescaped quotes in strings

### Issue: Navigation Broken

**Symptoms**: Lesson stops, can't proceed, "step not found" error

**Solution**:
1. Check all `next` fields point to valid `stepId` values
2. Ensure all step IDs are unique
3. Verify all paths eventually reach `final`
4. Use grep to find all step IDs: `grep -r "stepId" lesson.json`

### Issue: Missing Language Path

**Symptoms**: Some languages don't have coding steps

**Solution**:
1. Check if `coding-start-{lang}` exists
2. Add knowledge checks for that language
3. Add coding steps (5-8 steps)
4. Add `test-code-{lang}` step
5. Ensure path converges to `final`

### Issue: Duplicate Steps

**Symptoms**: Same step ID appears multiple times

**Solution**:
1. Search for duplicate step IDs
2. Remove duplicates
3. Ensure navigation still works

### Issue: Steps in Wrong Order

**Symptoms**: Steps appear in reverse order in JSON (works but confusing)

**Solution**:
1. Reorder steps logically (not required for functionality, but better for maintenance)
2. Ensure `next` fields are correct regardless of order

### Issue: Syntax Errors in Examples

**Symptoms**: Code examples have wrong syntax for language

**Solution**:
1. Check language-specific syntax
2. Use completed lessons as reference
3. Test examples in actual code editor

---

## Key Files Reference

- **Lesson Index**: `mentor-backend/mentor/lessons/index.json` - List of all lessons
- **Prerequisites**: `mentor-backend/mentor/prerequisites.json` - Concepts, levels, mappings
- **Server**: `mentor-backend/src/server.js` - Express server
- **Lesson Engine**: `mentor-backend/src/mentor/lesson-engine.js` - Lesson loading logic
- **Prerequisite Engine**: `mentor-backend/src/mentor/prerequisite-engine.js` - Prerequisite logic
- **API Router**: `mentor-backend/src/mentor/mentor-router.js` - API endpoints

---

## Best Practices Summary

1. ✅ **Always use concrete examples** - Same example throughout lesson
2. ✅ **Break coding into 5-8 steps** - Incremental learning
3. ✅ **Explain HOW, not just WHAT** - Detailed approach explanations
4. ✅ **Support all 5 languages** - Complete paths for each
5. ✅ **Test navigation** - All paths reach `final`
6. ✅ **Use specific knowledge check IDs** - Not generic ones
7. ✅ **Validate JSON** - Check syntax before committing
8. ✅ **Follow naming conventions** - Consistent step IDs
9. ✅ **Reference completed lessons** - Use as templates
10. ✅ **Quality over speed** - Better to have fewer complete lessons than many incomplete ones

---

## Next Steps

1. Review this guide
2. Check `mentor-backend/mentor/lessons/index.json` for lesson status
3. Identify incomplete lessons
4. Use completed lessons (e.g., `bubble-sort.json`, `two-sum.json`) as templates
5. Follow the lesson creation process
6. Use quality checklist before marking complete
7. Test navigation and JSON validity
8. Commit and push changes

---

**Good luck with continuing APTLEARN development! 🚀**

