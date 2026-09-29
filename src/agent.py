import os
from openai import OpenAI
import config


class CodeReviewAgent:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY") or getattr(config, "GEMINI_API_KEY", None)
        if not api_key:
            raise ValueError("GEMINI_API_KEY is missing! Please set it in your .env file.")

        # Point the OpenAI client to Google's Gemini endpoint
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )

    def generate_review(self, diff: str, pr_number: int) -> str:
        system_prompt = (
            "You are an expert automated code reviewer. "
            "Analyze code diffs thoroughly, pointing out bugs, security issues, "
            "syntax errors, and efficiency improvements concisely."
        )

        user_prompt = (
            f"Review the following diff for PR #{pr_number}:\n\n"
            f"```diff\n{diff}\n```"
        )

        response = self.client.chat.completions.create(
            model="gemini-3.8-flash",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.2
        )

        return response.choices[0].message.content