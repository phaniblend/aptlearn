# Level-Based Knowledge Checks (KCs)

## Overview

Knowledge checks (KCs) are now available **throughout lessons** and are **level-specific**. When a learner reaches a new level, they see a congratulatory message and can take a knowledge check for that level's advanced concepts.

## Architecture

### 1. Level Definitions
Each level in `prerequisites.json` has:
- **Name & Description**: What the level covers
- **Congratulation Message**: Shown when user reaches the level
- **Advanced Concepts**: New concepts introduced in this level
- **Knowledge Check**: Concepts to test for this level

### 2. Level Mapping
Lessons are mapped to levels in `lessonLevels`:
```json
{
  "print-array-elements": 1,
  "two-sum": 2,
  "max-sum-subarray-k": 3,
  ...
}
```

### 3. Knowledge Check Structure
Each level has a KC that tests:
- **Level 1**: Fundamentals (arrays, variables, functions, parameters, loops)
- **Level 2**: Hash maps, two pointers
- **Level 3**: Sliding window
- **Level 4+**: Advanced concepts for that level

## API Endpoints

### Get Level Information
```
GET /api/mentor/level?level={level}
```
Returns level name, description, congratulation message, and advanced concepts.

### Get Level Knowledge Check
```
GET /api/mentor/level/kc?level={level}&language={lang}
```
Returns the knowledge check for a level with all questions from all concepts.

### Validate Level Knowledge Check
```
POST /api/mentor/level/kc/validate
Body: {
  level: 2,
  language: "js",
  answers: {
    "hash-maps": [0, 1],
    "two-pointers": [1]
  }
}
```
Validates answers for all concepts in the level KC. Returns overall score (70% to pass).

### Get Lesson Level
```
GET /api/mentor/lesson/level?lessonId={id}
```
Returns the level number and level info for a lesson.

### Check Level Up
```
GET /api/mentor/level/check-up?currentLessonId={id}&completedLessonIds=id1,id2,id3
```
Checks if user should see level-up message (when all previous level lessons are completed).

## User Flow

### 1. Level-Up Detection
When user starts a lesson:
- System checks if they've completed all previous level lessons
- If yes → Show congratulatory message + offer level KC

### 2. Level-Up Message
```
🎉 Congratulations! You've made it to Level 2!

In this level, you'll learn more advanced concepts:
- Hash Maps (Objects/Dictionaries) for fast lookups
- Two Pointers technique for efficient array traversal
- Pair logic and index awareness

[Take Level 2 Knowledge Check] [Skip and Continue]
```

### 3. Knowledge Check Flow
If user chooses "Take Level 2 Knowledge Check":
- Show questions from all level concepts (hash-maps, two-pointers)
- User answers all questions
- System validates and shows score
- If ≥70%: "Great! You're ready for Level 2!"
- If <70%: "Let's review these concepts first" → Show learning path

### 4. KC Available Throughout Lessons
- **Button**: "Knowledge Check" button always visible in lesson UI
- **Click**: Opens KC modal for current level
- **Purpose**: Let users test their understanding anytime

## Implementation Status

✅ Level definitions in prerequisites.json
✅ Advanced concepts (hash-maps, two-pointers, sliding-window)
✅ Level mapping for lessons
✅ Level KC API endpoints
✅ Level-up detection logic
✅ Congratulatory messages
⏳ Frontend integration (next step)
⏳ KC button in lesson UI
⏳ Level-up modal component

## Example: Level 2 Knowledge Check

**Concepts Tested:**
1. Hash Maps
   - What is the main advantage of using a hash map?
   - How do you access a value in a JavaScript object?

2. Two Pointers
   - What is the two pointers technique used for?

**Passing Score**: 70% (2 out of 3 questions correct)

## Benefits

1. **Progressive Learning**: Ensures understanding before advancing
2. **Self-Assessment**: Users can test knowledge anytime
3. **Motivation**: Level-up messages celebrate progress
4. **Quality Control**: Prevents knowledge gaps
5. **Flexible**: Optional KCs don't block progress

## Next Steps

1. Add KC button to lesson UI
2. Create level-up modal component
3. Implement KC modal with questions
4. Add progress tracking (completed KCs)
5. Show KC completion badges
