#!/usr/bin/env python3
"""
Script to add variable and parameter checks to all fundamental block lessons.
Applies to first 10 lessons (Level 1 - Foundations).
"""

import json
import sys

# Language configurations
LANGUAGES = {
    'js': {'name': 'JavaScript', 'var_example': 'let numbers = [3, 7, 2, 9, 5];', 'func_example': 'function findMax(arr)'},
    'python': {'name': 'Python', 'var_example': 'numbers = [3, 7, 2, 9, 5]', 'func_example': 'def find_max(arr):'},
    'java': {'name': 'Java', 'var_example': 'int[] numbers = {3, 7, 2, 9, 5};', 'func_example': 'public int findMax(int[] arr)'},
    'cpp': {'name': 'C++', 'var_example': 'vector<int> numbers = {3, 7, 2, 9, 5};', 'func_example': 'int findMax(vector<int>& arr)'},
    'ts': {'name': 'TypeScript', 'var_example': 'let numbers: number[] = [3, 7, 2, 9, 5];', 'func_example': 'function findMax(arr: number[]): number'}
}

def create_variable_check(lang):
    lang_name = LANGUAGES[lang]['name']
    return {
        "stepId": f"variable-check-{lang}",
        "mentorSays": f"Before we start coding, let me ask: Do you know what a variable is in {lang_name}?",
        "choices": [
            {"label": f"Yes, I know variables", "next": f"function-check-{lang}"},
            {"label": f"No, explain variables", "next": f"variable-explanation-{lang}"}
        ]
    }

def create_variable_explanation(lang):
    lang_name = LANGUAGES[lang]['name']
    var_example = LANGUAGES[lang]['var_example']
    return {
        "stepId": f"variable-explanation-{lang}",
        "mentorSays": f"A variable is like a labeled box where you can store a value. You give it a name (like 'arr' or 'numbers') and put data inside it.\n\nFor example, '{var_example}' creates a variable that stores an array. Later, you can use that variable name to refer to the array.",
        "example": f"{var_example}\n\nNow the variable refers to the array\nWe can use the variable name to access this array",
        "action": "continue",
        "next": f"function-check-{lang}"
    }

def create_parameter_check(lang):
    lang_name = LANGUAGES[lang]['name']
    return {
        "stepId": f"parameter-check-{lang}",
        "mentorSays": "When we write a function, we can give it inputs. These inputs are called 'parameters'. Do you know what parameters are?",
        "choices": [
            {"label": "Yes, I know parameters", "next": f"loop-check-{lang}"},
            {"label": "No, explain parameters", "next": f"parameter-explanation-{lang}"}
        ]
    }

def create_parameter_explanation(lang):
    func_example = LANGUAGES[lang]['func_example']
    call_example = "findMax([3, 7, 2, 9, 5])" if lang != 'python' else "find_max([3, 7, 2, 9, 5])"
    if lang == 'java':
        call_example = "findMax(new int[]{3, 7, 2, 9, 5})"
    elif lang == 'cpp':
        call_example = "findMax({3, 7, 2, 9, 5})"
    
    return {
        "stepId": f"parameter-explanation-{lang}",
        "mentorSays": f"Parameters are like variables that receive values when you call the function. When you write '{func_example}', the 'arr' is a parameter - it's a placeholder that will receive an actual array when you call the function.\n\nWhen you call '{call_example}', the array [3, 7, 2, 9, 5] gets passed into the function and stored in the 'arr' parameter. Inside the function, you can use 'arr' to refer to that array.",
        "example": f"{func_example} {{\n  // 'arr' is a parameter\n  // It will receive an array when we call the function\n}}\n\n// When we call it:\n{call_example};\n// The array [3, 7, 2, 9, 5] goes into 'arr'\n// Inside the function, 'arr' refers to [3, 7, 2, 9, 5]",
        "action": "continue",
        "next": f"loop-check-{lang}"
    }

