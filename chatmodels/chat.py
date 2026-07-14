from dotenv import load_dotenv
from langchain.agents import create_agent

load_dotenv()

agent = create_agent(
    model="google_genai:gemini-2.5-flash"
)

print("Gemini Chatbot Started!")
print("Type 'exit' to quit.\n")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": user
                }
            ]
        }
    )

    # Print only the AI response
    print("\nGemini:", response["messages"][-1].content)
    print()