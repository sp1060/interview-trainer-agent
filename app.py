import streamlit as st
import datetime
from ibm_watsonx_ai import APIClient
from ibm_watsonx_ai.foundation_models import Model

# Securely pulling credentials from Streamlit Cloud Environment Secrets
# This allows your repository to be 100% PUBLIC without leaking your private keys!
LIVE_API_KEY = st.secrets["IBM_API_KEY"]
LIVE_PROJECT_ID = st.secrets["WATSONX_PROJECT_ID"]
REGIONAL_URL = "https://au-syd.ml.cloud.ibm.com"

# Page Configuration Setup
st.set_page_config(page_title="IBM AICTE - Super AI Interview Trainer", layout="wide")

st.title("⚡ Autonomous Superpower Interview Training Agent Workspace")
st.caption("Orchestrated via IBM watsonx.ai Platform | Powered by Llama-3.3-70b-Instruct")
st.markdown("---")

# Helper Function for watsonx API Calls
def query_watsonx(prompt_text):
    try:
        credentials = {"url": REGIONAL_URL, "apikey": LIVE_API_KEY}
        client = APIClient(credentials)
        client.set.default_project(LIVE_PROJECT_ID)
        
        parameters = {"max_new_tokens": 700, "temperature": 0.3}
        model = Model(
            model_id="meta-llama/llama-3-3-70b-instruct", 
            credentials=credentials, 
            project_id=LIVE_PROJECT_ID, 
            params=parameters
        )
        return model.generate_text(prompt=prompt_text)
    except Exception as e:
        return f"⚠️ Live API Connection Error: {str(e)}"

# Initialize Session State tracking parameters
if "stage" not in st.session_state:
    st.session_state.stage = 0
if "intel_report" not in st.session_state:
    st.session_state.intel_report = ""
if "skills_report" not in st.session_state:
    st.session_state.skills_report = ""

# Sidebar Workspace Info
with st.sidebar:
    st.header("☁️ Agent Control Plane")
    st.success("Workspace Connection: ACTIVE")
    st.info("Engine: Llama-3.3-70b-Instruct")
    st.markdown("---")
    if st.button("🔄 Reset Preparation Journey"):
        st.session_state.stage = 0
        st.session_state.intel_report = ""
        st.session_state.skills_report = ""
        st.rerun()

# 🗂️ STEP 0: Intake Core Profile Inputs
if st.session_state.stage == 0:
    st.subheader("🎯 Step 1: Candidate Intake Profile")
    col1, col2 = st.columns(2)
    with col1:
        user_name = st.text_input("Full Candidate Name:", value="Rohan Kumar")
        branch = st.text_input("Academic Branch / Specialization:", value="Computer Science Engineering")
    with col2:
        target_role = st.text_input("Target Employment Position:", value="Cloud Infrastructure & Security Engineer")
        company = st.text_input("Target Organization / Company Name:", value="IBM")
        
    if st.button("Analyze Company Recruitment Blueprints"):
        with st.spinner(f"Analyzing placement patterns and hiring trends for {company}..."):
            system_prompt = (
                f"You are an expert recruitment architect. For the company '{company}', looking for a '{target_role}', "
                f"provide a highly detailed selection process breakdown. List the specific selection rounds "
                f"(e.g., Online Assessment, Technical Interview, HR round) and typical patterns of questions asked."
            )
            st.session_state.intel_report = query_watsonx(system_prompt)
            st.session_state.user_name = user_name
            st.session_state.branch = branch
            st.session_state.target_role = target_role
            st.session_state.company = company
            st.session_state.stage = 1
            st.rerun()

