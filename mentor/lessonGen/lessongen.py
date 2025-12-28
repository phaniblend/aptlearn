#!/usr/bin/env python3
"""
APT LEARN Lesson Generator
Generates coding test lessons following the APT LEARN methodology
"""

import os
import sys
import json
import re
from typing import List, Dict, Any
from openai import OpenAI

# Configuration
SUPPORTED_LANGUAGES = ["javascript", "python", "java", "cpp", "typescript"]
API_KEY = os.getenv("OPENAI_API_KEY", "")


def parse_markdown_challenges(md_file: str) -> List[Dict[str, Any]]:
    """Parse challenges from markdown file"""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    challenges = []
    
    # Match challenge sections with ### headers
    pattern = r'###\s+(\d+)\.\s+(.+?)\s+(⭐+)\s*\n\*\*Time:\*\*\s*(\d+)\s*minutes?\s*\n\*\*Tests:\*\*\s*(.+?)\n\n\*\*Challenge:\*\*\s*```(?:typescript|javascript)?\s*\n(.*?)```\s*\n\*\*What interviewers look for:\*\*\s*```(?:typescript|javascript)?\s*\n(.*?)```'
    
    matches = re.finditer(pattern, content, re.DOTALL)
    
    for match in matches:
        number = match.group(1)
        title = match.group(2).strip()
        difficulty_stars = match.group(3)
        time = match.group(4)
        tests = match.group(5).strip()
        challenge = match.group(6).strip()
        solution = match.group(7).strip()
        
        # Determine difficulty
        difficulty = "junior" if len(difficulty_stars) == 1 else \
                    "mid" if len(difficulty_stars) == 2 else \
                    "senior" if len(difficulty_stars) == 3 else "lead"
        
        challenges.append({
            "id": f"angular-{number}-{title.lower().replace(' ', '-')}",
            "number": number,
            "title": title,
            "difficulty": difficulty,
            "time": time,
            "tests": tests,
            "challenge": challenge,
            "solution": solution,
            "technology": "Angular"
        })
    
    return challenges


def create_lesson_prompt(challenge: Dict[str, Any]) -> str:
    """Create prompt for AI to generate lesson content"""
    
    prompt = f"""You are an expert coding instructor creating lessons for APT LEARN, a platform that teaches coding interview problems.

**Your Task:**
Generate lesson content for this Angular coding challenge following the APT LEARN methodology.

**Challenge Details:**
- Title: {challenge['title']}
- Difficulty: {challenge['difficulty']}
- Time: {challenge['time']} minutes
- Tests: {challenge['tests']}
- Technology: Angular (TypeScript/JavaScript framework)

**Challenge Description:**
{challenge['challenge']}

**Expected Solution:**
{challenge['solution']}

**APT LEARN Core Rules:**
1. One lesson = one coding test
2. Assume NOTHING about learner knowledge
3. Check every concept before using it
4. Explain incrementally when learner says "No"
5. Never re-check or re-explain known concepts

**Required Lesson Steps (in order):**

1. **title** - Learning objectives (what they'll be able to do)

2. **problem-illustration** - Detailed problem explanation with:
   - Problem definition
   - Key observations
   - 2-3 examples with step-by-step traces
   - What makes this tricky
   - Common pitfalls

3. **thinking-challenge** - Ask how they'd solve it, provide 2-3 approach options

4. **explore-approach-N** - For each non-optimal approach, explain why it works but why there's a better way

5. **explore-optimal** - Explain the best approach with algorithm, why it works, and key insights

6. **language-selection** - Ask which language (JavaScript, TypeScript, Python, Java, C++)

7. **Knowledge checks for EACH language** (only for selected language):
   - variable-check-{{lang}}
   - function-check-{{lang}}
   - Technology-specific checks (for Angular: component-check, decorator-check, template-check, etc.)
   - Problem-specific concept checks (only what THIS problem needs)

8. **Knowledge explanations** (for each check that gets "No"):
   - variable-explanation-{{lang}}
   - function-explanation-{{lang}}
   - Technology explanations
   - Concept explanations
   
9. **Coding steps** - Incremental implementation (one concept per step):
   - coding-start-{{lang}}
   - coding-step-1-{{lang}} (e.g., "Create component class")
   - coding-step-2-{{lang}} (e.g., "Add decorator")
   - coding-step-3-{{lang}} (e.g., "Add template")
   - ... continue until solution complete

10. **test-code-{{lang}}** - Provide test cases

11. **final** - Congratulations, complexity analysis, key takeaways, related problems

**Step Format Requirements:**

Each step must be a JSON object with:
- stepId: unique identifier (e.g., "variable-check-js")
- mentorSays: the instruction/explanation text
- action: "continue" or omit for choice steps
- next: next stepId (for linear flow)
- choices: array of {{{{label, next}}}} (for branching)
- example: code example (optional)

**Knowledge Check Format:**
{{{{
  "stepId": "concept-check-{{lang}}",
  "mentorSays": "Before we start, do you know what [CONCEPT] is in [LANGUAGE]?",
  "choices": [
    {{{{"label": "Yes, I know [CONCEPT]", "next": "next-check-or-coding"}}}},
    {{{{"label": "No, please explain", "next": "concept-explanation-{{lang}}"}}}}
  ]
}}}}

**Explanation Format:**
{{{{
  "stepId": "concept-explanation-{{lang}}",
  "mentorSays": "Brief, scoped explanation of JUST what's needed for this task. Not a full tutorial.",
  "example": "code example showing the concept",
  "action": "continue",
  "next": "return-to-main-flow"
}}}}

**Important Angular Concepts to Check:**
- Components (@Component decorator)
- Templates (HTML templates)
- Data binding (interpolation, property, event, two-way)
- Directives (*ngIf, *ngFor, etc.)
- Services (@Injectable)
- Dependency Injection (inject function or constructor)
- Modules/Standalone (imports array)
- TypeScript basics (classes, types, interfaces)
- Reactive Forms (if applicable)
- RxJS Observables (if applicable)

Only check concepts THIS specific problem needs!

**Output Format:**
Return ONLY a JSON array of step objects. No explanations, no markdown, just the JSON array.

Example structure:
[
  {{{{
    "stepId": "title",
    "mentorSays": "At the end of this lesson...",
    "action": "continue",
    "next": "problem-illustration"
  }}}},
  {{{{
    "stepId": "problem-illustration",
    "mentorSays": "Let's understand what...",
    "example": "code example",
    "action": "continue",
    "next": "thinking-challenge"
  }}}},
  ...
]

Generate the complete lesson flow now."""

    return prompt


