#!/usr/bin/env python3
"""
Generate complete lesson JSON files from all markdown files in iprep folder.
Each challenge becomes a separate lesson file.
"""
import json
import re
from pathlib import Path
from typing import List, Dict, Optional

# Base directories
IPREP_DIR = Path(__file__).parent
LESSON_GEN_DIR = IPREP_DIR.parent / 'lessonGen'

# Technology mapping
TECH_MAP = {
    'angular.md': 'angular',
    'nextjs.md': 'nextjs',
    'nodejs-express.md': 'nodejs',
    'python.md': 'python',
    'react-javascript.md': 'react',
    'react-typescript.md': 'react',
    'vuejs-3.md': 'vue'
}

# Difficulty mapping
DIFFICULTY_MAP = {
    '⭐': 'junior',
    '⭐⭐': 'mid',
    '⭐⭐⭐': 'senior',
    '⭐⭐⭐⭐': 'lead'
}

def parse_challenge(md_content: str, challenge_num: int) -> Optional[Dict]:
    """Parse a single challenge from markdown content."""
    # Pattern to match challenge header
    pattern = rf'### {challenge_num}\. (.+?) (⭐+)'
    match = re.search(pattern, md_content)
    
    if not match:
        return None
    
    title = match.group(1).strip()
    stars = match.group(2)
    difficulty = DIFFICULTY_MAP.get(stars, 'junior')
    
    # Extract content after the header
    start_pos = match.end()
    
    # Find next challenge or end of section
    next_challenge = re.search(rf'### {challenge_num + 1}\.', md_content[start_pos:])
    if next_challenge:
        challenge_content = md_content[start_pos:start_pos + next_challenge.start()]
    else:
        challenge_content = md_content[start_pos:]
    
    # Extract time
    time_match = re.search(r'\*\*Time:\*\* (.+?)\n', challenge_content)
    time_estimate = time_match.group(1).strip() if time_match else "15 minutes"
    
    # Extract tests
    tests_match = re.search(r'\*\*Tests:\*\* (.+?)\n', challenge_content)
    tests = tests_match.group(1).strip() if tests_match else "General concepts"
    
    # Extract challenge description
    challenge_match = re.search(r'\*\*Challenge:\*\*\s*```(?:typescript|javascript|python|java|cpp)?\s*\n(.*?)\n```', challenge_content, re.DOTALL)
    challenge_desc = challenge_match.group(1).strip() if challenge_match else ""
    
    # Extract solution
    solution_match = re.search(r'\*\*What interviewers look for:\*\*\s*```(?:typescript|javascript|python|java|cpp)?\s*\n(.*?)\n```', challenge_content, re.DOTALL)
    solution = solution_match.group(1).strip() if solution_match else ""
    
    return {
        'number': challenge_num,
        'title': title,
        'difficulty': difficulty,
        'time_estimate': time_estimate,
        'tests': tests,
        'challenge': challenge_desc,
        'solution': solution
    }

