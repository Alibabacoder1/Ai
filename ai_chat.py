import random

# Define possible responses
greetings = ['hello', 'hi', 'hey']
farewells = ['goodbye', 'bye', 'see you later']
questions = ['how are you?', 'what is your name?', 'what do you do?']
responses = {
    'hello': ['Hello!', 'Hi there!', 'Hey!'],
    'goodbye': ['Goodbye!', 'Bye!', 'See you later!'],
    'how are you?': ['I am doing well, thank you!', 'Not too bad, thanks for asking!', 'I am great!'],
    'what is your name?': ['My name is Chatbot!', 'You can call me Chatbot!', 'I am Chatbot!'],
    'what do you do?': ['I am here to help you with your queries!', 'I can assist you with anything you need!', 'I am a customer service chatbot!']
}

# Define function to generate response
def generate_response(message):
    if message.lower() in greetings:
        return random.choice(responses['hello'])
    elif message.lower() in farewells:
        return random.choice(responses['goodbye'])
    elif message.lower() in questions:
        return random.choice(responses[message.lower()])
    else:
        return "I'm sorry, I didn't understand your message."

# Define main function to run chatbot
def main():
    print("Welcome to the chatbot!")
    while True:
        message = input("You: ")
        if message.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        else:
            response = generate_response(message)
            print("Chatbot:", response)

if __name__ == '__main__':
    main()
