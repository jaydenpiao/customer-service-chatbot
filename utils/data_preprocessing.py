import json

# path to raw json data
file_path = '../datasets/raw/Ecommerce_FAQ_Chatbot_dataset.json'

phone_number = '123-456-7890'
email_address = 'support@internetprovider.com'
working_hours = '9 AM to 5 PM'

# load json data
with open(file_path, 'r') as file:
    data = json.load(file)

# replace placeholders with actual data
for item in data['questions']:
    item['answer'] = item['answer'].replace('[phone number]', phone_number)
    item['answer'] = item['answer'].replace('[email address]', email_address)
    item['answer'] = item['answer'].replace('[working hours]', working_hours)

# new file name and directory
new_file_path = '../datasets/processed/' + file_path.split('/')[-1].replace('.json', '_cleaned.json')

# save processed data to new file
with open(new_file_path, 'w') as file:
    json.dump(data, file, indent=4)

print(f"File saved as {new_file_path}")
