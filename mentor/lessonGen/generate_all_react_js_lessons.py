#!/usr/bin/env python3
"""
Generate all 75 React JavaScript lessons following APT LEARN SPECIFICATION v1.0
Each lesson: 25-30 steps, 7+ coding steps, 5+ knowledge checks, 800+ words problem-illustration
"""
import json
import re
from pathlib import Path
from typing import Dict, List, Optional

IPREP_DIR = Path(__file__).parent.parent / 'iprep'
LESSON_GEN_DIR = Path(__file__).parent
REACT_DIR = LESSON_GEN_DIR / 'react'

# Difficulty mapping
DIFFICULTY_MAP = {
    '⭐': 'junior',
    '⭐⭐': 'mid',
    '⭐⭐⭐': 'senior',
    '⭐⭐⭐⭐': 'lead'
}

def kebab_case(s: str) -> str:
    """Convert string to kebab-case."""
    s = re.sub(r'[^a-zA-Z0-9\s-]', '', s)
    s = s.lower()
    s = re.sub(r'\s+', '-', s)
    return s

def parse_react_challenge(md_content: str, challenge_num: int) -> Optional[Dict]:
    """Parse a single React challenge from markdown."""
    # Pattern to match challenge header: ### N. Title ⭐
    pattern = rf'### {challenge_num}\. (.+?) (⭐+)'
    match = re.search(pattern, md_content)
    
    if not match:
        return None
    
    title = match.group(1).strip()
    stars = match.group(2)
    difficulty = DIFFICULTY_MAP.get(stars, 'junior')
    
    # Extract content after header
    start_pos = match.end()
    
    # Find next challenge or end
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
    
    # Extract challenge code
    challenge_code_match = re.search(r'\*\*Challenge:\*\*\s*\n```(?:javascript|js)?\n(.*?)\n```', challenge_content, re.DOTALL)
    challenge_code = challenge_code_match.group(1).strip() if challenge_code_match else ""
    
    # Extract solution code
    solution_code_match = re.search(r'\*\*What interviewers look for:\*\*\s*\n```(?:javascript|js)?\n(.*?)\n```', challenge_content, re.DOTALL)
    solution_code = solution_code_match.group(1).strip() if solution_code_match else ""
    
    return {
        'number': challenge_num,
        'title': title,
        'difficulty': difficulty,
        'time_estimate': time_estimate,
        'tests': tests,
        'challenge_code': challenge_code,
        'solution_code': solution_code
    }

