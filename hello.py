import streamlit as st

st.title("Hello All how are you")
st.subheader("Last Class")
st.code('print("this is some code")')
if st.checkbox('Balloons', False):
    st.balloons()
