from langchain.prompts import PromptTemplate

extract_prompt = PromptTemplate(
    input_variables=["resume"],
    template="""
You are an AI resume parser.

Extract the following from the resume:
- Skills
- Experience
- Tools

Return ONLY in JSON format:
{{
  "skills": [],
  "experience": "",
  "tools": []
}}

Resume:
{resume}
"""
)