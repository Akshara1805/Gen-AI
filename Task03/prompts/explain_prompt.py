from langchain.prompts import PromptTemplate

explain_prompt = PromptTemplate(
    input_variables=["match_data", "score"],
    template="""
Explain why this candidate got this score.

Include:
- Strengths
- Weaknesses
- Final reasoning

Match Data:
{match_data}

Score:
{score}
"""
)