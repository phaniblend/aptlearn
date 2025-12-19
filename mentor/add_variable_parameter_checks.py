#!/usr/bin/env python3
"""
Script to add variable and parameter checks to all fundamental block lessons.
This adds the checks for all remaining language paths.
"""

import json
import re

# Language configurations
LANGUAGES = {
    'js': {'name': 'JavaScript', 'var_example': 'let numbers = [3, 7, 2, 9, 5];', 'func_example': 'function findMax(arr)', 'call_example': 'findMax([3, 7, 2, 9, 5])'},
    'python': {'name': 'Python', 'var_example': 'numbers = [3, 7, 2, 9, 5]', 'func_example': 'def find_max(arr):', 'call_example': 'find_max([3, 7, 2, 9, 5])'},
    'java': {'name': 'Java', 'var_example': 'int[] numbers = {3, 7, 2, 9, 5};', 'func_example': 'public int findMax(int[] arr)', 'call_example': 'findMax(new int[]{3, 7, 2, 9, 5})'},
    'cpp': {'name': 'C++', 'var_example': 'vector<int> numbers = {3, 7, 2, 9, 5};', 'func_example': 'int findMax(vector<int>& arr)', 'call_example': 'findMax({3, 7, 2, 9, 5})'},
    'ts': {'name': 'TypeScript', 'var_example': 'let numbers: number[] = [3, 7, 2, 9, 5];', 'func_example': 'function findMax(arr: number[]): number', 'call_example': 'findMax([3, 7, 2, 9, 5])'}
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
    call_example = LANGUAGES[lang]['call_example']
    func_term = "method" if lang == 'java' else "function"
    
    return {
        "stepId": f"parameter-explanation-{lang}",
        "mentorSays": f"Parameters are like variables that receive values when you call the {func_term}. When you write '{func_example}', the 'arr' is a parameter - it's a placeholder that will receive an actual array when you call the {func_term}.\n\nWhen you call '{call_example}', the array [3, 7, 2, 9, 5] gets passed into the {func_term} and stored in the 'arr' parameter. Inside the {func_term}, you can use 'arr' to refer to that array.",
        "example": f"{func_example} {{\n  // 'arr' is a parameter\n  // It will receive an array when we call the {func_term}\n}}\n\n// When we call it:\n{call_example};\n// The array [3, 7, 2, 9, 5] goes into 'arr'\n// Inside the {func_term}, 'arr' refers to [3, 7, 2, 9, 5]",
        "action": "continue",
        "next": f"loop-check-{lang}"
    }

def fix_lesson_flow(flow, lesson_id):
    """Fix a single lesson flow by adding variable and parameter checks."""
    new_flow = []
    i = 0
    
    while i < len(flow):
        step = flow[i]
        step_id = step.get('stepId', '')
        
        # Update language-selection to point to variable-check
        if step_id == 'language-selection' and 'choices' in step:
            for choice in step['choices']:
                lang_map = {
                    'JavaScript': 'js',
                    'Python': 'python',
                    'Java': 'java',
                    'C++': 'cpp',
                    'TypeScript': 'ts'
                }
                lang_label = choice.get('label', '')
                if lang_label in lang_map:
                    lang = lang_map[lang_label]
                    choice['next'] = f"variable-check-{lang}"
            new_flow.append(step)
            i += 1
            continue
        
        # Check if this is a function-check step that needs variable-check before it
        if step_id.startswith('function-check-') and not step_id.startswith('function-check-hashmap-'):
            lang = step_id.replace('function-check-', '')
            
            # Check if variable-check already exists (skip if already added)
            has_variable_check = False
            for prev_step in new_flow:
                if prev_step.get('stepId') == f'variable-check-{lang}':
                    has_variable_check = True
                    break
            
            if not has_variable_check:
                # Insert variable-check before function-check
                new_flow.append(create_variable_check(lang))
                new_flow.append(create_variable_explanation(lang))
            
            # Update function-check to point to parameter-check
            if 'choices' in step:
                for choice in step['choices']:
                    if choice.get('label', '').startswith('Yes'):
                        choice['next'] = f"parameter-check-{lang}"
            new_flow.append(step)
            i += 1
            
            # Check if next is function-explanation
            if i < len(flow) and flow[i].get('stepId') == f'function-explanation-{lang}':
                func_expl = flow[i]
                func_expl['next'] = f"parameter-check-{lang}"
                new_flow.append(func_expl)
                i += 1
                
                # Insert parameter-check and explanation
                has_parameter_check = False
                for prev_step in new_flow:
                    if prev_step.get('stepId') == f'parameter-check-{lang}':
                        has_parameter_check = True
                        break
                
                if not has_parameter_check:
                    new_flow.append(create_parameter_check(lang))
                    new_flow.append(create_parameter_explanation(lang))
            continue
        
        # Check if this is coding-complete step that needs function call
        if step_id.startswith('coding-complete-') and not step_id.startswith('coding-complete-hashmap-'):
            lang = step_id.replace('coding-complete-', '')
            
            # Remove execution trace from example, keep only function definition
            if 'example' in step:
                example_lines = step['example'].split('\n')
                func_lines = []
                for line in example_lines:
                    func_lines.append(line)
                    # Stop at return statement or closing brace
                    if line.strip().startswith('return') or (line.strip() == '}' and len(func_lines) > 3):
                        break
                step['example'] = '\n'.join(func_lines)
            
            step['next'] = f"coding-call-{lang}"
            new_flow.append(step)
            i += 1
            
            # Insert coding-call step before test-code
            if i < len(flow) and flow[i].get('stepId') == 'test-code':
                # Extract function name from the example
                func_example = step['example']
                func_name = None
                
                # Try to extract function name from different language patterns
                if lang == 'js' or lang == 'ts':
                    match = re.search(r'function\s+(\w+)', func_example)
                    if match:
                        func_name = match.group(1)
                elif lang == 'python':
                    match = re.search(r'def\s+(\w+)', func_example)
                    if match:
                        func_name = match.group(1)
                elif lang == 'java':
                    match = re.search(r'public\s+\w+\s+(\w+)', func_example)
                    if match:
                        func_name = match.group(1)
                elif lang == 'cpp':
                    match = re.search(r'(\w+)\s*\([^)]*\)\s*\{', func_example)
                    if match:
                        func_name = match.group(1)
                
                # Fallback to default if extraction failed
                if not func_name:
                    func_name = "findMax" if lang != 'python' else "find_max"
                
                # Create call example based on language
                if lang == 'python':
                    call_example = f"{func_name}([3, 7, 2, 9, 5])"
                elif lang == 'java':
                    call_example = f"{func_name}(new int[]{{3, 7, 2, 9, 5}})"
                elif lang == 'cpp':
                    call_example = f"{func_name}({{3, 7, 2, 9, 5}})"
                else:
                    call_example = f"{func_name}([3, 7, 2, 9, 5])"
                
                # Complete the function example if it's incomplete
                if not func_example.strip().endswith('}'):
                    if lang == 'python':
                        if not func_example.strip().endswith('pass'):
                            func_example += "\n    return result"
                    else:
                        func_example += "\n  return result\n}"
                
                coding_call = {
                    "stepId": f"coding-call-{lang}",
                    "mentorSays": "Now, to use this function, we need to call it with an actual array. We pass the array as an argument (the value we give to the parameter).",
                    "example": f"// First, define the function:\n{func_example}\n\n// Then, call it with an array:\n{call_example};\n\n// When we call {call_example}:\n// The array [3, 7, 2, 9, 5] goes into the parameter\n// The function runs and returns the result",
                    "action": "continue",
                    "next": "test-code"
                }
                new_flow.append(coding_call)
            continue
        
        # Default: just add the step
        new_flow.append(step)
        i += 1
    
    return new_flow

def main():
    file_path = 'lessons.json'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # First 11 lessons are fundamental blocks
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
            lesson['flow'] = fix_lesson_flow(lesson['flow'], lesson['id'])
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print("Done! All fundamental block lessons have been updated.")

if __name__ == '__main__':
    main()

