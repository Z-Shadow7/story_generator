import json
from typing import List
from groq import Groq

def generate_story(prompt: str, genre: str, api_key: str, num_scenes: int = 4, characters: list = []) -> List[dict]:
    client = Groq(api_key=api_key)

    character_info = ""
    if characters:
        character_info = "Characters to include:\n" + "\n".join(
            [f"- {c['name']} ({c['role']}): {c['description']}" for c in characters]
        )

    system_prompt = f"""You are a creative family-friendly story writer. Generate a short story split into exactly {num_scenes} scenes.
    Keep all content appropriate for all ages. No adult, violent, or inappropriate content.
    {character_info}

    Respond with a JSON object containing a "scenes" array like this:
    {{
        "scenes": [
            {{
                "scene_number": 1,
                "title": "Scene title here",
                "story": "2-3 sentences of story text here.",
                "image_prompt": "Detailed visual description here, family friendly only."
            }}
        ]
    }}"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Genre: {genre}\nTopic: {prompt}"}
        ],
        max_tokens=2000,
        temperature=0.7,
        response_format={"type": "json_object"}
    )

    raw = response.choices[0].message.content
    data = json.loads(raw)
    return data["scenes"]