from dotenv import load_dotenv
import os
# from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(dotenv_path=".env")
# print("API KEY:", os.getenv("OPENAI_API_KEY"))
# llm = ChatOpenAI(
#     model="openrouter/deepseek/deepseek-v3.2",
#     api_key=os.getenv("OPENAI_API_KEY"),
#     base_url="https://openrouter.ai/api/v1",
#     temperature=0.3,
# )

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.3
)