from openai import OpenAI
import os
import dotenv

dotenv.load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_APIKEY'))

# send data to openai for fine-tuning
client.files.create(
    file=open('../datasets/processed/Ecommerce_FAQ_Chatbot_dataset.jsonl', 'rb'),
    purpose='fine-tune'
)

print("Data uploaded successfully!")