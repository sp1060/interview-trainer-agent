# Agentic AI Interview Trainer

An intelligent, multi-agent AI mock interview ecosystem designed to help job seekers practice realistic technical and behavioral interviews. The platform dynamically adapts to your personal resume and a target job description, delivering hyper-personalized interview loops and actionable, rubric-based feedback.

This project was built entirely within the **IBM Bob Desktop Application**, leveraging enterprise AI pipelines.

---

## 🚀 The Problem & Solution

### The Problem
Preparing for technical and behavioral job interviews is highly stressful, unguided, and expensive. Most current online preparation tools rely on static, generic question banks that fail to adapt to individual candidate resumes, specific company job descriptions, or real-time performance feedback. This leaves job seekers underprepared for dynamic, modern HR and technical recruitment processes.

### Our Solution
The **Agentic AI Interview Trainer** tackles this by creating a context-aware mock interview loop. Powered by **IBM watsonx.ai** and structured using **IBM Bob's Multi-Agent architecture**, the system parses resumes, evaluates target job roles, anchors responses to industry benchmarks using RAG, and generates real-time performance feedback aligned with professional rubrics (like the STAR method).

---

## 🛠️ Tech Stack & Ecosystem

*   **Development Environment:** IBM Bob Desktop Application (AI-Native SDLC workflow)
*   **AI Engine:** IBM watsonx.ai (utilizing high-performance foundation models like Llama 3.3)
*   **Interface Framework:** Streamlit (Python)
*   **Version Control & Deployment:** Git & GitHub

---

## 🤖 How We Leveraged IBM Bob

Instead of relying on a standard code editor, this application was developed using **IBM Bob's** advanced AI-native features:
*   **Plan Mode:** Used to architect the background agent communication flows before generating the script blocks.
*   **Agent Mode:** Handled real-time autonomous code execution, component structure generation, and API payload formatting.
*   **Ask Mode / Linting:** Utilized to analyze context windows, debug token thresholds, and verify secure environment variable isolation.

---
### 1. Clone the Repository

## 📦 Local Installation & Setup

Follow these steps to run the Interview Trainer on your local machine:

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
cd "Interview Trainer Agent"
```

### 2. Install Dependencies
Ensure you have Python installed, then run the direct module installer in your terminal:
```bash
python -m pip install streamlit ibm-watsonx-ai
```
### 3. Set Up Environment Variables
Create a local environment file or configuration block with your credentials:
```
WATSONX_APIKEY: Your official IBM Cloud Platform API key.

WATSONX_PROJECT_ID: Your associated watsonx project instance ID.
```
### 4. Run the Application
Launch the Streamlit dashboard using Python module execution:

```bash
python -m streamlit run app.py
Once executed, open http://localhost:8501 in your web browser to interact with the agent.
