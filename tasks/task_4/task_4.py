# Import necessary libraries
import streamlit as st
from langchain_google_vertexai import VertexAIEmbeddings  # Import the VertexAIEmbeddings class for text embeddings

class EmbeddingClient:
    def __init__(self, model_name, project, location):
        """
        Initializes the EmbeddingClient with the specified model, project, and location.
        :param model_name: The name of the model to use for embeddings.
        :param project: The Google Cloud project ID.
        :param location: The location of the Google Cloud project.
        """
        self.model_name = model_name  # Store the model name
        self.project = project        # Store the Google Cloud project ID
        self.location = location      # Store the location of the Google Cloud project

        # Initialize the VertexAIEmbeddings client with the provided parameters
        self.client = VertexAIEmbeddings(
            model_name, project, location  # Pass model name, project, and location to the client
        )

    def embed_query(self, query):
        """
        Uses the embedding client to retrieve embeddings for the given query.
        :param query: The text query to embed.
        :return: The embeddings for the query.
        """
        vectors = self.client.embed_query(query)  # Get embeddings for the query from the Vertex AI client
        return vectors  # Return the embeddings

    def embed_documents(self, documents):
        """
        Retrieve embeddings for multiple documents.
        :param documents: A list of documents to embed.
        :return: A list of embeddings for the documents or None if the method is not defined.
        """
        try:
            return self.client.embed_documents(documents)  # Try to get embeddings for the documents
        except AttributeError:
            # If the method embed_documents is not defined, print an error message
            print("Method embed_documents not defined for the client.")
            return None  # Return None to indicate failure

# Entry point of the script
if __name__ == "__main__":
    # Define the configuration for the embedding client
    model_name = "textembedding-gecko@003"  # Model name for embeddings
    project = "gemini-quizify-433501"       # Google Cloud project ID
    location = "us-central1"                # Location of the Google Cloud project

    # Initialize the EmbeddingClient with the specified parameters
    embedding_client = EmbeddingClient(model_name, project, location)

    # Use the embed_query method to get embeddings for a sample query
    vectors = embedding_client.embed_query("Hello World!")  # Get embeddings for the query "Hello World!"
    
    # Check if embeddings were successfully retrieved
    if vectors:
        st.write(vectors)  # Display the embeddings in the Streamlit app
        print(vectors)    # Print the embeddings to the console
        st.write("Successfully used the embedding client!")  # Display success message in Streamlit
        print("Successfully used the embedding client!")  # Print success message to the console
