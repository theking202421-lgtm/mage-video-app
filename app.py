import streamlit as st

st.set_page_config(page_title="Mage Video App")
st.title("🎬 Mage Video App")
st.write("Prompt eka dala Generate obanna")

prompt = st.text_input("Video eka gana liyanna", "A cute cat dancing in Colombo")

if st.button("Generate Video ✨"):
    st.image(f"https://image.pollinations.ai/prompt/{prompt}")
    st.success("Hadila iwarai!")
