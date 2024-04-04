from openai import OpenAI
import os
import dotenv
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "utils"))
from send_appointment_email import send_appointment_email

def prompt_for_appointment_details():
    date = input("Please enter a date for your appointment (YYYY-MM-DD): ")
    time = input("Please enter a time for your appointment (HH:MM): ")
    email = input("Please enter your email address: ")
    return date, time, email

dotenv.load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_APIKEY'))

# gives chatbot the instruction to be an assistant
conversation = [{"role": "system", "content": "You are an assistant."}]

print("How can I help you? (Type 'quit' to end the conversation)")

while True:
    inputquestion = input("Question: ")

    if inputquestion == "quit":
        break

    # append user's question to conversation
    conversation.append({"role": "user", "content": inputquestion})

    # send conversation to OpenAI
    response = client.chat.completions.create(
        model=os.getenv("TRAINED_MODELID"),
        messages=conversation,
        temperature=0 # 0 gives more precise answers
    )
    assistant_response = response.choices[0].message.content

    if "book an appointment" in assistant_response.lower():
        print(f"Assistant: {assistant_response}")
        user_response = input("Would you like to book an appointment? (yes/no): ")
        if user_response.lower() == "yes":
            # get appointment details from user
            date, time, email = prompt_for_appointment_details()
            # send appointment confirmation email
            send_appointment_email(email, date, time)
            print("your appointment has been booked, and an email confirmation has been sent.")

            conversation.append({"role": "system", "content": f"Appointment booked for {date} at {time}, confirmation sent to {email}."})
            continue
        else:
            print(f"Assistant: {assistant_response}")
            conversation.append({"role": "system", "content": assistant_response})
    else:
        print(f"Assistant: {assistant_response}")
        conversation.append({"role": "system", "content": assistant_response})