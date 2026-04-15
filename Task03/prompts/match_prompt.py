from langchain.prompts import PromptTemplate

match_prompt = PromptTemplate(
    input_variables=["resume_data", "job_description"],
    template="""
Compare the resume with the job description.

Return:
- Matching skills
- Missing skills

Format:
{{
  "matching_skills": [],
  "missing_skills": []
}}

Resume Data:
{resume_data}

Job Description:
{job_description}
"""
)