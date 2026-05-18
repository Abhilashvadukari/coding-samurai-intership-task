print("=== Coding Samurai Rule-Based Chatbot ===")

while True:
    user = input("You: ").lower()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")

    elif "name" in user:
        print("Bot: I am a Rule-Based Chatbot.")

    elif "how are you" in user:
        print("Bot: I am doing great!")

    elif "bye" in user or "exit" in user:
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
