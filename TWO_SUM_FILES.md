# Files Involved in Teaching "Two Sum" Algorithm

**Lesson ID**: `two-sum`  
**Level**: 2  
**Pattern**: hash-map  
**Difficulty**: easy

---

## Complete File List

### 1. Lesson Data Files

#### Primary Lesson File
- **`mentor-backend/mentor/lessons/two-sum.json`**
  - **Purpose**: Complete lesson flow for Two Sum algorithm
  - **Contains**: All steps, choices, coding instructions for all 5 languages
  - **Size**: ~1033 lines
  - **Key Sections**:
    - Title/learning goals
    - Problem illustration
    - Thinking challenge (3 approach options)
    - Language-specific paths (js, python, java, cpp, ts)
    - Prerequisite checks per language
    - Progressive coding steps per language
    - Test and completion steps

#### Lesson Metadata
- **`mentor-backend/mentor/lessons/index.json`**
  - **Purpose**: Metadata index for all lessons
  - **Contains**: Entry for two-sum with id, title, pattern, difficulty, status
  - **Used By**: Algorithm listing page, lesson loading

#### Legacy Fallback
- **`mentor-backend/mentor/lessons.json`** (if exists)
  - **Purpose**: Legacy format fallback
  - **Used By**: `lesson-engine.js` if modular file not found

---

### 2. Prerequisites & Concepts Files

#### Central Prerequisites File
- **`mentor-backend/mentor/prerequisites.json`**
  - **Purpose**: Central data file for concepts, levels, and mappings
  - **Contains**:
    - **`lessonPrerequisites["two-sum"]`**: `["arrays", "variables", "functions", "parameters", "loops"]`
    - **`lessonLevels["two-sum"]`**: `2` (Level 2)
    - **`concepts`**: Full definitions for all 5 prerequisite concepts
      - `concepts.arrays` - Arrays and Indexing concept
      - `concepts.variables` - Variables concept
      - `concepts.functions` - Functions/Methods concept
      - `concepts.parameters` - Function Parameters concept
      - `concepts.loops` - Loops concept
    - **`levels["2"]`**: Level 2 information and knowledge check
  - **Used By**: Prerequisite checks, concept explanations, KCQs

---

### 3. ICL Tool Config Files (Interactive Concept Learning)

These files are loaded when user chooses "I need to learn these" or "Open ICL":

- **`ide-frontend/concepts/arrays.json`**
  - **Purpose**: ICL Tool config for Arrays concept
  - **Contains**: Intro, builder, and quiz screens
  - **Used When**: User needs to learn arrays

- **`ide-frontend/concepts/variables.json`**
  - **Purpose**: ICL Tool config for Variables concept
  - **Contains**: Intro, builder, and quiz screens
  - **Used When**: User needs to learn variables

- **`ide-frontend/concepts/functions.json`**
  - **Purpose**: ICL Tool config for Functions concept
  - **Contains**: Intro, builder, and quiz screens
  - **Used When**: User needs to learn functions

- **`ide-frontend/concepts/parameters.json`**
  - **Purpose**: ICL Tool config for Parameters concept
  - **Contains**: Intro, builder, and quiz screens
  - **Used When**: User needs to learn function parameters

- **`ide-frontend/concepts/loops.json`**
  - **Purpose**: ICL Tool config for Loops concept
  - **Contains**: Intro, builder, and quiz screens
  - **Used When**: User needs to learn loops

---

### 4. Backend Engine Files

#### Lesson Engine
- **`mentor-backend/src/mentor/lesson-engine.js`**
  - **Purpose**: Load and navigate lesson flows
  - **Functions Used**:
    - `loadLessonById("two-sum")` - Loads two-sum.json
    - `findStepById(lesson, stepId)` - Finds specific step
    - `getNextStep(lesson, currentStep, choiceLabel)` - Navigates flow
  - **File Dependencies**:
    - Reads: `mentor/lessons/index.json`
    - Reads: `mentor/lessons/two-sum.json`

#### Prerequisite Engine
- **`mentor-backend/src/mentor/prerequisite-engine.js`**
  - **Purpose**: Handle prerequisites, concepts, levels, and KCQs
  - **Functions Used**:
    - `getLessonPrerequisites("two-sum")` - Returns concept IDs
    - `getConceptInfo(conceptId, language)` - Gets concept details
    - `validateTest(conceptId, language, answers)` - Validates KCQ
    - `getLessonLevel("two-sum")` - Returns level 2
    - `getLevelInfo(2)` - Gets Level 2 information
    - `getLevelKnowledgeCheck(2, language)` - Gets Level 2 KCQ
  - **File Dependencies**:
    - Reads: `mentor/prerequisites.json`

