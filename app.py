import streamlit as st 
import tiktoken 

GPT_35_TURBO_PROMPT_COST = 0.0015/1000 
GPT_35_TURBO_COMPLETIONS_COST = 0.002/1000
GPT4_PROMPT_COST = 0.03/1000
GPT4_COMPLETIONS_COST = 0.06/1000

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    print(num_tokens)
    return num_tokens

def main():
    st.set_page_config(layout="wide")
    st.title("LLM Cost Calculations")
    
    prompt_text = st.text_area("Prompt Text", height=400)

    if len(prompt_text) > 0:
        col1, col2, col3 = st.columns([1,1,1])

        with col1:
            st.info("Your Input Prompt: " + prompt_text)

if __name__ == "__main__":
    main()