"""this module is used for translation"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    function to convert english to french
    """
    #write the code here
    french_text = MyMemoryTranslator(source='en', target='fr').translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    function to convert french to english
    """
    #write the code here
    english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    return english_text
