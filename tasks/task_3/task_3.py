# Necessary imports
import streamlit as st  # Streamlit for building the web app
from langchain_community.document_loaders import PyPDFLoader  # PyPDFLoader for processing PDF files
import os  # OS module for file and directory operations
import tempfile  # Temporary file handling
import uuid  # UUID for generating unique file names

class DocumentProcessor:
   # """
   # This class encapsulates the functionality for processing uploaded PDF documents using Streamlit
   # and Langchain's PyPDFLoader. It provides a method to render a file uploader widget, process the
   # uploaded PDF files, extract their pages, and update the self.pages list with the total number of pages.
   # """
    def __init__(self):
        #"""
        #Initializes the DocumentProcessor class.
        #Sets up an empty list to store pages extracted from PDF documents.
        #"""
        self.pages = []  # List to keep track of pages from all documents
    
    def ingest_documents(self):
        #"""
        #Renders a file uploader in a Streamlit app, processes uploaded PDF files,
        #extracts their pages, and updates the self.pages list with the total number of pages.
        
        #Steps:
        #1. Utilize the Streamlit file uploader widget to allow users to upload PDF files.
        #2. For each uploaded PDF file:
        #   a. Generate a unique identifier and append it to the original file name before saving it temporarily.
        #   b. Use Langchain's PyPDFLoader on the path of the temporary file to extract pages.
        #   c. Clean up by deleting the temporary file after processing.
        #3. Keep track of the total number of pages extracted from all uploaded documents.
        #"""
        
        # Step 1: Render a file uploader widget
        st.title("Quizify")
        uploaded_files = st.file_uploader(
            
            "Choose a PDF file",  # Label for the file uploader widget
            type="pdf",  # Allow only PDF files
            accept_multiple_files=True  # Allow multiple file uploads
        )
        
        if uploaded_files:  # Check if files have been uploaded
            for uploaded_file in uploaded_files:
                # Generate a unique identifier to avoid file name conflicts
                unique_id = uuid.uuid4().hex  # Generate a unique UUID
                original_name, file_extension = os.path.splitext(uploaded_file.name)  # Split the file name and extension
                temp_file_name = f"{original_name}_{unique_id}{file_extension}"  # Create a unique file name
                temp_file_path = os.path.join(tempfile.gettempdir(), temp_file_name)  # Create a path for the temporary file

                # Write the uploaded PDF to a temporary file
                with open(temp_file_path, 'wb') as f:
                    f.write(uploaded_file.getvalue())  # Save the file content

                # Step 2: Process the temporary file
                loader = PyPDFLoader(temp_file_path)  # Create a PyPDFLoader instance with the temporary file path
                pages = loader.load()  # Extract pages from the PDF
                
                # Step 3: Add the extracted pages to the 'pages' list
                self.pages.extend(pages)  # Append the extracted pages to the self.pages list
                
                # Clean up by deleting the temporary file
                os.unlink(temp_file_path)  # Remove the temporary file

            # Display the total number of pages processed
            st.write(f"Total pages processed: {len(self.pages)}")  # Show the total count of pages extracted
        
# Run the Streamlit app when this script is executed directly
if __name__ == "__main__":
    processor = DocumentProcessor()  # Create an instance of DocumentProcessor
    processor.ingest_documents()  # Call the method to start processing documents
