from openai import OpenAI
import os
import dotenv

dotenv.load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_APIKEY'))

# train the model
client.fine_tuning.jobs.create(
    training_file=os.getenv('DATA_FILEID'),
    model="gpt-3.5-turbo-1106",
    hyperparameters={"n_epochs":8}
)