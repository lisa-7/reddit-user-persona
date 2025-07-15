# 🧠 Reddit User Persona Generator

This project generates a detailed psychological persona for any Reddit user based on their public posts and comments. It scrapes data using the Reddit API (via PRAW) and sends it to a large language model (LLM) via OpenRouter to infer personality traits, goals, frustrations, motivations, and more — with **citations** from the user's Reddit activity.

---

## ✨ Features

- 🔗 Accepts any Reddit user profile URL as input
- 📥 Scrapes recent posts and comments using Reddit API
- 🧠 Uses LLM (OpenRouter) to generate a detailed persona
- 🔖 Cites specific posts/comments for each personality trait
- 📄 Saves result as a `.txt` file in the `output/` folder
- ✅ Fully PEP-8 compliant and CLI-executable

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/reddit-user-persona.git
cd reddit-user-persona
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add OpenRouter API Key

In `persona_builder.py`, locate the line:

```python
api_key="sk-or-...",  # replace with your own key from https://openrouter.ai
```

You can get a free key at [https://openrouter.ai](https://openrouter.ai)

### 4. Configure Reddit API Access (PRAW)

In `scraper.py`, replace:

```python
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
user_agent = "script:reddit-persona:v1.0 (by u/yourusername)"
```

You can get credentials from: [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)

---

## 🚀 How to Run

```bash
python main.py --url https://www.reddit.com/user/kojied/
```

This will:

1. Extract the username from the URL
2. Scrape the user’s posts & comments (up to 50 each)
3. Build a prompt and send it to OpenRouter
4. Save the resulting persona to:

```
output/user_persona_kojied.txt
```

---

## 🧪 Sample Outputs

You can find generated samples inside the `output/` folder:

* `output/user_persona_kojied.txt`
* `output/user_persona_Hungry-Move-6603.txt`

These contain:

* Inferred occupation / interests
* Traits like introversion/extroversion
* Motivations (e.g., speed, wellness)
* Frustrations (cited)
* Communication style
* A quote from the user
* URLs linking back to the cited Reddit content

---

## 📦 File Structure

```
reddit-user-persona/
├── main.py                 # Entry script
├── scraper.py              # Reddit scraper using PRAW
├── prompt_builder.py       # Builds the LLM prompt
├── persona_builder.py      # Sends prompt to OpenRouter LLM
├── requirements.txt        # Dependencies
├── README.md               # You're here!
└── output/
    ├── user_persona_kojied.txt
    └── user_persona_Hungry-Move-6603.txt
```

---

## 💡 Technologies Used

* Python 3.10+
* [PRAW](https://praw.readthedocs.io/) for Reddit API
* [OpenRouter](https://openrouter.ai) for LLM inference
* `openai>=1.2.0` Python SDK (used for OpenRouter backend)

---

## 🧠 Example Prompt (Under the Hood)

A prompt sent to the LLM might look like this:

> Reddit user 'kojied' has shared the following content:
> 📌 Post: "The future of LLMs is more open-source than we think..."
> 💬 Comment: "I spend most mornings journaling about ADHD struggles."
>
> Based on the above Reddit activity, generate a detailed user persona. Include personality traits, motivations, frustrations, inferred background, and cite each trait with a source.

---

## ✅ PEP-8 Compliance

This codebase adheres to PEP-8 style guidelines using 4-space indentation and clear function separation. You may run `flake8` or format with VS Code.

---

## 🔐 Licensing & Ownership

> Your code is your property. The reviewing team will not use or distribute your code in any form unless you are selected for the internship.

---

## 📬 Questions?

For technical questions, please contact lisa3172003@gmail.ccom

---