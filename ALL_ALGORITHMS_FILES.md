# Files Involved in Teaching ALL Algorithms

**Total Algorithms**: 125  
**Total Languages**: 5 (JavaScript, Python, Java, C++, TypeScript)  
**Total ICL Paths**: 625 (125 algorithms × 5 languages)

---

## File Organization

The system uses a **shared architecture** where:
- **Common files** are shared by all algorithms
- **Algorithm-specific files** are individual lesson JSON files
- **Concept files** are shared across algorithms that use the same concepts

---

## Complete File List

### 1. Common Data Files (Shared by All Algorithms)

#### Lesson Metadata Index
- **`mentor-backend/mentor/lessons/index.json`**
  - **Purpose**: Metadata index for all 125 lessons
  - **Contains**: Array of lesson objects with:
    - `id`, `title`, `pattern`, `difficulty`, `status`, `prerequisites`
  - **Used By**: Algorithm listing page, lesson loading, lesson discovery
  - **Size**: ~1461 lines (125 lessons)

#### Central Prerequisites File
- **`mentor-backend/mentor/prerequisites.json`**
  - **Purpose**: Central data file for concepts, levels, and mappings
  - **Contains**:
    - **`concepts`**: All concept definitions (arrays, variables, functions, parameters, loops, hash-maps, two-pointers, sliding-window, etc.)
      - Each concept has language-specific: explanation, examples, officialDocs, test (KCQ)
    - **`levels`**: All 12 level definitions with knowledge checks
    - **`lessonLevels`**: Maps all 125 lesson IDs to level numbers (1-12)
    - **`lessonPrerequisites`**: Maps all 125 lesson IDs to required concept IDs
  - **Used By**: All algorithms for prerequisite checks, concept explanations, KCQs, level progression
  - **Size**: ~511 lines

#### AI Question Cache
- **`mentor-backend/mentor/questions-cache.json`**
  - **Purpose**: Cache for AI-generated question answers
  - **Contains**: Cached answers to user questions about concepts
  - **Used By**: AI helper when user asks questions
  - **Optional**: Created on first use

#### Legacy Fallback
- **`mentor-backend/mentor/lessons.json`** (if exists)
  - **Purpose**: Legacy format fallback
  - **Used By**: `lesson-engine.js` if modular file not found
  - **Status**: Deprecated, kept for backward compatibility

---

### 2. Algorithm-Specific Lesson Files (125 Files)

Each algorithm has its own lesson JSON file:

- **`mentor-backend/mentor/lessons/{lesson-id}.json`**

**Pattern**: One file per algorithm  
**Total**: 125 files  
**Location**: `mentor-backend/mentor/lessons/`

#### Example Files:
- `two-sum.json` - Two Sum algorithm
- `binary-search.json` - Binary Search algorithm
- `print-array-elements.json` - Print array elements
- `find-max-element.json` - Find maximum element
- `reverse-array.json` - Reverse array
- `bubble-sort.json` - Bubble Sort
- `merge-sort.json` - Merge Sort
- `valid-parentheses.json` - Valid Parentheses
- `fibonacci-dp.json` - Fibonacci with DP
- ... (125 total)

**Each File Contains**:
- Complete lesson flow with all steps
- Problem illustration
- Thinking challenge with approach options
- Language-specific paths for all 5 languages (js, python, java, cpp, ts)
- Prerequisite checks per language
- Progressive coding steps per language
- Test and completion steps

**Average Size**: ~500-1000 lines per file  
**Total Size**: ~62,500-125,000 lines across all lessons

---

### 3. ICL Tool Config Files (Concept Learning)

These files are shared across all algorithms that use the same concepts:

- **`ide-frontend/concepts/arrays.json`**
  - **Purpose**: ICL Tool config for Arrays concept
  - **Used By**: All algorithms requiring arrays (most algorithms)
  - **Contains**: Intro, builder, and quiz screens

