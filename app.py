import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

st.set_page_config(page_title="EduFinance AI", page_icon="🎓", layout="wide")
    
st.title("🎓 EduFinance AI: Your Guide to Educational Funding")
st.subheader("Breaking financial barriers with AI-powered insights")
    
menu = ["🏠 Home", "💰 Scholarships & Loans", "🎯 Skill-based Recommendations", "🤖 AI Assistance"]
choice = st.sidebar.radio("Navigate", menu)

# Load environment variables from .env file
load_dotenv()

# Get the API key from the .env file
api_key = os.getenv("GEMINI_API_KEY")

# Configure the API key
genai.configure(api_key=api_key)


def get_ai_response(query):
    try:
       model = genai.GenerativeModel("gemini-1.5-pro")
       response = model.generate_content(query)
       return response.text
    except Exception as e:
        return f"Error: {e}"

def main():

    if choice == "🏠 Home":
        st.write("Welcome to EduFinance AI! Our platform helps students navigate financial aid opportunities with AI-powered recommendations.")
    
    elif choice == "💰 Scholarships & Loans":
        st.write("Explore available scholarships and loan options.")
        country = st.text_input("Enter your country/region:")
        field = st.text_input("Enter your field of study:")
        if st.button("Search Opportunities"):
            query = f"Scholarships and student loans available in {country} for {field} students."
            response = get_ai_response(query)
            st.write(response)
    
    elif choice == "🎯 Skill-based Recommendations":
        st.write("Get recommendations based on your skills!")
        skills = st.text_area("List your skills (comma-separated):")
        if st.button("Get Recommendations"):
            query = f"Suggest career opportunities, scholarships, or financial aid for students with skills in {skills}."
            response = get_ai_response(query)
            st.write(response)
    
    elif choice == "🤖 AI Assistance":
        st.write("Ask AI for guidance on loans and scholarships!")
        query = st.text_area("What do you need help with?")
        if st.button("Ask AI"):
            response = get_ai_response(query)
            st.write(response)
    
if __name__ == "__main__":
    main()
