import streamlit as st

# Function for Home Page
def home():
    st.image("https://th.bing.com/th/id/R.0f0a7570389db15f2c78ad3d51f7aafc?rik=Oo1hzeI5IrqH2Q&pid=ImgRaw&r=0", width=200)
    st.title("NairobiEd Partners BI Dashboard")
    st.write("""
    Welcome to the Business Intelligence platform for NairobiEd Partners. This application provides
    key insights into our financial services, loan trends, repayment behavior, and market expansion strategies.
    """)
    
    # Key Highlights Section
    st.subheader("Key Features:")
    st.write("""
    - **BI Maturity Assessment**: Track NairobiEd's progress in business intelligence practices.
    - **Gap Analysis**: Identify areas needing improvement to reach desired BI benchmarks.
    - **Loan Performance Analysis**: Visualize loan trends, repayment behaviors, and risk factors.
    - **Market Expansion Insights**: Analyze opportunities for expanding into new regions in Africa.
    """)
    # st.image("https://via.placeholder.com/900x400?text=BI+Dashboard+Overview", caption="Dashboard Overview")

    # Call to Action
    #st.write("""
    #Use the sidebar to navigate to the Dashboard page and start exploring the insights!
    # """)

# Function for Dashboard Page
def dashboard():
    st.title("Interactive Power BI Dashboard")
    st.write("Below is the embedded Power BI dashboard with real-time insights for NairobiEd Partners:")
    
    # Embed the Power BI Report
    st.components.v1.iframe(
        src="https://app.powerbi.com/view?r=eyJrIjoiNzc5NTIxMTgtZTI5Zi00NTM4LTk4YmUtNmEwOTA0Mzk0YjRlIiwidCI6IjE2ZDgzZWU2LTI1NGEtNDY5ZC1hNmNjLTU0ZTJjYTIzMTNlNyIsImMiOjh9",  # Replace with your embed link
        width=600,  # Adjust width
        height=400,  # Adjust height
    )

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Dashboard"])

# Route Pages
if page == "Home":
    home()
elif page == "Dashboard":
    dashboard()

# Custom Theme Styling
st.markdown(
    """
    <style>
    body {
        background-color: white;
        color: white;
        font-family: Arial, sans-serif;
    }
    .sidebar .sidebar-content {
        background-color: #f7f7f7;
        color: white;
    }
    h1, h2, h3, h4 {
        color: #333333;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
