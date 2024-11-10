from CONFIG import *


def hello():
    if LANGUAGE == 'fr':
        response = "bonjour à vous monsieur"
    else: 
        response = "hello to you sir"
    return response