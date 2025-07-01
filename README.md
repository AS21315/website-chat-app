# Website Analyzer Chatbot

![Website Analyzer Chatbot Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## 🚀 Overview

The **Website Analyzer Chatbot** is an intelligent AI assistant that allows you to easily understand the content of any website through natural language conversations. Simply provide a website URL, and the chatbot will process its content, enabling you to ask questions, explore topics, and even listen to the AI's responses.

This application leverages **Retrieval Augmented Generation (RAG)** with local LLMs (Ollama's Mistral), robust web scraping, and advanced text-to-speech capabilities to provide a seamless and interactive analysis experience.

### Architecture Diagram

To better understand how the Website Analyzer Chatbot works under the hood, here's a diagram illustrating its core components and data flow:

![Website Analyzer Chatbot Architecture Diagram](https://i.ibb.co/dC88trq/image.png)
*A high-level overview of the RAG pipeline used for website analysis and intelligent Q&A.*

## ✨ Features

* **URL-based Analysis:** Input any valid website URL to begin the analysis.
* **Intelligent Q&A:** Ask natural language questions about the website's content after it's processed.
* **Contextual Understanding:** Powered by RAG, the chatbot provides accurate and relevant answers based on the website's information.
* **Local LLM Integration:** Uses [Ollama](https://ollama.com/) with the `mistral` model for secure and private language model interactions.
* **Text-to-Speech (TTS):** Get audio responses with options for both male and female voices, powered by [ElevenLabs](https://elevenlabs.io/).
* **Intuitive Web UI:** Built with [Gradio](https://www.gradio.app/) for a user-friendly and interactive chat interface.

## 🛠️ Technologies Used

* **Python:** The core programming language.
* **Gradio:** For building the web-based user interface.
* **Ollama:** To run local large language models (`mistral`).
* **ElevenLabs:** For high-quality text-to-speech synthesis.
* **LangChain:** Framework for building LLM applications (specifically `langchain-community` for document loading, embeddings, and vector stores).
* **Chroma:** Vector store for efficient similarity search.
* **BeautifulSoup4:** For parsing HTML content (underpins `WebBaseLoader`).
* **Validators:** For URL validation.

## ⚙️ Setup and Installation

Follow these steps to get the Website Analyzer Chatbot up and running on your local machine.

### Prerequisites

1.  **Python 3.9+:**
    * Download and install from [python.org](https://www.python.org/downloads/).
2.  **Ollama:**
    * Download and install Ollama from [ollama.com](https://ollama.com/).
    * Once installed, open your terminal and pull the `mistral` model:
        ```bash
        ollama pull mistral
        ```
        Ensure the Ollama server is running (it usually starts automatically after installation).
3.  **ElevenLabs API Key:**
    * Sign up for an account on [ElevenLabs](https://elevenlabs.io/).
    * Obtain your API key from your profile settings. You will need to set this as an environment variable or directly in the `app.py` file.

### Installation Steps

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/AS21315/website-chat-app.git](https://github.com/AS21315/website-chat-app.git)
    cd website-chat-app
    ```
    *(Replace `your-username/website-analyzer-chatbot` with your actual repository path)*

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    ```
    **Activate the Virtual Environment:**
    * **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```
    * **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set ElevenLabs API Key:**
    For security, it's highly recommended to set your ElevenLabs API key as an environment variable.
    * **macOS/Linux:**
        ```bash
        export ELEVEN_LABS_API_KEY="YOUR_ELEVENLABS_API_KEY"
        ```
    * **Windows (Command Prompt):**
        ```bash
        set ELEVEN_LABS_API_KEY="YOUR_ELEVENLABS_API_KEY"
        ```
    * **Windows (PowerShell):**
        ```powershell
        $env:ELEVEN_LABS_API_KEY="YOUR_ELEVENLABS_API_KEY"
        ```
    *(Replace `"YOUR_ELEVENLABS_API_KEY"` with your actual key.)*

    **Alternatively (Less Recommended for Production):**
    You can directly paste your API key into `app.py` (or `backend.py` if you named it that) by modifying this line:
    ```python
    client = ElevenLabs(api_key= 'YOUR_ELEVENLABS_API_KEY')
    ```
    Replace `'1aa93eaa6329a7124b099a6b875ac783'` with your actual API key.

## 🚀 How to Run the App

Once all the prerequisites and installation steps are complete, you can run the application.

1.  **Ensure your virtual environment is active.** (See step 2 in Installation).
2.  **Run the UI script:**
    ```bash
    python ui.py
    ```

3.  **Access the Application:**
    The script will output a local URL (e.g., `http://127.0.0.1:7860`). Open this URL in your web browser to access the Website Analyzer Chatbot interface.

## 🤖 How to Use the App

1.  **Start a New Conversation:**
    * The first message you send *must be a valid URL* (e.g., `https://www.example.com`).
    * Type the URL into the text box and press Enter or click the send button.
    * The chatbot will process the website. This might take a moment depending on the website's size.
    * Once processed, it will respond with "Analysis complete, feel free to ask any question."

2.  **Ask Questions:**
    * Now you can ask questions about the content of the website you provided.
    * Examples:
        * "What is this website about?"
        * "Who is the author of this article?"
        * "Summarize the main points of the page."
        * "What products or services are mentioned?"

3.  **Use Voice Output:**
    * After the AI provides a text response, you can click the "Male Voice" or "Female Voice" buttons to hear the last AI message spoken aloud.

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements, bug fixes, or new features, please feel free to:

1.  Fork the repository.
2.  Create a new branch 
3.  Make your changes.
4.  Commit your changes 
5.  Push to the branch 
6.  Open a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
