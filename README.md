# customer-service-chatbot

## Dependencies

pip install openai python-dotenv

## To run single question chatbot

python scripts/init_single_question_chatbot.py

## To run continuous question chatbot

python scripts/init_continuous_question_bot.py

## To run data cleaning script

1. edit file_path to be path to the raw data
2. cd utils
3. python data_preprocessing.py

## To run script to convert json to jsonl

1. edit input_filename and output_filename
2. cd utils
3. python convert_to_jsonl.py
