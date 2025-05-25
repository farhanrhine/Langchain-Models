from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-preview", temperature=0.5, max_tokens=100)
result=model.invoke("What is the  Capital of India?")
print(result.content)
# print(result)"