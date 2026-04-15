from langchain_openai import ChatOpenAI
from prompts.extract_prompt import extract_prompt

llm = ChatOpenAI(model="gpt-4o-mini")

def extract_chain(resume):
    return (extract_prompt | llm).invoke({"resume": resume})