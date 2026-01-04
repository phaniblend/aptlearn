# APT Learn - System Architecture & File Design

**Version:** 1.0  
**Last Updated:** 2024

---

## Table of Contents

1. [System Overview](#system-overview)
2. [File Structure](#file-structure)
3. [Data Flow Architecture](#data-flow-architecture)
4. [Lessons System](#lessons-system)
5. [KCQ System](#kcq-system)
6. [ICL System](#icl-system)
7. [Component Relationships](#component-relationships)
8. [API Layer](#api-layer)
9. [Frontend Components](#frontend-components)

---

## System Overview

APT Learn uses a **modular, JSON-based architecture** with clear separation between:
- **Backend**: Node.js/Express API server
- **Frontend**: Static HTML/JS/CSS
- **Data**: JSON files for lessons, concepts, prerequisites

### Architecture Pattern

```
┌─────────────────────────────────────────────────────────┐
│                    CLIENT (Browser)                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │  learn.html  │  │  algos.html  │  │  ICL Tool    │  │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘  │
│         │                  │                  │          │
└─────────┼──────────────────┼──────────────────┼──────────┘
          │                  │                  │
          │  HTTP Requests   │                  │
          │                  │                  │
┌─────────┼──────────────────┼──────────────────┼──────────┐
│         ▼                  ▼                  ▼          │
│  ┌──────────────────────────────────────────────────┐   │
│  │         EXPRESS API SERVER (Node.js)              │   │
│  │  ┌──────────────┐  ┌──────────────┐              │   │
│  │  │Lesson Engine │  │Prerequisite │              │   │
│  │  │              │  │   Engine     │              │   │
│  │  └──────┬───────┘  └──────┬───────┘              │   │
│  └─────────┼──────────────────┼──────────────────────┘   │
│            │                  │                           │
│            ▼                  ▼                           │
│  ┌──────────────────────────────────────────────────┐   │
│  │              DATA LAYER (JSON Files)              │   │
│  │  ┌──────────────┐  ┌──────────────┐              │   │
│  │  │   Lessons    │  │ Prerequisites│              │   │
│  │  │   JSON       │  │     JSON     │              │   │
│  │  └──────────────┘  └──────────────┘              │   │
│  └──────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────┘
```

---

## File Structure

### Complete Directory Tree

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
│   │   │   └── question-cache.js      # Question caching
│   │   ├── ide/
│   │   │   ├── file-api.js            # File operations
│   │   │   └── execute-api.js         # Code execution
│   │   └── utils/
│   │       └── fs-utils.js            # File utilities
│   │
│   └── mentor/                        # Data Files
│       ├── lessons/                   # Individual lesson files
│       │   ├── index.json             # Lesson metadata index
│       │   ├── two-sum.json           # Lesson: Two Sum
│       │   ├── binary-search.json     # Lesson: Binary Search
│       │   └── ... (125 total)
│       │
│       ├── prerequisites.json         # Concepts + Levels + Mappings
│       │   ├── concepts: {...}        # Concept definitions
│       │   ├── levels: {...}          # Level definitions
│       │   ├── lessonLevels: {...}    # Lesson → Level mapping
│       │   └── lessonPrerequisites: {...}  # Lesson → Concepts mapping
│       │
│       ├── questions-cache.json       # AI question cache
│       └── lessons.json               # Legacy (fallback)
│
└── ide-frontend/                      # Frontend
    ├── learn.html                     # Main lesson page
    ├── algos.html                     # Algorithm listing
    ├── assets/
    │   ├── app.js                     # Navigation utilities
    │   ├── concept-explainer.js      # ICL Tool component
    │   ├── concept-explainer.css      # ICL Tool styles
    │   └── styles.css                 # Main styles
    │
    └── concepts/                      # ICL Tool configs
        ├── arrays.json                # Arrays ICL config
        ├── variables.json              # Variables ICL config
        ├── functions.json              # Functions ICL config
        ├── parameters.json             # Parameters ICL config
        └── loops.json                 # Loops ICL config
```

---

## Data Flow Architecture

### Request Flow: Starting a Lesson

```
1. USER ACTION
   User clicks "Binary Search" on /algos
   ↓
2. FRONTEND REQUEST
   POST /api/mentor/start
   Body: { lessonId: "binary-search" }
   ↓
3. BACKEND PROCESSING
   mentor-router.js → lesson-engine.js
   ├─ Load lesson: loadLessonById("binary-search")
   │  └─ Read: mentor/lessons/binary-search.json
   │
   ├─ Check prerequisites: prerequisite-engine.js
   │  └─ Read: mentor/prerequisites.json
   │     └─ Get: lessonPrerequisites["binary-search"]
   │
   └─ Inject prerequisite step (if needed)
   ↓
4. RESPONSE
   {
     lessonId: "binary-search",
     step: {
       stepId: "prerequisites-display",
       prerequisites: ["arrays", "variables", "functions", ...]
     }
   }
   ↓
5. FRONTEND RENDERING
   learn.html displays prerequisite step
   User chooses: "I know all" / "Test" / "Learn"
```

### Request Flow: Getting Next Step

```
1. USER ACTION
   User clicks "Continue" or makes a choice
   ↓
2. FRONTEND REQUEST
   POST /api/mentor/next
   Body: {
     lessonId: "binary-search",
     stepId: "thinking-challenge",
     choiceLabel: "Use straightforward approach"
   }
   ↓
3. BACKEND PROCESSING
   mentor-router.js → lesson-engine.js
   ├─ Load lesson: loadLessonById("binary-search")
   ├─ Find current step: findStepById(lesson, "thinking-challenge")
   ├─ Get next step: getNextStep(lesson, currentStep, choiceLabel)
   └─ Return: { lessonId, step: {...} }
   ↓
4. RESPONSE
   {
     lessonId: "binary-search",
     step: {
       stepId: "explore-approach",
       mentorSays: "...",
       action: "continue",
       next: "language-selection"
     }
   }
   ↓
5. FRONTEND RENDERING
   learn.html updates UI with new step
```

### Request Flow: Loading ICL Tool

```
1. USER ACTION
   User clicks "Open ICL" for "arrays" concept
   ↓
2. FRONTEND JAVASCRIPT
   showICL("arrays")
   ↓
3. FETCH REQUEST
   GET /concepts/arrays.json
   (Served as static file by Express)
   ↓
4. RESPONSE
   {
     id: "arrays",
     title: "Arrays Explained",
     screens: [
       { type: "intro", ... },
       { type: "builder", ... },
       { type: "quiz", ... }
     ]
   }
   ↓
5. ICL TOOL RENDERING
   concept-explainer.js renders screens
   User interacts with intro/builder/quiz
```

---

## Lessons System

### File: `mentor/lessons/index.json`

**Purpose**: Metadata index for all lessons  
**Structure**:
```json
{
  "lessons": [
    {
      "id": "binary-search",
      "title": "Binary search",
      "pattern": "binary-search",
      "difficulty": "easy",
      "language": "javascript",
      "status": "draft",
      "prerequisites": ["arrays", "variables", "functions", "parameters", "loops"]
    },
    // ... 125 total
  ]
}
```

**Used By**:
- `lesson-engine.js` → `loadLessonsMetadata()`
- `generate_algos_page.py` → Generates algos.html

---

### File: `mentor/lessons/{lesson-id}.json`

**Purpose**: Complete lesson flow for one algorithm  
**Structure**:
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
      "mentorSays": "...",
      "action": "continue",
      "next": "problem-illustration"
    },
    {
      "stepId": "problem-illustration",
      "mentorSays": "...",
      "example": "...",
      "action": "continue",
      "next": "thinking-challenge"
    },
    {
      "stepId": "thinking-challenge",
      "mentorSays": "...",
      "choices": [
        { "label": "Option 1", "next": "path-1" },
        { "label": "Option 2", "next": "path-2" }
      ]
    },
    // ... language-specific paths
    {
      "stepId": "variable-check-js",
      "mentorSays": "Do you know variables?",
      "choices": [
        { "label": "Yes", "next": "function-check-js" },
        { "label": "No", "next": "variable-explanation-js" }
      ]
    },
    {
      "stepId": "coding-start-js",
      "mentorSays": "Let's code...",
      "example": "function binarySearch(...) { ... }",
      "action": "continue",
      "next": "coding-pointers-js"
    }
    // ... more steps
  ]
}
```

**Key Properties**:
- `flow`: Array of step objects
- Each step has `stepId`, `mentorSays`, `next` or `choices`
- Language-specific paths: `-js`, `-python`, `-java`, `-cpp`, `-ts` suffixes

**Used By**:
- `lesson-engine.js` → `loadLessonById()`, `findStepById()`, `getNextStep()`
- `mentor-router.js` → `/api/mentor/start`, `/api/mentor/next`

---

### Component: `lesson-engine.js`

**Purpose**: Load and navigate lesson flows  
**Key Functions**:

```javascript
// Load all lesson metadata
loadLessonsMetadata() → Array<LessonMetadata>

// Load all lessons (full data)
loadLessons() → Array<Lesson>

// Load single lesson
loadLessonById(lessonId) → Lesson

// Find step in lesson
findStepById(lesson, stepId) → Step

// Get next step based on current + choice
getNextStep(lesson, currentStep, choiceLabel) → Step
```

**File Dependencies**:
- Reads: `mentor/lessons/index.json`
- Reads: `mentor/lessons/{lesson-id}.json`
- Fallback: `mentor/lessons.json` (legacy)

---

## KCQ System

### File: `mentor/prerequisites.json`

**Purpose**: Central data file for concepts, levels, and mappings  
**Structure**:

```json
{
  "concepts": {
    "arrays": {
      "id": "arrays",
      "name": "Arrays and Indexing",
      "description": "...",
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
    },
    "variables": { /* ... */ },
    "functions": { /* ... */ },
    "parameters": { /* ... */ },
    "loops": { /* ... */ },
    "hash-maps": { /* ... */ },
    "two-pointers": { /* ... */ },
    "sliding-window": { /* ... */ }
  },
  
  "levels": {
    "1": {
      "name": "Level 1 - Foundations",
      "description": "...",
      "congratulationMessage": "🎉 Congratulations!...",
      "advancedConcepts": ["arrays", "variables", "functions", "parameters", "loops"],
      "knowledgeCheck": {
        "title": "Level 1 Knowledge Check",
        "description": "...",
        "concepts": ["arrays", "variables", "functions", "parameters", "loops"]
      }
    },
    "2": { /* ... */ },
    // ... up to level 12
  },
  
  "lessonLevels": {
    "print-array-elements": 1,
    "two-sum": 2,
    "binary-search": 5,
    // ... maps all 125 lessons to levels
  },
  
  "lessonPrerequisites": {
    "two-sum": ["arrays", "variables", "functions", "parameters", "loops"],
    "two-sum-hashmap": ["arrays", "variables", "functions", "parameters", "loops", "hash-maps"],
    "binary-search": ["arrays", "variables", "functions", "parameters", "loops"],
    // ... maps all lessons to required concepts
  }
}
```

**Key Sections**:
1. **`concepts`**: Concept definitions with language-specific content + KCQs
2. **`levels`**: Level definitions with knowledge checks
3. **`lessonLevels`**: Maps lesson IDs to level numbers
4. **`lessonPrerequisites`**: Maps lesson IDs to required concept IDs

**Used By**:
- `prerequisite-engine.js` → All prerequisite/level functions
- `mentor-router.js` → Prerequisite/level API endpoints

---

### Component: `prerequisite-engine.js`

**Purpose**: Handle prerequisites, concepts, levels, and KCQs  
**Key Functions**:

```javascript
// Load prerequisites data
loadPrerequisites() → PrerequisitesData

// Get prerequisites for a lesson
getLessonPrerequisites(lessonId) → Array<ConceptId>

// Get concept info for a language
getConceptInfo(conceptId, language) → ConceptInfo

// Validate concept test (KCQ)
validateTest(conceptId, language, answers) → ValidationResult

// Get lesson level
getLessonLevel(lessonId) → Number

// Get level info
getLevelInfo(level) → LevelInfo

// Get level knowledge check
getLevelKnowledgeCheck(level, language) → LevelKC

// Validate level KC
validateLevelTest(level, language, answers) → ValidationResult

// Check if should show level-up
shouldShowLevelUp(currentLessonId, completedLessonIds) → LevelUpInfo
```

**File Dependencies**:
- Reads: `mentor/prerequisites.json`
- Caches data in memory

---

### KCQ Data Structure

#### Prerequisite KCQ (Concept-Level)

**Location**: `prerequisites.json` → `concepts.{conceptId}.languages.{lang}.test`

**Structure**:
```json
{
  "test": {
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
}
```

**Validation**:
- API: `POST /api/mentor/test/validate`
- Input: `{ conceptId, language, answers: [0, 1] }`
- Output: `{ score, total, correct, passed, results }`
- Threshold: 70%

---

#### Level KCQ (Level-Level)

**Location**: `prerequisites.json` → `levels.{level}.knowledgeCheck`

**Structure**:
```json
{
  "knowledgeCheck": {
    "title": "Level 2 Knowledge Check",
    "description": "...",
    "concepts": ["hash-maps", "two-pointers"]
  }
}
```

**Validation**:
- API: `POST /api/mentor/level/kc/validate`
- Input: `{ level, language, answers: { "hash-maps": [0,1], "two-pointers": [1] } }`
- Output: `{ score, total, correct, passed, results, level }`
- Threshold: 70%

---

## ICL System

### ICL Tool (Interactive Concept Learning)

#### File: `ide-frontend/concepts/{concept-id}.json`

**Purpose**: ICL Tool configuration for foundational concepts  
**Structure**:

```json
{
  "id": "arrays",
  "title": "Arrays Explained",
  "screens": [
    {
      "type": "intro",
      "title": "Arrays: Your Digital Shopping List 🛒",
      "analogy": "Think of an array like a shopping list...",
      "code": "let fruits = [\"apple\", \"banana\", \"orange\"];",
      "visual": {
        "type": "array-boxes",
        "items": ["apple", "banana", "orange"]
      },
      "tip": "Computers count from 0, not 1!"
    },
    {
      "type": "builder",
      "title": "Build Your First Array",
      "instructions": "Create your own array...",
      "placeholder": "Type an item (e.g., pizza, 42, hello)",
      "examples": ["\"pizza\"", "42", "\"hello\""]
    },
    {
      "type": "quiz",
      "title": "Test Your Knowledge",
      "context": "let pets = [\"dog\", \"cat\", \"fish\"];",
      "question": "What does pets[1] return?",
      "options": ["\"dog\"", "\"cat\"", "\"fish\""],
      "correctIndex": 1,
      "correctFeedback": "✅ Correct!...",
      "incorrectFeedback": "❌ Remember: arrays start at 0..."
    }
  ]
}
```

**Screen Types**:
1. **`intro`**: Introduction with analogy, code, visual, tip
2. **`builder`**: Interactive builder tool
3. **`quiz`**: Quiz questions with feedback

**Used By**:
- `concept-explainer.js` → Loads and renders screens
- Frontend: `showICL(conceptId)` → Fetches `/concepts/{conceptId}.json`

---

#### Component: `concept-explainer.js`

**Purpose**: ICL Tool frontend component  
**Key Functions**:

```javascript
class ICL {
  constructor(containerId, conceptId)
  async init()                    // Loads concept JSON
  renderScreen()                   // Renders current screen
  buildScreenHTML(screen)          // Builds HTML for screen type
  buildIntroScreen(screen)         // Intro screen HTML
  buildBuilderScreen(screen)       // Builder screen HTML
  buildQuizScreen(screen)          // Quiz screen HTML
  nextScreen()                     // Navigate to next screen
  previousScreen()                 // Navigate to previous screen
  finish()                         // Close ICL tool
}

// Global function
showICL(conceptId)                 // Opens ICL tool modal
```

**File Dependencies**:
- Fetches: `/concepts/{conceptId}.json` (served as static file)
- Renders: HTML/CSS for interactive screens

---

### ICLs (Interactive Code Lessons)

**Location**: `mentor/lessons/{lesson-id}.json` (integrated in lesson flow)

**Structure**: Same as lesson files (see [Lessons System](#lessons-system))

**Key Steps**:
- `coding-start-{lang}`: Begin coding section
- `coding-{step}-{lang}`: Progressive coding steps
- `coding-complete-{lang}`: Complete solution

**Example Flow**:
```json
{
  "stepId": "coding-start-js",
  "mentorSays": "Let's implement binary search...",
  "example": "function binarySearch(nums, target) { ... }",
  "action": "continue",
  "next": "coding-pointers-js"
},
{
  "stepId": "coding-pointers-js",
  "mentorSays": "Initialize left and right pointers...",
  "example": "let left = 0;\nlet right = nums.length - 1;",
  "action": "continue",
  "next": "coding-loop-js"
},
// ... more coding steps
{
  "stepId": "coding-complete-js",
  "mentorSays": "Perfect! Here's the complete solution...",
  "example": "function binarySearch(nums, target) {\n  // Complete code\n}",
  "action": "continue",
  "next": "test-code"
}
```

---

## Component Relationships

### Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    USER REQUEST FLOW                        │
└─────────────────────────────────────────────────────────────┘

1. START LESSON
   Frontend: learn.html
      ↓
   API: POST /api/mentor/start
      ↓
   Backend: mentor-router.js
      ├─→ lesson-engine.js → loadLessonById()
      │   └─→ Reads: mentor/lessons/{lesson-id}.json
      │
      └─→ prerequisite-engine.js → getLessonPrerequisites()
          └─→ Reads: mentor/prerequisites.json
              └─→ Returns: ["arrays", "variables", ...]
      ↓
   Response: { lessonId, step: prerequisites-display }

2. GET NEXT STEP
   Frontend: learn.html
      ↓
   API: POST /api/mentor/next
      ↓
   Backend: mentor-router.js
      └─→ lesson-engine.js → getNextStep()
          ├─→ Loads: mentor/lessons/{lesson-id}.json
          ├─→ Finds: current step
          └─→ Returns: next step
      ↓
   Response: { lessonId, step: {...} }

3. LOAD CONCEPT (ICL Tool)
   Frontend: learn.html → showICL("arrays")
      ↓
   JavaScript: concept-explainer.js
      ↓
   Fetch: GET /concepts/arrays.json
      ↓
   Server: Express static file serving
      └─→ Reads: ide-frontend/concepts/arrays.json
      ↓
   Response: { id, title, screens: [...] }
      ↓
   Frontend: Renders ICL Tool screens

4. VALIDATE KCQ
   Frontend: learn.html
      ↓
   API: POST /api/mentor/test/validate
      ↓
   Backend: mentor-router.js
      └─→ prerequisite-engine.js → validateTest()
          ├─→ Loads: mentor/prerequisites.json
          ├─→ Gets: concepts.{conceptId}.languages.{lang}.test
          └─→ Validates: answers against correct answers
      ↓
   Response: { score, total, correct, passed, results }
```

---

## API Layer

### File: `mentor-router.js`

**Purpose**: Express router for all mentor/lesson APIs  
**Endpoints**:

#### Lesson APIs

```javascript
POST /api/mentor/start
Body: { lessonId }
Response: { lessonId, step: {...} }
Logic:
  - Load lesson via lesson-engine.js
  - Check prerequisites via prerequisite-engine.js
  - Inject prerequisite step if needed
  - Return first step or prerequisite step

POST /api/mentor/next
Body: { lessonId, stepId, choiceLabel? }
Response: { lessonId, step: {...} }
Logic:
  - Load lesson via lesson-engine.js
  - Find current step
  - Get next step via getNextStep()
  - Handle special steps (prerequisites-kc, prerequisites-learn)
  - Return next step

GET /api/mentor/lesson?lessonId={id}
Response: { lesson: {...} }
Logic:
  - Load full lesson data
  - Return complete lesson object
```

#### Prerequisite APIs

```javascript
GET /api/mentor/prerequisites?lessonId={id}&language={lang}
Response: { prerequisites: [...] }
Logic:
  - Get lesson prerequisites via prerequisite-engine.js
  - Return concept IDs

GET /api/mentor/concept?conceptId={id}&language={lang}
Response: { id, name, explanation, examples, officialDocs, test }
Logic:
  - Get concept info via prerequisite-engine.js
  - Return language-specific concept data

POST /api/mentor/test/validate
Body: { conceptId, language, answers: [0, 1, ...] }
Response: { score, total, correct, passed, results }
Logic:
  - Validate via prerequisite-engine.js → validateTest()
  - Calculate score (70% threshold)
  - Return results
```

#### Level APIs

```javascript
GET /api/mentor/lesson/level?lessonId={id}
Response: { lessonId, level, levelInfo }
Logic:
  - Get lesson level via prerequisite-engine.js
  - Get level info
  - Return level data

GET /api/mentor/level?level={level}
Response: { name, description, congratulationMessage, advancedConcepts }
Logic:
  - Get level info via prerequisite-engine.js
  - Return level information

GET /api/mentor/level/kc?level={level}&language={lang}
Response: { title, description, concepts: [...] }
Logic:
  - Get level KC via prerequisite-engine.js
  - Load all concept tests for level
  - Return level KC with questions

POST /api/mentor/level/kc/validate
Body: { level, language, answers: {...} }
Response: { score, total, correct, passed, results, level }
Logic:
  - Validate via prerequisite-engine.js → validateLevelTest()
  - Calculate overall score (70% threshold)
  - Return results

GET /api/mentor/level/check-up?currentLessonId={id}&completedLessonIds=id1,id2,id3
Response: { shouldShow: true/false, levelInfo: {...} }
Logic:
  - Check via prerequisite-engine.js → shouldShowLevelUp()
  - Determine if user should see level-up message
  - Return level-up info
```

#### AI Helper API

```javascript
POST /api/mentor/question
Body: { conceptId, question, language }
Response: { answer }
Logic:
  - Check question-cache.js for similar question
  - If found: Return cached answer
  - If not: Call OpenAI API via ai-helper.js
  - Store in cache
  - Return answer

GET /api/mentor/questions/stats
Response: { totalConcepts, totalQuestions, byConcept: {...} }
Logic:
  - Get stats via question-cache.js
  - Return cache statistics
```

---

## Frontend Components

### File: `learn.html`

**Purpose**: Main lesson page  
**Key Features**:
- Renders lesson steps
- Handles user choices
- Integrates ICL Tool
- Shows KCQ modals
- Manages lesson progress

**JavaScript Functions**:
```javascript
// Lesson flow
async function startLesson(lessonId)
async function getNextStep(stepId, choiceLabel)
function renderStep(step)

// Prerequisites
async function showPrerequisites(prerequisites)
async function openPrerequisitesKC(prerequisiteIds)
function showConceptLearning(concept)

// ICL Tool
function showICL(conceptId)  // Calls concept-explainer.js

// Knowledge Checks
async function openKnowledgeCheck()
async function openPrerequisitesKC(prerequisiteIds)
function validateKC(answers)

// Level progression
async function checkLevelUp()
function showLevelUpModal(levelInfo)
async function takeLevelKC()
```

**Dependencies**:
- `assets/app.js` - Navigation utilities
- `assets/concept-explainer.js` - ICL Tool component
- `assets/styles.css` - Styling

---

### File: `concept-explainer.js`

**Purpose**: ICL Tool component  
**Key Features**:
- Loads concept JSON files
- Renders interactive screens (intro, builder, quiz)
- Handles navigation between screens
- Provides interactive learning experience

**Class Structure**:
```javascript
class ICL {
  constructor(containerId, conceptId)
  async init()                    // Load JSON config
  renderScreen()                   // Render current screen
  buildScreenHTML(screen)          // Build HTML for screen
  buildIntroScreen(screen)         // Intro screen
  buildBuilderScreen(screen)       // Builder screen
  buildQuizScreen(screen)          // Quiz screen
  nextScreen()                     // Next screen
  previousScreen()                 // Previous screen
  finish()                         // Close tool
  close()                          // Remove modal
}

// Global function
function showICL(conceptId)        // Open ICL tool
```

**File Dependencies**:
- Fetches: `/concepts/{conceptId}.json`
- Uses: `concept-explainer.css` for styling

---

### File: `algos.html`

**Purpose**: Algorithm listing page  
**Key Features**:
- Lists all 125 algorithms
- Filter by level, difficulty, pattern
- Search functionality
- Numbered algorithms

**Generated By**:
- `generate_algos_page.py` script
- Reads: `mentor/lessons/index.json`
- Reads: `mentor/prerequisites.json` (for level mapping)
- Generates: Complete HTML with all lessons

---

## Data Relationships

### Concept → Lesson Mapping

```
prerequisites.json
  └─→ lessonPrerequisites
      ├─→ "two-sum": ["arrays", "variables", "functions", "parameters", "loops"]
      ├─→ "binary-search": ["arrays", "variables", "functions", "parameters", "loops"]
      └─→ "two-sum-hashmap": ["arrays", "variables", "functions", "parameters", "loops", "hash-maps"]
           ↓
      When lesson starts:
          1. Check lessonPrerequisites[lessonId]
          2. For each concept ID:
             - Load from concepts.{conceptId}
             - Show prerequisite step
             - User can: Skip, Test (KCQ), or Learn (ICL Tool)
```

### Lesson → Level Mapping

```
prerequisites.json
  └─→ lessonLevels
      ├─→ "print-array-elements": 1
      ├─→ "two-sum": 2
      ├─→ "binary-search": 5
      └─→ "fibonacci-dp": 12
           ↓
      When lesson completes:
          1. Check lessonLevels[lessonId] → Get level
          2. Check if all previous level lessons completed
          3. If yes → Show level-up message
          4. Offer level KCQ from levels.{level}.knowledgeCheck
```

### Concept → ICL Tool Mapping

```
Frontend: showICL("arrays")
    ↓
Fetches: /concepts/arrays.json
    ↓
Server: Express static file serving
    └─→ ide-frontend/concepts/arrays.json
    ↓
ICL Tool renders screens from JSON
```

---

## File Dependencies Graph

```
┌─────────────────────────────────────────────────────────────┐
│                    FILE DEPENDENCIES                        │
└─────────────────────────────────────────────────────────────┘

mentor-router.js
  ├─→ lesson-engine.js
  │   ├─→ Reads: mentor/lessons/index.json
  │   └─→ Reads: mentor/lessons/{lesson-id}.json
  │
  └─→ prerequisite-engine.js
      └─→ Reads: mentor/prerequisites.json
          ├─→ concepts: {...}
          ├─→ levels: {...}
          ├─→ lessonLevels: {...}
          └─→ lessonPrerequisites: {...}

learn.html
  ├─→ assets/app.js
  ├─→ assets/concept-explainer.js
  │   └─→ Fetches: /concepts/{concept-id}.json
  │       └─→ ide-frontend/concepts/{concept-id}.json
  │
  └─→ API Calls:
      ├─→ POST /api/mentor/start
      ├─→ POST /api/mentor/next
      ├─→ GET /api/mentor/prerequisites
      ├─→ GET /api/mentor/concept
      ├─→ POST /api/mentor/test/validate
      ├─→ GET /api/mentor/level/kc
      └─→ POST /api/mentor/level/kc/validate

algos.html
  └─→ Generated by: generate_algos_page.py
      ├─→ Reads: mentor/lessons/index.json
      └─→ Reads: mentor/prerequisites.json (lessonLevels)
```

---

## Key Design Patterns

### 1. Modular JSON Files

**Pattern**: One file per lesson  
**Benefit**: Easy to update individual lessons  
**Location**: `mentor/lessons/{lesson-id}.json`

### 2. Centralized Prerequisites

**Pattern**: Single file for all concepts/levels/mappings  
**Benefit**: Single source of truth  
**Location**: `mentor/prerequisites.json`

### 3. Language-Specific Paths

**Pattern**: Separate step chains per language  
**Benefit**: Native experience for each language  
**Implementation**: Step IDs with language suffix (`-js`, `-python`, etc.)

### 4. Static File Serving

**Pattern**: ICL Tool configs served as static files  
**Benefit**: No backend processing needed  
**Location**: `ide-frontend/concepts/*.json` → `/concepts/*.json`

### 5. Caching Strategy

**Pattern**: In-memory caching for frequently accessed data  
**Implementation**:
- `lesson-engine.js`: Caches lessons metadata and full lessons
- `prerequisite-engine.js`: Caches prerequisites data
- `question-cache.js`: Caches AI question answers

---

## Summary

### Files by System

| System | Files | Purpose |
|--------|-------|---------|
| **Lessons** | `mentor/lessons/index.json`<br>`mentor/lessons/{lesson-id}.json` | Lesson metadata & flows |
| **KCQs** | `mentor/prerequisites.json` | Concept tests & level KCs |
| **ICL Tool** | `ide-frontend/concepts/{concept-id}.json` | ICL Tool configs |
| **Engines** | `lesson-engine.js`<br>`prerequisite-engine.js` | Data loading & processing |
| **API** | `mentor-router.js` | API endpoints |
| **Frontend** | `learn.html`<br>`concept-explainer.js` | UI & ICL Tool |

### Data Flow Summary

1. **Lessons**: JSON files → `lesson-engine.js` → API → Frontend
2. **KCQs**: `prerequisites.json` → `prerequisite-engine.js` → API → Frontend
3. **ICL Tool**: `concepts/*.json` → Static serving → `concept-explainer.js` → Frontend

---

**For implementation details, see:**
- `TEACHING_BLUEPRINT.md` - Complete teaching system guide
- `TEACHING_PATTERN.md` - Teaching pattern rules
- `PREREQUISITE_SYSTEM.md` - Prerequisite system details
- `LEVEL_KNOWLEDGE_CHECKS.md` - Level KC system

