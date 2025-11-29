import streamlit as s
import google.generativeai as genai

key = ""
genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-2.5-flash")

s.title("Ultra Mind AI")
s.header("Welcome Sir")
s.subheader("How can i assist you today?")
s.write("Anything you can ask me, I am here to help you")

# keeps chat history

if "chat" not in s.session_state:
    s.session_state.chat = []

ip = s.text_input("What Is Today's Agenda !")
end_chat = s.button("End Chat")

if end_chat:
    s.success("Chat Ended..")
    s.session_state.chat = []
    s.stop()

if ip.strip():
    if ip.lower() == "exit":
        s.session_state.chat.append(("bot","Bye Bye Have a good day!"))
    else:
        s.session_state.chat.append(("user", ip))
        # response = model.generate_content(ip)
        # bot_reply = response.text
        # s.session_state.chat.append(("bot", bot_reply))

        with s.spinner("🤖 Ultra Mind AI is typing.."):
            response = model.generate_content(ip)
            bot_reply = response.text
            s.session_state.chat.append(("bot",bot_reply))

        
            

for role, msg in s.session_state.chat:
    if role == "user":
        with s.chat_message("user",avatar = "👤"):
            s.write(msg)
    else:
        with s.chat_message("assistant",avatar = "🤖"):
            s.write(msg)