- **`ide-frontend/concepts/variables.json`**
  - **Purpose**: ICL Tool config for Variables concept
  - **Used By**: All algorithms requiring variables (all algorithms)
  - **Contains**: Intro, builder, and quiz screens

- **`ide-frontend/concepts/functions.json`**
  - **Purpose**: ICL Tool config for Functions concept
  - **Used By**: All algorithms requiring functions (all algorithms)
  - **Contains**: Intro, builder, and quiz screens

- **`ide-frontend/concepts/parameters.json`**
  - **Purpose**: ICL Tool config for Parameters concept
  - **Used By**: All algorithms requiring function parameters (all algorithms)
  - **Contains**: Intro, builder, and quiz screens

- **`ide-frontend/concepts/loops.json`**
  - **Purpose**: ICL Tool config for Loops concept
  - **Used By**: All algorithms requiring loops (most algorithms)
  - **Contains**: Intro, builder, and quiz screens

**Note**: Additional ICL Tool configs can be added for advanced concepts (hash-maps, two-pointers, sliding-window, etc.) as needed.

---

### 4. Backend Engine Files (Shared by All Algorithms)

#### Lesson Engine
- **`mentor-backend/src/mentor/lesson-engine.js`**
  - **Purpose**: Load and navigate lesson flows
  - **Functions**:
    - `loadLessonsMetadata()` - Loads index.json
    - `loadLessons()` - Loads all lesson files
    - `loadLessonById(lessonId)` - Loads specific lesson file
    - `findStepById(lesson, stepId)` - Finds step in lesson
    - `getNextStep(lesson, currentStep, choiceLabel)` - Navigates flow
  - **File Dependencies**:
    - Reads: `mentor/lessons/index.json`
    - Reads: `mentor/lessons/{any-lesson-id}.json` (dynamically)
  - **Used By**: All 125 algorithms

#### Prerequisite Engine
- **`mentor-backend/src/mentor/prerequisite-engine.js`**
  - **Purpose**: Handle prerequisites, concepts, levels, and KCQs
  - **Functions**:
    - `loadPrerequisites()` - Loads prerequisites.json
    - `getLessonPrerequisites(lessonId)` - Gets prerequisites for any lesson
    - `getConceptInfo(conceptId, language)` - Gets concept details
    - `validateTest(conceptId, language, answers)` - Validates KCQ
    - `getLessonLevel(lessonId)` - Gets level for any lesson
    - `getLevelInfo(level)` - Gets level information
    - `getLevelKnowledgeCheck(level, language)` - Gets level KCQ
    - `validateLevelTest(level, language, answers)` - Validates level KCQ
    - `shouldShowLevelUp(currentLessonId, completedLessonIds)` - Checks level-up
  - **File Dependencies**:
    - Reads: `mentor/prerequisites.json`
  - **Used By**: All 125 algorithms

#### API Router
- **`mentor-backend/src/mentor/mentor-router.js`**
  - **Purpose**: Express router for all lesson APIs
  - **Endpoints** (used by all algorithms):
    - `POST /api/mentor/start` - Starts any lesson
    - `POST /api/mentor/next` - Gets next step in any lesson
    - `GET /api/mentor/lesson?lessonId={id}` - Gets any lesson
    - `GET /api/mentor/prerequisites?lessonId={id}` - Gets prerequisites for any lesson
    - `GET /api/mentor/concept?conceptId={id}` - Gets concept info
    - `POST /api/mentor/test/validate` - Validates prerequisite KCQ
    - `GET /api/mentor/lesson/level?lessonId={id}` - Gets level for any lesson
    - `GET /api/mentor/level?level={level}` - Gets level info
    - `GET /api/mentor/level/kc?level={level}` - Gets level KCQ
    - `POST /api/mentor/level/kc/validate` - Validates level KCQ
    - `GET /api/mentor/level/check-up?currentLessonId={id}` - Checks level-up
  - **File Dependencies**:
    - Uses: `lesson-engine.js`
    - Uses: `prerequisite-engine.js`
  - **Used By**: All 125 algorithms

