import openai
openai.api_key = "sk-Gm-7fUM-TkSdeJQAUNcYKLw7LE-_hT0Mrmq-4pAhjJT3BlbkFJ7dupKD-NLCbp2qV5m359wUCnHr3o9yUWI475eGQEwA"  

import streamlit as st

def main():
    st.set_page_config(page_title="The Bazi Destiny", layout="centered")
    st.title("🔮 The Bazi Destiny")
    st.markdown("กรอกวันเดือนปีเกิด + เวลาเกิด เพื่อดูดวงจีนของคุณ")

    name = st.text_input("ชื่อ (ไม่บังคับ)")
    date = st.date_input("วันเดือนปีเกิด")
    time = st.time_input("เวลาเกิด")

    if st.button("วิเคราะห์ดวง"):
        st.success("📌 คุณเกิดวันที่ **{} เวลา {}**".format(date.strftime("%d-%m-%Y"), time.strftime("%H:%M")))
        st.info("นี่คือตัวอย่างผลวิเคราะห์ดวงเบื้องต้น... (ระบบสมบูรณ์จะต่อเชื่อม GPT/สูตรดวง)")

if __name__ == "__main__":
    main()
