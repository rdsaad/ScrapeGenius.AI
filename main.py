import streamlit as st
from genius import (
    scrape_genius,
    split_content,
    clean_content,
    extract_content,
)
from extract import extract_with_ollama

st.title("ScrapeGenius.AI")
url = st.text_input("Enter Website URL")

if st.button("Scrape Website"):
    if url:
        st.write("Genius is currently at work...")

        result = scrape_genius(url)
        body_content = extract_content(result)
        cleaned_content = clean_content(body_content)

        st.session_state.dom_content = cleaned_content

        with st.expander("View Website Content"):
            st.text_area("Website Content", cleaned_content, height=300)

if "dom_content" in st.session_state:
    content_description = st.text_area("Describe What You Want to Know")

    if st.button("Extract Content"):
        if content_description:
            st.write("Genius is extracting the content...")

            dom_chunks = split_content(st.session_state.dom_content)
            result = extract_with_ollama(dom_chunks, content_description)
            st.write("Here is your extracted information:")
            st.write(result)
            st.write("Let me know if you have any more questions!")
