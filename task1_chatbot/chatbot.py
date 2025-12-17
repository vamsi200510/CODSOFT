def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "bye":
            print("Chatbot: Goodbye! Have a nice day 😊")
            break
        elif "hello" in user or "hi" in user:
            print("Chatbot: Hi there! How can I help you?")
        elif "your name" in user:
            print("Chatbot: I am a Rule-Based Chatbot.")
        elif "help" in user:
            print("Chatbot: I can answer simple questions.")
        elif "codsoft" in user:
            print("Chatbot: CODSOFT provides internship opportunities.")
        else:
            print("Chatbot: Sorry, I didn’t understand that.")

# IMPORTANT: function call
chatbot()
