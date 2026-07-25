def get_response(user_input):
    
    text = user_input.lower().strip()
 
    if text in ("hi", "hello", "hey", "hola"):
        return "Hello there! How can I help you today?"
 
    elif "how are you" in text:
        return "I'm just a program, but I'm running smoothly! How about you?"
 
    elif "your name" in text:
        return "I'm ChatBot, a simple rule-based assistant."
 
    elif "help" in text:
        return "I can chat about greetings, my name, or how I'm doing. Try saying 'hi' or 'bye'!"
 
    elif "thank" in text:
        return "You're welcome!"
 
    elif "weather" in text:
        return "I can't check live weather, but I hope it's nice where you are!"
 
    elif text in ("bye", "exit", "quit", "goodbye"):
        return "EXIT"  

    else:
        return "Sorry, I didn't understand that. Type 'help' for suggestions or 'bye' to exit."
    

print("ChatBot: Hello! Type 'bye', 'exit', or 'quit' to end the chat.")
 
while True:
    user_input = input("You: ")
 
    response = get_response(user_input)
 
    if response == "EXIT":
        print("ChatBot: Goodbye! Have a great day.")
        break
    else:
        print(f"ChatBot: {response}")