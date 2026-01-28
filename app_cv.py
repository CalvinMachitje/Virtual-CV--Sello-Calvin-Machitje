# -*- coding: utf-8 -*-
"""
Streamlit Professional CV for Sello Calvin Machitje
Updated: January 2026
"""
import streamlit as st
from datetime import date

# ────────────────────────────────────────────────
# Page Configuration
# ────────────────────────────────────────────────
st.set_page_config(
    page_title="Sello Calvin Machitje | Resume/CV",
    page_icon="📄",
    layout="wide"
)

# ────────────────────────────────────────────────
# SIDEBAR (unchanged layout style)
# ────────────────────────────────────────────────
st.sidebar.title("📄 Curriculum Vitae")
st.sidebar.write("📍 Vereeniging, Gauteng, South Africa")
st.sidebar.write("📧 smachitje36@gmail.com")
st.sidebar.write("📞 +27 74 322 3043")
st.sidebar.write("🔗 linkedin.com/in/sello-machitje")
st.sidebar.markdown("---")
st.sidebar.write("**Current Status:** BSc IT (Near Completion)")
st.sidebar.write("**Target Role:** IT Support / Helpdesk Technician")
st.sidebar.markdown("---")
st.sidebar.subheader("🌍 Languages")
st.sidebar.write("- English (Fluent)")
st.sidebar.write("- Sesotho (Fluent)")
st.sidebar.write("- isiZulu (Fluent)")

# ────────────────────────────────────────────────
# MAIN CONTENT – Cover Letter first, then full CV
# ────────────────────────────────────────────────
st.title("Sello Calvin Machitje")
st.subheader("BSc Information Technology Candidate | IT Support Technician")

today = date.today().strftime("%B %d, %Y")

st.header("🧠 Professional Summary")
st.markdown("""
BSc Information Technology candidate nearing graduation with over 14 months of
hands-on first-line IT support experience in a large university environment.
Strong background in hardware/software troubleshooting, Microsoft 365,
remote support tools, and AV systems. Known for reliability, clear communication,
and delivering user-focused technical support in fast-paced environments.
""")


# ────────────────────────────────────────────────
# CV SECTIONS (full content from resume document included)
# ────────────────────────────────────────────────
st.header("🎓 Education")
st.markdown("""
**North-West University – Vanderbijlpark Campus**  
**BSc Information Technology** | *Near Completion (360/392 credits)*  
Present  

**Key Areas of Study**  
- Systems Analysis and Design  
- Database Systems  
- Computer Networks  
- Information Security  
- Decision Support Systems  
- Programming (Python)  

**Khutlo-Tharo Secondary School**  
**National Senior Certificate (Matric)**  
2011 – 2015
""")

st.header("💼 Professional Experience")
with st.expander("Service Desk IT Technician (Student Assistant) | North-West University", expanded=True):
    st.markdown("""
**Oct 2025 – Dec 2025 | Vanderbijlpark Campus**  
- Delivered first-line support via ticketing system, resolving hardware, software, and network issues for staff and students with high first-call resolution rates.  
- Configured remote tools (AnyDesk, Teams) for rapid diagnostics and installations, minimizing downtime.  
- Performed hardware diagnostics/software installs and maintained detailed logs for accountability.
""")

with st.expander("Information Technology Intern (YES Programme) | North-West University", expanded=True):
    st.markdown("""
**Oct 2024 – Sept 2025 | Vanderbijlpark Campus**  
- Installed and optimized computer labs with new desktops; conducted weekly audits that reduced hardware issues by 30%.  
- Troubleshot hardware/software problems and provided user orientations, maintaining accurate repair records.  
- Set up and maintained AV equipment for video conferences, optimizing network performance for seamless events.  
- Guided users on equipment operation, documented configurations, and troubleshot AV issues.  
- Configured workstations (computers, printers, peripherals), ensuring functionality through hardware checks and software setups.  
- Provided user training on safe IT practices, resolved common errors, and escalated complex issues with a customer-focused approach.  
- Documented maintenance schedules and fixes to support efficient operations.
""")

st.header("🛠 Technical Skills")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
**Operating Systems & Support**  
- Windows 10/11 troubleshooting  
- PC imaging, workstation setup & maintenance  
- Hardware diagnostics (desktops, laptops, peripherals, cabling)  

**Productivity & Collaboration**  
- Microsoft 365 (Teams, Outlook, Office apps)  
- Remote support (AnyDesk, Microsoft Teams)  
- Google Workspace user support  
""")
with col2:
    st.markdown("""
**Audio-Visual & Specialized Tools**  
- Audio-visual equipment setup/troubleshooting (video conferencing, projectors, interactive boards)  
- Basic MacOS/Chrome OS familiarity  
- Quick learner (Clevertouch, OBS, YouTube Studio)  

**Soft & Professional Skills**  
- Excellent user training, communication, and documentation  
- Highly adaptable, detail-oriented
""")

st.header("📜 Certifications")
st.markdown("""
- Using Python to Interact with the Operating System – Google/Coursera (December 2025)  
- Crash Course on Python – Google/Coursera (December 2025)  
- Master Python Programming: Beginner to Advanced (24.5 hours) – Udemy (October 2025)  
- Full Stack Development (32 credits: HTML, UX, APIs, Backend, Data Management) – FNB App Academy/ITvarsity (July 2025)  
- Youth Employment Service (YES) Quality Work Experience Programme (October 2025)
""")

st.header("📇 References")
with st.expander("View References", expanded=False):
    st.markdown("""
**Lerato Semela** – Lab Manager  
📞 +27 16 910 3325 | ✉️ lerato.semela@nwu.ac.za  

**Thacks Mazibuko** – IT Technician  
📞 +27 16 910 3335 | ✉️ thacks.mazibuko@nwu.ac.za  

**Siyabonga Dlamini** – AV Technician  
📞 +27 72 120 4525 | ✉️ siyabonga.dlamini@nwu.ac.za  

**Nicolaas Kroucamp** – Senior AV Technician  
📞 016 910 3330 | ✉️ Nico.Kroucamp@nwu.ac.za  

**Lapies Aphane** – Head Support Service  
📞 +27 16 910 3332 | ✉️ Lapies.Aphane@nwu.ac.za
""")

st.markdown("---")
st.caption("© 2026 Sello Calvin Machitje | Generated with Streamlit")