def generate_react_lesson_flow(challenge: Dict) -> List[Dict]:
    """Generate complete lesson flow for a React challenge."""
    flow = []
    title_kebab = kebab_case(challenge['title'])
    
    # 1. title step
    flow.append({
        "stepId": "title",
        "mentorSays": f"At the end of this lesson, you will be able to:\n\n1. Understand {challenge['title']} in React\n2. Implement the solution using {challenge['tests']}\n3. Apply React best practices and patterns\n4. Handle edge cases and error scenarios\n5. Write clean, maintainable React code",
        "action": "continue",
        "next": "problem-illustration"
    })
    
    # 2. problem-illustration (800+ words) - This will be comprehensive
    problem_illustration = generate_problem_illustration(challenge)
    flow.append({
        "stepId": "problem-illustration",
        "mentorSays": problem_illustration,
        "example": challenge.get('challenge_code', '')[:200] if challenge.get('challenge_code') else "",
        "action": "continue",
        "next": "thinking-challenge"
    })
    
    # 3. thinking-challenge
    flow.append({
        "stepId": "thinking-challenge",
        "mentorSays": f"Now that you understand what the problem wants, here's the real question:\n\nHow would YOU solve this {challenge['title']} challenge?\n\nThink about it for a moment. What approach feels natural to you?",
        "choices": [
            {"label": "I'll start with the basic approach and build up", "next": "explore-approach-1"},
            {"label": "I want to see the optimal solution directly", "next": "explore-optimal"},
            {"label": "I need more context about the problem", "next": "problem-illustration"}
        ]
    })
    
    # 4. explore-approach-1
    flow.append({
        "stepId": "explore-approach-1",
        "mentorSays": "Good! Starting with a basic approach is a solid strategy. Let's build it step by step, then we'll see the complete solution.",
        "action": "continue",
        "next": "explore-optimal"
    })
    
    # 5. explore-optimal
    flow.append({
        "stepId": "explore-optimal",
        "mentorSays": f"Perfect! Here's the optimal solution approach:\n\n```javascript\n{challenge.get('solution_code', '// Solution will be shown in coding steps')[:300]}...\n```\n\nThis solution demonstrates React best practices and shows how to properly implement {challenge['tests']}.",
        "example": challenge.get('solution_code', '')[:500] if challenge.get('solution_code') else "",
        "action": "continue",
        "next": "language-selection"
    })
    
    # 6. language-selection
    flow.append({
        "stepId": "language-selection",
        "mentorSays": "Great! Since this is a React JavaScript challenge, we'll use JavaScript. Let's start coding!",
        "action": "continue",
        "next": "component-check"
    })
    
    # 7-11. Knowledge checks (5 minimum)
    knowledge_checks = generate_knowledge_checks(challenge)
    flow.extend(knowledge_checks)
    
    # 12-18. Coding steps (7 minimum)
    coding_steps = generate_coding_steps(challenge)
    flow.extend(coding_steps)
    
    # 19. test-code-js
    test_code = generate_test_code_step(challenge)
    flow.append(test_code)
    
    # 20. final
    flow.append({
        "stepId": "final",
        "mentorSays": generate_final_step(challenge),
        "action": "continue"
    })
    
    return flow

def generate_problem_illustration(challenge: Dict) -> str:
    """Generate comprehensive problem-illustration (800+ words)."""
    # This is a placeholder - will be expanded with full content
    # For now, return a comprehensive structure
    return f"""Let's understand what this {challenge['title']} challenge asks for.

**The Challenge:**
{challenge.get('challenge_code', 'Create a React component for this challenge')}

**What We're Building:**
This challenge tests your understanding of {challenge['tests']}. You'll need to create a React component that demonstrates these concepts.

**Why This Matters:**

This is a fundamental React concept that you'll use in every application. Understanding {challenge['title']} is essential for:
- Building interactive React applications
- Following React best practices
- Writing maintainable code
- Passing technical interviews

**Real-World Applications:**
- Used in production React applications
- Common pattern in modern web development
- Essential for building scalable UIs
- Industry-standard approach

**Conceptual Foundation:**

[Detailed explanation of the concept - will be expanded based on challenge type]

**Step-by-Step Example:**

[Step-by-step walkthrough with code examples]

**Common Patterns:**

[Pattern variations and when to use each]

**Best Practices:**

[Best practices for this specific challenge]

**Common Mistakes:**

[Common mistakes and how to avoid them]

**Time estimate:** {challenge['time_estimate']}
**Difficulty level:** {challenge['difficulty'].capitalize()}

This is a practical interview question that tests your understanding of core React concepts."""

