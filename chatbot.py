responses = {
    "hello":"hello how can i help you?",
    "hi":"hi there",
    "how are you":"i am doing well",
    "your name":"i ama ai chatbot",
    "python":"python is a popular programming language",
    "ai":"ai stands for artificial intelligence"
}
print("rule based ai chatbot")
while True:
    user = input("you:").strip().lower()
    
    if user == "exit":
        print("goodbye")
        break
    elif user in responses:
        print(responses[user])
    else:
        print("bot sorry,i do not have answer")