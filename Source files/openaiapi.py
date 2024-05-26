import openai
import pyttsx3

# Set up OpenAI API
openai.api_key = 'Your API Key'

# Initialize pyttsx3 for text-to-speech conversion
engine = pyttsx3.init('sapi5')

# Function to ask question and get AI response
def ask_question(query):
    response = openai.Completion.create(
        engine="davinci-002",
        prompt=query,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()
