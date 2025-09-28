import streamlit as st
from transformers import pipeline

# ---------------------------------------------------------
# Loading the model once and cache it for performance
# ---------------------------------------------------------


@st.cache_resource
def load_model():
    print("Loading Flan-T5-Large model... (this will only happen once)")
    # --- THIS IS THE CORRECTED LINE ---
    return pipeline("text2text-generation", model="google/flan-t5-large")


generator = load_model()

# ---------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------


def clean_output(text, max_sentences=3):
    # This function cleans up the model's output to be exactly 2-3 sentences
    sentences = [s.strip() for s in text.split(".") if s.strip()]
    result = []
    for s in sentences:
        if s not in result and len(result) < max_sentences:
            result.append(s)
    return ". ".join(result) + ("." if result else "")


def call_model(prompt, max_new_tokens=120):
    # This function calls the AI model with a prompt
    result = generator(prompt, max_new_tokens=max_new_tokens)
    text = result[0]["generated_text"].strip()
    return clean_output(text)

# ---------------------------------------------------------
# The Three Agent Functions
# ---------------------------------------------------------
# Agent 1: Knowledge Extractor (Professor role)


def knowledge_extractor(query):
    prompt = f"""
You are a university science professor who explains concepts in detail.
Give a clear explanation of {query} that is factual and accurate.
Write exactly three complete sentences. 
Each sentence should give new information and avoid repetition.
Answer:
"""
    return call_model(prompt)

# Agent 2: Teacher (Child-friendly)


def teacher_agent(query):
    prompt = f"""
You are a friendly school teacher explaining to a 12-year-old child.
Explain {query} in very simple language using only everyday words.
Write three short sentences. 
Each sentence should be clear and easy for a child to understand.
Do not use technical terms like "chloroplast" or "chemical energy."
Answer:
"""
    return call_model(prompt)

# Agent 3: Narrator (Analogy / Storyteller)


def creative_narrator(query):
    prompt = f"""
You are a creative storyteller.
Explain {query} using a fun and vivid analogy.
Pretend you are painting a picture with words so the idea is easy to imagine.
Write three sentences.
Use expressions like "imagine" or "it's like" to compare the concept to everyday things. 
Make sure the comparison is scientifically correct.
Answer:
"""
    return call_model(prompt)


# ---------------------------------------------------------
# The Streamlit User Interface (UI)
# ---------------------------------------------------------
st.set_page_config(page_title="💎 CogniPrism", layout="wide", page_icon="💎")

# CSS for the funky dark theme
st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
}
.output-card {
    background: linear-gradient(135deg, #1f1f1f, #2d2d2d);
    border: 2px solid #FF4B4B;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 20px;
    height: 280px; /* Increased height for longer text */
    box-shadow: 0 0 15px #FF4B4B55;
    transition: transform 0.2s ease-in-out;
    display: flex;
    flex-direction: column;
}
.output-card:hover {
    transform: scale(1.03);
    box-shadow: 0 0 25px #FF4B4B;
}
.agent-title {
    font-size: 24px;
    font-weight: bold;
    color: #FF4B4B;
    margin-bottom: 15px;
}
.card-text {
    flex-grow: 1; /* Allows text to fill the space */
}
</style>
""", unsafe_allow_html=True)

# --- App Layout ---
st.title("💎 CogniPrism")
st.caption("⚡ Refracting ideas into multiple perspectives with three AI agents.")

concept = st.text_input("💡 Enter a concept to refract:", "")

if concept:
    # Show a loading spinner while the model works
    with st.spinner("Refracting your concept..."):
        extractor_text = knowledge_extractor(concept)
        teacher_text = teacher_agent(concept)
        narrator_text = creative_narrator(concept)

    # Display the results in three styled columns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"<div class='output-card'><div class='agent-title'>👨‍🏫 The Professor</div><div class='card-text'>{extractor_text}</div></div>", unsafe_allow_html=True)

    with col2:
        st.markdown(
            f"<div class='output-card'><div class='agent-title'>👩‍🏫 The Teacher</div><div class='card-text'>{teacher_text}</div></div>", unsafe_allow_html=True)

    with col3:
        st.markdown(
            f"<div class='output-card'><div class='agent-title'>📖 The Storyteller</div><div class='card-text'>{narrator_text}</div></div>", unsafe_allow_html=True)