def fix_lesson(lesson, lesson_id):
    """Fix a single lesson by adding variable and parameter checks."""
    flow = lesson['flow']
    new_flow = []
    i = 0
    
    while i < len(flow):
        step = flow[i]
        
        # Check if this is a language-selection step that needs updating
        if step.get('stepId') == 'language-selection':
            new_flow.append(step)
            # Update choices to point to variable-check instead of function-check
            if 'choices' in step:
                for choice in step['choices']:
                    lang_map = {
                        'JavaScript': 'js',
                        'Python': 'python',
                        'Java': 'java',
                        'C++': 'cpp',
                        'TypeScript': 'ts'
                    }
                    lang_label = choice['label']
                    if lang_label in lang_map:
                        lang = lang_map[lang_label]
                        choice['next'] = f"variable-check-{lang}"
            i += 1
            continue
        
        # Check if this is a function-check step
        if step.get('stepId', '').startswith('function-check-'):
            lang = step['stepId'].replace('function-check-', '')
            
            # Insert variable-check before function-check
            new_flow.append(create_variable_check(lang))
            new_flow.append(create_variable_explanation(lang))
            
            # Update function-check to point to parameter-check
            step['choices'][0]['next'] = f"parameter-check-{lang}"
            new_flow.append(step)
            i += 1
            
            # Check if next is function-explanation
            if i < len(flow) and flow[i].get('stepId') == f'function-explanation-{lang}':
                func_expl = flow[i]
                func_expl['next'] = f"parameter-check-{lang}"
                new_flow.append(func_expl)
                i += 1
                
                # Insert parameter-check and explanation
                new_flow.append(create_parameter_check(lang))
                new_flow.append(create_parameter_explanation(lang))
            continue
        
        # Check if this is coding-complete step that needs function call
        if step.get('stepId', '').startswith('coding-complete-'):
            lang = step['stepId'].replace('coding-complete-', '')
            # Remove example output from coding-complete
            if 'example' in step:
                # Keep only the function definition, remove execution trace
                example_lines = step['example'].split('\n')
                func_lines = []
                for line in example_lines:
                    func_lines.append(line)
                    if line.strip().startswith('}') or line.strip().startswith('return'):
                        break
                step['example'] = '\n'.join(func_lines)
            
            step['next'] = f"coding-call-{lang}"
            new_flow.append(step)
            i += 1
            
            # Insert coding-call step
            if i < len(flow) and flow[i].get('stepId') == 'test-code':
                # Create coding-call step
                func_name = "findMax" if lang != 'python' else "find_max"
                call_example = f"{func_name}([3, 7, 2, 9, 5])"
                if lang == 'java':
                    call_example = f"{func_name}(new int[]{{3, 7, 2, 9, 5}})"
                elif lang == 'cpp':
                    call_example = f"{func_name}({{3, 7, 2, 9, 5}})"
                
                coding_call = {
                    "stepId": f"coding-call-{lang}",
                    "mentorSays": "Now, to use this function, we need to call it with an actual array. We pass the array as an argument (the value we give to the parameter).",
                    "example": f"// First, define the function:\n{step['example']}\n\n// Then, call it with an array:\n{call_example};\n\n// When we call {call_example}:\n// The array [3, 7, 2, 9, 5] goes into the parameter\n// The function runs and returns the result",
                    "action": "continue",
                    "next": "test-code"
                }
                new_flow.append(coding_call)
            continue
        
        # Default: just add the step
        new_flow.append(step)
        i += 1
    
    lesson['flow'] = new_flow
    return lesson

def main():
    if len(sys.argv) < 2:
        print("Usage: python fix_fundamental_blocks.py <lessons.json>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # First 10 lessons are fundamental blocks
    fundamental_lesson_ids = [
        'two-sum',
        'print-array-elements',
        'find-max-element',
        'find-min-element',
        'sum-array-elements',
        'reverse-array',
        'check-sorted-array',
        'find-index-of-element',
        'count-occurrences',
        'remove-duplicates-sorted',
        'merge-two-arrays'
    ]
    
    for lesson in data['lessons']:
        if lesson['id'] in fundamental_lesson_ids:
            print(f"Fixing lesson: {lesson['id']}")
            lesson = fix_lesson(lesson, lesson['id'])
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print("Done!")

if __name__ == '__main__':
    main()

