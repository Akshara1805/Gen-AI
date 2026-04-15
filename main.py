import os
from dotenv import load_dotenv

from chains.extract_chain import extract_chain
from chains.match_chain import match_chain
from chains.score_chain import score_chain
from chains.explain_chain import explain_chain

load_dotenv()

# Check for API key
if not os.getenv("OPENAI_API_KEY"):
    print("❌ ERROR: OPENAI_API_KEY not found in .env file!")
    print("Please add OPENAI_API_KEY=sk-... to your .env file")
    exit(1)

def load_file(path):
    with open(path, "r") as f:
        return f.read()

# Load data
print("📂 Loading data files...")
job_description = load_file("data/job_description.txt")

resumes = {
    "strong": load_file("data/strong_resume.txt"),
    "average": load_file("data/average_resume.txt"),
    "weak": load_file("data/weak_resume.txt"),
}

print("✅ Data files loaded successfully\n")

for label, resume in resumes.items():
    print(f"\n{'='*50}")
    print(f"--- Processing {label.upper()} candidate ---")
    print(f"{'='*50}")

    try:
        # Step 1: Extract
        print("\n📋 Step 1: Extracting resume data...")
        extracted = extract_chain(resume)
        print("✅ Extracted:", extracted.content)

        # Step 2: Match
        print("\n🔍 Step 2: Matching with job description...")
        matched = match_chain(extracted.content, job_description)
        print("✅ Matched:", matched.content)

        # Step 3: Score
        print("\n⭐ Step 3: Scoring candidate...")
        score = score_chain(matched.content)
        print("✅ Score:", score.content)

        # Step 4: Explain
        print("\n💡 Step 4: Generating explanation...")
        explanation = explain_chain(matched.content, score.content)
        print("✅ Explanation:", explanation.content)
        
    except Exception as e:
        print(f"❌ Error processing {label} candidate: {str(e)}")
        import traceback
        traceback.print_exc()