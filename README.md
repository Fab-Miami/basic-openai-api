# OpenAI Chat Application

This Python script allows users to interact with OpenAI's GPT-3.5-turbo model through a simple command-line interface. Users can send messages and receive responses from the model, facilitating an engaging and dynamic chat experience.

## Features

- Simple command-line interface for sending and receiving messages.
- Uses OpenAI's powerful GPT-3.5-turbo model for generating responses.
- Environment variable management for API keys.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or later
- `requests` library

## Setup

1. Clone this repository:
git clone https://github.com/yourusername/your-repository-name.git

2. Navigate into the project directory:
cd your-repository-name

3. Install the required packages:
pip install requirements.txt

4. Set up your OpenAI API key as an environment variable:
export OPENAI_API_KEY='your_openai_api_key_here'

Replace `'your_openai_api_key_here'` with your actual OpenAI API key.

## Usage

To start the chat application, run:
python openai_test.py

Type your message and press enter to send. To exit the chat, type `exit` or `quit`.