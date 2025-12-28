#!/usr/bin/env python3
"""
Generate comprehensive lesson JSON files from all markdown files in iprep folder.
Each challenge becomes a complete, production-ready lesson following APT LEARN format.
"""
import json
import re
from pathlib import Path
from typing import List, Dict, Optional, Tuple

# Base directories - handle both direct execution and module import
if __name__ == '__main__':
    # When run directly, __file__ is the script path
    IPREP_DIR = Path(__file__).parent
else:
    # When imported, use current working directory
    IPREP_DIR = Path('mentor/iprep')
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

def extract_code_block(content: str, marker: str) -> Optional[str]:
    """Extract code block after a marker."""
    # Find the marker
    marker_pos = content.find(marker)
    if marker_pos == -1:
        return None
    
    # Find code block after marker
    code_pattern = r'```(?:typescript|javascript|python|java|cpp)?\s*\n(.*?)\n```'
    match = re.search(code_pattern, content[marker_pos:], re.DOTALL)
    return match.group(1).strip() if match else None

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
        # Check for next tier section
        next_tier = re.search(r'## 🎯 Tier \d+', md_content[start_pos:])
        if next_tier:
            challenge_content = md_content[start_pos:start_pos + next_tier.start()]
        else:
            challenge_content = md_content[start_pos:]
    
    # Extract time
    time_match = re.search(r'\*\*Time:\*\* (.+?)\n', challenge_content)
    time_estimate = time_match.group(1).strip() if time_match else "15 minutes"
    
    # Extract tests
    tests_match = re.search(r'\*\*Tests:\*\* (.+?)\n', challenge_content)
    tests = tests_match.group(1).strip() if tests_match else "General concepts"
    
    # Extract challenge description
    challenge_desc = extract_code_block(challenge_content, '**Challenge:**')
    if not challenge_desc:
        challenge_desc = ""
    
    # Extract solution
    solution = extract_code_block(challenge_content, '**What interviewers look for:**')
    if not solution:
        solution = ""
    
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
            # Try to find if there are more challenges with different numbering
            # Some files might have challenges listed as "17-30" etc.
            break
        challenges.append(challenge)
        challenge_num += 1
    
    return challenges

def generate_angular_knowledge_checks(flow: List[Dict], challenge: Dict) -> Tuple[str, str]:
    """Generate Angular-specific knowledge checks and return next step."""
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
        "mentorSays": "Angular components are the building blocks of Angular applications. They consist of:\n- A TypeScript class with the @Component decorator\n- A template (HTML) that defines the view\n- Optional styles for component-specific CSS\n\nExample:\n```typescript\n@Component({\n  selector: 'app-example',\n  template: '<h1>Hello Angular</h1>',\n  standalone: true\n})\nexport class ExampleComponent {}\n```\n\nThe @Component decorator tells Angular that this class is a component. The selector is how you use it in templates (like `<app-example>`).",
        "example": "@Component({\n  selector: 'app-example',\n  template: '<h1>Hello Angular</h1>',\n  standalone: true\n})\nexport class ExampleComponent {}",
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
        "mentorSays": "Decorators are special functions that modify classes, methods, or properties. In Angular:\n- @Component marks a class as a component\n- @Input() marks a property to receive data from parent component\n- @Output() marks an EventEmitter to send data to parent component\n\nExample:\n```typescript\n@Component({\n  selector: 'app-user',\n  template: '<p>{{ name }}</p>',\n  standalone: true\n})\nexport class UserComponent {\n  @Input() name!: string;\n  @Output() clicked = new EventEmitter();\n}\n```",
        "example": "@Input() name!: string;\n@Output() clicked = new EventEmitter();",
        "action": "continue",
        "next": "template-check"
    })
    
    # Template check (only if challenge uses templates)
    if 'template' in challenge['challenge'].lower() or 'binding' in challenge['tests'].lower():
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
            "mentorSays": "Angular templates use special syntax for data binding:\n- {{ value }} for interpolation (displaying values)\n- [property]=\"value\" for property binding (setting element properties)\n- (event)=\"handler()\" for event binding (handling user events)\n- [(ngModel)]=\"value\" for two-way binding (requires FormsModule)\n\nExample:\n```html\n<p>{{ message }}</p>\n<img [src]=\"imageUrl\" />\n<button [disabled]=\"isDisabled\" (click)=\"handleClick()\">Click</button>\n<input [(ngModel)]=\"name\" />\n```",
            "example": "<p>{{ message }}</p>\n<img [src]=\"imageUrl\" />\n<button (click)=\"handleClick()\">Click</button>",
            "action": "continue",
            "next": "coding-start-ts"
        })
    else:
        flow.append({
            "stepId": "template-check",
            "mentorSays": "Good! Now let's start coding.",
            "action": "continue",
            "next": "coding-start-ts"
        })
    
    return "coding-start-ts"

