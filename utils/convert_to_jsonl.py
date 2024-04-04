import json

def convert_to_jsonl(input_filename, output_filename):
    # load json data
    with open(input_filename, 'r') as file:
        data = json.load(file)

    # write the converted data to a .jsonl file
    with open(output_filename, 'w') as outfile:
        for item in data['questions']:
            # transform each question-answer pair into the required format
            transformed_item = {
                "messages": [
                    {"role": "user", "content": item["question"]},
                    {"role": "assistant", "content": item["answer"]}
                ]
            }
            # write the transformed item to the .jsonl file
            outfile.write(json.dumps(transformed_item) + '\n')

input_filename = '../datasets/raw/Ecommerce_FAQ_Chatbot_dataset.json'
output_filename = '../datasets/processed/Ecommerce_FAQ_Chatbot_dataset.jsonl'
convert_to_jsonl(input_filename, output_filename)

print(f"File saved as {output_filename}")