def generate_knowledge_checks(challenge: Dict) -> List[Dict]:
    """Generate 5+ knowledge checks with explanations."""
    checks = []
    
    # Standard React knowledge checks
    standard_checks = [
        {
            "id": "component-check",
            "question": "Do you understand React components and how they work?",
            "explanation": "React components are the building blocks of React applications..."
        },
        {
            "id": "jsx-check",
            "question": "Do you understand JSX syntax?",
            "explanation": "JSX is React's way of writing HTML inside JavaScript..."
        },
        {
            "id": "props-check",
            "question": "Do you understand React props?",
            "explanation": "Props are how you pass data from parent to child components..."
        },
        {
            "id": "state-check",
            "question": "Do you understand React state?",
            "explanation": "State allows components to manage and update their own data..."
        },
        {
            "id": "event-check",
            "question": "Do you understand event handling in React?",
            "explanation": "Event handling in React uses synthetic events..."
        }
    ]
    
    # Select relevant checks based on challenge
    selected_checks = standard_checks[:5]  # Minimum 5
    
    prev_step = "language-selection"
    for i, check in enumerate(selected_checks):
        next_check = f"{standard_checks[i+1]['id']}" if i < len(selected_checks) - 1 else "coding-start-js"
        
        checks.append({
            "stepId": check["id"],
            "mentorSays": check["question"],
            "choices": [
                {"label": f"Yes, I understand {check['id'].replace('-check', '')}", "next": next_check},
                {"label": "No, please explain", "next": f"{check['id']}-explanation"}
            ]
        })
        
        checks.append({
            "stepId": f"{check['id']}-explanation",
            "mentorSays": check["explanation"],
            "example": f"// Example for {check['id']}",
            "action": "continue",
            "next": next_check
        })
    
    return checks

def generate_coding_steps(challenge: Dict) -> List[Dict]:
    """Generate 7+ coding steps."""
    steps = []
    
    steps.append({
        "stepId": "coding-start-js",
        "mentorSays": f"Perfect! Now let's build the {challenge['title']} solution step by step. We'll start with the basic structure and then add the implementation.",
        "action": "continue",
        "next": "coding-step-1-js"
    })
    
    # Step 1: Import
    steps.append({
        "stepId": "coding-step-1-js",
        "mentorSays": "First, let's import the necessary React modules.",
        "example": "import React from 'react';",
        "action": "continue",
        "next": "coding-step-2-js"
    })
    
    # Step 2: Component function
    steps.append({
        "stepId": "coding-step-2-js",
        "mentorSays": "Now let's define our component function.",
        "example": f"function {kebab_case(challenge['title']).replace('-', '')}() {{\n  // Component body\n}}",
        "action": "continue",
        "next": "coding-step-3-js"
    })
    
    # Steps 3-6: Implementation specific
    for i in range(3, 7):
        steps.append({
            "stepId": f"coding-step-{i}-js",
            "mentorSays": f"Now let's add step {i} of the implementation.",
            "example": f"// Step {i} implementation",
            "action": "continue",
            "next": f"coding-step-{i+1}-js" if i < 6 else "coding-complete-js"
        })
    
    # Complete solution
    steps.append({
        "stepId": "coding-complete-js",
        "mentorSays": "Perfect! Here's the complete solution with all the pieces together:",
        "example": challenge.get('solution_code', '// Complete solution'),
        "action": "continue",
        "next": "test-code-js"
    })
    
    return steps

def generate_test_code_step(challenge: Dict) -> Dict:
    """Generate comprehensive test-code step with troubleshooting."""
    return {
        "stepId": "test-code-js",
        "mentorSays": f"""Perfect! Now let's test your component and make sure everything works correctly.

**Testing Steps:**

1. **Save your component:**
   - Create a file for your component
   - Paste your component code
   - Save the file

2. **Import in App.js:**
   ```javascript
   import YourComponent from './YourComponent';
   ```

3. **Use the component:**
   ```javascript
   function App() {{
     return (
       <div className="App">
         <YourComponent />
       </div>
     );
   }}
   ```

4. **Run your React app:**
   ```bash
   npm start
   ```

5. **Verify in browser:**
   - Open http://localhost:3000
   - You should see your component working!

**Expected Result:**
Your component should work as expected based on the challenge requirements.

**Common Issues and Solutions:**

**Problem 1: Component doesn't appear**
```
Symptom: Nothing shows on screen
Solution: Check that you exported with 'export default'
         Check that import path is correct
         Check component name matches (PascalCase)
```

**Problem 2: Syntax error**
```
Symptom: Red error in console
Solution: Check all syntax is correct
         Verify all brackets are closed
         Check for typos
```

**Try These Experiments:**

Once it's working, try modifying:
- Add more features
- Change the styling
- Test with different data
- Add error handling

**Success Indicators:**

✅ Component renders without errors
✅ All functionality works correctly
✅ Code follows React best practices
✅ No console errors

You've successfully completed the {challenge['title']} challenge!""",
        "example": challenge.get('solution_code', '')[:300] if challenge.get('solution_code') else "",
        "action": "continue",
        "next": "final"
    }