def generate_lesson_with_ai(challenge: Dict[str, Any], api_key: str) -> Dict[str, Any]:
    """Generate lesson using OpenAI API"""
    
    client = OpenAI(api_key=api_key)
    prompt = create_lesson_prompt(challenge)
    
    print(f"  Generating lesson content with AI...")
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{
                "role": "user",
                "content": prompt
            }],
            max_tokens=16000,
            temperature=0.7
        )
        
        # Extract JSON from response
        content = response.choices[0].message.content
        
        # Try to find JSON array in the response
        # Look for content between first [ and last ]
        start_idx = content.find('[')
        end_idx = content.rfind(']')
        
        if start_idx == -1 or end_idx == -1:
            raise ValueError("No JSON array found in response")
        
        json_str = content[start_idx:end_idx + 1]
        flow = json.loads(json_str)
        
        # Create complete lesson structure
        lesson = {
            "id": challenge['id'],
            "title": challenge['title'],
            "technology": challenge['technology'],
            "difficulty": challenge['difficulty'],
            "language": "typescript",  # Default for Angular
            "status": "draft",
            "metadata": {
                "time_estimate": f"{challenge['time']} minutes",
                "tests": challenge['tests'],
                "challenge_number": challenge['number']
            },
            "flow": flow
        }
        
        return lesson
        
    except Exception as e:
        print(f"    Error generating lesson: {e}")
        raise


def save_lesson(lesson: Dict[str, Any], output_dir: str):
    """Save lesson to JSON file"""
    
    os.makedirs(output_dir, exist_ok=True)
    
    filename = f"{lesson['id']}.json"
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(lesson, f, indent=2, ensure_ascii=False)
    
    print(f"  ✓ Saved to {filepath}")


def main():
    """Main execution function"""
    
    if len(sys.argv) < 2:
        print("Usage: python lessongen.py <challenges.md> [api_key]")
        print("\nExample:")
        print("  python lessongen.py angular.md")
        print("  python lessongen.py angular.md sk-xxxxx")
        print("\nAPI key can also be set via OPENAI_API_KEY environment variable")
        sys.exit(1)
    
    md_file = sys.argv[1]
    
    # Get API key
    api_key = API_KEY
    if len(sys.argv) > 2:
        api_key = sys.argv[2]
    elif not api_key or api_key == "YOUR_OPENAI_API_KEY_HERE":
        api_key = os.environ.get('OPENAI_API_KEY')
    
    if not api_key or api_key == "YOUR_OPENAI_API_KEY_HERE":
        print("\n❌ Error: No API key provided!")
        print("\nProvide API key either:")
        print("  1. As command line argument: python lessongen.py angular.md sk-xxxxx")
        print("  2. As environment variable: export OPENAI_API_KEY=sk-xxxxx")
        sys.exit(1)
    
    # Validate input file
    if not os.path.exists(md_file):
        print(f"❌ Error: File not found: {md_file}")
        sys.exit(1)
    
    # Extract technology name from filename (e.g., "angular.md" -> "angular")
    tech_name = os.path.splitext(os.path.basename(md_file))[0]
    output_dir = tech_name
    
    print(f"\n🚀 APT LEARN Lesson Generator")
    print(f"=" * 50)
    print(f"Input file: {md_file}")
    print(f"Output directory: {output_dir}/")
    print(f"Technology: {tech_name}")
    print()
    
    # Parse challenges
    print("📖 Parsing challenges from markdown...")
    challenges = parse_markdown_challenges(md_file)
    print(f"   Found {len(challenges)} challenges")
    print()
    
    if not challenges:
        print("❌ No challenges found in markdown file!")
        print("   Make sure the file follows the expected format.")
        sys.exit(1)
    
    # Generate lessons
    print("🎓 Generating lessons...")
    print()
    
    for i, challenge in enumerate(challenges, 1):
        print(f"[{i}/{len(challenges)}] {challenge['title']}")
        
        try:
            lesson = generate_lesson_with_ai(challenge, api_key)
            save_lesson(lesson, output_dir)
            print()
            
        except Exception as e:
            print(f"  ❌ Failed: {e}")
            print(f"  Skipping to next challenge...")
            print()
            continue
    
    print("=" * 50)
    print(f"✅ Lesson generation complete!")
    print(f"   Generated lessons are in: {output_dir}/")
    print()


if __name__ == "__main__":
    main()