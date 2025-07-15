# main.py
import argparse
from scraper import extract_username_from_url, get_user_content
import os
from persona_builder import generate_persona
from prompt_builder import build_prompt


def save_output(username, content):
    os.makedirs("output", exist_ok=True)
    with open(f"output/user_persona_{username}.txt", "w", encoding="utf-8") as f:
        f.write(content)

def main(url):
    username = extract_username_from_url(url)
    print(f"[+] Generating persona for Reddit user: {username}")

    posts, comments = get_user_content(username)
    prompt = build_prompt(username, posts, comments)
    persona = generate_persona(prompt)

    save_output(username, persona)
    print(f"[+] Persona saved to output/user_persona_{username}.txt")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reddit User Persona Generator")
    parser.add_argument("--url", type=str, required=True, help="Reddit user profile URL")
    args = parser.parse_args()
    main(args.url)
