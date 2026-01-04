# Prerequisite Verification System (Option 2 Modified)

## Overview

We've implemented **Option 2 (Modified)** - a prerequisite verification system that ensures learners have the foundational knowledge before starting algorithm lessons, while maintaining flexibility.

## Architecture

### 1. Modular Lesson Structure
- **Before**: Single `lessons.json` file (462K+ characters)
- **After**: Individual lesson files in `mentor/lessons/{lesson-id}.json`
- **Index**: `mentor/lessons/index.json` contains metadata and prerequisites

### 2. Prerequisite System
- **File**: `mentor/prerequisites.json`
- **Structure**:
  - `concepts`: Language-specific explanations, examples, tests
  - `lessonPrerequisites`: Maps lesson IDs to required concept IDs

### 3. API Endpoints

#### Get Lesson Prerequisites
```
GET /api/mentor/prerequisites?lessonId={id}&language={lang}
```
Returns all prerequisites for a lesson with language-specific information.

#### Get Concept Details
```
GET /api/mentor/concept?conceptId={id}&language={lang}
```
Returns detailed information about a specific concept (explanation, examples, docs, test).

#### Validate Test
```
POST /api/mentor/test/validate
Body: { conceptId, language, answers: [0, 1, ...] }
```
Validates test answers and returns score (70% threshold to pass).

## User Flow (Option 2 Modified)

### Step 1: Prerequisite Display
When user clicks on a lesson, show:
```
Before learning [Lesson Name], you are expected to know:

1. Fundamentals of [Language]
   1.1. Arrays and Indexing
   1.2. Variables
   1.3. Functions/Methods
   1.4. Function Parameters
   1.5. Loops

[I know all these] [Test my knowledge] [I need to learn these]
```

### Step 2: User Choices

#### Choice A: "I know all these"
- Proceed directly to lesson
- Trust the user, but allow fallback during lesson

#### Choice B: "Test my knowledge"
- Show quick test (2-3 questions per concept)
- If score ≥ 70%: Proceed to lesson
- If score < 70%: Show "I need to learn these" path

#### Choice C: "I need to learn these"
- Show structured learning path
- For each concept:
  - Explanation
  - Examples
  - "I understand" → Next concept
  - "Need more info" → Options:
    - "Read official docs" (opens link)
    - "More examples" (shows additional examples)
    - "Other" (custom question field)

### Step 3: During Lesson (Fallback)
If user says "I don't know [concept]" during lesson:
- Show quick explanation
- Offer "Need more info" with same options as above
- Continue lesson after explanation

## Benefits

1. **Ensures Foundation**: Learners have required knowledge before building on it
2. **Flexible**: Optional test doesn't block motivated learners
3. **Scalable**: Prerequisites can be reused across lessons
4. **Language-Specific**: Each concept has language-specific explanations
5. **Self-Paced**: Learners can skip test if confident
6. **Fallback Support**: "Need more info" available during lessons too

## Implementation Status

✅ Modular lesson structure
✅ Prerequisite data structure
✅ Backend API endpoints
✅ Prerequisite engine
⏳ Frontend integration (next step)
⏳ Test UI components
⏳ Prerequisite display UI

## Next Steps

1. Update frontend to show prerequisites before lesson starts
2. Implement test UI component
3. Create "Need more info" modal with options
4. Integrate with existing lesson flow
5. Add prerequisite completion tracking

## File Structure

```
mentor-backend/
├── mentor/
│   ├── lessons/
│   │   ├── index.json (metadata + prerequisites)
│   │   ├── two-sum.json
│   │   ├── print-array-elements.json
│   │   └── ...
│   ├── prerequisites.json (concept definitions)
│   └── lessons.json (legacy, kept for fallback)
└── src/
    └── mentor/
        ├── lesson-engine.js (loads modular lessons)
        ├── prerequisite-engine.js (handles prerequisites)
        └── mentor-router.js (API endpoints)
```