#### API Router
- **`mentor-backend/src/mentor/mentor-router.js`**
  - **Purpose**: Express router for all lesson APIs
  - **Endpoints Used**:
    - `POST /api/mentor/start` - Starts two-sum lesson
    - `POST /api/mentor/next` - Gets next step in two-sum
    - `GET /api/mentor/prerequisites?lessonId=two-sum` - Gets prerequisites
    - `GET /api/mentor/concept?conceptId={id}` - Gets concept info
    - `POST /api/mentor/test/validate` - Validates prerequisite KCQ
    - `GET /api/mentor/level/kc?level=2` - Gets Level 2 KCQ
    - `POST /api/mentor/level/kc/validate` - Validates Level 2 KCQ
  - **File Dependencies**:
    - Uses: `lesson-engine.js`
    - Uses: `prerequisite-engine.js`

#### AI Helper (Optional)
- **`mentor-backend/src/mentor/ai-helper.js`**
  - **Purpose**: Answer user questions about concepts
  - **Used When**: User asks "I have a specific question" about a concept
  - **File Dependencies**:
    - Uses: `question-cache.js`

#### Question Cache
- **`mentor-backend/src/mentor/question-cache.js`**
  - **Purpose**: Cache AI question answers
  - **File Dependencies**:
    - Reads/Writes: `mentor/questions-cache.json`

---

### 5. Frontend Files

#### Main Lesson Page
- **`ide-frontend/learn.html`**
  - **Purpose**: Main lesson rendering page
  - **Contains**: HTML structure, JavaScript for lesson flow
  - **Functions**:
    - `startLesson("two-sum")` - Starts the lesson
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

#### ICL Tool Component
- **`ide-frontend/assets/concept-explainer.js`**
  - **Purpose**: ICL Tool frontend component
  - **Functions**:
    - `showICL("arrays")` - Opens ICL Tool for arrays
    - `ICL.init()` - Loads concept JSON files
    - `ICL.renderScreen()` - Renders intro/builder/quiz screens
  - **File Dependencies**:
    - Fetches: `/concepts/arrays.json`
    - Fetches: `/concepts/variables.json`
    - Fetches: `/concepts/functions.json`
    - Fetches: `/concepts/parameters.json`
    - Fetches: `/concepts/loops.json`

#### ICL Tool Styles
- **`ide-frontend/assets/concept-explainer.css`**
  - **Purpose**: Styling for ICL Tool
  - **Used By**: `concept-explainer.js`

#### Navigation Utilities
- **`ide-frontend/assets/app.js`**
  - **Purpose**: Navigation and utility functions
  - **Used By**: `learn.html`

#### Main Styles
- **`ide-frontend/assets/styles.css`**
  - **Purpose**: Main application styles
  - **Used By**: `learn.html`

#### Algorithm Listing Page
- **`ide-frontend/algos.html`**
  - **Purpose**: Lists all algorithms (including two-sum)
  - **Contains**: Two Sum card with link to `/learn/two-sum`
  - **Generated By**: `generate_algos_page.py`

---

### 6. Server Configuration

#### Main Server
- **`mentor-backend/src/server.js`**
  - **Purpose**: Express server setup
  - **Configures**:
    - Static file serving for `/concepts/*.json`
    - Route: `GET /learn/:lessonId` → serves `learn.html`
    - Route: `GET /algos` → serves `algos.html`
    - API routes: `/api/mentor/*` → `mentor-router.js`
  - **File Dependencies**:
    - Uses: `mentor-router.js`
    - Serves: `ide-frontend/concepts/*.json`
    - Serves: `ide-frontend/learn.html`

---

### 7. Generation Scripts (Optional)

#### Algorithm Page Generator
- **`mentor-backend/generate_algos_page.py`**
  - **Purpose**: Generates algos.html with all lessons
  - **Reads**: `mentor/lessons/index.json`
  - **Reads**: `mentor/prerequisites.json` (for level mapping)
  - **Generates**: `ide-frontend/algos.html` (includes two-sum)

---

## File Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│              TWO-SUM LESSON FILE FLOW                      │
└─────────────────────────────────────────────────────────────┘

USER CLICKS "Two Sum" ON /algos
    ↓
1. FRONTEND: algos.html
   └─→ Links to: /learn/two-sum
    ↓
2. SERVER: server.js
   └─→ Serves: ide-frontend/learn.html
    ↓
3. FRONTEND: learn.html
   └─→ Calls: POST /api/mentor/start { lessonId: "two-sum" }
    ↓
4. BACKEND: mentor-router.js
   ├─→ lesson-engine.js
   │   └─→ Reads: mentor/lessons/two-sum.json
   │
   └─→ prerequisite-engine.js
       └─→ Reads: mentor/prerequisites.json
           ├─→ Gets: lessonPrerequisites["two-sum"]
           │   └─→ ["arrays", "variables", "functions", "parameters", "loops"]
           │
           └─→ Gets: concepts.arrays, concepts.variables, etc.
    ↓
5. RESPONSE: { lessonId: "two-sum", step: prerequisites-display }
    ↓
6. FRONTEND: learn.html
   └─→ Renders prerequisite step
    ↓
7. USER CHOOSES: "I need to learn these"
    ↓
8. FRONTEND: learn.html
   └─→ Calls: showICL("arrays")
    ↓
9. FRONTEND: concept-explainer.js
   └─→ Fetches: GET /concepts/arrays.json
    ↓
10. SERVER: server.js
    └─→ Serves: ide-frontend/concepts/arrays.json (static file)
    ↓
