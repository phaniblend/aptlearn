#!/usr/bin/env python3
"""Validate the fixed lessons"""
import json
from pathlib import Path

def validate_lesson(file_path):
    """Validate and analyze a lesson file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        lesson = json.load(f)
    
    flow = lesson['flow']
    total_steps = len(flow)
    
    # Count coding steps
    coding_steps = [s for s in flow if s['stepId'].startswith('coding-')]
    coding_count = len(coding_steps)
    
    # Count knowledge checks
    check_steps = [s for s in flow if 'check' in s['stepId'] or 'explanation' in s['stepId']]
    check_count = len([s for s in check_steps if 'check' in s['stepId']])
    
    # Get problem-illustration word count
    prob_illus = next((s for s in flow if s['stepId'] == 'problem-illustration'), None)
    prob_words = len(prob_illus['mentorSays'].split()) if prob_illus else 0
    
    # Count total lines (approximate)
    total_lines = sum(len(s.get('mentorSays', '').split('\n')) for s in flow)
    
    print(f"\n{file_path.name}:")
    print(f"  Total Steps: {total_steps}")
    print(f"  Coding Steps: {coding_count}")
    print(f"  Knowledge Checks: {check_count}")
    print(f"  Problem Illustration: ~{prob_words} words")
    print(f"  Total Lines (approx): ~{total_lines}")
    
    # Calculate scores
    steps_score = min(100, (total_steps / 25) * 100)
    checks_score = min(100, (check_count / 5) * 100)
    coding_score = min(100, (coding_count / 7) * 100)
    final_score = (steps_score * 0.4) + (checks_score * 0.3) + (coding_score * 0.3)
    
    print(f"\n  Scores:")
    print(f"    Steps: {steps_score:.1f}/100")
    print(f"    Checks: {checks_score:.1f}/100")
    print(f"    Coding: {coding_score:.1f}/100")
    print(f"    Final: {final_score:.1f}/100")
    
    return {
        'steps': total_steps,
        'coding': coding_count,
        'checks': check_count,
        'prob_words': prob_words,
        'score': final_score
    }

if __name__ == '__main__':
    base_dir = Path(__file__).parent
    
    react_file = base_dir / 'react' / 'react-1-hello-world-component-review.json'
    angular_file = base_dir / 'angular' / 'angular-8-component-input-review.json'
    
    print("=" * 60)
    print("LESSON VALIDATION REPORT")
    print("=" * 60)
    
    validate_lesson(react_file)
    validate_lesson(angular_file)
    
    print("\n" + "=" * 60)
    print("VALIDATION COMPLETE")
    print("=" * 60)

