import os

from dotenv import load_dotenv, find_dotenv
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

_ = load_dotenv(find_dotenv()) # read local .env file

GROQ_API_KEY=os.environ['GROQ_API_KEY']
# File to store responses
markdown_file = "responses.md"
if not os.path.exists(markdown_file):
    with open(markdown_file, "w", encoding="utf-8") as file:
        file.write("# AI Responses\n\n")
absolute_path = os.path.abspath(markdown_file)
print(f"Saving responses to: {absolute_path}")

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
#
# # Invoke the chain
# response = chain.invoke({"topic": "LangChain"})
#
# print(response.content)
#

def save_response_to_markdown(topic, response):
    """Saves the response at the top of the Markdown file"""
    new_entry = f"## {topic}\n\n{response.content}\n\n---\n"

    # Read existing content
    if os.path.exists(markdown_file):
        with open(markdown_file, "r", encoding="utf-8") as file:
            existing_content = file.read()
    else:
        existing_content = ""

    # Write new response first, then existing content
    with open(markdown_file, "w", encoding="utf-8") as file:
        file.write(new_entry + existing_content)

# Example usage
topic = "LangChain"
response = chain.invoke({"topic": topic})

# Loop to take user input until "exit"
while True:
    topic = input("Enter a topic (or type 'exit' to quit): ").strip()

    if topic.lower() == "exit":
        print("Exiting... All responses are saved in responses.md.")
        break

    response = chain.invoke({"topic": topic})

    save_response_to_markdown(topic, response)

    print(f"Response saved for '{topic}'!\n")