def generate_coding_steps(flow: List[Dict], challenge: Dict, technology: str, solution: str):
    """Generate incremental coding steps."""
    # Start coding
    flow.append({
        "stepId": "coding-start-ts",
        "mentorSays": f"Perfect! Let's build the {challenge['title']} solution step by step. We'll start with the basic structure and then add the implementation.",
        "action": "continue",
        "next": "coding-imports-ts"
    })
    
    # Imports
    flow.append({
        "stepId": "coding-imports-ts",
        "mentorSays": "First, we need to import the necessary Angular modules and dependencies. Let's identify what we need based on the solution.",
        "example": "import { Component } from '@angular/core';",
        "action": "continue",
        "next": "coding-component-decorator-ts"
    })
    
    # Component decorator
    flow.append({
        "stepId": "coding-component-decorator-ts",
        "mentorSays": "Now let's create the component class with the @Component decorator. We'll set up the selector, template, and make it standalone.",
        "example": "@Component({\n  selector: 'app-example',\n  template: '...',\n  standalone: true\n})",
        "action": "continue",
        "next": "coding-class-ts"
    })
    
    # Class definition
    flow.append({
        "stepId": "coding-class-ts",
        "mentorSays": "Now let's define the component class. This is where we'll add our properties and methods.",
        "example": "export class ExampleComponent {\n  // Properties and methods go here\n}",
        "action": "continue",
        "next": "coding-properties-ts"
    })
    
    # Properties
    flow.append({
        "stepId": "coding-properties-ts",
        "mentorSays": "Let's add the properties we need. These will hold our component's data.",
        "example": "export class ExampleComponent {\n  message = 'Hello';\n  isActive = true;\n}",
        "action": "continue",
        "next": "coding-methods-ts"
    })
    
    # Methods
    flow.append({
        "stepId": "coding-methods-ts",
        "mentorSays": "Now let's add the methods that implement our logic. These methods will handle the component's behavior.",
        "example": "export class ExampleComponent {\n  handleClick() {\n    // Implementation\n  }\n}",
        "action": "continue",
        "next": "coding-complete-ts"
    })
    
    # Complete solution
    flow.append({
        "stepId": "coding-complete-ts",
        "mentorSays": "Perfect! Here's the complete solution with all the pieces together:",
        "example": solution,
        "action": "continue",
        "next": "test-code-ts"
    })

