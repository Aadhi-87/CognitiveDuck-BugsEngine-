import streamlit as st
from google import genai
from google.genai import types

# ---------------------------------------------------------
# 1. Page Configuration & Title Setup
# ---------------------------------------------------------
st.set_page_config(
    page_title="Cognitive Duck",
    page_icon="🦆",
    layout="wide"
)

# New High-Impact Hackathon Title
st.title("🦆 Cognitive Duck: Bug Forensics Engine")
st.caption("A high-speed reasoning agent that traces execution logic, flags edge-case vulnerabilities, and outputs optimized fixes.")

# ---------------------------------------------------------
# 2. Restored Configuration Panel (No Hidden Files Needed!)
# ---------------------------------------------------------
st.sidebar.header("Authentication")
# This creates a safe password field right inside your sidebar
api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")

client = None
if api_key:
    client = genai.Client(api_key=api_key)
    st.sidebar.success("Agent Engine Activated!")
else:
    st.sidebar.info("Paste your free API key above to unlock the reasoning framework.")

st.sidebar.markdown("""
---
### Architecture Protocol:
This system forces a strict **Chain-of-Thought (CoT)** breakdown to trace functional execution blocks deterministically.
""")

# ---------------------------------------------------------
# 3. Main Interface Layout
# ---------------------------------------------------------
col1, col2 = st.columns([2, 1])

with col1:
    code_input = st.text_area(
        "Code Snippet:", 
        height=300,
        placeholder="def parse_data(x):\n    # Paste code here..."
    )

with col2:
    context_input = st.text_area(
        "Observed Symptoms / Context:", 
        height=150,
        placeholder="e.g., 'Throws a Time Limit Exceeded error for large inputs'"
    )
    
    language = st.selectbox(
        "Language:",
        ["Python", "JavaScript/TypeScript", "C/C++", "Java", "SQL", "Other"]
    )
    
    submit_button = st.button("Debug", type="primary")

# ---------------------------------------------------------
# 4. Fast Reasoning Inference Engine
# ---------------------------------------------------------
if submit_button:
    if not api_key or client is None:
        st.error("⚠️ Authentication Key missing. Please provide a valid key in the sidebar panel.")
    elif not code_input:
        st.warning("⚠️ Code workspace is empty.")
    else:
        with st.spinner("Compiling execution graphs..."):
            try:
                # Optimized instructions: demanding direct bullet points for ultra-fast generation
                system_instruction = """
                You are a high-speed code reasoning agent. Provide brief, highly technical, bulleted engineering feedback. 
                
                Format your response precisely with these headers:
                
                ### 🧭 Step 1: Control Flow 
                Explain the structural intent and execution path in 2-3 dense bullet points.
                
                ### ⚠️ Step 2: Logic Flaws
                Pinpoint the exact edge case, boundary vulnerability, or complexity problem.
                
                ### 🛠️ Step 3: Optimized code
                Provide the clean, corrected code block with concise inline comments explaining why the fix works.
                """
                
                user_payload = f"Language: {language}\nContext: {context_input}\n\nCode:\n{code_input}"
                
                # Using a fast generation model with low temperature for rapid, targeted processing
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=user_payload,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        temperature=0.1
                    )
                )
                
                st.success("✅ Logical Analysis Complete!")
                st.markdown("---")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"Inference Error: {str(e)}")