# Algorithm Lesson Content Completion Plan

**Status**: Acknowledged & Planning  
**Date**: 2024  
**Scope**: 125 algorithm lessons

---

## Current Situation

### ✅ Completed (Reference Quality)
- **two-sum.json** - Full custom content, multiple approaches, detailed coding steps
- **binary-search.json** - Full custom content, algorithm explanation, detailed coding steps

### ❌ Needs Complete Rewrite (123 files)
**Problem Confirmed**: Quality checker script identified 123 files with template content:
- Generic problem illustrations ("Example input and expected output")
- Template explanations ("We need to solve this step by step")
- Broken choice branches (all choices lead to same step)
- Missing coding steps (jumps from "start" to "complete")

**Example Issues Found:**
- `task-scheduler.json` - 559 lines of generic template
- `basic-calculator.json` - Generic problem illustration, template explanation
- `bubble-sort.json` - Jumps from start to complete with no intermediate steps
- All 123 files have similar template content issues

---

## Requirements Acknowledged

### Content Standards
1. **Custom Problem Explanations**
   - Use concrete examples (not "example input")
   - Walk through examples step-by-step
   - Explain what makes the problem tricky

2. **Multiple Approaches**
   - At least 2-3 different solution approaches
   - Each approach has separate exploration steps
   - Choice branches lead to different content

3. **Incremental Coding Steps**
   - 5-8 progressive coding steps per language
   - Each step adds ONE new concept
   - Explain WHY each part is needed
   - Build from skeleton → complete solution

4. **Language Support**
   - All 5 languages (JavaScript, Python, Java, C++, TypeScript)
   - Language-specific syntax and terminology
   - Independent paths per language

5. **Test Cases**
   - Specific test cases with expected outputs
   - Edge cases included
   - Clear verification instructions

### Quality Checklist (Per Algorithm)
- [ ] Problem explained with concrete example
- [ ] At least 2 different approaches discussed
- [ ] Each approach has "why this works" explanation
- [ ] Choice branches lead to different content
- [ ] Code builds incrementally (5-8 steps)
- [ ] Each coding step explains WHY
- [ ] Test cases include edge cases
- [ ] All 5 languages fully implemented
- [ ] No broken navigation
- [ ] No placeholder text

---

## Implementation Plan

### Phase 1: High-Value Foundation (10 algorithms)
**Priority Order:**
1. ✅ two-sum - DONE
2. ✅ binary-search - DONE
3. **three-sum** - Next (builds on two-sum)
4. **top-k-frequent-elements** - Hash map + sorting
5. **trapping-rain-water** - Two pointers
6. **trapping-rain-water-stack** - Stack alternative
7. **task-scheduler** - Greedy approach
8. **valid-parentheses** - Stack fundamentals
9. **longest-substring-no-repeat** - Sliding window
10. **reverse-array** - Two pointers basics

**Estimated Time**: 80-120 hours (8-12 hours each)

### Phase 2-8: Remaining 113 Algorithms
**Estimated Time**: 1,130-1,695 hours (10-15 hours each)

**Total Estimated Time**: 1,210-1,815 hours

---

## Tools Created

### 1. Quality Checker Script
**File**: `mentor-backend/scripts/check_lesson_quality.py`

**Purpose**: Automatically identify template content vs. real content

**Usage**:
```bash
python mentor-backend/scripts/check_lesson_quality.py
```

**Output**:
- Console report showing status of all files
- Detailed markdown report: `mentor-backend/LESSON_QUALITY_REPORT.md`

### 2. Progress Tracker
**File**: `LESSON_CONTENT_TRACKER.md`

**Purpose**: Track completion status and prioritize algorithms

**Contains**:
- Priority order by phase
- Quality checklist
- Workflow per algorithm
- Progress tracking

---

## Workflow Per Algorithm

### Step 1: Research (2-3 hours)
- Solve problem in 2-3 different ways
- Find best teaching examples
- Outline key concepts
- Identify common mistakes

### Step 2: Draft Structure (1 hour)
- Map out flow graph
- Decide which approaches to teach
- Plan branching logic

### Step 3: Write Content (4-6 hours)
- Write problem illustration with concrete example
- Write approach explorations
- Write incremental coding steps for ONE language
- Test the flow mentally

### Step 4: Replicate for Other Languages (2-3 hours)
- Adapt coding steps for Python, Java, C++, TypeScript
- Adjust syntax and language-specific concepts

### Step 5: Test & Polish (1 hour)
- Walk through as a learner
- Fix confusing parts
- Verify all navigation works

**Total: 10-15 hours per algorithm**

---

## Reference Files

### Use as Quality Standards:
- **`mentor-backend/mentor/lessons/two-sum.json`**
  - Excellent problem illustration with concrete example
  - Multiple approach branches (pairs, sort, subtract)
  - Detailed incremental coding steps
  - All 5 languages fully implemented

- **`mentor-backend/mentor/lessons/binary-search.json`**
  - Clear algorithm explanation
  - Step-by-step trace examples
  - Progressive coding steps
  - Complete language support

### What NOT to Do:
❌ Don't copy-paste from two-sum  
❌ Don't use placeholder text  
❌ Don't have choices that all go to same step  
❌ Don't jump from "start" to "complete"  
❌ Don't write generic advice - be specific

---

## Next Steps

1. **Start with Phase 1, Algorithm #3: three-sum**
   - Research the problem thoroughly
   - Write custom content following two-sum pattern
   - Complete all 5 language paths
   - Verify quality checklist

2. **Track Progress**
   - Update `LESSON_CONTENT_TRACKER.md` as algorithms are completed
   - Run quality checker after each completion
   - Review against reference files

3. **Iterate**
   - Complete Phase 1 (10 algorithms)
   - Review and adjust process
   - Continue with Phase 2-8

---

## Notes

- **This is high-value work**: Done right, these lessons will actually teach people
- **Quality over speed**: Better to do 10 algorithms well than 50 poorly
- **Reference quality**: Every algorithm should match two-sum quality level
- **Custom content**: Each algorithm needs its own problem explanation and examples
- **Incremental building**: Code should build step-by-step, not jump from start to done

---

**For detailed tracking, see**: `LESSON_CONTENT_TRACKER.md`  
**For quality reports, run**: `python mentor-backend/scripts/check_lesson_quality.py`