def generate_lesson_json(challenge: Dict, technology: str) -> Dict:
    """Generate complete lesson JSON for a challenge."""
    # Create kebab-case ID
    title_kebab = re.sub(r'[^\w\s-]', '', challenge['title']).strip().lower()
    title_kebab = re.sub(r'[-\s]+', '-', title_kebab)
    lesson_id = f"{technology}-{challenge['number']}-{title_kebab}"
    
    # Determine language
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
        f"Implement the solution using {challenge['tests']}",
        f"Apply Angular best practices and patterns",
        f"Handle edge cases and error scenarios",
        f"Write clean, maintainable {technology.title()} code"
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
    problem_text += f"**Challenge Description:**\n{challenge['challenge']}\n\n" if challenge['challenge'] else ""
    problem_text += f"**What we need to build:**\nThis challenge tests your understanding of {challenge['tests']}.\n\n"
    problem_text += f"**Time estimate:** {challenge['time_estimate']}\n"
    problem_text += f"**Difficulty level:** {challenge['difficulty'].title()}\n\n"
    
    if challenge['solution']:
        problem_text += f"**Expected Solution Overview:**\n```typescript\n{challenge['solution'][:300]}...\n```\n\n"
    
    problem_text += "This is a practical interview question that tests your understanding of core Angular concepts and your ability to implement them correctly."
    
    flow.append({
        "stepId": "problem-illustration",
        "mentorSays": problem_text,
        "example": challenge['challenge'] if challenge['challenge'] else "See challenge description above",
        "action": "continue",
        "next": "thinking-challenge"
    })
    
    # Thinking challenge
    flow.append({
        "stepId": "thinking-challenge",
        "mentorSays": f"Now that you understand what the problem wants, here's the real question:\n\nHow would YOU solve this {challenge['title']} challenge?\n\nThink about it for a moment. What approach feels natural to you?",
        "choices": [
            {
                "label": "I'll start with the basic approach and build up",
                "next": "explore-approach-1"
            },
            {
                "label": "I want to see the optimal solution directly",
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
        "mentorSays": "Good! Starting with a basic approach is a solid strategy. Let's build it step by step, then we'll see the complete solution.",
        "action": "continue",
        "next": "explore-optimal"
    })
    
    flow.append({
        "stepId": "explore-optimal",
        "mentorSays": f"Perfect! Here's the optimal solution approach:\n\n```typescript\n{challenge['solution']}\n```\n\nThis solution demonstrates best practices for {technology.title()} development and shows how to properly implement {challenge['tests']}.",
        "example": challenge['solution'],
        "action": "continue",
        "next": "language-selection"
    })
    
    # Language selection
    if technology == 'angular':
        flow.append({
            "stepId": "language-selection",
            "mentorSays": "Great! Now let's code this solution. Since this is an Angular challenge, we'll use TypeScript.",
            "action": "continue",
            "next": "component-check"
        })
        
        # Generate Angular-specific knowledge checks
        next_step = generate_angular_knowledge_checks(flow, challenge)
        
        # Generate coding steps
        generate_coding_steps(flow, challenge, technology, challenge['solution'])
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
        # For non-Angular, we'd need to add language-specific checks
        # For now, add a simple coding step
        flow.append({
            "stepId": "coding-start-ts",
            "mentorSays": f"Let's implement the solution:",
            "example": challenge['solution'],
            "action": "continue",
            "next": "test-code-ts"
        })
    
    # Test code
    flow.append({
        "stepId": "test-code-ts",
        "mentorSays": f"Perfect! Now test your code. Make sure it works correctly for the {challenge['title']} challenge.\n\n**Test Cases:**\n1. Test with basic input\n2. Test with edge cases\n3. Test with empty/null values\n4. Verify the output matches expected behavior\n\nTry running it and verify the solution works as expected.",
        "example": f"// Test cases for {challenge['title']}\n// 1. Basic functionality\n// 2. Edge cases\n// 3. Error handling",
        "action": "continue",
        "next": "final"
    })
    
    # Final step
    flow.append({
        "stepId": "final",
        "mentorSays": f"🎉 Well done! You've completed the {challenge['title']} challenge.\n\n**Key Takeaways:**\n- You've mastered {challenge['tests']}\n- You understand how to implement {challenge['title']} in {technology.title()}\n- You've applied best practices for {technology.title()} development\n- You can handle this type of interview question confidently\n\n**Time Complexity:** Varies based on implementation\n**Space Complexity:** Varies based on implementation\n\n**Related Challenges:**\n- Practice similar {technology.title()} concepts\n- Try variations of this challenge\n- Explore more advanced {technology.title()} patterns\n\nKeep practicing!",
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
    
    for md_file in sorted(IPREP_DIR.glob('*.md')):
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
                try:
                    lesson_json = generate_lesson_json(challenge, tech)
                    
                    # Save lesson file
                    lesson_file = tech_dir / f"{lesson_json['id']}.json"
                    with open(lesson_file, 'w', encoding='utf-8') as f:
                        json.dump(lesson_json, f, indent=2, ensure_ascii=False)
                    
                    print(f"  [OK] Generated: {lesson_file.name} ({len(lesson_json['flow'])} steps)")
                    total_lessons += 1
                except Exception as e:
                    print(f"  [ERROR] Error generating lesson {challenge['number']}: {e}")
                    import traceback
                    traceback.print_exc()
                    
        except Exception as e:
            print(f"  [ERROR] Error processing {md_file.name}: {e}")
            import traceback
            traceback.print_exc()
    
    print(f"\n{'='*60}")
    print(f"[SUCCESS] Total lessons generated: {total_lessons}")
    print(f"[INFO] Lessons saved to: {LESSON_GEN_DIR}")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()

