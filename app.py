import streamlit as st
from deepface import DeepFace
import random
import tempfile

st.set_page_config(page_title="AI แนะนำเพลงตามอารมณ์", page_icon="🎵")

st.title("🎵 AI แนะนำเพลงตามอารมณ์จากใบหน้า")
st.write("อัปโหลดรูปใบหน้า แล้วระบบจะแนะนำเพลงให้")

music_dict = {
    "happy": ["Happy - Pharrell Williams", "Can't Stop The Feeling - Justin Timberlake"],
    "sad": ["Fix You - Coldplay", "Someone Like You - Adele"],
    "angry": ["Believer - Imagine Dragons"],
    "surprise": ["Shake It Off - Taylor Swift"],
    "neutral": ["Let It Be - The Beatles"],
    "fear": ["Lovely - Billie Eilish"],
    "disgust": ["Creep - Radiohead"]
}

uploaded_file = st.file_uploader("📸 อัปโหลดรูปภาพใบหน้า", type=["jpg", "png", "jpeg"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        image_path = tmp.name

    with st.spinner("กำลังวิเคราะห์อารมณ์..."):
        result = DeepFace.analyze(img_path=image_path, actions=["emotion"])
        emotion = result[0]["dominant_emotion"]

    song = random.choice(music_dict.get(emotion, ["ไม่พบเพลงที่เหมาะสม"]))

    st.success(f"😄 อารมณ์ที่ตรวจพบ: {emotion}")
    st.write(f"🎶 เพลงที่แนะนำ: **{song}**")
