import os
from typing import Dict, Any
from openai import OpenAI


class OpenAIPipeline:
    """
    A minimal OpenAI-based planning pipeline for the agent.
    It generates a structured action plan based on user input.
    """

    def __init__(self, model: str | None = None):
        self.model = model or os.getenv("OPENAI_MODEL", "gpt-4.1")
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def plan(self, user_input: str) -> Dict[str, Any]:
        """
        Generates a simple action plan for the agent.
        Returns a dictionary with:
        - action: name of the tool to execute
        - input: arguments for the tool
        """

        system_prompt = (
            "You are a planning module for an AI agent. "
            "Your task is to output a JSON-like dictionary with two fields: "
            "'action' (string) and 'input' (string). "
            "Choose the simplest tool that can solve the user's request. "
            "If the user wants to repeat or transform text, use 'echo'. "
            "If the user asks for math, use 'calculator'. "
            "If the user asks for time/date, use 'datetime'. "
            "If no tool fits, default to action='echo'."
        )

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input},
            ],
            temperature=0.2,
        )

        content = response.choices[0].message.content

        # Minimal parsing — safe fallback to echo
        try:
            plan = eval(content)
            if isinstance(plan, dict) and "action" in plan and "input" in plan:
                return plan
        except Exception:
            pass

        return {"action": "echo", "input": user_input}
