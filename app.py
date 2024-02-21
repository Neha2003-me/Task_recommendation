# app.py
import streamlit as st
import pandas as pd
from random import sample

# Create a dataset
df = pd.DataFrame({
    'Skills': ['Programming', 'Communication', 'TeamWork', 'Problem-Solving', 'Leadership', 'Creativity', 'Marketing', 'Event Planning', 'Logistics Management', 'Sponsorship', 'Venue setup and decoration', 'Technical and Audio-Visual Support', 'Participant Engagement'],
    'Tasks': ['Develop and implement software solutions for event management.', 'Craft engaging communication materials and manage public relations.', 'Collaborate with team members to achieve common goals.', 'Analyze and solve challenges that may arise during the event.', 'Lead and inspire a team towards successful event execution.', 'Design innovative and visually appealing event materials.', 'Create and execute marketing strategies to promote the event.', 'Plan and organize various aspects of the event, including scheduling and logistics.', 'Coordinate transportation, setup, and logistics for the event.', 'Secure sponsorships and organize fundraising initiatives.', 'Coordinate the setup and decoration of event venues.', 'Set up and manage technology and audio-visual components for the event.', 'Plan and execute activities to engage event participants.']
})

# Streamlit app
def main():
    st.title('CONTRIBUTE TO NOURISH360 WITH YOUR SKILLS!')  # Change the title here
    selected_skills = st.multiselect('Select skills:', df['Skills'])
    if st.button('Recommend Tasks'):
        recommendations = recommend_tasks(selected_skills)
        st.write('Recommended Tasks:')
        for task in recommendations:
            st.write('-', task)

# Function to recommend tasks based on selected skills
def recommend_tasks(selected_skills):
    relevant_tasks = df[df['Skills'].isin(selected_skills)]
    tasks = relevant_tasks['Tasks'].tolist()
    # Ensure we have at least four tasks available
    if len(tasks) >= 4:
        return sample(tasks, 4)  # Select four random tasks
    else:
        return tasks  # Return available tasks if less than four

if __name__ == '__main__':
    main()
