# 🔍 Reddit User Persona Builder

This project takes a Reddit profile URL, scrapes the user's latest comments and posts, and uses an AI API to generate a structured **user persona** in JSON format and human-readable `.txt` format.

---

## 📁 Folder Structure

.  
├── main.py # Main executable script  
├── builder.py # Handles persona generation logic using OpenRouter API  
├── scrap.py # Extracts Reddit user data  
├── reddit_client.py # Reddit API (PRAW) setup  
├── templates/ # HTML templates for frontend (Flask)  
├── static/ # Optional: static assets like CSS/JS  
├── .env # Holds OpenRouter API Key and Reddit API credentials  
├── requirements.txt # Python dependencies  
├── <username>_persona.txt # Output persona for a given Reddit user  
└── README.md # This file  


---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/reddit-persona-builder.git
cd reddit-persona-builder
2. Set Up the Environment
bash
Copy
Edit
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
3. Add Environment Variables
Create a .env file in the root folder with the following:


OPENROUTER_API_KEY=your_openrouter_key
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_secret
REDDIT_USER_AGENT=your_user_agent
🧪 Run the App Locally (Flask)

python main.py
Then open your browser and visit:
http://localhost:5000

Paste any Reddit profile URL like:


https://www.reddit.com/user/Hungry-Move-6603/

📝 Output Format
ONe formats are generated:



✅ Web-based JSON: For frontend rendering

🧼 Format Code with Black (PEP-8 Compliance)

pip install black
black .
📦 Deployment (Optional)
Deployed on Render

For production:

Set all environment variables in Render dashboard.

Use gunicorn to run the app:


gunicorn main:app
🧪 Example Output Files
Sample output .txt files are included for:

Hungry-Move-6603_persona.txt

(You can generate more by entering other Reddit profile URLs.)

🛠 Technologies Used
Python 3.10+

Flask

PRAW (Python Reddit API Wrapper)

OpenRouter AI API

markdown2

Gunicorn (for deployment)

📌 Notes


The project is built following Python PEP-8 guidelines.

No Reddit login required — public data only.



👨‍💻 License & Ownership
This project and code are the property of the author. Submitted only for internship evaluation. No code may be reused unless the author is selected for the paid role.

🙌 Made by Amaan Shaikh


---
