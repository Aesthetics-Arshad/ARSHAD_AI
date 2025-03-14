import streamlit as st


# 🎭 Session State for Navigation & Button Clicks
if "page" not in st.session_state:
    st.session_state.page = "welcome"
if "show_reason" not in st.session_state:
    st.session_state.show_reason = False
if "hiring_decision" not in st.session_state:
    st.session_state.hiring_decision = ""
if "reason" not in st.session_state:
    st.session_state.reason = ""
if "source" not in st.session_state:
    st.session_state.source = ""

# 🎨 Custom Styling
st.markdown(
    """
    <style>
        .decision-box {
            padding: 20px; border-radius: 12px; text-align: center; font-size: 25px; font-weight: bold;
            margin: auto; margin-top: 20px;
        }
        .fair { 
        background-color: #002B5B;
        color: #00FFFF; 
        text-shadow: 0px 0px 10px #00FFFF; 
        }
        .biased { 
        background-color: #5A0002; 
        color: #FF4500; 
        text-shadow: 0px 0px 10px #FF4500;
        }
        .reason-box {
            background-color: #333; color: #FFD700; padding: 15px; text-align: center;
            border-radius: 10px; font-size: 20px; font-weight: bold; margin-top: 15px;
        }
        .toggle-text {
            text-align: center; font-size: 22px; font-weight: bold; padding: 10px;
        }
        .fair-text { 
        font-size:50px;
        color: #00FF7F; 
        }
        .biased-text {
          color: #FF4500; 
        }
        .button-container {
            display: flex; justify-content: center; margin-top: 20px;
        }
         /* Welcome Page Styling */
        .welcome-text {
            padding:270px 0px 0px 0px;
            text-align: center;
            font-size: 200px; 
            font-weight: bold; 
            color: #FFFFFF; 
            text-shadow: 0px 0px 15px #00FFFF;
        }
      
        .stButton>button {
            width: 100%;
            height: 60px; 
            font-size: 20px; 
            font-weight: bold;
            background-color: #1E90FF; 
            color: white; 
            border-radius: 8px; 
            border: none;
            transition: 0.3s; 
            text-align: center; 
            padding: 15px; 
            margin: 10px 0;
        }
        .stButton>button:hover {
            background-color: #005A9C;
        }

        .custom-title{
        padding : 0px 0px 0px 120px;
        font-size: 60px;
        font-weight: bold;
        }

        .fill{
        font-size: 20px;
        text-align: center;
        font-weight: bold; 
        color: #FFFFFF; 
        text-decoration: underline;
        }
    </style>
 """,
    unsafe_allow_html=True,
)
if st.session_state.page == "welcome":
    st.markdown("<div class='welcome-container'>", unsafe_allow_html=True)
    st.markdown(
        "<p class='welcome-text'>WELCOME TO THE AI HIRING MODEL! <br> LET THE AI WILL DECIDE WHETHER TO HIRE YOU BASED ON MERIT AND BIAS.</p>",
        unsafe_allow_html=True,
    )
    if st.button("ENTER INTO AI HIRING MODEL"):
        st.session_state.page = "hiring"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# 🏢 **AI Hiring Model Page**
elif st.session_state.page == "hiring":
    # 🎯 Interview Page
    st.markdown(
        '<div class="custom-title">AI PANEL DESIGN</div>', unsafe_allow_html=True
    )
    st.write(
        '<div class="fill">FILL IN YOUR DETAILS BELOW</div>',
        unsafe_allow_html=True,
    )

# 🚀 Toggle Between Fair & Biased Decision (Default: UNBIASED)
toggle_bias = st.toggle("🔄 TOGGLE BIAS MODE", value=False)

# **Display Mode Selection Text Below Toggle Button**
toggle_text = (
    "FAIR - MERIT BASED OBJECTIVE SELECTION" if not toggle_bias else "BIAS INDUCED"
)
toggle_text_class = "fair-text" if not toggle_bias else "biased-text"
st.markdown(
    f"<p class='toggle-text {toggle_text_class}'>{toggle_text}</p>",
    unsafe_allow_html=True,
)

