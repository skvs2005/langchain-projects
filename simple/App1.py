import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

GROQ_API_KEY=os.environ['GROQ_API_KEY']

from langchain_openai import ChatOpenAI

# Use Groq's LLMs like Mixtral, Llama 3, or Gemma
llm = ChatOpenAI(
    model="llama3-70b-8192",  # Change this to "llama3-8b-8192" or "gemma-7b-it" if needed
    openai_api_key=os.getenv("GROQ_API_KEY"),
    openai_api_base="https://api.groq.com/openai/v1"
)

# Generate a response
response = llm.invoke("Explain LangGraph in simple terms.")
print(response.content)
