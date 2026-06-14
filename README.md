# CognitiveDuck-BugsEngine-
An advanced, single-agent engineering companion built for the Agents League Hackathon. It utilizes a deterministic **Chain-of-Thought (CoT)** framework to trace execution logic, flag boundary edge cases, and output mathematically optimized runtime fixes.

## 🚀 Features
- **Control Flow :** Maps execution blocks step-by-step.
- **Vulnerability Forensics:** Isolates algorithmic bottlenecks (e.g., $O(N^2)$ loops) and edge-case failure traps.
- **Automated Refactoring:** Provides clean structural fixes optimized for scaling safety.

## 🛠️ Installation & Setup
1. Clone the repository: `git clone <your-repo-url>`
2. Install dependencies: `pip install streamlit google-genai`
3. Launch the application: `python -m streamlit run app.py`
4. Enter your Gemini API key in the sidebar panel to unlock inference.
