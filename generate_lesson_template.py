"""
Helper script to generate lesson templates for the remaining 4 lessons.
This creates the base structure that can be customized per algorithm.
"""
import json

def create_language_paths(base_id, lang_suffixes=['js', 'python', 'java', 'cpp', 'ts']):
    """Generate knowledge checks and coding steps for all languages"""
    paths = []
    
    for lang in lang_suffixes:
        lang_name = {'js': 'JavaScript', 'python': 'Python', 'java': 'Java', 'cpp': 'C++', 'ts': 'TypeScript'}[lang]
        
        # Knowledge checks
        checks = ['variable', 'function', 'parameter', 'array', 'loop']
        if 'linked' in base_id:
            checks = ['variable', 'function', 'parameter', 'linked-list', 'loop']
        
        prev_step = f"variable-check-{lang}"
        
        for i, check in enumerate(checks):
            if check == 'array' and 'linked' in base_id:
                continue  # Skip array check for linked list
            
            check_id = f"{check}-check-{lang}"
            explanation_id = f"{check}-explanation-{lang}"
            
            if i == 0:
                # First check comes from language selection
                pass
            else:
                # Add check step
                paths.append({
                    "stepId": check_id,
                    "mentorSays": f"Before we start coding, let me ask: Do you know what a {check} is in {lang_name}?",
                    "choices": [
                        {"label": f"Yes, I know {check}s", "next": f"{checks[i+1] if i+1 < len(checks) else 'coding-start-' + lang}-check-{lang}" if i+1 < len(checks) else f"coding-start-{lang}"},
                        {"label": f"No, explain {check}s", "next": explanation_id}
                    ]
                })
                
                # Add explanation step
                paths.append({
                    "stepId": explanation_id,
                    "mentorSays": f"[Explanation for {check} in {lang_name}]",
                    "example": f"[Example for {check}]",
                    "action": "continue",
                    "next": f"{checks[i+1] if i+1 < len(checks) else 'coding-start-' + lang}-check-{lang}" if i+1 < len(checks) else f"coding-start-{lang}"
                })
    
    return paths

# This is a template generator - actual lessons need to be customized
print("Template generator created. Use this to help generate lesson structures.")


