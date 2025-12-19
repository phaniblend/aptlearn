#!/usr/bin/env python3
"""
Script to update all lesson introductions to learning goals format.
"""

import json
import re

# Learning goals for each lesson
LESSON_GOALS = {
    "two-sum": [
        "define and use variables in your chosen language",
        "understand what arrays are and how indexing works",
        "create functions with parameters",
        "use loops to iterate through arrays",
        "solve the Two Sum problem using different approaches"
    ],
    "print-array-elements": [
        "define and use variables in your chosen language",
        "create functions with parameters",
        "loop through arrays using 'for loop' in your chosen language",
        "print or display each element of an array"
    ],
    "find-max-element": [
        "define and use variables in your chosen language",
        "create functions with parameters",
        "loop through arrays using 'for loop' in your chosen language",
        "compare values to find the maximum element in an array"
    ],
    "find-min-element": [
        "define and use variables in your chosen language",
        "create functions with parameters",
        "loop through arrays using 'for loop' in your chosen language",
        "compare values to find the minimum element in an array"
    ],
    "sum-array-elements": [
        "define and use variables in your chosen language",
        "create functions with parameters",
        "loop through arrays using 'for loop' in your chosen language",
        "accumulate values to calculate the sum of all array elements"
    ],
    "reverse-array": [
        "define and use variables in your chosen language",
        "create functions with parameters",
        "loop through arrays using 'for loop' in your chosen language",
        "swap elements to reverse an array in-place"
    ],
    "check-sorted-array": [
        "define and use variables in your chosen language",
        "create functions with parameters",
        "loop through arrays using 'for loop' in your chosen language",
        "compare adjacent elements to check if an array is sorted"
    ],
    "find-index-of-element": [
        "define and use variables in your chosen language",
        "create functions with parameters",
        "loop through arrays using 'for loop' in your chosen language",
        "search for an element and return its index position"
    ],
    "count-occurrences": [
        "define and use variables in your chosen language",
        "create functions with parameters",
        "loop through arrays using 'for loop' in your chosen language",
        "count how many times a specific value appears in an array"
    ],
    "remove-duplicates-sorted": [
        "define and use variables in your chosen language",
        "create functions with parameters",
        "loop through arrays using 'for loop' in your chosen language",
        "use two pointers to remove duplicates from a sorted array"
    ],
    "merge-two-arrays": [
        "define and use variables in your chosen language",
        "create functions with parameters",
        "loop through arrays using 'for loop' in your chosen language",
        "combine two arrays into one while maintaining order"
    ]
}

def create_learning_goals_text(lesson_id):
    """Create learning goals text for a lesson."""
    goals = LESSON_GOALS.get(lesson_id, [])
    if not goals:
        return None
    
    goals_text = "At the end of this lesson, you will be able to:\n\n"
    for i, goal in enumerate(goals, 1):
        goals_text += f"{i}. {goal.capitalize()}\n"
    
    return goals_text.strip()

def update_lesson_intro(lesson):
    """Update the introduction step of a lesson."""
    lesson_id = lesson.get('id')
    if not lesson_id:
        return lesson
    
    goals_text = create_learning_goals_text(lesson_id)
    if not goals_text:
        return lesson
    
    # Find the intro step (usually the first step or one with "Welcome" or "Today we'll learn")
    flow = lesson.get('flow', [])
    for i, step in enumerate(flow):
        step_id = step.get('stepId', '')
        mentor_says = step.get('mentorSays', '')
        
        # Check if this is an intro step
        if (step_id == 'title' or 
            'Welcome! Today we\'ll learn' in mentor_says or 
            'Welcome! Today we\'re going to learn' in mentor_says or
            (i == 0 and 'Welcome' in mentor_says)):
            
            # Update the mentorSays
            step['mentorSays'] = goals_text
            break
    
    return lesson

def main():
    file_path = 'lessons.json'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Update all lessons
    for lesson in data['lessons']:
        lesson_id = lesson.get('id')
        if lesson_id in LESSON_GOALS:
            print(f"Updating lesson: {lesson_id}")
            lesson = update_lesson_intro(lesson)
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print("Done! All lesson introductions have been updated to learning goals format.")

if __name__ == '__main__':
    main()

