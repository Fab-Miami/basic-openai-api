# in shell:
# export OPENAI_API_KEY=write_your_api_key_here

# ----------------------- CURL SHELL TEST -----------------------
#
# curl https://api.openai.com/v1/chat/completions \
#   -H "Content-Type: application/json" \
#   -H "Authorization: Bearer $OPENAI_API_KEY" \
#   -d '{
#      "model": "gpt-3.5-turbo",
#      "messages": [{"role": "user", "content": "Say this is a test!"}],
#      "temperature": 0.7
#    }'
#
# ---------------------------------------------------------------

import requests
import os

# Set your OpenAI API key
api_key = os.getenv('OPENAI_API_KEY')

# Define the headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}
url = 'https://api.openai.com/v1/chat/completions'

def main():
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting the chat.")
            break
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code != 200:
            print("Error: ", response.json())
            break

        # print("\nRAWjson: ", response.json())
        print("\n\nGPT: ", response.json()['choices'][0]['message']['content'])

if __name__ == "__main__":
    main()


# run the script by typing: python openai_test.py
