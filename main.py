import os
from med_validators import validations
import streamlit as st
import PIL.Image as Pil
import google.generativeai as genai
import pickle
from googletrans import Translator

loaded_history = []

# File paths for the two history files
file_paths = ['chat_history1.pkl', 'chat_history2.pkl']

# Loop through the file paths and load each history file
for file_path in file_paths:
    with open(file_path, 'rb') as file:
        # Load the history from the current file and extend the loaded_history list
        loaded_history.extend(pickle.load(file))

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=loaded_history)

def validate_queries(user_message):
    splitted_user_message = user_message.split()
    for word in splitted_user_message:
        if word.lower() in validations:
            return False
    return True


def translate_text(text, target_language='en'):
    translator = Translator()
    try:
        translation = translator.translate(text, dest=target_language)
        return translation.text
    except Exception as e:
        st.error(f"Error translating text: {e}")
        return None


def main():
    st.session_state.conversation = []
    st.set_page_config(page_title="YUNIGMA Medical Chatbot")
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    st.title("Yunigma Medical Chatbot")

    with st.sidebar:
        st.title('Medical ChatBot')
        st.write("")
        st.markdown(":blue[About]")
        st.subheader('Hi i am a Yunigma! \n A medical ChatBot built by Team VVCE.')
        st.markdown(":red[DISCLAIMER : ]")
        st.write('This CHATBOT is trained on few medical textbooks.\nIt is fine-tuned to answer medical related '
                 'queries.\nPlease do not ask irrelevant questions.')
        st.write("")
        option = st.selectbox(
            'Choose your Response Language : ',
            ('en', 'hi', 'kn', 'ta', 'te'))

    st.markdown("""
        <style>
            #file-upload {
                display: block;
                margin: 10px 0;
            }
            .chat-container {
                display: flex;
                flex-direction: column;
                height: 400px;
                overflow-y: auto;
                padding: 10px;
                color: white; /* Font color */
            }
            .user-bubble {
                background-color: #007bff; /* Blue color for user */
                align-self: flex-end;
                border-radius: 10px;
                padding: 8px;
                margin: 5px;
                max-width: 70%;
                word-wrap: break-word;
            }
            .bot-bubble {
                background-color: #363636; /* Slightly lighter background color */
                align-self: flex-start;
                border-radius: 10px;
                padding: 8px;
                margin: 5px;
                max-width: 70%;
                word-wrap: break-word;
            }
        </style>
        """, unsafe_allow_html=True)

    conversation = st.session_state.get("conversation", [])

    # File upload for the image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if user_prompt := st.chat_input("Enter your prompt here: "):
        st.markdown(":orange[User Prompt: ]")
        st.write(user_prompt)
        if uploaded_file is not None:
            # Open and display the uploaded image
            image = Pil.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)

            # Process the image and prompt
            vision_model = genai.GenerativeModel('gemini-pro-vision')
            try:
                with st.spinner(text="Generating response..."):
                    response = vision_model.generate_content([user_prompt, image])
            except Exception:
                st.error("An error occured to connect to Gemini Vision Pro")
            # response.prompt_feedback
            response.resolve()

            try:
                with st.spinner(text="Translating response..."):
                    translated_response = translate_text(response.text, target_language=option)
                conversation.append({"role": "bot", "message": response.text})
                st.session_state.conversation = conversation
                st.markdown(":blue[Response : ]")
                st.write("")
                st.write(translated_response)
            except Exception as e:
                st.error(f"Error generating response: {e}")

        else:
            try:
                with st.spinner(text="Generating response..."):
                    response = chat.send_message(user_prompt)
            except Exception as e:
                st.error("An error occured to connect to Gemini Pro")
            if validate_queries(user_prompt):
                try:
                    with st.spinner(text="Translating response..."):
                        translated_response = translate_text(response.text, target_language=option)
                    conversation.append({"role": "bot", "message": response.text})
                    st.session_state.conversation = conversation
                    st.markdown(":blue[Response : ]")
                    st.write("")
                    st.write(translated_response)
                except Exception as e:
                    st.error(f"Error generating response: {e}")
            else:
                st.markdown(":blue[Response : ]")
                st.write("")
                translated_response = translate_text("I am sorry! I am a medical chatbot. "
                                                     "Try asking questions relevent to medical field.",
                                                     target_language=option)
                st.write(translated_response)


if __name__ == '__main__':
    main()
