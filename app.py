import streamlit as st

st.set_page_config(
    page_title="Теория игр для всех",
    page_icon="🌐",
    layout="wide"
)

# ---------- ЗАГОЛОВОК ----------
st.title("🌐 Теория игр для всех")
st.write(
    "Интерактивное изучение теории игр, "
    "равновесия Нэша и переговорных стратегий."
)

st.divider()

# ---------- МЕНЮ ----------
section = st.sidebar.radio(
    "📚 Разделы приложения",
    [
        "📚 Теория",
        "🎲 Классические игры",
        "🧮 Анализатор матриц",
        "🇰🇿 Реальные кейсы Казахстана",
        "📊 Что если?",
        "🤖 ИИ-ассистент"
    ]
)

# ---------- ТЕОРИЯ ----------
if section == "📚 Теория":
    st.header("📚 Теория игр")

    st.write(
        "Здесь будет учебник по теории игр, "
        "основным понятиям и равновесию Нэша."
    )

    st.info("🚧 Раздел находится в разработке.")

# ---------- КЛАССИЧЕСКИЕ ИГРЫ ----------
elif section == "🎲 Классические игры":
    st.header("🎲 Классические игры")

    st.write(
        "Здесь появятся известные игры "
        "с матрицами выигрышей и объяснениями."
    )

    st.info("🚧 Раздел находится в разработке.")

# ---------- АНАЛИЗАТОР ----------
# ---------- АНАЛИЗАТОР ----------
elif section == "🧮 Анализатор матриц":
    st.header("🧮 Анализатор матриц 2×2")

    st.write(
        "Введите выигрыши двух игроков для каждой комбинации стратегий."
    )

    # Имена игроков
    col1, col2 = st.columns(2)

    with col1:
        player1 = st.text_input(
            "Игрок 1",
            "Казахстан"
        )

    with col2:
        player2 = st.text_input(
            "Игрок 2",
            "Кыргызстан"
        )

    st.divider()

    # Названия стратегий
    st.subheader("🎯 Стратегии")

    col1, col2 = st.columns(2)

    with col1:
        p1_strategy1 = st.text_input(
            f"{player1}: стратегия 1",
            "Сотрудничать"
        )

        p1_strategy2 = st.text_input(
            f"{player1}: стратегия 2",
            "Не сотрудничать"
        )

    with col2:
        p2_strategy1 = st.text_input(
            f"{player2}: стратегия 1",
            "Сотрудничать"
        )

        p2_strategy2 = st.text_input(
            f"{player2}: стратегия 2",
            "Не сотрудничать"
        )

    st.divider()

    st.subheader("💰 Матрица выигрышей")

    st.write(
        "В каждой клетке укажите: "
        "(выигрыш Игрока 1, выигрыш Игрока 2)"
    )

    # Заголовки матрицы
       # ---------- КРАСИВАЯ МАТРИЦА ----------
    st.subheader("💰 Матрица выигрышей")

    st.caption(
        "Вводите выигрыш каждого игрока в формате "
        "отдельных чисел. Первое число — Игрок 1, "
        "второе — Игрок 2."
    )

    # Заголовок таблицы
    h1, h2, h3 = st.columns([2, 3, 3])

    with h1:
        st.write("")

    with h2:
        st.markdown(f"### {p2_strategy1}")

    with h3:
        st.markdown(f"### {p2_strategy2}")

    # Строка 1
    c1, c2, c3 = st.columns([2, 3, 3])

    with c1:
        st.markdown(f"### {p1_strategy1}")

    with c2:
        st.markdown("**Клетка (1,1)**")
        a11 = st.number_input(
            f"{player1} — {p1_strategy1}/{p2_strategy1}",
            value=3.0,
            key="a11_new"
        )
        b11 = st.number_input(
            f"{player2} — {p1_strategy1}/{p2_strategy1}",
            value=3.0,
            key="b11_new"
        )

        st.info(f"({a11:.2f}, {b11:.2f})")

    with c3:
        st.markdown("**Клетка (1,2)**")
        a12 = st.number_input(
            f"{player1} — {p1_strategy1}/{p2_strategy2}",
            value=0.0,
            key="a12_new"
        )
        b12 = st.number_input(
            f"{player2} — {p1_strategy1}/{p2_strategy2}",
            value=5.0,
            key="b12_new"
        )

        st.info(f"({a12:.2f}, {b12:.2f})")

    # Строка 2
    c1, c2, c3 = st.columns([2, 3, 3])

    with c1:
        st.markdown(f"### {p1_strategy2}")

    with c2:
        st.markdown("**Клетка (2,1)**")
        a21 = st.number_input(
            f"{player1} — {p1_strategy2}/{p2_strategy1}",
            value=5.0,
            key="a21_new"
        )
        b21 = st.number_input(
            f"{player2} — {p1_strategy2}/{p2_strategy1}",
            value=0.0,
            key="b21_new"
        )

        st.info(f"({a21:.2f}, {b21:.2f})")

    with c3:
        st.markdown("**Клетка (2,2)**")
        a22 = st.number_input(
            f"{player1} — {p1_strategy2}/{p2_strategy2}",
            value=1.0,
            key="a22_new"
        )
        b22 = st.number_input(
            f"{player2} — {p1_strategy2}/{p2_strategy2}",
            value=1.0,
            key="b22_new"
        )

        st.info(f"({a22:.2f}, {b22:.2f})")

    st.divider()

    st.divider()

    if st.button(
        "🧮 Рассчитать равновесие Нэша",
        use_container_width=True
    ):

        # Матрица выигрышей
        payoffs = [
            [(a11, b11), (a12, b12)],
            [(a21, b21), (a22, b22)]
        ]

        # Поиск чистых равновесий
        equilibria = []

        # Клетка (1,1)
        if a11 >= a21 and b11 >= b12:
            equilibria.append(
                (
                    p1_strategy1,
                    p2_strategy1,
                    a11,
                    b11
                )
            )

        # Клетка (1,2)
        if a12 >= a22 and b12 >= b11:
            equilibria.append(
                (
                    p1_strategy1,
                    p2_strategy2,
                    a12,
                    b12
                )
            )

        # Клетка (2,1)
        if a21 >= a11 and b21 >= b22:
            equilibria.append(
                (
                    p1_strategy2,
                    p2_strategy1,
                    a21,
                    b21
                )
            )

        # Клетка (2,2)
        if a22 >= a12 and b22 >= b21:
            equilibria.append(
                (
                    p1_strategy2,
                    p2_strategy2,
                    a22,
                    b22
                )
            )

        st.subheader("📊 Результат")

        if equilibria:

            st.success(
                f"Найдено чистых равновесий Нэша: "
                f"{len(equilibria)}"
            )

            for eq in equilibria:

                strategy1 = eq[0]
                strategy2 = eq[1]
                payoff1 = eq[2]
                payoff2 = eq[3]

                st.write(
                    f"### 🎯 Равновесие"
                )

                st.write(
                    f"**{player1}:** {strategy1}"
                )

                st.write(
                    f"**{player2}:** {strategy2}"
                )

                st.write(
                    f"💰 Выигрыш {player1}: **{payoff1}**"
                )

                st.write(
                    f"💰 Выигрыш {player2}: **{payoff2}**"
                )

                st.info(
                    "Ни одному игроку не выгодно "
                    "односторонне менять свою стратегию."
                )

        else:

            st.warning(
                "Чистого равновесия Нэша нет."
            )

            # Проверяем возможность смешанного равновесия

            denominator_p = (
                b11 - b12 - b21 + b22
            )

            denominator_q = (
                a11 - a12 - a21 + a22
            )

            if (
                denominator_p != 0
                and denominator_q != 0
            ):

                p = (
                    b12 - b22
                ) / denominator_p

                q = (
                    a21 - a22
                ) / denominator_q

                if 0 <= p <= 1 and 0 <= q <= 1:

                    st.success(
                        "🎲 Найдено смешанное равновесие Нэша!"
                    )

                    st.write(
                        f"Вероятность стратегии "
                        f"**{p1_strategy1}** "
                        f"для {player1}: "
                        f"**{p:.2%}**"
                    )

                    st.write(
                        f"Вероятность стратегии "
                        f"**{p2_strategy1}** "
                        f"для {player2}: "
                        f"**{q:.2%}**"
                    )

                    expected1 = (
                        p * q * a11
                        + p * (1 - q) * a12
                        + (1 - p) * q * a21
                        + (1 - p) * (1 - q) * a22
                    )

                    expected2 = (
                        p * q * b11
                        + p * (1 - q) * b12
                        + (1 - p) * q * b21
                        + (1 - p) * (1 - q) * b22
                    )

                    st.write(
                        f"Ожидаемый выигрыш "
                        f"{player1}: **{expected1:.2f}**"
                    )

                    st.write(
                        f"Ожидаемый выигрыш "
                        f"{player2}: **{expected2:.2f}**"
                    )

                else:

                    st.warning(
                        "Смешанное равновесие "
                        "с вероятностями от 0 до 1 "
                        "не найдено."
                    )

            else:

                st.warning(
                    "Для данной матрицы стандартное "
                    "смешанное равновесие не определяется."
                )
