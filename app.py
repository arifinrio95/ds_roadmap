import streamlit as st
from _01_pandas import content as cont_pandas

def main():
    # st.title("Data Science Roadmap")

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

    # Initialize a session state variable for 'started'
    if 'started' not in st.session_state:
        st.session_state['started'] = False

    # Show welcome message and start button if not 'started'
    if not st.session_state['started']:
        # Welcome message in the main area
        st.write("""
        ## Selamat Datang Self-Learner! 🌟📊🚀
        
        Kalo kamu bingung belajar Data Science mulai dari mana dulu. Dari sini!🧭✨
        """)

        # Center the "Start" button using columns
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button('Start'):
                st.session_state['started'] = True
                st.experimental_rerun()
                
        # # Start button
        # if st.button('Mulai!'):
        #     st.session_state['started'] = True
        #     st.experimental_rerun()
    # Once 'started', show sidebar and content
    if st.session_state['started']:
        # Sidebar for topics
        with st.sidebar:
            st.title("Data Science Roadmap")
            selected_topic = st.radio("Topik", list(topics.keys()))
            
            # Displaying sub-topics based on topic selection
            if selected_topic:
                selected_subtopic = st.radio("Sub-Topik", list(topics[selected_topic].keys()))
    
        # Display sub-topic content in the main area
        if selected_topic and selected_subtopic:
            st.write(topics[selected_topic][selected_subtopic])

if __name__ == "__main__":
    main()
