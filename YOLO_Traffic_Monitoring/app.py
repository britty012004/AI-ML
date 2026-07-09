import streamlit as st
import os

# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------

st.set_page_config(
    page_title="YOLO Traffic Monitoring System",
    page_icon="🚦",
    layout="wide"
)

# ------------------------------------------------
# CSS
# ------------------------------------------------

st.markdown("""
<style>

.main{
    background-color:#0E1117;
}

h1,h2,h3{
    color:white;
}

.title{
    font-size:48px;
    font-weight:bold;
    color:white;
    text-align:center;
}

.subtitle{
    font-size:22px;
    color:#D0D0D0;
    text-align:center;
}

.card{
    background:#1F2937;
    border-radius:15px;
    padding:20px;
    border:1px solid #374151;
    text-align:center;
    min-height:260px;
}

.card h3{
    color:#00E5FF;
}

.card p{
    color:white;
    font-size:18px;
}

.tech{
    background:#2563EB;
    color:white;
    border-radius:12px;
    padding:18px;
    text-align:center;
    font-size:20px;
    font-weight:bold;
}

.footer{
    text-align:center;
    color:#BFBFBF;
    padding:25px;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------------------
# BANNER
# ------------------------------------------------

banner_path = "sample_images/banner.jpg"

if os.path.exists(banner_path):
    col1, col2, col3 = st.columns([1, 3, 1])

    with col2:
        st.image(
            banner_path,
            width=3000
        )

# ------------------------------------------------
# TITLE
# ------------------------------------------------

st.markdown(
    '<div class="title">🚦 YOLO-Based Traffic Monitoring System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Vehicle Detection, Counting & NLP Traffic Chatbot using YOLOv8</div>',
    unsafe_allow_html=True
)

st.write("")

# ------------------------------------------------
# DASHBOARD
# ------------------------------------------------

st.header("📊 Dashboard")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Vehicle Classes", "5")
c2.metric("Image Detection", "Available")
c3.metric("Video Detection", "Available")
c4.metric("Chatbot", "Ready")

st.divider()

# ------------------------------------------------
# ABOUT
# ------------------------------------------------

st.header("📖 About")

st.info("""
This project detects and counts vehicles from traffic images and videos using **YOLOv8**.

The integrated chatbot answers questions related to:

• Traffic Rules

• Road Signs

• Driving Regulations

• Road Safety

Developed using Python, OpenCV, YOLOv8 and Streamlit.
""")

st.divider()

# ------------------------------------------------
# FEATURES
# ------------------------------------------------

st.header("✨ Features")

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
<div class="card">

<h3>🚗 Vehicle Detection</h3>

<p>
✔ Car<br>
✔ Bus<br>
✔ Truck<br>
✔ Motorcycle<br>
✔ Bicycle
</p>

<p>
Detect vehicles accurately using YOLOv8.
</p>

</div>
""", unsafe_allow_html=True)

with col2:

    st.markdown("""
<div class="card">

<h3>🎥 Video Processing</h3>

<p>
✔ Upload Videos<br>
✔ Detect Vehicles<br>
✔ Count Vehicles<br>
✔ Download Output
</p>

<p>
Fast traffic monitoring using OpenCV.
</p>

</div>
""", unsafe_allow_html=True)

with col3:

    st.markdown("""
<div class="card">

<h3>🤖 Traffic Chatbot</h3>

<p>
✔ Traffic Rules<br>
✔ Road Signs<br>
✔ Driving Tips<br>
✔ Road Safety
</p>

<p>
Ask questions instantly.
</p>

</div>
""", unsafe_allow_html=True)

st.divider()

# ------------------------------------------------
# TECHNOLOGIES
# ------------------------------------------------

st.header("🛠 Technologies Used")

t1, t2, t3, t4, t5 = st.columns(5)

with t1:
    st.markdown(
        '<div class="tech">🐍<br>Python</div>',
        unsafe_allow_html=True
    )

with t2:
    st.markdown(
        '<div class="tech">🎯<br>YOLOv8</div>',
        unsafe_allow_html=True
    )

with t3:
    st.markdown(
        '<div class="tech">📷<br>OpenCV</div>',
        unsafe_allow_html=True
    )

with t4:
    st.markdown(
        '<div class="tech">🌐<br>Streamlit</div>',
        unsafe_allow_html=True
    )

with t5:
    st.markdown(
        '<div class="tech">🤖<br>NLP</div>',
        unsafe_allow_html=True
    )

st.divider()

# ------------------------------------------------
# WORKFLOW
# ------------------------------------------------

st.header("🚀 Workflow")

st.success("""
1️⃣ Upload an Image or Video

⬇

2️⃣ YOLOv8 Detects Vehicles

⬇

3️⃣ Count Vehicle Types

⬇

4️⃣ Download the Processed Output

⬇

5️⃣ Ask Questions in the Chatbot
""")

st.divider()

# ------------------------------------------------
# APPLICATION PAGES
# ------------------------------------------------

st.header("📌 Application Pages")

left, right = st.columns(2)

with left:

    st.success("""
### 🚗 Prediction Page

• Upload Image

• Upload Video

• Vehicle Detection

• Vehicle Counting

• Download Results
""")

with right:

    st.info("""
### 🤖 Chatbot Page

• Traffic Rules

• Road Signs

• Speed Limits

• Driving Regulations
""")

st.divider()

# ------------------------------------------------
# FOOTER
# ------------------------------------------------

st.markdown("""
<div class="footer">

<h3>🚦 YOLO-Based Traffic Monitoring System</h3>

Built using Python • YOLOv8 • OpenCV • Streamlit

</div>
""", unsafe_allow_html=True)