# ---------- КЕЙСЫ ----------
elif section == "🇰🇿 Реальные кейсы Казахстана":
    st.header("🇰🇿 Реальные кейсы Казахстана")

    st.write(
        "Здесь будут пять переговорных кейсов:"
    )

    st.write("1. 💧 Водные ресурсы — Сырдарья")
    st.write("2. 🛢️ Нефтегазовый транзит")
    st.write("3. 📦 ЕАЭС — торговля")
    st.write("4. 🌱 Климатические переговоры")
    st.write("5. 🚂 Транскаспийский маршрут — ТМТМ")

    st.info("🚧 Подробные кейсы добавим позже.")

# ---------- ЧТО ЕСЛИ ----------
elif section == "📊 Что если?":
    st.header("📊 Прогноз и аналитика «Что если?»")

    st.write(
        "Здесь можно будет менять компенсации, "
        "штрафы, тарифы и другие параметры."
    )

    st.info("🚧 Этот раздел добавим после анализатора.")

# ---------- ИИ ----------
elif section == "🤖 ИИ-ассистент":
    st.header("🤖 ИИ-ассистент")

    st.write(
        "Опишите переговорную ситуацию обычным языком, "
        "а ИИ сможет определить игроков, стратегии "
        "и построить матрицу."
    )

    st.info("🚧 ИИ подключим после создания математического ядра.")

st.divider()

st.caption(
    "Проект «Теория игр для всех» • "
    "Математическое моделирование переговорных стратегий"
)
