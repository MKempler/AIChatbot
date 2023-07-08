# AI Chatbot
## Welcome to my Chatbot project! This project implements a simple chatbot using natural language processing techniques and a neural network model. The chatbot can understand user inputs, classify intents, and generate appropriate responses.

## Overview
### The project consists of the following files:

chatbot.py: Contains the code for the chatbot model and functions to interact with it.
chatgui.py: Implements a graphical user interface (GUI) using Tkinter for users to interact with the chatbot.
train_chatbot.py: Used to train the chatbot model based on the intents defined in intents.json.
intents.json: Contains the intents and their corresponding patterns and responses used for training and interaction.

## Dependencies
### To run the chatbot project, the following dependencies are required:

Python 3.x
Keras
NLTK (Natural Language Toolkit)
Tkinter

### You can install the required dependencies by running the following command:

pip install keras nltk

## Usage
### To use the chatbot, follow these steps:

Ensure that all the project files are in the same directory.
Run the train_chatbot.py script to train the chatbot model based on the intents defined in intents.json.
After training, you can run the chatbot GUI by executing the chatgui.py script. This will open a chat window.
In the chat window, type your messages in the input box and press Enter or click the Send button to send them to the chatbot.
The chatbot will process your input, predict the intent, and generate an appropriate response, which will be displayed in the chat window.
Feel free to modify the intents.json file to define additional intents and responses for the chatbot.

## Limitations
The chatbot's performance relies on the quality and variety of training data provided in intents.json. Adding more diverse examples can improve its accuracy and ability to handle different user inputs.
The chatbot uses a simple bag-of-words representation and a neural network model. It may not handle complex language structures or understand context beyond individual messages.
The chatbot does not have real-time data capabilities, such as providing current weather information or time.

## Contributing
Contributions to this chatbot project are welcome! If you have any ideas, improvements, or bug fixes, feel free to submit a pull request.

## License
This project is licensed under the MIT License.
