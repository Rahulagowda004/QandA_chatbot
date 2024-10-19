import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
import os

load_dotenv() 

#langsmith tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACKING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "QandA Chatbot with groq"

prompt = ChatPromptTemplate(
    [
        ("system","you are helpful assistant.Please respond to the user queries"),
        ("user","Question:{question}")
    ]
)

def generate_response(question,api_key, llm, temperature,max_tokens):
    llm = ChatGroq(model = llm, api_key = str(api_key),temperature=temperature,max_tokens=max_tokens)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question': question})
    return answer

st.title("Enhanced Q&A Chatbot With groq")

st.sidebar.title("settings")
api_key = st.sidebar.text_input("enter your groq api key")

llm = st.sidebar.selectbox("select an OpenAI model",["gemma2-9b-it","llama3-groq-70b-8192-tool-use-preview","gemma-7b-it","llama3-groq-8b-8192-tool-use-preview"])

temperature  = st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens = st.sidebar.slider("Max tokens",min_value=50,max_value=300,value=150)

st.write("go ahead and ask any question")
user_input = st.text_input("you:")

if user_input: 
    response = generate_response(user_input,api_key,llm,temperature,max_tokens)
    st.write(response)
else:
    st.write("Please provide the query")