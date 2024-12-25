
# 🌟 Enhanced Q&A Chatbot with Groq 🧠💬

Welcome to the **Enhanced Q&A Chatbot**, an AI-powered application built with **Streamlit** and **LangChain Groq**. This chatbot enables seamless interaction with advanced language models to answer your questions accurately and efficiently. 🎯✨

---

## 🚀 Features

- **🌐 Interactive User Interface**: Powered by Streamlit for a smooth and intuitive experience.
- **🤖 Groq Model Integration**: Access a range of powerful LLMs for versatile use cases.
- **⚙️ Customizable Settings**: Easily adjust parameters like temperature, model selection, and token limits.
- **🔒 Secure API Integration**: Manage your API keys securely using environment variables.

---

## 🛠️ Requirements

- **Python**: Version 3.7 or higher 🐍
- **Libraries**: Streamlit, LangChain Groq, dotenv 📦

---

## 📥 Installation

1. Clone the repository 📂:
   ```bash
   git clone https://github.com/Rahulagowda004/QandA_chatbot.git
   cd Rahulagowda004/QandA_chatbot
   ```

2. Install dependencies 📦:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your `.env` file for secure API key management 🔑:
   ```
   LANGCHAIN_API_KEY=<your-api-key>
   ```

---

## 📖 Usage Guide

1. Start the application 🚀:
   ```bash
   streamlit run app.py
   ```

2. Open the app in your browser 🌐 (default: `http://localhost:8501`).

3. Configure settings in the **Sidebar** 🛠️:
   - Enter your Groq API Key.
   - Select a model (e.g., `gemma2-9b-it`, `llama3-groq-70b`).
   - Adjust **Temperature** (controls randomness) and **Max Tokens** (response length).

4. Ask your question in the input box ✍️ and get instant AI responses! 🤖✨

---

## 🧩 Key Features in Detail

### 🎛️ Sidebar Configuration
- **API Key Input**: Add your Groq API key for secure access.
- **Model Selection**: Choose from a range of state-of-the-art language models:
  - `gemma2-9b-it`
  - `llama3-groq-70b-8192-tool-use-preview`
  - `gemma-7b-it`
  - `mixtral-8x7b-32768`
  - And more! 🚀
- **Temperature**: Fine-tune creativity in responses (0.0 = deterministic, 1.0 = highly creative). 🎨
- **Max Tokens**: Set the length of responses to suit your needs. 📝

### 💡 Dynamic Chat Interface
- Type your query and let the chatbot handle the rest! ⚡
- Real-time response generation with Groq-powered models. 🧠

---

## 🔧 Customization Options

- **Update Models**: Modify the model list in `st.sidebar.selectbox` to include new Groq models.
- **Adjust Defaults**: Change default slider values for **Temperature** and **Max Tokens**.
- **Enhance Prompts**: Customize the chatbot’s behavior by tweaking the `ChatPromptTemplate`.

---

## 🌟 Why Use This Chatbot?

- **High Accuracy**: Leverage advanced Groq models for precise answers. ✅
- **Customizable**: Tailor settings to fit your unique requirements. 🛠️
- **Easy to Use**: A no-frills interface that simplifies AI-powered interactions. 🎉

---

## 📜 Acknowledgements

- **Streamlit**: Simplifying web app development. 🌐
- **LangChain Groq**: Advanced AI language model framework. 🤖
- **dotenv**: Secure and efficient environment variable management. 🔒

---

## 📝 License

This project is licensed under the **MIT License**. Feel free to fork, modify, and distribute as you see fit! 🎉

---

## 🛡️ Future Improvements

- **🎨 UI Enhancements**: Add themes and customization options.
- **📊 Analytics Dashboard**: Track usage and performance metrics.
- **🔗 Model Integration**: Expand compatibility with additional LLMs.

---

Happy querying! 🚀💬
