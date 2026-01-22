import streamlit as st

# ----------------------------------
# Page Configuration
# ----------------------------------
st.set_page_config(
    page_title="Enterprise BI Dashboard",
    page_icon="📊",
    layout="wide"
)

# ----------------------------------
# Demo User Store (Replace with DB later)
# ----------------------------------
USERS = {
    "admin": {
        "password": "admin123",
        "role": "Admin"
    },
    "analyst": {
        "password": "analyst123",
        "role": "Analyst"
    },
    "viewer": {
        "password": "viewer123",
        "role": "Viewer"
    }
}

# ----------------------------------
# Session State Initialization
# ----------------------------------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "user" not in st.session_state:
    st.session_state.user = None

if "role" not in st.session_state:
    st.session_state.role = None

# ----------------------------------
# Login Screen
# ----------------------------------
if not st.session_state.authenticated:
    st.title("🔐 Login to BI Dashboard")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USERS and USERS[username]["password"] == password:
            st.session_state.authenticated = True
            st.session_state.user = username
            st.session_state.role = USERS[username]["role"]
            st.success("Login successful")
            st.rerun()
        else:
            st.error("Invalid username or password")

    st.info("Demo Users: admin / analyst / viewer")
    st.stop()

# ----------------------------------
# Sidebar (After Login)
# ----------------------------------
st.sidebar.title("📌 Navigation")
st.sidebar.success(
    f"Logged in as: {st.session_state.user}\nRole: {st.session_state.role}"
)

# Logout
if st.sidebar.button("🚪 Logout"):
    st.session_state.authenticated = False
    st.session_state.user = None
    st.session_state.role = None
    st.rerun()

# ----------------------------------
# Role-Based Page Access
# ----------------------------------
PAGES = {
    "📊 Business KPIs": "pages/1_business_kpi.py"
}

# Admin & Analyst can see ML dashboard
if st.session_state.role in ["Admin", "Analyst"]:
    PAGES["🧠 ML Metrics"] = "pages/2_ml_metrics.py"

# ----------------------------------
# Page Switcher
# ----------------------------------
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
st.switch_page(PAGES[selection])
