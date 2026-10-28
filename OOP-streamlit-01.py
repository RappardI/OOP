import streamlit as st
from PIL import Image
col1, col2 = st.columns((4, 5))

with col1:
    st.title("Isaac Rappard")
    st.header("Student, Computer Science")

with col2:
    image = Image.open("OOP image.jpg")
    st.image(image, width = 200)



st.title("Isaac Rappard")
st.header("Student, Computer Science")

st.markdown("About Me")
st.text("I am a student at JBU, class of 2030")
st.divider()

st.markdown("Qualificaitons")
st.text("N/A")
st.divider()

st.markdown("Job Experience")
st.text("Worked at Dynamic Fastener for 1 year")
st.text("Worked at Longview Rec Center for 3.5 years")
st.text("Ran my own lawn mowing business for 3 years")
st.divider()

st.markdown("Projects")
st.text("Worked on several busines projects in highschool")
st.text("Currently working on 3 projects in college")
st.divider()

st.markdown("Contact Info")
st.text("Cell - 918-965-7155")
st.text("School email - rappardi@jbu.edu")
st.text("Home email - isaac.rappard@gmail.com")
st.divider()

st.markdown("**Contact me:**")
userName = st.text_input("Your name")
userEmail = st.text_input("Your email")
userMessage = st.text_input("Your Message")
st.button("Send Message")
