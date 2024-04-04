from openai import OpenAI
import os
import dotenv

dotenv.load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_APIKEY'))

# gives chatbot the instruction to be an assistant
conversation = [{"role": "system", "content": "You are an assistant."}]

print("How can I help you?")
inputquestion = input("Question: ")

# append user's question to conversation
conversation.append({"role": "user", "content": inputquestion})

# send conversation to OpenAI
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=conversation
)

assistant_response = response.choices[0].message.content
print(f"Assistant: {assistant_response}")