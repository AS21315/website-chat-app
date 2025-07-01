import gradio as gr
import random
import time
import validators
from app import WebsiteAnalyzerChat

website_analyzer_chat = None
global_history = []
with gr.Blocks(theme='earneleh/paris', title='Website Analyzer') as demo:
    with gr.Column():
        chatbot = gr.Chatbot()
        msg = gr.Textbox()
        with gr.Row():
            MaleButton = gr.Button("Male Voice")
            FemaleButton = gr.Button("Female Voice")

    def user(user_message, history):
        global website_analyzer_chat
        if website_analyzer_chat is None:
            if validators.url(user_message) == False:
                raise ValueError("The massage give is not a link")
            else:
                website_analyzer_chat = WebsiteAnalyzerChat(url=user_message)
                history.append((user_message, "Analysis complete, feel free to ask any question"))
                return "", history
        else:
            answer = website_analyzer_chat.rag_chain(user_message)
            history.append((user_message, answer))
            global_history.append(answer)
            return "", history

    def handle_male_voice():
        if website_analyzer_chat:
            return website_analyzer_chat.voiceUp(1)

    def handle_female_voice():
        if website_analyzer_chat:
            return website_analyzer_chat.voiceUp(0)

    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False)
    MaleButton.click(handle_male_voice)
    FemaleButton.click(handle_female_voice)

demo.queue()
demo.launch(favicon_path='favicon-16x16.png')