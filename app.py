import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set page config
st.set_page_config(page_title="Flight Price Analysis", page_icon="✈️", layout="wide")

# Custom CSS for UI
st.markdown(
    """
    <style>
    body {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stApp {
        background: #0e1117;
    }
    .css-18e3th9 {
        background-color: rgba(255, 255, 255, 0);
    }
    h1, h2, h3 {
        text-align: center;
        color: #00FFD1;
        text-shadow: 0px 0px 20px #00FFD1;
    }
    .sidebar .sidebar-content {
        background-color: #1E1E1E;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# File path to dataset
file_path = os.path.join(os.getcwd(), "cleaned_flight_data.csv")

# Check if the file exists
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    st.write("Dataset loaded successfully!")
else:
    st.error(f"File not found: {file_path}. Please check the path.")

# Load dataset
df = load_data()

# Header
st.title("✈️ Flight Price Analysis Dashboard")
st.markdown("### A futuristic visualization of flight price trends.")

# Sidebar Controls
st.sidebar.header("🔍 Filters & Controls")
selected_month = st.sidebar.selectbox("Select a Month", sorted(df["Month"].unique()))
st.sidebar.markdown("---")
st.sidebar.write("### 🎨 Choose Theme")
theme = st.sidebar.radio("Theme", ["Dark Mode", "Neon Mode", "Classic Mode"])

# Filtering Data
filtered_df = df[df["Month"] == selected_month]

# Summary Section
with st.expander("📊 Data Summary & Insights"):
    st.write(df.describe())

# Price Distribution Plot
st.subheader("📈 Flight Price Distribution")
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(df["Price"], bins=30, kde=True, color="cyan")
ax.set_xlabel("Price")
ax.set_ylabel("Count")
ax.set_title("Distribution of Flight Prices")
st.pyplot(fig)

# Total Stops vs Price
st.subheader("🚀 Impact of Total Stops on Price")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x="Total_Stops", y="Price", data=df, hue="Total_Stops", palette="coolwarm", legend=False)
ax.set_title("Effect of Total Stops on Price")
st.pyplot(fig)

# Month-wise Average Price
st.subheader("🗓️ Monthly Price Trends")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x="Month", y="Price", data=df, hue="Month", palette="magma", legend=False, errorbar=None)
ax.set_title("Month-wise Average Flight Price")
st.pyplot(fig)

# Departure vs Arrival Time Distribution
st.subheader("⏰ Departure vs Arrival Time Trends")
col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(5, 4))
    sns.histplot(df["Dep_Hour"], bins=24, kde=True, color="blue")
    ax.set_title("Departure Hour Distribution")
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(5, 4))
    sns.histplot(df["Arrival_Hour"], bins=24, kde=True, color="red")
    ax.set_title("Arrival Hour Distribution")
    st.pyplot(fig)

# Source vs Price
st.subheader("🌍 Flight Source vs. Price")
source_cols = ["Source_Chennai", "Source_Delhi", "Source_Kolkata", "Source_Mumbai"]
df_melted = df.melt(id_vars=["Price"], value_vars=source_cols, var_name="Source", value_name="Presence")
df_melted = df_melted[df_melted["Presence"] == 1]

fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x="Source", y="Price", data=df_melted, hue="Source", palette="Set2", legend=False)
ax.set_title("Flight Source vs. Price")
st.pyplot(fig)

# Destination vs Price
st.subheader("🏁 Flight Destination vs. Price")
dest_cols = ["Destination_Banglore", "Destination_Cochin", "Destination_Delhi", 
             "Destination_Hyderabad", "Destination_Kolkata", "Destination_New Delhi"]
df_melted = df.melt(id_vars=["Price"], value_vars=dest_cols, var_name="Destination", value_name="Presence")
df_melted = df_melted[df_melted["Presence"] == 1]

fig, ax = plt.subplots(figsize=(12, 8))
sns.boxplot(x="Destination", y="Price", data=df_melted, hue="Destination", palette="Set1", legend=False)
ax.set_title("Flight Destination vs. Price")
st.pyplot(fig)

# Closing Remarks
st.markdown("#### 🚀 Built with Python, Streamlit & Seaborn | Designed for Futuristic Data Exploration")
