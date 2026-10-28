import streamlit as st
from html import escape

st.set_page_config(page_title="Tech Stack Grid", layout="centered")

st.markdown("""
<style>
.tech-card {
    background-color: #ffffff;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 15px;
    text-align: center;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    margin-bottom: 15px;
    transition: transform 0.2s;
}
.tech-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}
.tech-name {
    margin-top: 8px;
    font-size: 14px;
    font-weight: 500;
    color: #333333;
}
</style>
""", unsafe_allow_html=True)

st.title("Tech Stack Dashboard")
st.write("Explore the frameworks, libraries, databases, and languages used in the project.")

tech_stack = [
    ("React", "⚛️"),
    ("Three.js", "📦"),
    ("Redux", "��"),
    ("Django", "🎸"),
    ("Tailwind", "🎨"),
    ("Kubernetes", "⚓"),
    ("MaterialUI", "🔷"),
    ("GraphQL", "⬡"),
    ("Vue", "💚"),
    ("Nuxt.js", "🟢"),
    ("AWS", "☁️"),
    ("TypeScript", "📘"),
    ("Go", "🐹"),
    ("MySQL", "🐬"),
    ("PostgreSQL", "🐘"),
    ("SQLite", "🗄️"),
    ("Python", "🐍"),
    ("API", "🔌"),
    ("JavaScript", "💛"),
    ("Docker", "🐳"),
]

cols_per_row = 6

for i in range(0, len(tech_stack), cols_per_row):
    cols = st.columns(cols_per_row)

    for j in range(cols_per_row):
        if i + j < len(tech_stack):
            name, icon = tech_stack[i + j]

            with cols[j]:
                st.markdown(
                    f"""
                    <div class="tech-card">
                        <div style="font-size:32px;">{escape(icon)}</div>
                        <div class="tech-name">{escape(name)}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