11. FRONTEND: concept-explainer.js
    └─→ Renders ICL Tool screens
    ↓
12. USER COMPLETES PREREQUISITES → Starts lesson
    ↓
13. FRONTEND: learn.html
    └─→ Calls: POST /api/mentor/next { lessonId: "two-sum", stepId: "title" }
    ↓
14. BACKEND: mentor-router.js
    └─→ lesson-engine.js
        └─→ Reads: mentor/lessons/two-sum.json
        └─→ Returns: Next step from flow array
    ↓
15. FRONTEND: learn.html
    └─→ Renders step (problem illustration, thinking challenge, coding steps, etc.)
    ↓
16. USER COMPLETES LESSON
    ↓
17. FRONTEND: learn.html
    └─→ Calls: GET /api/mentor/level/check-up?currentLessonId=two-sum
    ↓
18. BACKEND: prerequisite-engine.js
    └─→ Reads: mentor/prerequisites.json
        └─→ Gets: lessonLevels["two-sum"] = 2
        └─→ Checks if Level 1 lessons completed
        └─→ Returns: Level-up info
    ↓
19. FRONTEND: learn.html
    └─→ Shows Level 2 level-up message
    └─→ Offers: Level 2 Knowledge Check
    ↓
20. IF USER TAKES LEVEL KC:
    └─→ Calls: GET /api/mentor/level/kc?level=2
    └─→ Backend: prerequisite-engine.js
        └─→ Reads: mentor/prerequisites.json
            └─→ Gets: levels["2"].knowledgeCheck
            └─→ Returns: Level 2 KCQ questions
```

---

## File Summary by Category

### Data Files (5 files)
1. `mentor/lessons/two-sum.json` - Main lesson file
2. `mentor/lessons/index.json` - Lesson metadata
3. `mentor/prerequisites.json` - Concepts, levels, mappings
4. `mentor/questions-cache.json` - AI question cache (optional)
5. `mentor/lessons.json` - Legacy fallback (optional)

### ICL Tool Configs (5 files)
6. `ide-frontend/concepts/arrays.json`
7. `ide-frontend/concepts/variables.json`
8. `ide-frontend/concepts/functions.json`
9. `ide-frontend/concepts/parameters.json`
10. `ide-frontend/concepts/loops.json`

### Backend Engine Files (5 files)
11. `src/mentor/lesson-engine.js` - Lesson loading
12. `src/mentor/prerequisite-engine.js` - Prerequisites/levels
13. `src/mentor/mentor-router.js` - API endpoints
14. `src/mentor/ai-helper.js` - AI questions (optional)
15. `src/mentor/question-cache.js` - Question caching

### Frontend Files (6 files)
16. `ide-frontend/learn.html` - Main lesson page
17. `ide-frontend/assets/concept-explainer.js` - ICL Tool
18. `ide-frontend/assets/concept-explainer.css` - ICL Tool styles
19. `ide-frontend/assets/app.js` - Navigation utilities
20. `ide-frontend/assets/styles.css` - Main styles
21. `ide-frontend/algos.html` - Algorithm listing

### Server Files (1 file)
22. `src/server.js` - Express server

### Generation Scripts (1 file, optional)
23. `generate_algos_page.py` - Generates algos.html

---

## Total: 23 Files

### Breakdown:
- **Data Files**: 5
- **ICL Tool Configs**: 5
- **Backend Engines**: 5
- **Frontend Files**: 6
- **Server**: 1
- **Scripts**: 1

---

## Key File Relationships

### Core Lesson Flow
```
two-sum.json (lesson data)
    ↓
lesson-engine.js (loads & navigates)
    ↓
mentor-router.js (API endpoints)
    ↓
learn.html (renders UI)
```

### Prerequisites Flow
```
prerequisites.json (concept definitions)
    ↓
prerequisite-engine.js (processes)
    ↓
mentor-router.js (API endpoints)
    ↓
learn.html (shows prerequisites)
    ↓
concepts/*.json (ICL Tool configs)
    ↓
concept-explainer.js (renders ICL Tool)
```

### Level Progression Flow
```
prerequisites.json (level definitions)
    ↓
prerequisite-engine.js (checks level-up)
    ↓
mentor-router.js (API endpoints)
    ↓
learn.html (shows level-up & Level KC)
```

---

## Notes

1. **Primary Lesson File**: `two-sum.json` contains the complete lesson flow
2. **Prerequisites**: 5 concepts required (arrays, variables, functions, parameters, loops)
3. **ICL Tool**: 5 config files available for concept learning
4. **Level**: Two Sum is in Level 2, so Level 2 KCQ may be offered after completion
5. **Languages**: Lesson supports all 5 languages (js, python, java, cpp, ts)
6. **Related Lessons**: 
   - `two-sum-hashmap.json` - Hash map approach variant
   - `two-sum-optimized.json` - Optimized approach variant

---

**For detailed architecture, see**: `SYSTEM_ARCHITECTURE.md`  
**For teaching patterns, see**: `TEACHING_BLUEPRINT.md`

