import streamlit as st
from huggingface_hub import InferenceClient
import tempfile

st.set_page_config(page_title="Mage Video App")
st.title("🎬 Mage Video App - Real Video")
st.write("Prompt eka dala Generate obanna, video ekak enawa!")

prompt = st.text_input("Video eka gana liyanna", "A cute cat dancing in Colombo")

if st.button("Generate Video ✨"):
    with st.spinner("Video eka hadanawa... miniththu 1-2k inna..."):
        try:
            # Secrets eken token eka gannawa
            token = st.secrets["HF_TOKEN"]
            client = InferenceClient("Wan-AI/Wan2.1-T2V-1.3B", token=token)
            video_bytes = client.text_to_video(prompt)
            
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as f:
                f.write(video_bytes)
                st.video(f.name)
            st.success("Video eka hadila iwarai! 🎉")
        except Exception as e:
            st.error("Error ekak awa")
            st.write(e)
