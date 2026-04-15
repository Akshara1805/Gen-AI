from langchain_openai import ChatOpenAI
from prompts.score_prompt import score_prompt

llm = ChatOpenAI(model="gpt-4o-mini")

def score_chain(match_data):
    return (score_prompt | llm).invoke({
        "match_data": match_data
    })