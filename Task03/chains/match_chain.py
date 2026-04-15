from langchain_openai import ChatOpenAI
from prompts.match_prompt import match_prompt

llm = ChatOpenAI(model="gpt-4o-mini")

def match_chain(resume_data, job_description):
    return (match_prompt | llm).invoke({
        "resume_data": resume_data,
        "job_description": job_description
    })