#### AI Helper
- **`mentor-backend/src/mentor/ai-helper.js`**
  - **Purpose**: Answer user questions about concepts
  - **Used By**: All algorithms (when user asks questions)
  - **File Dependencies**:
    - Uses: `question-cache.js`
    - Reads/Writes: `mentor/questions-cache.json`

#### Question Cache
- **`mentor-backend/src/mentor/question-cache.js`**
  - **Purpose**: Cache AI question answers
  - **Used By**: AI helper for all algorithms
  - **File Dependencies**:
    - Reads/Writes: `mentor/questions-cache.json`

---

### 5. Frontend Files (Shared by All Algorithms)

#### Main Lesson Page
- **`ide-frontend/learn.html`**
  - **Purpose**: Main lesson rendering page
  - **Contains**: HTML structure, JavaScript for lesson flow
  - **Functions** (used by all algorithms):
    - `startLesson(lessonId)` - Starts any lesson
    - `getNextStep(stepId, choiceLabel)` - Gets next step
    - `renderStep(step)` - Renders lesson step
    - `showPrerequisites(prerequisites)` - Shows prerequisite step
    - `openPrerequisitesKC(prerequisiteIds)` - Opens KCQ modal
    - `showConceptLearning(concept)` - Shows concept learning options
    - `showICL(conceptId)` - Opens ICL Tool
    - `checkLevelUp()` - Checks for level-up after completion
  - **File Dependencies**:
    - Uses: `assets/app.js`
    - Uses: `assets/concept-explainer.js`
    - Uses: `assets/styles.css`
  - **Used By**: All 125 algorithms

#### ICL Tool Component
- **`ide-frontend/assets/concept-explainer.js`**
  - **Purpose**: ICL Tool frontend component
  - **Functions**:
    - `showICL(conceptId)` - Opens ICL Tool for any concept
    - `ICL.init()` - Loads concept JSON files
    - `ICL.renderScreen()` - Renders intro/builder/quiz screens
  - **File Dependencies**:
    - Fetches: `/concepts/{any-concept-id}.json` (dynamically)
  - **Used By**: All algorithms (when user needs to learn concepts)

#### ICL Tool Styles
- **`ide-frontend/assets/concept-explainer.css`**
  - **Purpose**: Styling for ICL Tool
  - **Used By**: `concept-explainer.js` (for all algorithms)

#### Navigation Utilities
- **`ide-frontend/assets/app.js`**
  - **Purpose**: Navigation and utility functions
  - **Used By**: `learn.html` (for all algorithms)

#### Main Styles
- **`ide-frontend/assets/styles.css`**
  - **Purpose**: Main application styles
  - **Used By**: `learn.html` (for all algorithms)

#### Algorithm Listing Page
- **`ide-frontend/algos.html`**
  - **Purpose**: Lists all 125 algorithms
  - **Contains**: Cards for all algorithms with links to `/learn/{lesson-id}`
  - **Generated By**: `generate_algos_page.py`
  - **Used By**: All 125 algorithms (entry point)

---

### 6. Server Configuration (Shared by All Algorithms)

#### Main Server
- **`mentor-backend/src/server.js`**
  - **Purpose**: Express server setup
  - **Configures**:
    - Static file serving for `/concepts/*.json`
    - Route: `GET /learn/:lessonId` → serves `learn.html` (for any lesson)
    - Route: `GET /algos` → serves `algos.html`
    - API routes: `/api/mentor/*` → `mentor-router.js` (for all algorithms)
  - **File Dependencies**:
    - Uses: `mentor-router.js`
    - Serves: `ide-frontend/concepts/*.json`
    - Serves: `ide-frontend/learn.html`
  - **Used By**: All 125 algorithms

---

### 7. Generation Scripts (Optional)

#### Algorithm Page Generator
- **`mentor-backend/generate_algos_page.py`**
  - **Purpose**: Generates algos.html with all 125 lessons
  - **Reads**: `mentor/lessons/index.json`
  - **Reads**: `mentor/prerequisites.json` (for level mapping)
  - **Generates**: `ide-frontend/algos.html` (includes all 125 algorithms)

