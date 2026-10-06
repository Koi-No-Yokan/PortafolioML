import os
import streamlit as st
from PIL import Image

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Portafolio | Proyectos de Machine Learning",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# Custom Modern CSS
# ---------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    .hero-container {
        background: linear-gradient(135deg, rgba(37, 99, 235, 0.12) 0%, rgba(14, 165, 233, 0.08) 50%, rgba(99, 102, 241, 0.06) 100%);
        border: 1px solid rgba(37, 99, 235, 0.20);
        border-radius: 22px;
        padding: 34px 38px;
        margin-bottom: 28px;
        position: relative;
        overflow: hidden;
    }

    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: linear-gradient(90deg, #2563eb, #4f46e5);
        color: white;
        padding: 6px 14px;
        border-radius: 50px;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        margin-bottom: 12px;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.22);
    }

    .hero-title {
        font-size: 2.45rem;
        font-weight: 800;
        line-height: 1.18;
        margin-bottom: 10px;
        background: linear-gradient(90deg, #0f172a, #334155);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-desc {
        font-size: 1.02rem;
        color: #64748b;
        max-width: 900px;
        line-height: 1.6;
        margin-bottom: 14px;
    }

    .metric-pill {
        display: inline-flex;
        align-items: center;
        gap: 7px;
        background: rgba(255, 255, 255, 0.75);
        border: 1px solid rgba(0, 0, 0, 0.06);
        padding: 7px 14px;
        border-radius: 12px;
        font-size: 0.83rem;
        font-weight: 600;
        margin-right: 7px;
        margin-bottom: 7px;
        backdrop-filter: blur(10px);
    }

    /* Horizontal floating project card */
    .project-card {
        border-radius: 22px;
        background: rgba(255, 255, 255, 0.82);
        border: 1px solid rgba(15, 23, 42, 0.08);
        box-shadow: 0 8px 26px rgba(15, 23, 42, 0.07);
        padding: 18px;
        margin: 0 0 22px 0;
        transition: all 0.25s ease;
    }

    .project-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 16px 38px rgba(37, 99, 235, 0.13);
        border-color: rgba(37, 99, 235, 0.25);
    }

    .project-image {
        border-radius: 16px;
        overflow: hidden;
        min-height: 255px;
        background: #f1f5f9;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .project-image img {
        width: 100%;
        height: 255px;
        object-fit: cover;
        border-radius: 16px;
    }

    .badge-category {
        display: inline-block;
        padding: 5px 11px;
        font-size: 0.75rem;
        font-weight: 700;
        border-radius: 8px;
        background: rgba(37, 99, 235, 0.10);
        color: #1d4ed8;
        margin-bottom: 9px;
    }

    .project-number {
        color: #94a3b8;
        font-size: 0.76rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 5px;
    }

    .card-title {
        font-size: 1.42rem;
        font-weight: 800;
        margin: 3px 0 8px;
        color: #0f172a;
        line-height: 1.25;
    }

    .card-desc {
        font-size: 0.91rem;
        color: #64748b;
        line-height: 1.55;
        margin-bottom: 12px;
    }

    .tech-pill {
        display: inline-block;
        padding: 4px 9px;
        font-size: 0.72rem;
        font-weight: 650;
        border-radius: 7px;
        background: rgba(148, 163, 184, 0.13);
        color: #475569;
        margin-right: 5px;
        margin-bottom: 6px;
        border: 1px solid rgba(148, 163, 184, 0.10);
    }

    .links-label {
        color: #94a3b8;
        font-size: 0.72rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin: 5px 0 7px;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 18px !important;
    }

    .portfolio-footer {
        text-align: center;
        padding: 35px 15px 20px;
        color: #94a3b8;
        font-size: 0.85rem;
        border-top: 1px solid rgba(0, 0, 0, 0.06);
        margin-top: 40px;
    }

    @media (max-width: 900px) {
        .hero-title { font-size: 2rem; }
        .project-image, .project-image img { min-height: 210px; height: 210px; }
        .card-title { font-size: 1.2rem; }
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Project Data
# ---------------------------------------------------------
PROJECTS = [{'id': 'clase2', 'title': 'Descenso de Gradiente Interactivo', 'category': 'Optimización', 'image': 'img2.jpg', 'desc': 'Exploración interactiva del descenso de gradiente y su comportamiento durante el proceso de optimización.', 'tags': ['Machine Learning', 'Optimización', 'Descenso de Gradiente', 'Visualización'], 'url': 'https://proav-clase2-l8zdhf5bhpzbpra3id4bjh.streamlit.app/', 'github': 'https://github.com/Koi-No-Yokan/ProAV-Clase2', 'colab': 'https://colab.research.google.com/drive/1ROulq8AUtKWkdyVtx-o21qzmMJyQFsGa'}, {'id': 'clase3', 'title': 'Z Detector de Anomalías: Lógica + Big-O + NumPy', 'category': 'Detección de Anomalías', 'image': 'img3.png', 'desc': 'Detector de anomalías que conecta lógica algorítmica, análisis de complejidad Big-O y operaciones numéricas con NumPy.', 'tags': ['Machine Learning', 'Anomalías', 'Big-O', 'NumPy', 'Algoritmos'], 'url': 'https://proavclas3-uzjewhjfkyht7smedspdgp.streamlit.app/#detector-de-anomalias-logica-big-o-num-py', 'github': 'https://github.com/Koi-No-Yokan/ProAvClas3', 'colab': 'https://colab.research.google.com/drive/1Ppa2YV4PwjuXCLwk3ZMOwBAo8cQBA56q'}, {'id': 'clase4', 'title': 'Datos: Preparación y Estructura', 'category': 'Preparación de Datos', 'image': 'img4.png', 'desc': 'Trabajo enfocado en la preparación, organización y estructuración de datos como base para proyectos de Machine Learning.', 'tags': ['Machine Learning', 'Datos', 'Data Preparation', 'Estructuras', 'Data Science'], 'url': 'https://proav4-7ufs2nqvd8jzcrrwr9pdnx.streamlit.app/', 'github': 'https://github.com/Koi-No-Yokan/ProAV4', 'colab': 'https://colab.research.google.com/drive/1akgZIUHlCzRl9dvhnyXamFFLFA_IHBWM'}, {'id': 'clase5', 'title': 'Predictor de Calidad del Aire — CORNARE (MARCO)', 'category': 'Predicción', 'image': 'img5.png', 'desc': 'Proyecto de predicción aplicado a datos de calidad del aire de CORNARE, integrando análisis de datos y modelado predictivo.', 'tags': ['Machine Learning', 'Predicción', 'Calidad del Aire', 'Estadística', 'Datos'], 'url': 'https://prueba-4thu49jmpmaznzyuj7zcfs.streamlit.app/', 'github': 'https://github.com/Koi-No-Yokan/ProgAv5', 'colab': 'https://colab.research.google.com/drive/1xdDdRyZ8CTmKjLNW97CA--W1ZDcKCRrL#scrollTo=c3a82513'}, {'id': 'clase6', 'title': 'Regresiones Lineales, Múltiple, Costo y Gradiente', 'category': 'Regresión', 'image': 'img6.jpg', 'desc': 'Aplicación de regresión lineal y múltiple, funciones de costo y gradiente para comprender el aprendizaje de modelos predictivos.', 'tags': ['Machine Learning', 'Regresión', 'Estadística', 'Función de Costo', 'Gradiente'], 'url': 'https://proavclass6-3uef5fdnslkdvt9emtnfq3.streamlit.app/', 'github': 'https://github.com/Koi-No-Yokan/ProAVClass6', 'colab': 'https://colab.research.google.com/drive/1zDfXY3TCvyevXBDOSuHc45kCEg_eb3Vm'}, {'id': 'clase7', 'title': 'Series de Tiempo', 'category': 'Series de Tiempo', 'image': 'img7.png', 'desc': 'Análisis de series de tiempo para explorar patrones, comportamiento temporal y herramientas estadísticas aplicadas a datos secuenciales.', 'tags': ['Machine Learning', 'Series de Tiempo', 'Estadística', 'Análisis Temporal', 'Datos'], 'url': 'https://progava7-enjxq5gqlxwjozbubcopwf.streamlit.app/', 'github': 'https://github.com/Koi-No-Yokan/ProgAva8', 'colab': 'https://colab.research.google.com/drive/144q5WnNPQwgs6jS_gNz0zL4S8qNlIFst'}, {'id': 'clase8', 'title': 'Sistema de IoT: Captura de Datos y Procesamiento', 'category': 'IoT & Datos', 'image': 'img8.png', 'desc': 'Sistema orientado a la captura de datos mediante IoT y su posterior procesamiento para convertir señales en información utilizable.', 'tags': ['IoT', 'Machine Learning', 'Captura de Datos', 'Procesamiento', 'Sensores'], 'url': 'https://progav9-kvre4tkgtneam5ptmrhtze.streamlit.app/', 'github': 'https://github.com/koi-no-yokan/progav9/blob/main/app.py', 'colab': 'https://colab.research.google.com/drive/1rP7-_pfTKa1pBpGjpexHD6guTuAAcPBs'}, {'id': 'clase9', 'title': 'Regresión Logística: Predicción de Lluvias', 'category': 'Clasificación', 'image': 'img9.png', 'desc': 'Modelo de regresión logística aplicado a la predicción de lluvias, abordando clasificación y probabilidad de ocurrencia.', 'tags': ['Machine Learning', 'Regresión Logística', 'Clasificación', 'Estadística', 'Predicción'], 'url': 'https://progavclass10-iwk2t6yuyj7lkaztkzte6m.streamlit.app/', 'github': 'https://github.com/koi-no-yokan/progavclass10/blob/main/app_regresion_logistica.py', 'colab': 'https://colab.research.google.com/drive/10gzK1BTerqD32u8xX2upEzhzrxVJ7X5x'}, {'id': 'clase10', 'title': 'Clasificación y Exploración KNN', 'category': 'K-Nearest Neighbors', 'image': 'img10.png', 'desc': 'Exploración del algoritmo KNN para clasificación, analizando la relación entre observaciones y sus vecinos más cercanos.', 'tags': ['Machine Learning', 'KNN', 'Clasificación', 'Estadística', 'Exploración de Datos'], 'url': 'https://progav12-xzvungjnkqgjrg3fyc6fjx.streamlit.app/', 'github': 'https://github.com/koi-no-yokan/progav12/blob/main/app.py', 'colab': 'https://colab.research.google.com/drive/1osLyo-TwjSsB3LvANJ1Kvkt5Yms8GFl8'}]

# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------
with st.sidebar:
    if os.path.exists("audio_to_txt.png"):
        avatar_img = Image.open("audio_to_txt.png")
        st.image(avatar_img, use_container_width=True)

    st.markdown("""
        <div style="text-align:center; margin-top:-10px; margin-bottom:15px;">
            <h2 style="margin:0; font-size:1.35rem; font-weight:800;">Joseph Santiago Jimenez Jimenez</h2>
            <p style="color:#2563eb; font-weight:600; font-size:0.85rem; margin-top:4px; margin-bottom:10px;">
                Desarrollador & Especialista en IA
            </p>
            <p style="font-size:0.82rem; color:#64748b; line-height:1.45; text-align:justify;">
                Portafolio académico y práctico enfocado en Machine Learning, estadística,
                análisis de datos, optimización, clasificación, regresión, series de tiempo e IoT.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("📚 Recursos & Prácticas")
    st.markdown("Accede al portal oficial con guías didácticas, ejercicios prácticos y material formativo paso a paso:")
    st.link_button("🌐 Abrir Portal de Ejercicios",
                   "https://sites.google.com/view/aplicacionesdeia/inicio",
                   use_container_width=True)

    st.markdown("---")
    st.subheader("🧠 Temas del portafolio")
    st.markdown("""
    <div style="display:flex; flex-wrap:wrap; gap:4px;">
        <span class="tech-pill">Machine Learning</span>
        <span class="tech-pill">Estadística</span>
        <span class="tech-pill">Regresión</span>
        <span class="tech-pill">Clasificación</span>
        <span class="tech-pill">Series de Tiempo</span>
        <span class="tech-pill">Optimización</span>
        <span class="tech-pill">NumPy</span>
        <span class="tech-pill">IoT</span>
        <span class="tech-pill">Data Science</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.caption("© 2026 Joseph Santiago Jimenez Jimenez • Proyectos de Machine Learning")

# ---------------------------------------------------------
# Main Header
# ---------------------------------------------------------
st.markdown("""
<div class="hero-container">
    <div class="hero-badge">⚡ Portafolio académico y aplicado</div>
    <div class="hero-title">Proyectos de Machine Learning</div>
    <div class="hero-desc">
        Explora una colección de proyectos enfocados en aprendizaje automático,
        estadística, análisis de datos, optimización, clasificación, regresión,
        series de tiempo e integración con sistemas IoT.
    </div>
    <div style="margin-top:10px;">
        <span class="metric-pill">🤖 <b>10</b> proyectos</span>
        <span class="metric-pill">📊 Machine Learning & Estadística</span>
        <span class="metric-pill">☁️ Streamlit + Colab</span>
        <span class="metric-pill">💻 Código disponible en GitHub</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Search & Filter
# ---------------------------------------------------------
all_tags = sorted({tag for p in PROJECTS for tag in p["tags"]})
categories = ["🌟 Todos los proyectos"] + sorted({p["category"] for p in PROJECTS})

col_search, col_filter = st.columns([1.5, 1])
with col_search:
    search_query = st.text_input(
        "Buscar",
        placeholder="🔍 Busca por proyecto, tema, algoritmo o tecnología...",
        label_visibility="collapsed"
    )
with col_filter:
    selected_cat = st.selectbox(
        "Categoría",
        categories,
        label_visibility="collapsed"
    )

filtered_projects = []
for p in PROJECTS:
    category_match = selected_cat == "🌟 Todos los proyectos" or p["category"] == selected_cat
    q = search_query.strip().lower()
    search_match = (
        not q or
        q in p["title"].lower() or
        q in p["desc"].lower() or
        q in p["category"].lower() or
        any(q in tag.lower() for tag in p["tags"])
    )
    if category_match and search_match:
        filtered_projects.append(p)

st.markdown(
    f"<p style='color:#64748b; font-size:0.9rem; margin:7px 0 18px;'>"
    f"Mostrando <b>{len(filtered_projects)}</b> de <b>{len(PROJECTS)}</b> proyectos</p>",
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# Horizontal Floating Projects
# ---------------------------------------------------------
if not filtered_projects:
    st.info("No se encontraron proyectos con los criterios seleccionados.")
else:
    for i, proj in enumerate(filtered_projects, start=1):
        st.markdown("<div class='project-card'>", unsafe_allow_html=True)
        left, right = st.columns([1.05, 1.95], gap="large")

        with left:
            if os.path.exists(proj["image"]):
                st.image(Image.open(proj["image"]), use_container_width=True)
            else:
                st.markdown(
                    "<div class='project-image'><span>📷 Imagen no disponible</span></div>",
                    unsafe_allow_html=True
                )

        with right:
            st.markdown(f"<div class='project-number'>Proyecto {i:02d}</div>", unsafe_allow_html=True)
            st.markdown(
                f"<div class='badge-category'>{proj['category']}</div>",
                unsafe_allow_html=True
            )
            st.markdown(
                f"<div class='card-title'>{proj['title']}</div>",
                unsafe_allow_html=True
            )
            st.markdown(
                f"<div class='card-desc'>{proj['desc']}</div>",
                unsafe_allow_html=True
            )

            tags_html = "".join(
                f"<span class='tech-pill'>{tag}</span>" for tag in proj["tags"]
            )
            st.markdown(
                f"<div style='margin-bottom:10px;'>{tags_html}</div>",
                unsafe_allow_html=True
            )

            st.markdown("<div class='links-label'>Explorar proyecto</div>", unsafe_allow_html=True)
            b1, b2, b3 = st.columns(3)
            with b1:
                st.link_button("🚀 Aplicación", proj["url"], use_container_width=True)
            with b2:
                st.link_button("💻 GitHub", proj["github"], use_container_width=True)
            with b3:
                st.link_button("📓 Colab", proj["colab"], use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------
st.markdown("""
<div class="portfolio-footer">
    <p><b>Portafolio de Proyectos de Machine Learning</b> • Desarrollado con Streamlit & Python</p>
    <p style="font-size:0.8rem; margin-top:4px;">
        Descubre más proyectos, tutoriales y documentación en el
        <a href="https://sites.google.com/view/aplicacionesdeia/inicio" target="_blank"
           style="color:#2563eb; text-decoration:none; font-weight:600;">
           Portal de Aplicaciones de IA
        </a>
    </p>
</div>
""", unsafe_allow_html=True)
