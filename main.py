from scrap import extract_username, scrape_user_content
from builder import generate_persona
from flask import Flask,render_template,request
import json
import markdown2
app =Flask(__name__)

def get_main(url,r):
    reddit_url = url
    username = extract_username(reddit_url)
    print(f"Scraping content from u/{username}...")
    user_data= scrape_user_content(username)
    content_list = user_data["content"]
    icon_url = user_data["icon_img"]

    print(f"Generating user persona for u/{username}...")
    persona = generate_persona(content_list,referer=r)

    
    persona = persona.strip()

# Remove ```json ... ``` block if present
    if persona.startswith("```json"):
        persona = persona.replace("```json", "").replace("```", "").strip()

    persona_json=json.loads(persona) 
    return {
    "persona": persona_json,
    "icon_url": icon_url
    }


@app.route("/",methods=["POST","GET"])
def render_homepage():
    return render_template("index.html")


@app.route("/generate",methods=["POST","GET"])
def generate():
    url=request.form.get("reddit_url")
    referer = request.headers.get("Origin") or "https://reddit-user-persona-builder.onrender.com"
    result=get_main(url,r=referer)
    return render_template("generate.html",result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
