import streamlit as st
from _01_web_scraping_content import content as wsc

def main():
    st.title("Data Science Roadmap")

    # Data structure for topics and sub-topics
    topics = {
        "Data Collection": {
            "Web Scraping": wsc,
            "APIs": "Learn about REST APIs, authentication"
        },
        "Data Cleaning": {
            "Pandas Basics": "Learn about DataFrame operations",
            "Data Transformation": "Learn about data normalization, transformation"
        },
        # More topics and sub-topics can be added here
    }

    # Sidebar for topics
    with st.sidebar:
        selected_topic = st.radio("Select a Topic", list(topics.keys()))
        
        # Displaying sub-topics based on topic selection
        if selected_topic:
            selected_subtopic = st.radio("Select a Sub-Topic", list(topics[selected_topic].keys()))

    # Display sub-topic content in the main area
    if selected_topic and selected_subtopic:
        st.write(topics[selected_topic][selected_subtopic])

if __name__ == "__main__":
    main()
