# Making this so that i dont have to import this everytime a need my model
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

groq_model = ChatGroq(model ='openai/gpt-oss-120b')