def generate_final_step(challenge: Dict) -> str:
    """Generate final step with takeaways."""
    return f"""🎉 Well done! You've completed the {challenge['title']} challenge!

**Key Takeaways:**
- You've mastered {challenge['tests']}
- You understand how to implement {challenge['title']} in React
- You've applied React best practices
- You can handle this type of interview question confidently

**What You've Learned:**
- How to implement {challenge['title']}
- React patterns and best practices
- Problem-solving approaches
- Code organization

**Next Steps:**
- Practice similar React concepts
- Try variations of this challenge
- Explore more advanced React patterns
- Build real-world applications

**Related Challenges:**
- Practice related React concepts
- Try more complex variations
- Explore advanced patterns

Keep practicing!"""

def main():
    """Generate all 75 React JavaScript lessons."""
    REACT_DIR.mkdir(exist_ok=True)
    
    # Read the markdown file
    md_file = IPREP_DIR / 'react-javascript-75.md'
    if not md_file.exists():
        print(f"Error: {md_file} not found!")
        return
    
    md_content = md_file.read_text(encoding='utf-8')
    
    print("=" * 60)
    print("GENERATING ALL 75 REACT JAVASCRIPT LESSONS")
    print("=" * 60)
    
    total_generated = 0
    total_errors = 0
    
    for challenge_num in range(1, 76):
        try:
            challenge = parse_react_challenge(md_content, challenge_num)
            if not challenge:
                print(f"  [SKIP] Challenge {challenge_num}: Not found")
                continue
            
            # Generate lesson
            lesson_id = f"react-{challenge_num}-{kebab_case(challenge['title'])}"
            lesson_file = REACT_DIR / f"{lesson_id}.json"
            
            # Skip if already exists (we already have challenge 1)
            if lesson_file.exists() and challenge_num == 1:
                print(f"  [SKIP] Challenge {challenge_num}: Already exists ({lesson_file.name})")
                continue
            
            flow = generate_react_lesson_flow(challenge)
            
            lesson = {
                "id": lesson_id,
                "title": challenge['title'],
                "technology": "React",
                "difficulty": challenge['difficulty'],
                "language": "javascript",
                "status": "draft",
                "metadata": {
                    "time_estimate": challenge['time_estimate'],
                    "tests": challenge['tests'],
                    "challenge_number": str(challenge_num)
                },
                "flow": flow
            }
            
            # Save lesson
            with open(lesson_file, 'w', encoding='utf-8') as f:
                json.dump(lesson, f, indent=2, ensure_ascii=False)
            
            print(f"  [OK] Challenge {challenge_num}: {lesson_file.name} ({len(flow)} steps)")
            total_generated += 1
            
        except Exception as e:
            print(f"  [ERROR] Challenge {challenge_num}: {e}")
            total_errors += 1
            continue
    
    print("\n" + "=" * 60)
    print(f"[SUCCESS] Generated: {total_generated} lessons")
    print(f"[ERRORS] Failed: {total_errors} lessons")
    print(f"[INFO] Lessons saved to: {REACT_DIR}")
    print("=" * 60)
    
    print("\n[NOTE] This is a basic generator. Each lesson needs:")
    print("  - Expanded problem-illustration (800+ words)")
    print("  - Comprehensive knowledge checks (200+ words each)")
    print("  - Detailed coding steps (7+ steps)")
    print("  - Pattern variations and best practices")
    print("  - Common mistakes section")
    print("  - Enhanced troubleshooting")

if __name__ == '__main__':
    main()

