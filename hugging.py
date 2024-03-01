import streamlit as st
from docx import Document
import io


# Streamlit app layout
st.title('Custom DOCX Document Generator')
user_input = st.text_area("Enter your text here")

if st.button('Generate Document'):
    # Create a document in memory
    doc = Document()
    doc.add_paragraph(user_input)
    doc_io = io.BytesIO()  # Create a BytesIO buffer
    doc.save(doc_io)  # Save the document to the buffer
    doc_io.seek(0)  # Go to the beginning of the buffer
    
    # Download button
    st.download_button(
        label="Download Document",
        data=doc_io,  # The buffer to download
        file_name="custom_document.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"  # MIME type
    )