import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
groq_client = Groq()

def talk(query):
    prompt = f'''You are a helpful and friendly chatbot designed for small talk. You can answer questions about the weather, your name, your purpose, and more.
    
    QUESTION: {query}
    '''
    completion = groq_client.chat.completions.create(
        model=os.environ.get('GROQ_MODEL', 'openai/gpt-oss-20b'),
        messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ]
    )
    return completion.choices[0].message.content

if __name__ == '__main__':
    query = "Are you a robot?"
    answer = talk(query)
    print("Answer:",answer)