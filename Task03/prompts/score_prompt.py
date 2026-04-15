from langchain.prompts import PromptTemplate

score_prompt = PromptTemplate(
    input_variables=["match_data"],
    template="""
Based on matching and missing skills, give a score from 0 to 100.

Rules:
- More matches → higher score
- More missing → lower score

Return only:
{{
  "score": number
}}

Match Data:
{match_data}
"""
)