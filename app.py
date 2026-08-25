import streamlit as st

st.set_page_config(
    page_title="Дипломатия: Центральная Азия",
    page_icon="🌍"
)

st.title("🌍 Дипломатия: Переговоры в Центральной Азии")

st.write("Добро пожаловать в дипломатическую игру!")

st.subheader("Выберите страну")

country = st.selectbox(
    "Ваша страна:",
    [
        "🇰🇿 Казахстан",
        "🇰🇬 Кыргызстан",
        "🇷🇺 Россия",
        "🇨🇳 Китай"
    ]
)

st.success(f"Вы выбрали: {country}")

if st.button("Начать игру"):
    st.balloons()
    st.write("🎮 Игра начинается!")
