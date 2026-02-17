import config
from openai import OpenAI

client = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=config.GROQ_API_KEY)

def get_response(prompt, role_context=""):
    system_message = "You are a helpful assistant." if not role_context else role_context
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content

print("--- Reinforcement Learning Task ---")
topic = "Describe the future of artificial intelligence"
initial_ai_resp = get_response(topic)
print(f"Initial Response: {initial_ai_resp[:100]}...")

feedback = "Make it more poetic and focus on the harmony between humans and machines."
refined_prompt = f"{topic}. Feedback to incorporate: {feedback}"
refined_resp = get_response(refined_prompt)
print(f"Refined Response: {refined_resp[:100]}...\n")

print("--- Role-Based Prompting Task ---")
topic_2 = "Explain machine learning algorithms"
roles = {
    "Teacher": "Explain simply with analogies for a beginner.",
    "Expert": "Provide a technical, in-depth explanation with jargon.",
    "Business Leader": "Focus on practical applications and ROI.",
    "Peer Student": "Explain for a high school student with basic knowledge."
}

for role, context in roles.items():
    print(f"[{role}'s Perspective]:")
    print(get_response(topic_2, role_context=context))
    print("-" * 30)