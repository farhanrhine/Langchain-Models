from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4",temperature=0.5, max_tokens=100)
result=model.invoke("What is the  Capital of India?")
print(result.content)
# print(result)