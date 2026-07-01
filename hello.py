import streamlit as st
import pandas as pd

st.title("Hello All how are you")
st.subheader("Last Class")
st.code('print("this is some code")')
if st.checkbox('Balloons', False):
    st.balloons()
    
df=pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)
