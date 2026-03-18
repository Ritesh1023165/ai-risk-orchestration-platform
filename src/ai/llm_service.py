import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
# Initialize the Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def explain_risk(data, risk_score, decision):

    prompt = f"""
    A loan application was evaluated.

    Applicant data:
    {data}

    Risk score: {risk_score}
    Decision: {decision}

    Explain the decision in simple business terms.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a financial risk analyst."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content