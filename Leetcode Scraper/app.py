import json
import pandas as pd
from leetscrape import GetQuestionsList

def clean_topic_tags(raw):
    if isinstance(raw, list):
        try:
            topic_str = ''.join(raw)
        except:
            return "Not Available"
    elif isinstance(raw, str):
        topic_str = raw
    else:
        return "Not Available"

    topics = [t.strip() for t in topic_str.split(',') if t.strip()]
    return ', '.join(topics) if topics else "Not Available"

def load_questions_from_json(path="questions.json"):
    try:
        with open(path, "r") as f:
            questions = json.load(f)
        if isinstance(questions, list):
            return questions
        else:
            print("❌ Invalid JSON format: Expected a list.")
            return []
    except Exception as e:
        print(f"❌ Error reading {path}: {e}")
        return []

def generate_leetcode_csv(target_questions):
    ls = GetQuestionsList()
    ls.scrape()
    df_all = ls.questions

    output = []

    for question in target_questions:
        row = df_all[df_all["title"].str.lower() == question.lower()]
        
        if not row.empty:
            data = row.iloc[0]

            title = data["title"]
            slug = data["titleSlug"]
            difficulty = data["difficulty"]
            topics = clean_topic_tags(data["topicTags"])
            category = data["categorySlug"] if data["categorySlug"] else "Not Available"

            companies = "Not Available"
            link = f"https://leetcode.com/problems/{slug}/"

            output.append([
                title,
                link,
                difficulty,
                topics,
                category,
                companies,
                "Not Available",
                "Not Available"
            ])
        else:
            output.append([
                question,
                "Not Found",
                "Not Found",
                "",
                "",
                "",
                "",
                ""
            ])

    df_out = pd.DataFrame(output, columns=[
        "Question Name", "Question Link", "Difficulty",
        "Topics", "Category", "Companies",
        "Time Complexity", "Space Complexity"
    ])
    df_out.to_csv("leetcode_questions.csv", index=False)
    print("✅ Saved: leetcode_questions.csv")

if __name__ == "__main__":
    questions = load_questions_from_json("questions.json")
    if questions:
        generate_leetcode_csv(questions)
    else:
        print("⚠️ No questions found in questions.json.")
