import streamlit as st

# url = "https://github.com/csk190/miniproject/blob/main/images/Gemini_Generated_Image_q5723kq5723kq572.png"

st.markdown("#### Spring 2026")
st.caption("This page is continuously updated.")

IMAGE_URL = "https://raw.githubusercontent.com/csk190/Myproject/blob/main/images/Gemini_Generated_Image_4k37ym4k37ym4k37.png"

# 파일 구조가 Home.py와 같은 위치에 images 폴더가 있다면
st.image(
    "images/Gemini_Generated_Image_q5723kq5723kq572.png",
    use_container_width=True
)
