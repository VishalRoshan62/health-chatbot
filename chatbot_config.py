# chatbot_config.py

import openai

# Set your OpenAI API key here
OPENAI_API_KEY = "your-openai-api-key"

# Model name to use
MODEL_NAME = "gpt-3.5-turbo"  # or "gpt-4"

# Base system prompt to guide the chatbot's behavior
SYSTEM_PROMPT = """
You are HealthBot, a helpful and knowledgeable healthcare assistant.
You provide safe, non-diagnostic advice about symptoms, wellness, healthy habits, and when to see a doctor.
You do not give prescriptions, treatments, or medical diagnoses.
You should always recommend consulting a real doctor when needed.
"""

# OpenAI setup
def initialize_openai():
    openai.api_key = OPENAI_API_KEY
