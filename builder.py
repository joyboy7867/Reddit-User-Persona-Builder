import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
def build_prompt(content_list):
    examples = "\n\n".join(
        f"[{item['type'].capitalize()}]({item['permalink']}): {item['text'][:500]}"
        for item in content_list
    )

    prompt = f"""
    You are an AI trained to analyze a Reddit user's posts and generate a structured JSON-based persona.
    
    Analyze the following Reddit content and return the output strictly as JSON in this format:
    
    {{
      "name": "string (nickname or Reddit handle if found)",
      "age": "string (like '20-30 years')",
      "gender": "string ('Male', 'Female', or 'Unknown')",
      "occupation": "string (like 'Student', 'Software Engineer', etc)",
      "hobbies": ["list of hobbies"],
      "political_views": ["list of views"],
      "personality": ["list of traits"],
      "language_style": ["list of patterns (e.g. 'sarcastic', 'casual')"],
      "frequent_subreddits": ["list of subreddits"],
      "notable_beliefs": ["list of opinions"],
      "summary": "A paragraph summarizing the user persona"
    }}
    
    ONLY RETURN THE JSON OBJECT. DO NOT include any commentary, markdown formatting, or explanation.
    
    Use these Reddit posts and comments to extract information:
    
    {examples}
    """
    return prompt

def generate_persona(content_list,referer):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": referer,
        "X-Title": "RedditPersonaBuilder"
    }

    data = {
        "model": "deepseek/deepseek-chat-v3-0324:free",  # or try "mistralai/mixtral-8x7b-instruct"
        "messages": [
            {"role": "system", "content": "You are a helpful AI that creates user personas from Reddit data."},
            {"role": "user", "content": build_prompt(content_list)}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.HTTPError as e:
        print("❌ HTTP Error:", e)
        print("🔍 Response Body:\n", response.text)
        return "Failed to generate persona due to API error."
