from llm import client_groq

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        messages = [{"role": "user", "content": user_input}]
        response = client_groq.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
        )
        # response = chat_gemini.send_message(user_input)

        print(f"AI: {response.choices[0].message.content}")