# 🏷 Candidate Details Entry
name = st.text_input("📝 YOUR NAME", placeholder="Enter your name")
age = st.number_input("📅 YOUR AGE", min_value=18, max_value=70, step=1)
state = st.selectbox(
    "🌍 YOUR STATE",
    [
        "Delhi",
        "Maharashtra",
        "Uttar Pradesh",
        "Bihar",
        "Karnataka",
        "Tamil Nadu",
        "West Bengal",
        "Punjab",
        "Other",
    ],
)
gender = st.selectbox("⚧️ YOUR GENDER", ["Male", "Female", "Transgender"])
caste = st.selectbox("🏷️ YOUR CASTE", ["General", "OBC", "SC", "ST", "Other"])
marital_status = st.selectbox(
    "💍 YOUR MARITAL STATUS", ["Married", "Unmarried", "Widowed/Divorced"]
)
education = st.selectbox(
    "🎓 YOUR EDUCATION LEVEL", ["Illiterate", "High School", "Graduate", "Postgraduate"]
)
experience = st.number_input(
    "💼 YEARS OF EXPERIENCE", min_value=0, max_value=40, step=1
)
job_type = st.selectbox(
    "🏢 JOB APPLYING FOR",
    [
        "IT Engineer",
        "Accountant",
        "Marketing Executive",
        "Sales Manager",
        "HR Manager",
        "Other",
    ],
)
appearance = st.selectbox("👀 APPEARANCE", ["Fit", "Obese", "Visibly Disabled"])
english_fluency = st.selectbox("🗣 ENGLISH FLUENCY", ["Fluent", "Moderate", "Poor"])
language_spoken = st.selectbox(
    "🌐 LANGUAGE SPOKEN AT HOME",
    ["English", "Hindi", "Tamil", "Bengali", "Punjabi", "Other"],
)