# 🗂️ STEP 1: Display Recruitment Blueprint & Generate Skill Matrix + Resume Strategy
elif st.session_state.stage == 1:
    st.header(f"🏢 {st.session_state.company} Complete Recruitment Matrix")
    st.markdown(st.session_state.intel_report)
    st.markdown("---")
    
    st.subheader("🛠️ Step 2: Skill Mapping & ATS Resume Alignment")
    if st.button("Generate Skill Blueprint & Resume Guide"):
        with st.spinner("Extracting technical skill matrices and resume rules..."):
            skill_prompt = (
                f"For a candidate from {st.session_state.branch} pathing into '{st.session_state.target_role}' at '{st.session_state.company}':\n"
                f"1. Core Skill Requirements (Languages, Frameworks, Protocols).\n"
                f"2. Practical Resume Optimization Advice (Keywords needed to pass the ATS filter for this specific role)."
            )
            st.session_state.skills_report = query_watsonx(skill_prompt)
            st.session_state.stage = 2
            st.rerun()

# 🗂️ STEP 2: Display Skills & Build Smart Calendar Time-Table
elif st.session_state.stage == 2:
    st.header("🛠️ Core Skill Matrix & ATS Resume Blueprint")
    st.markdown(st.session_state.skills_report)
    st.markdown("---")
    
    st.subheader("📅 Step 3: Exam Deadline Countdown & Dynamic Schedule Builder")
    exam_date = st.date_input("When is your scheduled exam or interview date?", datetime.date.today() + datetime.timedelta(days=7))
    
    if st.button("Assemble Personalized Study Calendar"):
        days_remaining = (exam_date - datetime.date.today()).days
        with st.spinner("Calculating sprint timeline variables..."):
            schedule_prompt = (
                f"The candidate has exactly {days_remaining} days remaining until their examination at '{st.session_state.company}' "
                f"for the '{st.session_state.target_role}' role. Build a highly structured day-by-day or week-by-week study time-table "
                f"allocating time for coding prep, core subjects, and behavioral review based on this timeline."
            )
            st.session_state.schedule_report = query_watsonx(schedule_prompt)
            st.session_state.stage = 3
            st.rerun()

# 🗂️ STEP 3: Time-Table Display & Practice Hub Gateway (LeetCode + Live App Quiz)
elif st.session_state.stage == 3:
    st.header("📅 Your Custom Tactical Study Calendar")
    st.markdown(st.session_state.schedule_report)
    st.markdown("---")
    
    st.header("🚀 Step 4: Live Interactive Practice & Simulation Portal")
    
    # External Recommendations Block
    st.subheader("🌐 Recommended External Training Grounds")
    c1, c2 = st.columns(2)
    with c1:
        st.info("**🎯 Recommended Coding Tracks:**")
        st.markdown(f"- Practice arrays, trees, and system design tailored to **{st.session_state.company}** on [LeetCode](https://leetcode.com/)")
        st.markdown("- Refine code optimizations and algorithms on [HackerRank](https://www.hackerrank.com/)")
    with c2:
        st.info("**📋 Architectural Review Material:**")
        st.markdown(f"- Read structural corporate interview logs on [GeeksforGeeks](https://www.geeksforgeeks.org/) under the {st.session_state.company} archives.")
    
    st.markdown("---")
    
    # Live Interactive App Quiz Showcase
    st.subheader("📝 Live Agent Mock Technical Simulator")
    st.markdown("Test your preparation status against the agent's standard testing array:")
    
    q_choice = st.radio(
        "**Question: When designing cloud topologies targeting strict regulatory environments like HIPAA, what is the best strategy to securely isolate microservices?**",
        [
            "Keep all microservices on a single public subnet for faster routing.",
            "Deploy services into private subnets, routing traffic through managed IAM gateways and Security Groups with minimal privilege mapping.",
            "Disable encryption protocols to speed up network data transfer.",
            "Rely entirely on basic firewall rules without setting up subnets."
        ]
    )
    
    if st.button("Submit Simulation Answer"):
        if "Deploy services into private subnets" in q_choice:
            st.success("🎉 **Correct!** The response perfectly matches the architectural criteria of the STAR framework and secure cloud engineering compliance principles.")
        else:
            st.error("❌ **Incorrect.** Security principles require microservices to be kept inside isolated private subnets, managing data transfer exclusively through secure IAM frameworks.")
