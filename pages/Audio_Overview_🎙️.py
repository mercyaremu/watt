import streamlit as st

st.markdown("# [Watt Protocol](https://watt.si) Audio Overview")
st.markdown("Listen to a podcast-style audio overview of Watt protocol.")

# Play audio file
st.audio("audio.wav", format="audio/wav")
