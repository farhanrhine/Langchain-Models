# from langchain_community.llms import Ollama
# from langchain.chains import LLMChain
# from langchain.prompts import PromptTemplate

# # Step 1: Connect to local llama3 running via ollama
# llm = Ollama(model="llama3.2")

# # Step 2: Create a prompt template
# prompt = PromptTemplate(
#     input_variables=["question"],
#     template="Answer this question: {question}"
# )

# # Step 3: Create a chain
# chain = LLMChain(llm=llm, prompt=prompt)

# # Step 4: Ask a question
# question = "What is the capital of India?"
# response = chain.run(question)

# # Step 5: Print the answer
# print("💬 Answer:", response)

# # C:\Users\farha\Downloads\Langchain Models\ChatModels/ollama_chat.py

from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate

# Define your Ollama model
llm = Ollama(model="llama3.2")

# Define the prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{question}"),
])

# Build a runnable chain: (prompt | llm)
chain = prompt | llm

# Ask a question
response = chain.invoke({"question": "What is the capital of India?"})

print(response)
