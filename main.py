import os
import warnings
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText

from openfabric_pysdk.context import OpenfabricExecutionRay
from openfabric_pysdk.loader import ConfigClass
from time import time

from nlp_engine import answer_question

############################################################
# Callback function called on update config
############################################################
def config(configuration: ConfigClass):
    # Set the chatbot's name
    configuration.name = "ScienceBot"

    # Set the chatbot's welcome message
    configuration.welcome_message = "Welcome to ScienceBot! I'm here to answer any science questions you may have."

    # Set the chatbot's default response
    configuration.default_response = "Sorry, I didn't understand your question. Can you please try again?"

    # Set the chatbot's language
    configuration.language = "en"

    # Set the maximum length of the chatbot's responses
    configuration.max_response_length = 500

    # Set the chatbot's confidence threshold for accepting a response
    configuration.confidence_threshold = 0.6

    # Set the chatbot's maximum number of attempts to answer a question
    configuration.max_attempts = 3

    # Set the chatbot's response delay in seconds
    configuration.response_delay = 0.5

    # Set the chatbot's response timeout in seconds
    configuration.response_timeout = 30


############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    output = []
    for text in request.text:
        # TODO Add code here
        response = answer_question(text)
        output.append(response)

    return SimpleText(dict(text=output))