---

## File Count Summary

### By Category

| Category | Count | Description |
|---------|-------|-------------|
| **Common Data Files** | 4 | Shared by all algorithms |
| **Algorithm-Specific Files** | 125 | One per algorithm |
| **ICL Tool Configs** | 5 | Concept learning configs |
| **Backend Engines** | 5 | Shared processing engines |
| **Frontend Files** | 6 | Shared UI components |
| **Server Files** | 1 | Express server |
| **Generation Scripts** | 1 | Page generator |
| **TOTAL** | **151** | All files in the system |

### By Type

| Type | Count | Files |
|------|-------|-------|
| **JSON Data Files** | 135 | 125 lesson files + 4 common + 5 ICL configs + 1 cache |
| **JavaScript Files** | 6 | 5 backend engines + 1 frontend component |
| **HTML Files** | 2 | learn.html + algos.html |
| **CSS Files** | 2 | styles.css + concept-explainer.css |
| **Python Scripts** | 1 | generate_algos_page.py |
| **Node.js Files** | 1 | server.js |

---

## File Flow for Any Algorithm

```
┌─────────────────────────────────────────────────────────────┐
│         UNIVERSAL FILE FLOW FOR ANY ALGORITHM              │
└─────────────────────────────────────────────────────────────┘

USER CLICKS ALGORITHM ON /algos
    ↓
1. FRONTEND: algos.html
   └─→ Links to: /learn/{any-lesson-id}
    ↓
2. SERVER: server.js
   └─→ Serves: ide-frontend/learn.html
    ↓
3. FRONTEND: learn.html
   └─→ Calls: POST /api/mentor/start { lessonId: "{any-id}" }
    ↓
4. BACKEND: mentor-router.js
   ├─→ lesson-engine.js
   │   └─→ Reads: mentor/lessons/{any-lesson-id}.json
   │
   └─→ prerequisite-engine.js
       └─→ Reads: mentor/prerequisites.json
           ├─→ Gets: lessonPrerequisites["{any-lesson-id}"]
           └─→ Gets: concepts.{conceptId} for each prerequisite
    ↓
5. RESPONSE: { lessonId: "{any-id}", step: prerequisites-display }
    ↓
6. FRONTEND: learn.html
   └─→ Renders prerequisite step
    ↓
7. USER CHOOSES: "I need to learn these"
    ↓
8. FRONTEND: learn.html
   └─→ Calls: showICL("{concept-id}")
    ↓
9. FRONTEND: concept-explainer.js
   └─→ Fetches: GET /concepts/{concept-id}.json
    ↓
10. SERVER: server.js
    └─→ Serves: ide-frontend/concepts/{concept-id}.json (static file)
    ↓
11. FRONTEND: concept-explainer.js
    └─→ Renders ICL Tool screens
    ↓
12. USER COMPLETES PREREQUISITES → Starts lesson
    ↓
13. FRONTEND: learn.html
    └─→ Calls: POST /api/mentor/next { lessonId: "{any-id}", stepId: "title" }
    ↓
14. BACKEND: mentor-router.js
    └─→ lesson-engine.js
        └─→ Reads: mentor/lessons/{any-lesson-id}.json
        └─→ Returns: Next step from flow array
    ↓
15. FRONTEND: learn.html
    └─→ Renders step (problem illustration, thinking challenge, coding steps, etc.)
    ↓
16. USER COMPLETES LESSON
    ↓
17. FRONTEND: learn.html
    └─→ Calls: GET /api/mentor/level/check-up?currentLessonId={any-id}
    ↓
18. BACKEND: prerequisite-engine.js
    └─→ Reads: mentor/prerequisites.json
        └─→ Gets: lessonLevels["{any-lesson-id}"]
        └─→ Checks if previous level lessons completed
        └─→ Returns: Level-up info
    ↓
19. FRONTEND: learn.html
    └─→ Shows level-up message (if applicable)
    └─→ Offers: Level Knowledge Check (if applicable)
```

