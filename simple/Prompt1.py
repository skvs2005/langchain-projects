import os

from dotenv import load_dotenv, find_dotenv
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

_ = load_dotenv(find_dotenv()) # read local .env file

GROQ_API_KEY=os.environ['GROQ_API_KEY']

# Use Groq's LLMs like Mixtral, Llama 3, or Gemma
llm = ChatOpenAI(
    model="llama3-70b-8192",  # Change this to "llama3-8b-8192" or "gemma-7b-it" if needed
    openai_api_key=os.getenv("GROQ_API_KEY"),
    openai_api_base="https://api.groq.com/openai/v1"
)

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in simple terms."
)


# New way to create a chain using RunnableSequence
chain = prompt | llm

# Invoke the chain
response = chain.invoke({"topic": "LangChain"})

print(response.content)