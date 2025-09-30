# 💎 CogniPrism

**CogniPrism** is an AI application that refracts complex ideas into multiple, easy-to-understand perspectives. Using a three-agent system, it explains any concept from the viewpoint of a Professor, a Teacher, and a Storyteller. This project demonstrates a multi-agent architecture for enhancing educational content.

---

### ✨ Features

- **Three AI Agents**:
  - **👨‍🏫 The Professor**: Provides a detailed, factual, and scientifically accurate explanation.
  - **👩‍🏫 The Teacher**: Simplifies the concept for a younger audience (like a 12-year-old).
  - **📖 The Storyteller**: Creates a fun and vivid analogy to make the idea memorable.
- **Interactive UI**: Built with a custom, dark-themed Streamlit interface for a modern user experience.
- **Powered by Open Source**: Uses a lightweight, open-source model that can run on consumer hardware.

---

### 🧠 Model & Performance Notes

This implementation uses the **`google/flan-t5-large`** model from Hugging Face. It was chosen because it is open-source, relatively lightweight (~2.5GB), and can run on a local machine without requiring a high-end GPU.

**Important Consideration:**
While `flan-t5-large` is great for accessibility and demonstration, it is not a state-of-the-art model. For simpler concepts, it performs well. However, for more complex or nuanced topics, it may occasionally produce hallucinations or less accurate explanations.

For significantly better and more reliable results, the agent prompts in this application can be easily adapted for more powerful models like **OpenAI's GPT-4** or **Anthropic's Claude 3**. Using these models would dramatically improve the quality and consistency of the generated explanations.

---

### 🚀 How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/cogniprism.git
    cd cogniprism
    ```

2.  **Install the required libraries:**
    *   It's recommended to use a virtual environment.
    ```bash
    pip install streamlit transformers torch
    ```

3.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```
    The app will open in your browser at `http://localhost:8501`.

---

### 🛠️ Tech Stack

- **Language**: Python
- **AI/ML**: Hugging Face Transformers (`google/flan-t5-large`)
- **UI**: Streamlit
