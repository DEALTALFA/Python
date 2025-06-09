from requests import post
from dotenv import load_dotenv
from os import getenv
from pprint import pprint
import ollama
load_dotenv()
prompt="""
    create dockerfile for {language} which contains a multistage so that the image is slim. Do not provide any Description/Explaination.
    Include:
    - make multiple stage
    - setup workdirectory
    - and expose apropriate port if required
"""
def generate_dockerfile(x) -> str:
    key=getenv("GEMINI_API_KEY")
    url=f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={key}"
    reponse=post(url, json=convert_tojson(prompt,x))
    return reponse.json()["candidates"][0]["content"]["parts"][0]["text"]

def generate_dockerfile_ollama(x) -> str:
    '''Local genai model lunch using ollama'''
    return ollama.generate(model="llama3.2:1b", prompt=prompt.format(language=x))["response"]

def convert_tojson(prompt:str,language:str):
    return {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt.format(language=language)
                    }
                ]
            }
        ]
    }

if __name__=="__main__":
    x=input("input the language:")
    print(generate_dockerfile(x))