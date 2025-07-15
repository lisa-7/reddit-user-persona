def build_prompt(username, posts, comments):
    """
    Builds a prompt for the LLM using the Reddit user's posts and comments.

    Args:
        username (str): Reddit username.
        posts (list): List of dictionaries containing post data.
        comments (list): List of dictionaries containing comment data.

    Returns:
        str: A formatted prompt string to send to the LLM.
    """
    prompt = f"Reddit user '{username}' has shared the following content:\n\n"

    if posts:
        prompt += "📌 Posts:\n"
        for i, post in enumerate(posts[:5]):  # Limit to 5 for token efficiency
            prompt += f"{i+1}. Title: {post.get('title', '')}\n"
            prompt += f"   Body: {post.get('body', '')}\n"
            prompt += f"   URL: {post.get('url', '')}\n\n"

    if comments:
        prompt += "💬 Comments:\n"
        for i, comment in enumerate(comments[:5]):  # Limit to 5 for token efficiency
            prompt += f"{i+1}. {comment.get('body', '')}\n"
            prompt += f"   URL: {comment.get('url', '')}\n\n"

    prompt += (
        "Based on the above Reddit activity, generate a detailed user persona. "
        "Include the user's interests, personality traits, possible occupation or background, communication style, and online behavior. "
        "Cite specific posts or comments when inferring traits, and be as specific and accurate as possible."
    )
    return prompt
