import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')
llm = ChatOpenAI(temperature=0, openai_api_key=openai_api_key, model='gpt-4')

def generate_response(message):
    output = llm.predict(message)
    return output

def main():
    st.set_page_config(
        page_title="GPT-4", page_icon=":bird:")

    st.header("Well Well Well :bird:")
    message = st.text_area("message...")

    if message:
        st.write("Generating best message...")

        result = generate_response(message)

        st.info(result)


if __name__ == '__main__':
    main()