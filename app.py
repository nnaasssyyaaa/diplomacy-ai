import streamlit as st

st.set_page_config(
    page_title="Дипломатия: Центральная Азия",
    page_icon="🌍",
    layout="centered"
)

st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    margin-top: 30px;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #555;
    margin-bottom: 40px;
}

.country-card {
    padding: 20px;
    border-radius: 15px;
    background-color: white;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">🌍 ДИПЛОМАТИЯ</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Переговоры в Центральной Азии</div>',
    unsafe_allow_html=True
)

st.divider()

st.write("### 🎮 Добро пожаловать!")

st.write(
    "Выберите страну, за которую будете играть. "
    "Ваша задача — вести переговоры, управлять ресурсами "
    "и набрать больше всего очков."
)

st.write("### 🏳️ Выберите свою страну")

country = st.selectbox(
    "Страна:",
    [
        "🇰🇿 Казахстан",
        "🇰🇬 Кыргызстан",
        "🇷🇺 Россия",
        "🇨🇳 Китай"
    ]
)

st.info(f"Вы выбрали: **{country}**")

st.write("")

if st.button("🚀 НАЧАТЬ ИГРУ", use_container_width=True):
    st.success("🎉 Игра начинается!")
    st.balloons()

st.divider()

st.caption("2–4 игрока • 5 раундов • Дипломатия • Стратегия")
