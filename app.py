import streamlit as st
from _01_pandas import content as cont_pandas

def main():
    st.title("Data Science Roadmap")

    # Data structure for topics and sub-topics
    topics = {
        "Python Programming": {
            "Pandas": cont_pandas,
            "Numpy": "Learn about Numpy"
        },
        "Machine Learning": {
            "Klasifikasi": "Placeholder content.",
            "Regresi": "Placeholder content.",
            "Clustering": "Placeholder content.",
            "Deep Learning": "Placeholder content.",
        },
        "Statistika": {
            "Statistika untuk Data Science": "Placeholder content."
        },
        "Data Visualisasi": {
            "Data Visualisasi dengan Matplotlib": "Placeholder content.",
            "Data Visualisasi dengan Seaborn": "Placeholder content."
        },
        "SQL": {
            "SQL": "Placeholder content."
        },
        "Natural Language Programming": {
            "NLP": "Placeholder content."
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