---

## Algorithm-Specific File Pattern

For any algorithm with ID `{lesson-id}`, the system uses:

### Required File
- **`mentor-backend/mentor/lessons/{lesson-id}.json`**
  - Must exist for the algorithm to be teachable
  - Contains complete lesson flow

### Referenced in
- **`mentor-backend/mentor/lessons/index.json`**
  - Entry in lessons array with metadata

- **`mentor-backend/mentor/prerequisites.json`**
  - Entry in `lessonPrerequisites["{lesson-id}"]` → Array of concept IDs
  - Entry in `lessonLevels["{lesson-id}"]` → Level number (1-12)

### Example: Binary Search

- **Lesson File**: `mentor-backend/mentor/lessons/binary-search.json`
- **Index Entry**: `index.json` → `{ id: "binary-search", title: "Binary search", ... }`
- **Prerequisites**: `prerequisites.json` → `lessonPrerequisites["binary-search"]: ["arrays", "variables", "functions", "parameters", "loops"]`
- **Level**: `prerequisites.json` → `lessonLevels["binary-search"]: 5`

---

## Concept Usage Across Algorithms

### Most Common Concepts (Used by Most Algorithms)

| Concept | Algorithms Using It | ICL Tool Config |
|---------|---------------------|-----------------|
| **arrays** | ~120/125 | `arrays.json` ✅ |
| **variables** | 125/125 | `variables.json` ✅ |
| **functions** | 125/125 | `functions.json` ✅ |
| **parameters** | 125/125 | `parameters.json` ✅ |
| **loops** | ~120/125 | `loops.json` ✅ |

### Advanced Concepts (Used by Some Algorithms)

| Concept | Algorithms Using It | ICL Tool Config |
|---------|---------------------|-----------------|
| **hash-maps** | ~30/125 | Not yet created |
| **two-pointers** | ~25/125 | Not yet created |
| **sliding-window** | ~20/125 | Not yet created |
| **recursion** | ~15/125 | Not yet created |
| **backtracking** | ~10/125 | Not yet created |
| **dynamic-programming** | ~10/125 | Not yet created |

**Note**: ICL Tool configs for advanced concepts can be added as needed.

---

## Level Distribution

All 125 algorithms are distributed across 12 levels:

| Level | Algorithms | Concepts Covered |
|-------|------------|------------------|
| **Level 1** | ~10 | Foundations (arrays, variables, functions, parameters, loops) |
| **Level 2** | ~10 | Two Sum & Pair Logic (hash-maps, two-pointers) |
| **Level 3** | ~10 | Sliding Window Pattern |
| **Level 4** | ~10 | Two Pointers Pattern (Advanced) |
| **Level 5** | ~10 | Searching (Linear → Binary) |
| **Level 6** | ~10 | Sorting Fundamentals |
| **Level 7** | ~10 | Hashing & Frequency Maps |
| **Level 8** | ~10 | Stack Fundamentals |
| **Level 9** | ~10 | Queue & Deque |
| **Level 10** | ~10 | Recursion Basics |
| **Level 11** | ~10 | Backtracking (Intro) |
| **Level 12** | ~15 | Dynamic Programming (Beginner-Friendly) |

**Total**: 125 algorithms across 12 levels

---

## File Dependencies Graph

