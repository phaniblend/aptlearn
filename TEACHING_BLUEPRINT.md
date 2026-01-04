# APT Learn - Complete Teaching System Blueprint

**Version:** 1.0  
**Last Updated:** 2024

---

## Table of Contents

1. [System Overview](#system-overview)
2. [Complete User Journey](#complete-user-journey)
3. [Lesson Structure & Flow](#lesson-structure--flow)
4. [Concept Introduction System](#concept-introduction-system)
5. [Knowledge Check System (KCQs)](#knowledge-check-system-kcqs)
6. [Interactive Code Lessons (ICLs)](#interactive-code-lessons-icls)
7. [Language-Specific Paths](#language-specific-paths)
8. [Level System](#level-system)
9. [File Structure](#file-structure)
10. [API Endpoints](#api-endpoints)

---

## System Overview

APT Learn uses a **mentor-led, beginner-first, interactive learning system** with three core components:

1. **ICLs (Interactive Code Lessons)**: Step-by-step algorithm lessons with code
2. **KCQs (Knowledge Check Questions)**: Tests to verify understanding
3. **Concept Learning**: Interactive tools to learn foundational concepts

### Core Principles

- ✅ **Never assume prior knowledge** - Every concept is checked before use
- ✅ **Progressive disclosure** - Build understanding step by step
- ✅ **Language-agnostic teaching** - Same pattern, different syntax
- ✅ **Self-paced learning** - Users control their journey
- ✅ **Flexible prerequisites** - Test, learn, or skip

---

## Complete User Journey

### Phase 1: Discovery & Selection

```
User visits /algos
    ↓
Browse 125 algorithms (filtered by level/difficulty/pattern)
    ↓
Click on algorithm (e.g., "Binary Search")
    ↓
System checks lesson prerequisites
```

### Phase 2: Prerequisite Verification

```
System shows prerequisites:
"Before learning Binary Search, you need to know:
1. Arrays and Indexing
2. Variables
3. Functions/Methods
4. Parameters
5. Loops"

User chooses:
├─ "I know all these" → Go to lesson
├─ "Test my knowledge" → Take KCQ
└─ "I need to learn these" → Open ICL learning path
```

### Phase 3: Learning Path (if needed)

```
If "I need to learn these":
    ↓
For each concept:
    ├─ Show ICL (Interactive Concept Learning)
    │   ├─ Intro screen with analogy
    │   ├─ Builder screen (hands-on)
    │   └─ Quiz screen (verify understanding)
    │
    ├─ OR show concept explanation
    │   ├─ Explanation text
    │   ├─ Code examples
    │   └─ "Need more info?" options:
    │       ├─ Read official docs
    │       ├─ More examples
    │       └─ Ask a question (AI helper)
    │
    └─ Mark as learned → Next concept
    ↓
All prerequisites learned → Start lesson
```

### Phase 4: Lesson Flow

```
1. Title/Welcome
    ↓
2. Problem Illustration
   - What the problem is asking
   - Concrete example with input/output
   - NOT the solution, just the problem
    ↓
3. Thinking Challenge
   - "How would YOU solve this?"
   - Multiple approach options
   - User chooses their approach
    ↓
4. Explore Chosen Approach
   - Walk through their approach step-by-step
   - Explain the algorithm logic
   - Use concrete example throughout
    ↓
5. Language Selection
   - JavaScript, Python, Java, C++, TypeScript
   - Each path is independent
    ↓
6. Prerequisite Checks (Language-Specific)
   - Variable check → Explanation if needed
   - Function check → Explanation if needed
   - Parameter check → Explanation if needed
   - Loop check → Explanation if needed
   - (Only checks NEW concepts for advanced lessons)
    ↓
7. Coding Steps (Progressive)
   - Step 1: Function skeleton
   - Step 2: Initialize variables/pointers
   - Step 3: Loop structure
   - Step 4: Logic implementation
   - Step 5: Complete solution
   - Each step shows code + explanation
    ↓
8. Test Step
   - "Try running your code"
   - Show expected input/output
    ↓
9. Completion
   - Celebration message
   - Option to learn more efficient approach (if applicable)
```

### Phase 5: Level Progression

```
After completing lesson:
    ↓
System checks: "Have you completed all Level N lessons?"
    ↓
If YES → Show Level-Up Message:
    "🎉 Congratulations! You've made it to Level N+1!"
    "In this level, you'll learn: [concepts]"
    ↓
User chooses:
    ├─ "Take Level Knowledge Check" → Level KCQ
    └─ "Skip and Continue" → Next lesson
```

---

## Lesson Structure & Flow

### Standard Lesson Flow

Every lesson follows this structure (defined in `lessons/{lesson-id}.json`):

```json
{
  "id": "binary-search",
  "title": "Binary search",
  "pattern": "binary-search",
  "difficulty": "easy",
  "status": "draft",
  "flow": [
    {
      "stepId": "title",
      "mentorSays": "Learning goals...",
      "action": "continue",
      "next": "problem-illustration"
    },
    {
      "stepId": "problem-illustration",
      "mentorSays": "What the problem is asking...",
      "example": "Input/output example",
      "action": "continue",
      "next": "thinking-challenge"
    },
    {
      "stepId": "thinking-challenge",
      "mentorSays": "How would YOU solve this?",
      "choices": [
        { "label": "Approach 1", "next": "explore-approach-1" },
        { "label": "Approach 2", "next": "explore-approach-2" }
      ]
    },
    {
      "stepId": "explore-approach-1",
      "mentorSays": "Walk through approach...",
      "action": "continue",
      "next": "language-selection"
    },
    {
      "stepId": "language-selection",
      "mentorSays": "Which language?",
      "choices": [
        { "label": "JavaScript", "next": "variable-check-js" },
        { "label": "Python", "next": "variable-check-python" }
      ]
    },
    // Language-specific paths continue...
  ]
}
```

### Step Types

1. **Continue Steps**: Single action, moves forward
   ```json
   {
     "stepId": "title",
     "mentorSays": "Text",
     "action": "continue",
     "next": "next-step-id"
   }
   ```

2. **Choice Steps**: User selects from options
   ```json
   {
     "stepId": "thinking-challenge",
     "mentorSays": "Question?",
     "choices": [
       { "label": "Option 1", "next": "path-1" },
       { "label": "Option 2", "next": "path-2" }
     ]
   }
   ```

3. **Knowledge Check Steps**: Verify understanding
   ```json
   {
     "stepId": "variable-check-js",
     "mentorSays": "Do you know what a variable is?",
     "choices": [
       { "label": "Yes", "next": "function-check-js" },
       { "label": "No, explain", "next": "variable-explanation-js" }
     ]
   }
   ```

4. **Explanation Steps**: Teach a concept
   ```json
   {
     "stepId": "variable-explanation-js",
     "mentorSays": "A variable is like a labeled box...",
     "example": "let x = 5;",
     "action": "continue",
     "next": "function-check-js"
   }
   ```

5. **Coding Steps**: Progressive code building
   ```json
   {
     "stepId": "coding-pointers-js",
     "mentorSays": "Initialize left and right pointers...",
     "example": "let left = 0;\nlet right = nums.length - 1;",
     "action": "continue",
     "next": "coding-loop-js"
   }
   ```

---

## Concept Introduction System

### When Concepts Are Introduced

Concepts are introduced in two scenarios:

1. **Prerequisites (Before Lesson)**
   - Shown when user starts a lesson
   - Listed in `prerequisites.json` → `lessonPrerequisites`
   - User can: Skip, Test, or Learn

2. **During Lesson (Fallback)**
   - If user says "No, explain [concept]" during a knowledge check
   - Quick explanation shown inline
   - Option to get more info via ICL

### Concept Data Structure

Concepts are defined in `mentor/prerequisites.json`:

```json
{
  "concepts": {
    "arrays": {
      "id": "arrays",
      "name": "Arrays and Indexing",
      "description": "Understanding arrays...",
      "languages": {
        "js": {
          "explanation": "An array is like a list...",
          "examples": ["let arr = [1, 2, 3];", "arr[0] = 1"],
          "officialDocs": "https://...",
          "test": {
            "questions": [
              {
                "question": "What is the index of the first element?",
                "options": ["0", "1", "-1", "first"],
                "correct": 0
              }
            ]
          }
        },
        "python": { /* same structure */ },
        "java": { /* same structure */ },
        "cpp": { /* same structure */ },
        "ts": { /* same structure */ }
      }
    }
  }
}
```

### Concept Learning Options

When user needs to learn a concept, they see:

```
Concept: Arrays and Indexing

[Explanation Text]
[Code Examples]

Options:
├─ "I understand" → Next concept
└─ "Need more info" → 
    ├─ "Open ICL" (Interactive Concept Learning)
    ├─ "Read official docs" (external link)
    ├─ "More examples" (show additional examples)
    └─ "I have a specific question" (AI helper)
```

---

## Knowledge Check System (KCQs)

### Two Types of KCQs

#### 1. Prerequisite KCQs

**When**: Before starting a lesson  
**Purpose**: Verify user knows required concepts  
**Location**: `prerequisites.json` → `concepts.{conceptId}.languages.{lang}.test`

**Flow**:
```
User clicks "Test my knowledge"
    ↓
System loads all prerequisite concepts
    ↓
For each concept, show questions (2-3 per concept)
    ↓
User answers all questions
    ↓
System validates (70% threshold)
    ↓
If ≥70%: "Great! Proceed to lesson"
If <70%: "Let's review these concepts" → Learning path
```

**Example**:
```json
{
  "conceptId": "arrays",
  "language": "js",
  "questions": [
    {
      "question": "What is the index of the first element?",
      "options": ["0", "1", "-1", "first"],
      "correct": 0
    },
    {
      "question": "What does arr.length return?",
      "options": ["Last index", "Number of elements", "First element"],
      "correct": 1
    }
  ]
}
```

#### 2. Level KCQs

**When**: After completing all lessons in a level  
**Purpose**: Verify understanding of level's advanced concepts  
**Location**: `prerequisites.json` → `levels.{level}.knowledgeCheck`

**Flow**:
```
User completes last lesson in Level 1
    ↓
System shows: "🎉 Level Up! You've reached Level 2!"
    ↓
User chooses:
    ├─ "Take Level 2 Knowledge Check"
    └─ "Skip and Continue"
    ↓
If "Take KC":
    - Show questions from all Level 2 concepts
    - User answers
    - Validate (70% threshold)
    - If pass: "Ready for Level 2!"
    - If fail: "Let's review" → Learning path
```

**Structure**:
```json
{
  "levels": {
    "2": {
      "name": "Level 2 - Two Sum & Pair Logic",
      "advancedConcepts": ["hash-maps", "two-pointers"],
      "knowledgeCheck": {
        "title": "Level 2 Knowledge Check",
        "concepts": ["hash-maps", "two-pointers"]
      }
    }
  }
}
```

### KCQ Validation

**API**: `POST /api/mentor/test/validate`

**Request**:
```json
{
  "conceptId": "arrays",
  "language": "js",
  "answers": [0, 1]  // Selected option indices
}
```

**Response**:
```json
{
  "score": 100,
  "total": 2,
  "correct": 2,
  "passed": true,
  "results": [
    { "question": 0, "correct": true },
    { "question": 1, "correct": true }
  ]
}
```

**Passing Threshold**: 70%

---

## Interactive Code Lessons (ICLs)

### What Are ICLs?

**ICLs (Interactive Code Lessons)** are the main algorithm lessons - step-by-step interactive tutorials that teach algorithms with code.

**Not to be confused with**: ICL also refers to "Interactive Concept Learning" tool for learning foundational concepts.

### ICL Structure

ICLs are stored as JSON files: `mentor/lessons/{lesson-id}.json`

Each ICL contains:
- **Metadata**: id, title, pattern, difficulty, status
- **Flow**: Array of steps that guide the user through the lesson
- **Language Paths**: Separate flows for each language (js, python, java, cpp, ts)

### ICL Features

1. **Progressive Code Disclosure**
   - Start with function skeleton
   - Add variables/pointers
   - Add loops
   - Add logic
   - Show complete solution

2. **Concrete Examples**
   - Same example used throughout lesson
   - Step-by-step trace of execution
   - Shows what happens at each step

3. **Language Support**
   - All 125 lessons support all 5 languages
   - Language-specific syntax and terminology
   - Independent paths per language

4. **Interactive Elements**
   - User choices (approach selection)
   - Knowledge checks (concept verification)
   - Code execution (test in IDE)

### ICL Example Flow

```
Title → Problem Illustration → Thinking Challenge
    ↓
Explore Approach (explain algorithm logic)
    ↓
Language Selection
    ↓
[Language Path: JavaScript]
    ├─ Variable Check → Explanation (if needed)
    ├─ Function Check → Explanation (if needed)
    ├─ Parameter Check → Explanation (if needed)
    ├─ Loop Check → Explanation (if needed)
    ↓
Coding Steps:
    ├─ Step 1: Function skeleton
    ├─ Step 2: Initialize pointers
    ├─ Step 3: While loop
    ├─ Step 4: Middle calculation
    ├─ Step 5: Comparison logic
    ├─ Step 6: Update pointers
    └─ Step 7: Complete solution
    ↓
Test Step → Completion
```

---

## Interactive Concept Learning (ICL Tool)

### What Is It?

**ICL Tool** is an interactive learning component for foundational concepts (arrays, variables, functions, etc.).

**Files**:
- `ide-frontend/assets/concept-explainer.js` - Main ICL class
- `ide-frontend/concepts/{concept-id}.json` - Concept configurations

### ICL Tool Structure

Each concept has a JSON config with screens:

```json
{
  "concept": "arrays",
  "screens": [
    {
      "type": "intro",
      "title": "What is an Array?",
      "analogy": "An array is like a row of lockers...",
      "code": "let numbers = [1, 2, 3];",
      "visual": "array-diagram",
      "tip": "Arrays start at index 0!"
    },
    {
      "type": "builder",
      "title": "Build Your Own Array",
      "instructions": "Add items to create an array",
      "placeholder": "Enter a number",
      "examples": ["5", "10", "15"]
    },
    {
      "type": "quiz",
      "title": "Quick Check",
      "questions": [
        {
          "question": "What is the first index?",
          "options": ["0", "1"],
          "correct": 0
        }
      ]
    }
  ]
}
```

### Screen Types

1. **Intro Screen**
   - Title, analogy, code example
   - Visual diagram
   - Pro tip

2. **Builder Screen**
   - Interactive tool to build examples
   - User adds items, sees result
   - Try suggestions

3. **Quiz Screen**
   - Quick verification questions
   - Immediate feedback

### When ICL Tool Is Used

1. **"I need to learn these"** path
   - User clicks on a concept
   - ICL tool opens in modal
   - User goes through screens
   - Closes when done

2. **"Need more info"** during lesson
   - User says "No, explain [concept]"
   - Quick explanation shown
   - Option: "Open ICL" → Opens ICL tool

3. **"More examples"** option
   - Shows additional examples
   - Can open ICL for interactive learning

---

## Language-Specific Paths

### Supported Languages

1. **JavaScript** (`js`)
2. **Python** (`python`)
3. **Java** (`java`)
4. **C++** (`cpp`)
5. **TypeScript** (`ts`)

### Language Path Structure

After language selection, each language has its own independent path:

```
Language Selection
    ↓
[Selected: JavaScript]
    ↓
variable-check-js
    ├─ Yes → function-check-js
    └─ No → variable-explanation-js → function-check-js
    ↓
function-check-js
    ├─ Yes → parameter-check-js
    └─ No → function-explanation-js → parameter-check-js
    ↓
parameter-check-js
    ├─ Yes → coding-start-js
    └─ No → parameter-explanation-js → coding-start-js
    ↓
coding-start-js → coding-step-1-js → ... → coding-complete-js
    ↓
test-code → final
```

### Language-Specific Considerations

1. **Terminology**
   - JavaScript/Python/C++/TypeScript: "function"
   - Java: "method"

2. **Syntax Differences**
   - Variable declaration: `let` (JS/TS) vs no keyword (Python) vs `int[]` (Java/C++)
   - Array access: Same `arr[i]` syntax
   - Function definition: Different syntax per language

3. **Examples**
   - All examples use language-specific syntax
   - Same algorithm, different code

---

## Level System

### Level Structure

Lessons are organized into 12 levels:

```
Level 1: Foundations (Arrays, Indexing, Loops)
Level 2: Two Sum & Pair Logic (Hash Maps, Two Pointers)
Level 3: Sliding Window Pattern
Level 4: Two Pointers Pattern (Advanced)
Level 5: Searching (Linear → Binary)
Level 6: Sorting Fundamentals
Level 7: Hashing & Frequency Maps
Level 8: Stack Fundamentals
Level 9: Queue & Deque
Level 10: Recursion Basics
Level 11: Backtracking (Intro)
Level 12: Dynamic Programming (Beginner-Friendly)
```

### Level Mapping

Lessons are mapped to levels in `prerequisites.json`:

```json
{
  "lessonLevels": {
    "print-array-elements": 1,
    "two-sum": 2,
    "max-sum-subarray-k": 3,
    "reverse-string": 4,
    "binary-search": 5,
    "bubble-sort": 6,
    "group-anagrams": 7,
    "valid-parentheses": 8,
    "implement-queue": 9,
    "factorial-recursive": 10,
    "subsets": 11,
    "fibonacci-dp": 12
  }
}
```

### Level Progression

1. **Level Detection**
   - System checks user's completed lessons
   - Determines current level

2. **Level-Up Trigger**
   - When user starts a lesson from a new level
   - AND has completed all previous level lessons
   - Show level-up message

3. **Level Knowledge Check**
   - Optional KCQ for level's advanced concepts
   - Tests understanding before advancing
   - 70% threshold to pass

---

## File Structure

### Backend Structure

```
mentor-backend/
├── mentor/
│   ├── lessons/
│   │   ├── index.json              # All lessons metadata
│   │   ├── two-sum.json            # Individual lesson files
│   │   ├── binary-search.json
│   │   └── ... (125 total)
│   │
│   ├── prerequisites.json          # Concepts + Level definitions
│   │   ├── concepts: {...}         # Concept definitions
│   │   ├── levels: {...}           # Level info + KCs
│   │   ├── lessonLevels: {...}     # Lesson → Level mapping
│   │   └── lessonPrerequisites: {...}  # Lesson → Concepts mapping
│   │
│   └── questions-cache.json        # AI question cache
│
└── src/
    └── mentor/
        ├── lesson-engine.js        # Loads and manages lessons
        ├── prerequisite-engine.js  # Handles prerequisites & levels
        ├── mentor-router.js        # API endpoints
        ├── ai-helper.js            # AI question answering
        └── question-cache.js       # Question caching system
```

### Frontend Structure

```
ide-frontend/
├── learn.html                      # Main lesson page
├── algos.html                      # Algorithm listing page
├── assets/
│   ├── app.js                      # Navigation utilities
│   ├── concept-explainer.js       # ICL Tool component
│   ├── concept-explainer.css       # ICL Tool styles
│   └── styles.css                  # Main styles
└── concepts/
    ├── arrays.json                 # ICL Tool configs
    ├── variables.json
    ├── functions.json
    ├── parameters.json
    └── loops.json
```

---

## API Endpoints

### Lesson APIs

#### Start Lesson
```
POST /api/mentor/start
Body: { lessonId }
Response: { lessonId, step: {...} }
```
- Loads lesson
- Checks prerequisites
- Returns first step or prerequisites display

#### Get Next Step
```
POST /api/mentor/next
Body: { lessonId, stepId, choiceLabel? }
Response: { lessonId, step: {...} }
```
- Finds next step based on current step
- Handles user choices
- Returns next step in flow

#### Get Lesson
```
GET /api/mentor/lesson?lessonId={id}
Response: { lesson: {...} }
```
- Returns full lesson data

### Prerequisite APIs

#### Get Lesson Prerequisites
```
GET /api/mentor/prerequisites?lessonId={id}&language={lang}
Response: { prerequisites: [...] }
```
- Returns list of required concepts

#### Get Concept Info
```
GET /api/mentor/concept?conceptId={id}&language={lang}
Response: { 
  id, name, description,
  explanation, examples, officialDocs, test
}
```
- Returns concept details for a language

#### Validate Test
```
POST /api/mentor/test/validate
Body: { conceptId, language, answers: [0, 1, ...] }
Response: { score, total, correct, passed, results }
```
- Validates KCQ answers
- Returns score and results

### Level APIs

#### Get Lesson Level
```
GET /api/mentor/lesson/level?lessonId={id}
Response: { lessonId, level, levelInfo }
```
- Returns level number and level info

#### Get Level Info
```
GET /api/mentor/level?level={level}
Response: { name, description, congratulationMessage, advancedConcepts }
```
- Returns level information

#### Get Level Knowledge Check
```
GET /api/mentor/level/kc?level={level}&language={lang}
Response: { title, description, concepts: [...] }
```
- Returns level KC with all questions

#### Validate Level KC
```
POST /api/mentor/level/kc/validate
Body: { level, language, answers: {...} }
Response: { score, total, passed, results }
```
- Validates level KC answers

#### Check Level Up
```
GET /api/mentor/level/check-up?currentLessonId={id}&completedLessonIds=id1,id2,id3
Response: { shouldShow: true/false, levelInfo: {...} }
```
- Checks if user should see level-up message

### AI Helper API

#### Answer Concept Question
```
POST /api/mentor/question
Body: { conceptId, question, language }
Response: { answer }
```
- Uses question cache first
- Falls back to OpenAI if not cached
- Returns answer

#### Get Cache Stats
```
GET /api/mentor/questions/stats
Response: { totalConcepts, totalQuestions, byConcept: {...} }
```
- Returns question cache statistics

---

## Complete Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    USER JOURNEY FLOW                        │
└─────────────────────────────────────────────────────────────┘

1. SELECT ALGORITHM
   /algos → Filter → Click algorithm
   
2. PREREQUISITE CHECK
   ├─ Display prerequisites
   ├─ User chooses:
   │  ├─ "I know all" → Go to lesson
   │  ├─ "Test my knowledge" → KCQ → Pass/Fail
   │  └─ "I need to learn" → ICL Tool → Learn concepts
   
3. LESSON FLOW
   ├─ Title/Welcome
   ├─ Problem Illustration (what problem asks)
   ├─ Thinking Challenge (choose approach)
   ├─ Explore Approach (explain algorithm logic)
   ├─ Language Selection
   │
   ├─ [LANGUAGE PATH]
   │  ├─ Variable Check → Explain if needed
   │  ├─ Function Check → Explain if needed
   │  ├─ Parameter Check → Explain if needed
   │  ├─ Loop Check → Explain if needed
   │  │
   │  └─ CODING STEPS
   │     ├─ Function skeleton
   │     ├─ Initialize variables
   │     ├─ Loop structure
   │     ├─ Logic implementation
   │     └─ Complete solution
   │
   ├─ Test Step
   └─ Completion
   
4. LEVEL PROGRESSION
   ├─ Check if level-up
   ├─ Show level-up message
   ├─ Offer Level KCQ
   └─ Continue to next lesson
```

---

## Key Design Decisions

### 1. Modular Lesson Files
- **Why**: Easier to maintain, update individual lessons
- **How**: Each lesson in separate JSON file
- **Benefit**: Can update one lesson without affecting others

### 2. Language-Specific Paths
- **Why**: Different syntax, same algorithm
- **How**: Separate step chains per language
- **Benefit**: Native experience for each language

### 3. Prerequisite System
- **Why**: Ensure foundation before building
- **How**: Check before lesson, fallback during lesson
- **Benefit**: Flexible, doesn't block motivated learners

### 4. Level-Based Progression
- **Why**: Structured learning path
- **How**: Lessons mapped to levels, level KCs
- **Benefit**: Clear progression, milestone achievements

### 5. Question Caching
- **Why**: Reduce API costs, faster responses
- **How**: Cache similar questions, reuse answers
- **Benefit**: Cost-effective, consistent answers

---

## Best Practices

### Writing Lessons

1. **Always use concrete examples**
   - Same example throughout lesson
   - Show step-by-step execution

2. **Progressive disclosure**
   - Start simple, build complexity
   - One concept per step

3. **Language-agnostic teaching**
   - Focus on algorithm logic
   - Adapt syntax per language

4. **Never assume knowledge**
   - Check every concept before use
   - Provide explanations inline

5. **Validate user choices**
   - All approaches are valid
   - Guide through their choice

### Adding Concepts

1. **Language-specific content**
   - Explanation, examples, tests per language
   - Use native terminology

2. **Multiple learning options**
   - ICL Tool (interactive)
   - Text explanation
   - Code examples
   - Official docs link

3. **Test questions**
   - 2-3 questions per concept
   - Clear, unambiguous
   - 70% threshold

### Creating ICL Tool Configs

1. **Start with analogy**
   - Relatable, concrete
   - Non-technical language

2. **Interactive builder**
   - Hands-on learning
   - Immediate feedback

3. **Quick quiz**
   - Verify understanding
   - Reinforce learning

---

## Summary

This blueprint covers:

✅ **Complete user journey** from algorithm selection to completion  
✅ **Lesson structure** with all step types  
✅ **Concept introduction** via prerequisites and ICL Tool  
✅ **Knowledge check system** (prerequisite + level KCs)  
✅ **ICL structure** (Interactive Code Lessons)  
✅ **Language-specific paths** for 5 languages  
✅ **Level system** with progression  
✅ **File structure** and organization  
✅ **API endpoints** reference  
✅ **Best practices** for content creation  

**Total System Coverage**: 125 algorithms × 5 languages = 625 ICL paths

---

**For questions or updates, refer to:**
- `TEACHING_PATTERN.md` - Detailed teaching rules
- `PREREQUISITE_SYSTEM.md` - Prerequisite system details
- `LEVEL_KNOWLEDGE_CHECKS.md` - Level KC system
- `AVAILABILITY_REPORT.md` - Current coverage status

