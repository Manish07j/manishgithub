from openai import OpenAI
import streamlit as st
 
# Initialize the OpenAI client
clt = OpenAI(api_key='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')
 
def main():
    st.title("Article Writer")
    notes = st.text_area("Enter Topic Information:")
    content = "I want you to write a short literature review on the topic: " + notes
    if st.button("Generate Article"):
        with st.spinner("Generating Article..."):
            response = clt.chat.completions.create(
                model="text-davinci-003",
                messages=[{'role': 'system', 'content': content}]
            )
        description = response.choices[0].message.content
        st.subheader("Generated Writeup:")
        st.write(description)
 
if __name__ == '__main__':
    main()

