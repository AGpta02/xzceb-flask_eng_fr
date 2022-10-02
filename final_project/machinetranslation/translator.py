"""
Translator functions
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_disable_ssl_verification(True)
language_translator.set_service_url(url)

def englishToFrench(english_text):
    """
    Converts English to French
    """
    if english_text == '':
        french_text = 'entrée invalide'
    else:
        french_text = language_translator.translate(text=english_text, model_id='en-fr').get_result()

    return french_text

def frenchToEnglish(french_text):
    """
    Converts French to English
    """
    if french_text == '':
        english_text = 'invalid entry'
    else:
        english_text = language_translator.translate(text=french_text, model_id='fr-en').get_result()

    return english_text
