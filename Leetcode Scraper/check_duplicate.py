import json
from collections import Counter

# Load your JSON file
with open("questions.json", "r") as f:
    questions = json.load(f)  # Assumes it's a JSON list (not `questions = [...]`)

# Count occurrences of each question
question_counts = Counter(questions)

# Find duplicates
duplicates = {q: count for q, count in question_counts.items() if count > 1}

# Print results
if duplicates:
    print("Duplicate questions found:\n")
    for question, count in duplicates.items():
        print(f'"{question}" appears {count} times')
else:
    print("✅ No duplicate questions found.")
