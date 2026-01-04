# Algorithm Lesson Content Completion Tracker

**Status**: Planning Phase  
**Total Algorithms**: 125  
**Completed**: 2 (two-sum, binary-search)  
**Needs Work**: 123  
**Estimated Time**: 1,230-1,845 hours (10-15 hours per algorithm)

---

## Quality Standards

### ✅ Completed (Reference Quality)
- **two-sum.json** - Full custom content, multiple approaches, detailed coding steps
- **binary-search.json** - Full custom content, algorithm explanation, detailed coding steps

### ⚠️ Needs Complete Rewrite (Template Content)
All other 123 files contain generic templates like:
- "Example input and expected output for [Algorithm]"
- "We need to solve this step by step, building our solution gradually"
- "Use a straightforward approach step by step" (both choices go to same place)
- Jump from "start coding" to "done" with no actual steps

---

## Priority Order

### Phase 1: High-Value Foundation Algorithms (10 algorithms)
**Goal**: Complete core patterns that other algorithms build on

1. ✅ **two-sum** - DONE (reference quality)
2. ✅ **binary-search** - DONE (reference quality)
3. 🔄 **three-sum** - Next priority (builds on two-sum)
4. ⏳ **top-k-frequent-elements** - Hash map + sorting pattern
5. ⏳ **trapping-rain-water** - Two pointers pattern
6. ⏳ **trapping-rain-water-stack** - Stack pattern alternative
7. ⏳ **task-scheduler** - Greedy approach
8. ⏳ **valid-parentheses** - Stack fundamentals
9. ⏳ **longest-substring-no-repeat** - Sliding window pattern
10. ⏳ **reverse-array** - Two pointers basics

### Phase 2: Pattern Completion (20 algorithms)
Complete all variations of core patterns

**Two Pointers:**
- container-with-most-water
- squares-of-sorted-array
- move-zeros-to-end
- remove-duplicates-unsorted
- check-palindrome
- reverse-string

**Sliding Window:**
- max-sum-subarray-k
- min-sum-subarray-k
- longest-substring-k-distinct
- fruits-into-baskets
- count-subarrays-size-k
- max-average-subarray
- smallest-subarray-sum-s

**Hash Maps:**
- group-anagrams
- valid-anagram
- contains-duplicate
- first-repeating-element
- first-non-repeating-element
- count-pairs-with-sum-k
- subarray-sum-equals-k

### Phase 3: Sorting Algorithms (10 algorithms)
- bubble-sort
- selection-sort
- insertion-sort
- merge-sort
- quick-sort
- heap-sort
- counting-sort
- radix-sort
- sort-colors
- kth-largest-element

### Phase 4: Stack & Queue (15 algorithms)
- min-stack
- daily-temperatures
- next-greater-element
- largest-rectangle-histogram
- evaluate-reverse-polish
- remove-k-digits
- decode-string
- basic-calculator
- implement-queue
- design-circular-queue
- design-hit-counter
- moving-average
- sliding-window-maximum
- rearrange-string-k-distance
- design-phone-directory

### Phase 5: Recursion (10 algorithms)
- factorial-recursive
- fibonacci-recursive
- reverse-string-recursive
- palindrome-check-recursive
- reverse-linked-list-recursive
- tree-traversal-recursive
- binary-search-recursive
- climbing-stairs
- power-of-two
- pow-x-n

### Phase 6: Backtracking (15 algorithms)
- subsets
- subsets-ii
- permutations
- permutations-ii
- combination-sum
- combination-sum-ii
- generate-parentheses
- letter-combinations-phone
- word-search
- n-queens

### Phase 7: Dynamic Programming (15 algorithms)
- fibonacci-dp
- climbing-stairs-dp
- coin-change
- house-robber
- min-cost-climbing-stairs
- unique-paths
- longest-common-subsequence
- longest-increasing-subsequence
- edit-distance
- maximum-subarray

### Phase 8: Advanced Patterns (28 algorithms)
- Remaining algorithms covering:
  - Advanced two pointers
  - Advanced sliding window
  - Advanced hash maps
  - Search variations
  - String manipulation
  - Array manipulation

---

## Progress Tracking

### Completed (2/125)
- [x] two-sum.json
- [x] binary-search.json

### In Progress (0/125)
- [ ] (none currently)

### Pending (123/125)
- [ ] All other algorithms

---

## Quality Checklist Per Algorithm

Before marking as complete, verify:

### Content Quality
- [ ] Problem explained with concrete example (not "example input")
- [ ] At least 2 different approaches discussed
- [ ] Each approach has "why this works" explanation
- [ ] Choice branches lead to different content (not same step)
- [ ] Code builds incrementally (5-8 steps, not "start...done")
- [ ] Each coding step explains WHY, not just WHAT
- [ ] Test cases include edge cases
- [ ] Final step has actual encouragement/summary

### Technical Accuracy
- [ ] Code examples are syntactically correct for each language
- [ ] Examples match the problem (not copy-paste from two-sum)
- [ ] Variable names make sense for the problem
- [ ] Test cases produce correct expected output

### Flow Structure
- [ ] No broken navigation (all "next" step IDs exist)
- [ ] All language paths converge to common test-code
- [ ] No orphaned steps (unreachable from any path)
- [ ] Final step has no "next" field

### Completeness
- [ ] All 5 languages fully implemented
- [ ] All knowledge check explanations present
- [ ] mentorSays text is specific to this algorithm
- [ ] Example field shows actual code, not placeholders

---

## Workflow Per Algorithm

### Step 1: Research (2-3 hours)
- [ ] Solve problem in 2-3 different ways
- [ ] Find best teaching examples
- [ ] Outline key concepts
- [ ] Identify common mistakes

### Step 2: Draft Structure (1 hour)
- [ ] Map out flow graph
- [ ] Decide which approaches to teach
- [ ] Plan branching logic

### Step 3: Write Content (4-6 hours)
- [ ] Write problem illustration with concrete example
- [ ] Write approach explorations
- [ ] Write incremental coding steps for ONE language
- [ ] Test the flow mentally

### Step 4: Replicate for Other Languages (2-3 hours)
- [ ] Adapt coding steps for Python, Java, C++, TypeScript
- [ ] Adjust syntax and language-specific concepts

### Step 5: Test & Polish (1 hour)
- [ ] Walk through as a learner
- [ ] Fix confusing parts
- [ ] Verify all navigation works

**Total: 10-15 hours per algorithm**

---

## Tools & Scripts Needed

### 1. Template Detector Script
Identify which files have template content vs. real content

### 2. Progress Tracker Script
Track completion status automatically

### 3. Quality Checker Script
Verify checklist items programmatically

### 4. Content Generator Helper
Templates for common patterns (but still need custom content)

---

## Notes

- **Reference Files**: Use `two-sum.json` and `binary-search.json` as quality standards
- **No Copy-Paste**: Each algorithm needs custom problem explanation and examples
- **Incremental Building**: Code should build step-by-step, not jump from start to done
- **Multiple Approaches**: Most algorithms should teach 2-3 different approaches
- **Language Support**: All 5 languages must have complete paths

---

**Last Updated**: 2024  
**Next Review**: After Phase 1 completion

