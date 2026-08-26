import os
from dotenv import load_dotenv
from nemoguardrails import RailsConfig, LLMRails
from langchain_google_genai import ChatGoogleGenerativeAI
from nemoguardrails.llm.providers import register_llm_provider

load_dotenv()

# Register the provider so engine: google_genai works!
try:
    register_llm_provider("google_genai", ChatGoogleGenerativeAI)
    print("Registered google_genai provider!")
except Exception as e:
    print(f"Failed to register provider: {e}")

config = RailsConfig.from_path('guardrails')
rails = LLMRails(config)
print('NeMo Loaded OK')
