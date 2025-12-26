import json
import os

# Read algorithm list
with open('mentor/algorithm-list.json', 'r', encoding='utf-8') as f:
    algo_list = json.load(f)

# Get existing lesson files
existing_lessons = set()
lessons_dir = 'mentor/lessons'
if os.path.exists(lessons_dir):
    for filename in os.listdir(lessons_dir):
        if filename.endswith('.json') and 'iprep' not in filename:
            lesson_id = filename.replace('.json', '')
            existing_lessons.add(lesson_id)

# Collect all algorithms from the list
all_algorithms = []
for category, algorithms in algo_list.items():
    for algo in algorithms:
        all_algorithms.append({
            'id': algo['id'],
            'title': algo['title'],
            'difficulty': algo['difficulty'],
            'pattern': algo['pattern'],
            'category': category
        })

# Find missing lessons
missing_lessons = []
for algo in all_algorithms:
    if algo['id'] not in existing_lessons:
        missing_lessons.append(algo)

# Sort by category and difficulty
missing_lessons.sort(key=lambda x: (x['category'], x['difficulty'], x['title']))

# Print results
print(f"Total algorithms in list: {len(all_algorithms)}")
print(f"Existing lessons: {len(existing_lessons)}")
print(f"Missing lessons: {len(missing_lessons)}")
print("\n" + "="*80)
print("MISSING LESSONS TO BE CREATED:")
print("="*80)

# Group by category
current_category = None
for lesson in missing_lessons:
    if lesson['category'] != current_category:
        current_category = lesson['category']
        print(f"\n[{current_category.upper().replace('-', ' ')}]")
    print(f"  - {lesson['id']:40} | {lesson['title']:50} | {lesson['difficulty']:6} | {lesson['pattern']}")

# Save to file
with open('missing_lessons_list.txt', 'w', encoding='utf-8') as f:
    f.write(f"Total algorithms: {len(all_algorithms)}\n")
    f.write(f"Existing lessons: {len(existing_lessons)}\n")
    f.write(f"Missing lessons: {len(missing_lessons)}\n\n")
    f.write("="*80 + "\n")
    f.write("MISSING LESSONS TO BE CREATED:\n")
    f.write("="*80 + "\n\n")
    
    current_category = None
    for lesson in missing_lessons:
        if lesson['category'] != current_category:
            current_category = lesson['category']
            f.write(f"\n[{current_category.upper().replace('-', ' ')}]\n")
        f.write(f"  - {lesson['id']:40} | {lesson['title']:50} | {lesson['difficulty']:6} | {lesson['pattern']}\n")

print(f"\n\nList saved to: missing_lessons_list.txt")