def parse_markdown_file(file_path: Path) -> List[Dict]:
    """Parse all challenges from a markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    challenges = []
    challenge_num = 1
    
    while True:
        challenge = parse_challenge(content, challenge_num)
        if not challenge:
            break
        challenges.append(challenge)
        challenge_num += 1
    
    return challenges

def generate_lesson_json(challenge: Dict, technology: str) -> Dict:
    """Generate complete lesson JSON for a challenge."""
    # Create kebab-case ID
    title_kebab = re.sub(r'[^\w\s-]', '', challenge['title']).strip().lower()
    title_kebab = re.sub(r'[-\s]+', '-', title_kebab)
    lesson_id = f"{technology}-{challenge['number']}-{title_kebab}"
    
    # Determine language based on technology
    lang_map = {
        'angular': 'typescript',
        'nextjs': 'typescript',
        'nodejs': 'javascript',
        'python': 'python',
        'react': 'javascript',
        'vue': 'javascript'
    }
    default_lang = lang_map.get(technology, 'javascript')
    
    # Generate learning objectives
    objectives = [
        f"Understand {challenge['title']} in {technology.title()}",
        f"Implement the solution step by step",
        f"Master the concepts tested: {challenge['tests']}",
        f"Apply best practices for {technology.title()} development",
        f"Handle edge cases and error scenarios"
    ]
    
    # Build flow
    flow = []
    
    # Title step
    flow.append({
        "stepId": "title",
        "mentorSays": f"At the end of this lesson, you will be able to:\n\n" + "\n".join(f"{i+1}. {obj}" for i, obj in enumerate(objectives)),
        "action": "continue",
        "next": "problem-illustration"
    })
    
    # Problem illustration
    problem_text = f"Let's understand what this {challenge['title']} challenge asks for.\n\n"
    problem_text += f"**Challenge:**\n{challenge['challenge']}\n\n"
    problem_text += f"**What we need to build:**\n{challenge['solution'][:200]}...\n\n"
    problem_text += f"**Time estimate:** {challenge['time_estimate']}\n"
    problem_text += f"**Concepts tested:** {challenge['tests']}\n\n"
    problem_text += "This is a practical interview question that tests your understanding of core Angular concepts."
    
    flow.append({
        "stepId": "problem-illustration",
        "mentorSays": problem_text,
        "example": challenge['challenge'],
        "action": "continue",
        "next": "thinking-challenge"
    })
    
    # Thinking challenge
    flow.append({
        "stepId": "thinking-challenge",
        "mentorSays": f"Now that you understand what the problem wants, here's the real question:\n\nHow would YOU solve this {challenge['title']} challenge?\n\nThink about it for a moment. What approach feels natural to you?",
        "choices": [
            {
                "label": "I'll start with the basic approach",
                "next": "explore-approach-1"
            },
            {
                "label": "I want to see the optimal solution",
                "next": "explore-optimal"
            },
            {
                "label": "I need more context about the problem",
                "next": "problem-illustration"
            }
        ]
    })
    
    # Approach exploration
    flow.append({
        "stepId": "explore-approach-1",
        "mentorSays": "Good! Starting with a basic approach is a solid strategy. Let's build it step by step, then we'll optimize if needed.",
        "action": "continue",
        "next": "explore-optimal"
    })
    
    flow.append({
        "stepId": "explore-optimal",
        "mentorSays": f"Perfect! Here's the optimal solution approach:\n\n```{default_lang}\n{challenge['solution']}\n```\n\nThis solution demonstrates best practices for {technology.title()} development.",
        "example": challenge['solution'],
        "action": "continue",
        "next": "language-selection"
    })
    
    # Language selection (for Angular, we'll focus on TypeScript)
    if technology == 'angular':
        flow.append({
            "stepId": "language-selection",
            "mentorSays": "Great! Now let's code this solution. Since this is an Angular challenge, we'll use TypeScript.",
            "action": "continue",
            "next": "component-check"
        })
    else:
        flow.append({
            "stepId": "language-selection",
            "mentorSays": f"Great! Now let's code this solution. Which programming language would you like to use?",
            "choices": [
                {"label": "JavaScript", "next": f"variable-check-js"},
                {"label": "TypeScript", "next": f"variable-check-ts"},
                {"label": "Python", "next": f"variable-check-python"}
            ]
        })
    
    # Angular-specific knowledge checks
    if technology == 'angular':
        # Component check
        flow.append({
            "stepId": "component-check",
            "mentorSays": "Before we start coding, let me check: Do you know what Angular components are and how to use the @Component decorator?",
            "choices": [
                {"label": "Yes, I know components", "next": "decorator-check"},
                {"label": "No, please explain", "next": "component-explanation"}
            ]
        })
        
        flow.append({
            "stepId": "component-explanation",
            "mentorSays": "Angular components are the building blocks of Angular applications. They consist of:\n- A TypeScript class with the @Component decorator\n- A template (HTML)\n- Optional styles\n\nExample:\n```typescript\n@Component({\n  selector: 'app-example',\n  template: '<h1>Hello</h1>',\n  standalone: true\n})\nexport class ExampleComponent {}\n```",
            "example": "@Component({\n  selector: 'app-example',\n  template: '<h1>Hello</h1>',\n  standalone: true\n})\nexport class ExampleComponent {}",
            "action": "continue",
            "next": "decorator-check"
        })
        
        # Decorator check
        flow.append({
            "stepId": "decorator-check",
            "mentorSays": "Do you understand TypeScript decorators like @Component, @Input, @Output?",
            "choices": [
                {"label": "Yes, I know decorators", "next": "template-check"},
                {"label": "No, please explain", "next": "decorator-explanation"}
            ]
        })
        
        flow.append({
            "stepId": "decorator-explanation",
            "mentorSays": "Decorators are special functions that modify classes, methods, or properties. In Angular:\n- @Component marks a class as a component\n- @Input() marks a property to receive data from parent\n- @Output() marks an EventEmitter to send data to parent\n\nExample:\n```typescript\n@Input() name!: string;\n@Output() clicked = new EventEmitter();\n```",
            "example": "@Input() name!: string;\n@Output() clicked = new EventEmitter();",
            "action": "continue",
            "next": "template-check"
        })
        
        # Template check
        flow.append({
            "stepId": "template-check",
            "mentorSays": "Do you understand Angular templates and data binding (interpolation, property binding, event binding)?",
            "choices": [
                {"label": "Yes, I know templates", "next": "coding-start-ts"},
                {"label": "No, please explain", "next": "template-explanation"}
            ]
        })
        
        flow.append({
            "stepId": "template-explanation",
            "mentorSays": "Angular templates use special syntax:\n- {{ value }} for interpolation\n- [property]=\"value\" for property binding\n- (event)=\"handler()\" for event binding\n- [(ngModel)]=\"value\" for two-way binding\n\nExample:\n```html\n<p>{{ message }}</p>\n<button [disabled]=\"isDisabled\" (click)=\"handleClick()\">Click</button>\n```",
            "example": "<p>{{ message }}</p>\n<button [disabled]=\"isDisabled\" (click)=\"handleClick()\">Click</button>",
            "action": "continue",
            "next": "coding-start-ts"
        })
    
    # Coding steps
    flow.append({
        "stepId": "coding-start-ts",
        "mentorSays": f"Perfect! Let's build the {challenge['title']} solution step by step.",
        "action": "continue",
        "next": "coding-imports-ts"
    })
    
    flow.append({
        "stepId": "coding-imports-ts",
        "mentorSays": "First, we need to import the necessary Angular modules and dependencies.",
        "example": "import { Component } from '@angular/core';",
        "action": "continue",
        "next": "coding-component-ts"
    })
    
    flow.append({
        "stepId": "coding-component-ts",
        "mentorSays": "Now let's create the component class with the @Component decorator.",
        "example": "@Component({\n  selector: 'app-example',\n  template: '...',\n  standalone: true\n})\nexport class ExampleComponent {}",
        "action": "continue",
        "next": "coding-implementation-ts"
    })
    
    flow.append({
        "stepId": "coding-implementation-ts",
        "mentorSays": "Now let's implement the core logic. Here's the complete solution:",
        "example": challenge['solution'],
        "action": "continue",
        "next": "test-code-ts"
    })
    
    # Test code
    flow.append({
        "stepId": "test-code-ts",
        "mentorSays": f"Perfect! Now test your code. Make sure it works correctly for the {challenge['title']} challenge.\n\nTry running it and verify the output matches the expected behavior.",
        "example": f"// Test cases for {challenge['title']}\n// Verify the solution works correctly",
        "action": "continue",
        "next": "final"
    })
    
    # Final step
    flow.append({
        "stepId": "final",
        "mentorSays": f"🎉 Well done! You've completed the {challenge['title']} challenge.\n\n**Key Takeaways:**\n- You've mastered {challenge['tests']}\n- You understand how to implement {challenge['title']} in {technology.title()}\n- You've applied best practices for {technology.title()} development\n\n**Time Complexity:** Varies based on implementation\n**Space Complexity:** Varies based on implementation\n\n**Related Challenges:**\n- Practice similar {technology.title()} concepts\n- Try variations of this challenge\n\nKeep practicing!",
        "action": "continue"
    })
    
    return {
        "id": lesson_id,
        "title": challenge['title'],
        "technology": technology.title(),
        "difficulty": challenge['difficulty'],
        "language": default_lang,
        "status": "draft",
        "metadata": {
            "time_estimate": challenge['time_estimate'],
            "tests": challenge['tests'],
            "challenge_number": str(challenge['number'])
        },
        "flow": flow
    }

def main():
    """Main function to process all markdown files."""
    # Create lessonGen directory structure
    LESSON_GEN_DIR.mkdir(exist_ok=True)
    
    # Process each markdown file
    total_lessons = 0
    
    for md_file in IPREP_DIR.glob('*.md'):
        if md_file.name == 'CHATGPT_PROMPT_FOR_LESSONS.md':
            continue
        
        tech = TECH_MAP.get(md_file.name, md_file.stem)
        tech_dir = LESSON_GEN_DIR / tech
        tech_dir.mkdir(exist_ok=True)
        
        print(f"\n{'='*60}")
        print(f"Processing: {md_file.name}")
        print(f"Technology: {tech}")
        print(f"{'='*60}")
        
        try:
            challenges = parse_markdown_file(md_file)
            print(f"Found {len(challenges)} challenges")
            
            for challenge in challenges:
                lesson_json = generate_lesson_json(challenge, tech)
                
                # Save lesson file
                lesson_file = tech_dir / f"{lesson_json['id']}.json"
                with open(lesson_file, 'w', encoding='utf-8') as f:
                    json.dump(lesson_json, f, indent=2, ensure_ascii=False)
                
                print(f"  ✓ Generated: {lesson_file.name}")
                total_lessons += 1
                
        except Exception as e:
            print(f"  ✗ Error processing {md_file.name}: {e}")
            import traceback
            traceback.print_exc()
    
    print(f"\n{'='*60}")
    print(f"✅ Total lessons generated: {total_lessons}")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()

