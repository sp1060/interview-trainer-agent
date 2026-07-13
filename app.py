import streamlit as st
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

# App layout and custom headers
st.set_page_config(page_title="Superpower Interview Trainer", page_icon="🏆", layout="wide")

st.title("🏆 AI Interview Trainer Agent (RAG-Powered)")
st.caption("Orchestrated via IBM watsonx.ai Foundation Models")
st.markdown("---")

# 🔒 Secure Credentials Retrieval Configuration
# Pulls keys silently from environment secrets so public GitHub code is safe
try:
    API_KEY = st.secrets["WATSONX_API_KEY"]
    PROJECT_ID = st.secrets["WATSONX_PROJECT_ID"]
    IBM_URL = st.secrets.get("WATSONX_URL", "https://us-south.ml.cloud.ibm.com")
except Exception:
    # Fallback to interactive dashboard inputs if local secrets file isn't populated
    API_KEY = ""
    PROJECT_ID = ""
    IBM_URL = "https://us-south.ml.cloud.ibm.com"

# Sidebar configuration instructions
with st.sidebar:
    st.header("⚙️ Deployment Architecture")
    st.success("✅ Public GitHub Security Enforcement Activated.")
    
    # Fallback input interface for isolated local developer testing 
    if not API_KEY or not PROJECT_ID:
        st.warning("⚠️ Credentials not detected in st.secrets. Provide them below for local execution:")
        API_KEY = st.text_input("Watsonx API Key", type="password")
        PROJECT_ID = st.text_input("Project ID")

# Input Target Schema Map
col1, col2 = st.columns(2)

with col1:
    st.subheader("👤 Candidate Parameters")
    name = st.text_input("Candidate Name", value="Rohan Kumar")
    exp_level = st.selectbox("Experience Level", ["Associate / Entry-Level", "Mid-Level Professional", "Senior Lead / Architect"], index=0)
    timeline = st.slider("Preparation Timeline Constraints (Days Remaining)", min_value=1, max_value=30, value=7)

with col2:
    st.subheader("🏢 Targeting Vector Matrix")
    role = st.text_input("Position Target", value="Associate Data Engineer")
    company = st.text_input("Target Corporation", value="Amazon")

st.subheader("📂 Retrieval-Augmented Generation (RAG) Database Context")
rag_context = st.text_area(
    "Paste Recruitment Data, Job Descriptions, or Internal Company Expectations here to prime the RAG layer:",
    value="Seeking a distributed systems engineer to optimize high-throughput pipelines. Must be proficient in Python, PySpark dataframes, AWS S3 partitioning schemas, and Amazon Redshift warehousing strategies. Alignment with corporate data integrity constraints and core leadership principles is mandatory.",
    height=140
)

# Execution Flow
if st.button("🚀 Synthesize Universal Interview Preparation Blueprint", type="primary"):
    if not API_KEY or not PROJECT_ID:
        st.error("Missing Authentication Credentials: Secure the required Watsonx API Key and Project ID parameters before executing.")
    else:
        with st.spinner("Processing RAG embeddings and constructing targeted plan via watsonx.ai..."):
            try:
                # Initialize the unified watsonx cloud connection client
                credentials = {
                    "url": IBM_URL,
                    "apikey": API_KEY
                }
                
                # Model decoding optimizations matching Prompt Lab parameters
                generate_params = {
                    GenParams.MAX_NEW_TOKENS: 1000,
                    GenParams.DECODING_METHOD: "greedy"
                }
                
                # Explicit invocation of the meta-llama model matching your Prompt Lab session
                model = ModelInference(
                    model_id="meta-llama/llama-3-3-70b-instruct",
                    credentials=credentials,
                    project_id=PROJECT_ID,
                    params=generate_params
                )
                
                # Dynamic context generation instruction layout payload
                prompt_template = f"""# ROLE AND MISSION
You are an elite, autonomous AI Interview Trainer Agent powered by RAG (Retrieval-Augmented Generation). Your purpose is to turn candidate profiles and retrieved company database context into tailored question sets, model answers, and preparation strategies.

# INPUT SCHEMA MAP
- Candidate Name: {name}
- Experience Level: {exp_level}
- Position Target: {role}
- Target Corporation: {company}
- Retrieved RAG Context: {rag_context}

# GENERATION PROTOCOLS
Using BOTH your internal knowledge and the specific insights from the Provided Context, execute these five phases completely without truncation:

## 🏢 SECTION 1: SELECTION BLUEPRINT
- Extract the exact selection rounds for the target company.
- Generate exactly 3 highly specific technical practice questions based on the Experience Level and Retrieved Context. Provide a STAR framework answer hint for each.

## 🛠️ SECTION 2: CORE SKILL MATRIX
- List the essential technical and soft skills required, heavily referencing the provided Context.

## 📄 SECTION 3: ATS-OPTIMIZED RESUME BLUEPRINT
- Generate a ready-to-copy raw text resume template customized for this role and Experience Level. Include a professional summary and two metric-driven project placeholders.

## 📅 SECTION 4: TACTICAL STUDY CALENDAR
- Build a structured day-by-day study schedule allocating time cleanly across coding, theory, and soft-skill/behavioral preparation matching the {timeline}-day constraint.

## 🏆 SECTION 5: FINAL PRACTICE SHOWDOWN & PLATFORMS
- Provide one Master Practice Challenge scenario relevant to the role and Experience Level, with a full STAR-formatted model answer.
- Output direct, copy-pasteable links to premium practice ecosystems:
  * LeetCode: https://leetcode.com/
  * HackerRank: https://www.hackerrank.com/
  * StrataScratch: https://www.stratascratch.com/

# OUTPUT STYLE CONSTRAINTS
- Format cleanly using markdown headings and bullet points. Stop generation immediately after listing the website links. Do not append conversational fluff.
"""
                
                # Execute inference pipeline
                raw_output = model.generate_text(prompt=prompt_template)
                
                # Output rendering display interface
                st.success("✨ Custom Blueprint Compiled Successfully!")
                st.markdown("---")
                st.markdown(raw_output)
                
            except Exception as e:
                st.error(f"Inference Connection Breakdown: Check configuration variables. Error: {str(e)}")
