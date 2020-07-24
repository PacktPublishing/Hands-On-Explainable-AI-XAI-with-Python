# Python client for Google Dialogflow API V2
# Copyright 2019 Denis Rothman MIT License. See LICENSE.
import os
import dialogflow_v2 as dialogflow
from google.api_core.exceptions import InvalidArgument

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] ='private_key.json'#'private_key.json'
DIALOGFLOW_PROJECT_ID = '[YOUR PROJECT_ID]' #'[PROJECT_ID]'
DIALOGFLOW_LANGUAGE_CODE ='en'       #'[LANGUAGE]'
SESSION_ID = '[YOUR SESSION ID]'

our_query = "Hi" # our query

#session variables
session_client = dialogflow.SessionsClient() 
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)

# Our query 
our_input = dialogflow.types.TextInput(text=our_query, language_code=DIALOGFLOW_LANGUAGE_CODE)
query = dialogflow.types.QueryInput(text=our_input)

# try or raise exceptions
try:
    response = session_client.detect_intent(session=session, query_input=query)
except InvalidArgument:
    raise

print("Our text:", response.query_result.query_text)
print("Dialogflow's response:", response.query_result.fulfillment_text)
print("Dialogflow's intent:", response.query_result.intent.display_name)


