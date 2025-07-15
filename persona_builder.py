from openai import OpenAI

client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)

def generate_persona(prompt, model="mistralai/mistral-7b-instruct"):
    print(f"[+] Using OpenRouter model: {model}")
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates detailed psychological personas from Reddit user data."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("[!] Error while generating persona:", e)
        raise
