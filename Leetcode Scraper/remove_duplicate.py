import json
from collections import Counter

# Step 1: Load the list of question titles
with open('questions.json', 'r') as file:
    questions = json.load(file)

# Step 2: Count all occurrences
counts = Counter(questions)

# Step 3: Build list of unique questions (preserving order)
seen = set()
unique_questions = []
for q in questions:
    if q not in seen:
        unique_questions.append(q)
        seen.add(q)

# Step 4: Save the unique questions
with open('unique_questions.json', 'w') as f:
    json.dump(unique_questions, f, indent=2)

# Step 5: Save the duplicate counts (only those > 1)
duplicates = {q: c for q, c in counts.items() if c > 1}
with open('duplicate_counts.json', 'w') as f:
    json.dump(duplicates, f, indent=2)

print("✅ Finished:")
print(f"  Total original: {len(questions)}")
print(f"  Unique questions: {len(unique_questions)}")
print(f"  Duplicates found: {len(duplicates)} (see 'duplicate_counts.json')")
