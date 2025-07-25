import pandas as pd
import json

def update_companies(csv_file, json_file, output_file="leetcode_questions.csv"):
    # Step 1: Load CSV
    df = pd.read_csv(csv_file)

    # Step 2: Load JSON data
    with open(json_file, "r") as f:
        company_data = json.load(f)

    # Step 3: Create a mapping from URL → companies list
    url_to_companies = {item["url"]: item.get("companies", []) for item in company_data}

    # Step 4: Update the Companies column
    updated_companies = []
    for link in df["Question Link"]:
        if link in url_to_companies:
            companies_list = url_to_companies[link]
            companies_str = ', '.join(companies_list) if companies_list else "Not Available"
            updated_companies.append(companies_str)
        else:
            updated_companies.append("Not Available")

    df["Companies"] = updated_companies

    # Step 5: Save updated CSV
    df.to_csv(output_file, index=False)
    print(f"✅ Updated CSV saved as: {output_file}")

# === SAMPLE USAGE ===
if __name__ == "__main__":
    update_companies(
        csv_file="leetcode_questions.csv",
        json_file="data.json"
    )
