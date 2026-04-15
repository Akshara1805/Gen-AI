from langchain_openai import ChatOpenAI
from prompts.explain_prompt import explain_prompt

llm = ChatOpenAI(model="gpt-4o-mini")

def explain_chain(match_data, score):
    return (explain_prompt | llm).invoke({
        "match_data": match_data,
        "score": score
    })