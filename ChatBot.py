# Simple Rule-Based Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"

    # Asking about chatbot
    elif "who are you" in user_input:
        return "I am a simple rule-based chatbot created using Python."

    # Asking about name
    elif "your name" in user_input:
        return "I don't have a specific name, but you can call me ChatBot!"

    # Asking about well-being
    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking. How can I help you today?"

    # Goodbye
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day."

    # Default response
    else:
        return "Sorry, I did not understand that. Can you rephrase?"

# Main chat loop
print("ChatBot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("ChatBot: Goodbye! Have a nice day.")
        break

    response = chatbot_response(user_input)
    print("ChatBot:", response)