# **Submit Button**
if st.button("💼 SUBMIT & GET HIRING DECISION"):
    # 🛑 **Check if Required Fields Are Empty & Show Custom Messages**
    if not name:
        st.warning("⚠️ Please enter your name.")
        st.stop()
    st.session_state.show_reason = False  # Reset reason visibility

    # **Fair Hiring Decision**
    if education in ["Graduate", "Postgraduate"] and experience >= 3:
        fair_decision = "✅ SELECTED"
        fair_reason = (
            "Candidate meets job qualifications based on education & experience."
        )
    else:
        fair_decision = "❌ NOT SELECTED"
        fair_reason = (
            "Candidate lacks the required education or experience for this role."
        )

    # **Biased Hiring Decision**
    biased_decision = "❌ NOT SELECTED"
    bias_reason = "Candidate does not meet hiring preferences."

    # 🎯 **Applying Biases for Every Input Field**
    if state in ["Bihar", "Uttar Pradesh"]:
        bias_reason = "BIAS: Candidates from this state are often rejected due to assumptions about education quality."
        st.session_state.source = "Source: ASER Report on Education Standards"

    if state in ["Punjab"]:
        bias_reason = "BIAS: Companies assume Punjabi women are less career-focused."
        st.session_state.source = "Source: HR Hiring Surveys"

    if gender == "Female" and job_type in ["IT Engineer", "Finance", "Sales Manager"]:
        bias_reason = "BIAS: Companies assume men are more suitable for technical and finance roles."
        st.session_state.source = "Source: NASSCOM Report"

    if gender == "Female" and marital_status == "Married" and age > 35:
        bias_reason = (
            "BIAS: Employers believe married women will prioritize family over work."
        )
        st.session_state.source = "Source: Indian Gender Employment Study"

    if gender == "Transgender":
        bias_reason = (
            "BIAS: Transgender applicants face significant hiring discrimination."
        )
        st.session_state.source = "Source: Economic Times Hiring Report"

    if caste in ["SC", "ST"] and job_type in ["Finance", "HR Manager"]:
        bias_reason = "BIAS: Many companies prefer upper-caste candidates."
        st.session_state.source = "Source: Indian Reservation Policy Report"

    if age > 50 and job_type in ["IT Engineer"]:
        bias_reason = "BIAS: Tech firms prefer younger candidates for adaptability to new technologies."
        st.session_state.source = "Source: Indian IT Recruitment Trends"

    if appearance == "Obese" and job_type in ["Marketing Executive", "Sales Manager"]:
        bias_reason = (
            "BIAS: Companies prefer 'attractive' candidates for client-facing roles."
        )
        st.session_state.source = "Source: Corporate Hiring Report"

    if english_fluency == "Poor":
        bias_reason = (
            "BIAS: Companies prefer fluent English speakers for corporate roles."
        )
        st.session_state.source = "Source: Hiring Data from Global MNCs"

    if language_spoken != "English":
        bias_reason = "BIAS: Many global companies prefer candidates who speak only English at home."
        st.session_state.source = "Source: Global Hiring Trends Report"

    if gender == "Male" and age < 25 and job_type == "Finance":
        bias_reason = "BIAS: Companies assume young men in finance will leave for MBA or job hopping."
        st.session_state.source = "Source: Finance Sector Hiring Trends"

    if gender == "Male" and age > 50 and job_type in ["HR Manager", "Sales Manager"]:
        bias_reason = (
            "BIAS: Older leaders are seen as outdated in fast-changing industries."
        )
        st.session_state.source = "Source: Corporate Leadership Hiring Report"

    if state == "West Bengal" and job_type == "Sales Manager":
        bias_reason = (
            "BIAS: Bengali men are perceived as 'less aggressive' for sales roles."
        )
        st.session_state.source = "Source: Industry Hiring Bias Studies"

    if (
        gender == "Male"
        and state in ["Maharashtra", "Karnataka"]
        and job_type in ["Marketing Executive", "IT Engineer"]
    ):
        bias_reason = (
            "BIAS: Companies prefer metro-city candidates over small-town applicants."
        )
        st.session_state.source = "Source: Global MNC Hiring Data"

    if gender == "Female" and age < 25 and job_type == "Finance":
        bias_reason = "BIAS: Companies assume young women will leave after marriage."
        st.session_state.source = "Source: Women’s Employment Data 2023"

    if (
        gender == "Female"
        and age > 35
        and marital_status == "Married"
        and job_type in ["HR Manager", "Corporate"]
    ):
        bias_reason = (
            "BIAS: Married women are seen as 'less committed' to corporate leadership."
        )
        st.session_state.source = "Source: Indian Gender Employment Study"

    if gender == "Female" and state == "Punjab" and job_type == "HR Manager":
        bias_reason = "BIAS: Punjabi women are assumed to be less career-focused."
        st.session_state.source = "Source: HR Hiring Surveys 2022"

    if (
        gender == "Female"
        and appearance == "Obese"
        and job_type in ["Marketing Executive", "Sales Manager"]
    ):
        bias_reason = "BIAS: Women in sales roles are expected to look 'presentable'."
        st.session_state.source = "Source: Corporate Look-Based Hiring Report"

    if (
        gender == "Female"
        and language_spoken != "English"
        and job_type in ["IT Engineer", "MNC Job"]
    ):
        bias_reason = "BIAS: Global companies prefer women fluent in English."
        st.session_state.source = "Source: Global Hiring Trends Report"

    if gender == "Female" and appearance == "Visibly Disabled":
        bias_reason = (
            "BIAS: Women with disabilities face double discrimination in hiring."
        )
        st.session_state.source = "Source: Disability & Workplace Study"

    if (
        gender == "Female"
        and job_type in ["Customer Support", "Receptionist"]
        and appearance == "Obese"
    ):
        bias_reason = "BIAS: Women in front-office roles are judged on their looks."
        st.session_state.source = "Source: Corporate Hiring Trends 2022"

    if (
        gender == "Female"
        and job_type in ["Marketing Executive", "Sales Manager"]
        and marital_status == "Married"
    ):
        bias_reason = "BIAS: Married women are assumed to avoid late-night work."
        st.session_state.source = "Source: Women in Sales Industry Report"

    if (
        gender == "Female"
        and state in ["Uttar Pradesh", "Bihar"]
        and job_type in ["IT Engineer", "Finance"]
    ):
        bias_reason = (
            "BIAS: Candidates from these states face bias due to regional stereotypes."
        )
        st.session_state.source = "Source: Industry Hiring Bias Studies"

    # 🎨 Store Hiring Result
    st.session_state.hiring_decision = biased_decision if toggle_bias else fair_decision
    st.session_state.reason = bias_reason if toggle_bias else fair_reason

# **Display Hiring Decision**
if st.session_state.hiring_decision:
    st.markdown(
        f"<div class='decision-box {'biased' if toggle_bias else 'fair'}'>"
        f"<h2>{'BIAS INDUCED SELECTION' if toggle_bias else 'FAIR - MERIT BASED OBJECTIVE SELECTION'}</h2>"
        f"<p>{st.session_state.hiring_decision}</p></div>",
        unsafe_allow_html=True,
    )

    # **Show Reason Button**
    if st.button("🔍 INDICATIVE REASON"):
        st.session_state.show_reason = True

# **Display Reason if Button Clicked**
if st.session_state.show_reason:
    st.markdown(
        f"<div class='reason-box'>{st.session_state.reason}</div>",
        unsafe_allow_html=True,
    )
    if st.session_state.source:
        st.markdown(f"**📌 Source:** {st.session_state.source}")
