from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# Load environment variables
load_dotenv()

# Create the Hugging Face endpoint
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1"
)

# Create the chat model
model = ChatHuggingFace(llm=llm)

# Ask a question
response = model.invoke("Who are you?")

print(response.content)