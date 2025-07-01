import bs4
import ollama
import os
from elevenlabs import play, save
from elevenlabs.client import ElevenLabs
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load the ElevenLabs API key from an environment variable.
elevenlabs_api_key = os.getenv("ELEVEN_LABS_API_KEY")
if not elevenlabs_api_key:
    print("Warning: ELEVEN_LABS_API_KEY environment variable not set. ElevenLabs functionality may not work.")

client = ElevenLabs(
    api_key=elevenlabs_api_key
)

class WebsiteAnalyzerChat:
    def __init__(self, url):
        self.url = url
        self.retriever = self.load_and_retrieve_docs()
        self.chat_history = []

    def load_and_retrieve_docs(self):
        loader = WebBaseLoader(
            web_paths=(self.url,),
            bs_kwargs={}
        )
        docs = loader.load()
        
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        splits = text_splitter.split_documents(docs)
        
        embeddings = OllamaEmbeddings(model="mistral")
        
        vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
        
        return vectorstore.as_retriever()

    def format_docs(self, docs):
        return "\n\n".join(doc.page_content for doc in docs)

    def rag_chain(self, question):
        self.chat_history.append({'role': 'user', 'content': question})
        
        retrieved_docs = self.retriever.invoke(question)
        formatted_context = self.format_docs(retrieved_docs)
        
        self.chat_history.append({'role': 'ai', 'content': formatted_context}) 

        formatted_prompt = [{"role": "user", "content": entry['content']} for entry in self.chat_history]
        formatted_prompt.append({"role": "system", "content": f"Context: {formatted_context}"})
        
        response = ollama.chat(model='mistral', messages=formatted_prompt)

        llm_response_content = response['message']['content']
        self.chat_history.append({'role': 'system', 'content': llm_response_content})
        
        print(self.chat_history[-1]['content'])
        
        return llm_response_content
    
    def voiceUp(self, voiceType):
        if not self.chat_history:
            print("No message in chat history to convert to voice.")
            return

        message = self.chat_history[-1]['content']
        
        if not client.api_key:
            print("ElevenLabs API key is not set. Cannot generate voice.")
            return

        audio = None
        if voiceType == 0: # Female voice
            audio = client.generate(
                text=message,
                voice="XfNU2rGpBa01ckF309OY",
                model="eleven_multilingual_v2"
            )
        elif voiceType == 1: # Male voice
            audio = client.generate(
                text=message,
                voice="pVnrL6sighQX7hVz89cp",
                model="eleven_multilingual_v2"
            )
        
        if audio:
            play(audio)
        else:
            print(f"Invalid voiceType: {voiceType} or no audio generated.")

