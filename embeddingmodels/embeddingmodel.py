from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

# Load API key
load_dotenv()

# Create the embedding model
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=64
)

# Generate embedding
vector = embeddings.embed_query("You are going to learn Gen AI")

print(vector)
print(f"\nVector Length: {len(vector)}")