```
┌─────────────────────────────────────────────────────────────┐
│              FILE DEPENDENCIES (ALL ALGORITHMS)           │
└─────────────────────────────────────────────────────────────┘

Common Files (Shared)
├─→ index.json (125 lessons metadata)
├─→ prerequisites.json (concepts, levels, mappings)
├─→ questions-cache.json (AI cache)
│
Algorithm-Specific Files (125 files)
├─→ {lesson-id-1}.json
├─→ {lesson-id-2}.json
├─→ ...
└─→ {lesson-id-125}.json
    ↓
Backend Engines (Shared)
├─→ lesson-engine.js
│   ├─→ Reads: index.json
│   └─→ Reads: {any-lesson-id}.json (dynamically)
│
├─→ prerequisite-engine.js
│   └─→ Reads: prerequisites.json
│
├─→ mentor-router.js
│   ├─→ Uses: lesson-engine.js
│   └─→ Uses: prerequisite-engine.js
│
├─→ ai-helper.js
│   └─→ Uses: question-cache.js
│
└─→ question-cache.js
    └─→ Reads/Writes: questions-cache.json
    ↓
Frontend Files (Shared)
├─→ learn.html
│   ├─→ Uses: app.js
│   ├─→ Uses: concept-explainer.js
│   └─→ Uses: styles.css
│
├─→ concept-explainer.js
│   └─→ Fetches: /concepts/{concept-id}.json (dynamically)
│
├─→ algos.html
│   └─→ Generated by: generate_algos_page.py
│       ├─→ Reads: index.json
│       └─→ Reads: prerequisites.json
│
└─→ Server: server.js
    ├─→ Uses: mentor-router.js
    ├─→ Serves: learn.html (for any lesson)
    └─→ Serves: /concepts/*.json (static files)
```

---

## Key Design Principles

### 1. Modular Architecture
- **One file per algorithm**: Easy to update individual lessons
- **Shared engines**: Consistent behavior across all algorithms
- **Shared frontend**: Single UI for all algorithms

### 2. Centralized Configuration
- **Single prerequisites file**: All concepts, levels, mappings in one place
- **Single index file**: All lesson metadata in one place
- **Easy to maintain**: Update once, affects all algorithms

### 3. Dynamic Loading
- **Lesson files loaded on demand**: Only load when needed
- **Concept files loaded on demand**: Only load when user needs to learn
- **Efficient**: No need to load all 125 lessons at once

### 4. Language Support
- **All 5 languages in each lesson file**: Complete support per algorithm
- **Language-specific paths**: Independent flows per language
- **Total**: 625 ICL paths (125 algorithms × 5 languages)

### 5. Extensibility
- **Easy to add new algorithms**: Create new JSON file + add to index
- **Easy to add new concepts**: Add to prerequisites.json + create ICL config
- **Easy to add new levels**: Add to prerequisites.json

---

## Adding a New Algorithm

To add a new algorithm:

1. **Create lesson file**: `mentor/lessons/{new-lesson-id}.json`
   - Follow structure from existing lessons
   - Include all 5 language paths

2. **Add to index**: `mentor/lessons/index.json`
   - Add entry to lessons array

3. **Add prerequisites**: `mentor/prerequisites.json`
   - Add to `lessonPrerequisites["{new-lesson-id}"]`
   - Add to `lessonLevels["{new-lesson-id}"]`

4. **Regenerate algos.html**: Run `generate_algos_page.py`
   - Automatically includes new algorithm

**That's it!** The algorithm is now teachable using all existing infrastructure.

---

## Summary

### Total Files: 151

- **Common/Shared**: 26 files (used by all 125 algorithms)
- **Algorithm-Specific**: 125 files (one per algorithm)
- **Total System Files**: 151 files

### File Breakdown:
- **JSON Data**: 135 files (125 lessons + 10 common/config)
- **JavaScript**: 6 files (5 engines + 1 component)
- **HTML**: 2 files (learn.html + algos.html)
- **CSS**: 2 files (styles + ICL Tool styles)
- **Python**: 1 file (generator script)
- **Node.js**: 1 file (server.js)

### Coverage:
- **125 Algorithms**: All have lesson files
- **5 Languages**: All supported per algorithm
- **625 ICL Paths**: Complete coverage
- **12 Levels**: All levels defined
- **8+ Concepts**: All concepts defined

---

**For algorithm-specific details, see**: `TWO_SUM_FILES.md`  
**For system architecture, see**: `SYSTEM_ARCHITECTURE.md`  
**For teaching patterns, see**: `TEACHING_BLUEPRINT.md`

