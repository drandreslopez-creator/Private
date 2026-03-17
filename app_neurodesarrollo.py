import streamlit as st

st.set_page_config(
    page_title="Neurodesarrollo Pediátrico",
    page_icon="🧠",
    layout="wide"
)

# =========================
# ESTILOS
# =========================
st.markdown("""
<style>
.block-container {
    padding-top: 1.2rem;
    padding-bottom: 2rem;
    max-width: 1250px;
}

.main-header {
    padding: 1.3rem 1.4rem;
    border-radius: 20px;
    background: linear-gradient(135deg, #0f172a, #1e293b);
    border: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 1rem;
}

.main-title {
    font-size: 2rem;
    font-weight: 700;
    color: #f8fafc;
    line-height: 1.25;
    margin-bottom: 0.35rem;
}

.main-subtitle {
    font-size: 1rem;
    color: #cbd5e1;
}

.card {
    background: rgba(15, 23, 42, 0.70);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 1rem 1rem 0.8rem 1rem;
    margin-bottom: 1rem;
}

.section-title {
    font-size: 1.1rem;
    font-weight: 600;
    color: #f8fafc;
    margin-bottom: 0.5rem;
}

.small-label {
    color: #94a3b8;
    font-size: 0.9rem;
    margin-bottom: 0.1rem;
}

.result-card {
    background: rgba(15, 23, 42, 0.80);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 1rem;
    margin-top: 0.8rem;
    margin-bottom: 1rem;
}

.area-ok {
    padding: 0.8rem 0.9rem;
    border-radius: 14px;
    background: rgba(22, 163, 74, 0.12);
    border: 1px solid rgba(22, 163, 74, 0.28);
    margin-bottom: 0.7rem;
}

.area-mid {
    padding: 0.8rem 0.9rem;
    border-radius: 14px;
    background: rgba(245, 158, 11, 0.12);
    border: 1px solid rgba(245, 158, 11, 0.28);
    margin-bottom: 0.7rem;
}

.area-bad {
    padding: 0.8rem 0.9rem;
    border-radius: 14px;
    background: rgba(239, 68, 68, 0.12);
    border: 1px solid rgba(239, 68, 68, 0.28);
    margin-bottom: 0.7rem;
}

.flag-box {
    padding: 0.85rem 0.95rem;
    border-radius: 14px;
    background: rgba(59, 130, 246, 0.10);
    border: 1px solid rgba(59, 130, 246, 0.25);
    margin-bottom: 0.7rem;
}

.footer-note {
    color: #94a3b8;
    font-size: 0.9rem;
}
</style>
""", unsafe_allow_html=True)

# =========================
# BASE DE DATOS
# =========================
# Estructura por dominios tipo vigilancia del desarrollo
hitos_desarrollo = {
    2: {
        "motor_grueso": [
            "Levanta la cabeza en prono",
            "Mejor control cefálico"
        ],
        "motor_fino_adaptativo": [
            "Abre más las manos",
            "Sigue objetos con la mirada"
        ],
        "lenguaje": [
            "Hace sonidos vocálicos",
            "Balbuceo inicial"
        ],
        "personal_social": [
            "Sonrisa social",
            "Se calma con la voz del cuidador"
        ],
        "alarma": [
            "No sonrisa social",
            "No fija la mirada",
            "Hipotonía marcada"
        ]
    },

    4: {
        "motor_grueso": [
            "Sostén cefálico completo",
            "Se apoya en antebrazos en prono"
        ],
        "motor_fino_adaptativo": [
            "Lleva manos a la boca",
            "Toma objetos brevemente"
        ],
        "lenguaje": [
            "Ríe",
            "Balbucea"
        ],
        "personal_social": [
            "Reconoce cuidadores",
            "Disfruta la interacción"
        ],
        "alarma": [
            "No sostiene la cabeza",
            "No vocaliza",
            "Escasa interacción"
        ]
    },

    6: {
        "motor_grueso": [
            "Se voltea",
            "Se sienta con apoyo"
        ],
        "motor_fino_adaptativo": [
            "Toma objetos voluntariamente",
            "Transfiere objetos"
        ],
        "lenguaje": [
            "Balbuceo más variado",
            "Responde a sonidos"
        ],
        "personal_social": [
            "Responde a caras familiares",
            "Expresa alegría o disgusto"
        ],
        "alarma": [
            "No se voltea",
            "No toma objetos",
            "No interacción social"
        ]
    },

    9: {
        "motor_grueso": [
            "Se sienta sin apoyo",
            "Inicia gateo o desplazamiento"
        ],
        "motor_fino_adaptativo": [
            "Pinza inmadura",
            "Golpea objetos entre sí"
        ],
        "lenguaje": [
            "Dice bisílabos no específicos",
            "Responde a su nombre"
        ],
        "personal_social": [
            "Ansiedad ante extraños",
            "Juega a esconderse"
        ],
        "alarma": [
            "No se sienta solo",
            "No responde al nombre",
            "No se interesa por el entorno"
        ]
    },

    12: {
        "motor_grueso": [
            "Se pone de pie con apoyo",
            "Da pasos con ayuda o apoyado"
        ],
        "motor_fino_adaptativo": [
            "Pinza fina",
            "Señala objetos"
        ],
        "lenguaje": [
            "Dice 1 a 3 palabras con significado",
            "Entiende órdenes simples"
        ],
        "personal_social": [
            "Imita gestos",
            "Hace adiós"
        ],
        "alarma": [
            "No se pone de pie con apoyo",
            "No señala",
            "No dice palabras con significado"
        ]
    },

    18: {
        "motor_grueso": [
            "Camina solo",
            "Sube escalones con ayuda"
        ],
        "motor_fino_adaptativo": [
            "Hace torre de 2 a 3 cubos",
            "Garabatea"
        ],
        "lenguaje": [
            "Dice varias palabras",
            "Señala partes del cuerpo"
        ],
        "personal_social": [
            "Juego simbólico inicial",
            "Imita actividades del hogar"
        ],
        "alarma": [
            "No camina",
            "No tiene palabras comprensibles",
            "Pobre contacto social"
        ]
    },

    24: {
        "motor_grueso": [
            "Corre",
            "Patea pelota"
        ],
        "motor_fino_adaptativo": [
            "Torre de 4 a 6 cubos",
            "Pasa páginas"
        ],
        "lenguaje": [
            "Une 2 palabras",
            "Sigue órdenes simples"
        ],
        "personal_social": [
            "Juego paralelo",
            "Imita adultos"
        ],
        "alarma": [
            "No corre",
            "No combina 2 palabras",
            "No sigue instrucciones simples"
        ]
    },

    30: {  # 2-3 años
        "motor_grueso": [
            "Se empina con ambos pies",
            "Sube 2 escalones sin apoyo"
        ],
        "motor_fino_adaptativo": [
            "Rasga papel con pinza de ambas manos"
        ],
        "lenguaje": [
            "Dice su nombre completo"
        ],
        "personal_social": [
            "Identifica qué es de él y qué es de otros",
            "Dice los nombres de las personas con quienes vive o comparte"
        ],
        "alarma": [
            "No sube escaleras sin apoyo",
            "Lenguaje poco comprensible para cuidadores",
            "No identifica personas cercanas"
        ]
    },

    36: {
        "motor_grueso": [
            "Sube escaleras alternando parcialmente",
            "Salta con ambos pies"
        ],
        "motor_fino_adaptativo": [
            "Copia círculo simple"
        ],
        "lenguaje": [
            "Frases de 3 palabras",
            "Habla entendible para familiares"
        ],
        "personal_social": [
            "Juego imaginativo",
            "Comparte parcialmente"
        ],
        "alarma": [
            "No habla en frases",
            "No interacción social",
            "Caídas frecuentes"
        ]
    },

    48: {  # 3-4 años
        "motor_grueso": [
            "Camina en punta de pies",
            "Se para en un solo pie"
        ],
        "motor_fino_adaptativo": [
            "Copia círculo"
        ],
        "lenguaje": [
            "Define por su uso 5 objetos"
        ],
        "personal_social": [
            "Rechaza ayuda del cuidador cuando intenta hacer algo por sí mismo",
            "Comparte juego con otros niños"
        ],
        "alarma": [
            "No lenguaje funcional",
            "No juego con otros niños",
            "Dificultad motora evidente"
        ]
    },

    60: {  # 4-5 años
        "motor_grueso": [
            "Hace rebotar y agarra la pelota"
        ],
        "motor_fino_adaptativo": [
            "Figura humana rudimentaria"
        ],
        "lenguaje": [
            "Denomina 5 colores"
        ],
        "personal_social": [
            "Puede desvestirse y vestirse solo",
            "Propone juegos",
            "Sabe cuántos años tiene"
        ],
        "alarma": [
            "Lenguaje limitado",
            "No autonomía básica esperada",
            "No interacción social adecuada"
        ]
    }
}

AREAS = ["motor_grueso", "motor_fino_adaptativo", "lenguaje", "personal_social"]

# =========================
# ESTADO
# =========================
if "evaluar" not in st.session_state:
    st.session_state.evaluar = False

if "reset_counter" not in st.session_state:
    st.session_state.reset_counter = 0

# =========================
# FUNCIONES
# =========================
def buscar_edad_referencia(edad_meses: int):
    edades = sorted(hitos_desarrollo.keys())
    edad_ref = None
    for e in edades:
        if edad_meses >= e:
            edad_ref = e
    return edad_ref

def calcular_edad_corregida(edad_cronologica, edad_gestacional):
    if edad_gestacional >= 37:
        return float(edad_cronologica)
    semanas_prematurez = 40 - edad_gestacional
    meses_prematurez = semanas_prematurez / 4.0
    edad_corregida = edad_cronologica - meses_prematurez
    return round(max(edad_corregida, 0), 1)

def interpretar_resultado_global(fallas, alarmas_marcadas):
    if alarmas_marcadas >= 1:
        return "alerta", "🚨 SOSPECHA DE ALTERACIÓN DEL DESARROLLO / REQUIERE VALORACIÓN MÁS DETALLADA"
    if fallas == 0:
        return "ok", "✅ DESARROLLO APARENTEMENTE ACORDE PARA LA EDAD EVALUADA"
    if fallas <= 2:
        return "vigilar", "⚠️ HALLAZGOS PARA VIGILAR Y REEVALUAR EN PRÓXIMO CONTROL"
    return "alerta", "🚨 SOSPECHA DE RETRASO DEL DESARROLLO"

def interpretar_area(fallas_area, total_area):
    if fallas_area == 0:
        return "Conservada", "ok"
    if fallas_area < total_area:
        return "Con observaciones", "mid"
    return "Comprometida", "bad"

def detectar_banderas_orientativas(detalle_areas, alarmas_marcadas):
    """
    Lógica orientativa, NO validada como escala diagnóstica.
    """
    banderas = []

    fallas_motor = detalle_areas["motor_grueso"]["fallas"]
    fallas_fino = detalle_areas["motor_fino_adaptativo"]["fallas"]
    fallas_lenguaje = detalle_areas["lenguaje"]["fallas"]
    fallas_social = detalle_areas["personal_social"]["fallas"]

    if fallas_lenguaje >= 1:
        banderas.append("⚑ ALERTA DE LENGUAJE / COMUNICACIÓN: conviene ampliar interrogatorio y reevaluar lenguaje expresivo y comprensivo.")

    if fallas_motor + fallas_fino >= 2:
        banderas.append("⚑ ALERTA MOTORA: considerar revisión más detallada de motricidad gruesa, fina, tono, coordinación y desempeño funcional.")

    if fallas_social >= 1 and fallas_lenguaje >= 1:
        banderas.append("⚑ ALERTA SOCIAL-COMUNICATIVA: valorar con mayor detalle interacción social, juego compartido, comunicación y signos de alerta para TEA.")

    if alarmas_marcadas >= 1:
        banderas.append("⚑ HAY SIGNOS DE ALARMA MARCADOS: amerita profundizar valoración clínica y definir conducta según contexto.")

    return banderas

def generar_recomendacion_global(tipo_resultado, area_mas_comprometida, banderas):
    base = {
        "ok": "Continuar vigilancia habitual del desarrollo, reforzar estimulación en casa y reevaluar en control rutinario.",
        "vigilar": "Reforzar estimulación dirigida y programar reevaluación cercana del desarrollo.",
        "alerta": "Ampliar valoración clínica del neurodesarrollo y definir tamizaje o seguimiento especializado según hallazgos."
    }[tipo_resultado]

    extra = ""
    if area_mas_comprometida:
        extra += f" Área con mayor compromiso aparente: {area_mas_comprometida.replace('_', ' ')}."
    if banderas:
        extra += " Revisar especialmente las banderas orientativas generadas por la evaluación."
    return base + extra

def generar_resumen_medico(nombre, edad_ref, texto_edad, fallas, total_items, alarmas_marcadas, interpretacion, recomendacion, banderas):
    nombre_texto = nombre.strip() if nombre.strip() else "PACIENTE"
    texto_banderas = " | ".join(banderas) if banderas else "SIN BANDERAS ORIENTATIVAS ESPECÍFICAS."
    return (
        f"{nombre_texto}. VALORACIÓN DE NEURODESARROLLO SEGÚN HITOS ESPERADOS PARA {edad_ref} MESES. "
        f"EDAD EVALUADA: {texto_edad}. "
        f"ÍTEMS NO CUMPLIDOS: {fallas}/{total_items}. "
        f"SIGNOS DE ALARMA PRESENTES: {alarmas_marcadas}. "
        f"IMPRESIÓN CLÍNICA: {interpretacion}. "
        f"BANDERAS ORIENTATIVAS: {texto_banderas}. "
        f"CONDUCTA SUGERIDA: {recomendacion}"
    )

def generar_resumen_padres(nombre, tipo_resultado, recomendacion):
    nombre_texto = nombre.strip() if nombre.strip() else "Su hijo(a)"
    if tipo_resultado == "ok":
        return f"{nombre_texto} presenta habilidades esperadas para la edad evaluada. {recomendacion}"
    if tipo_resultado == "vigilar":
        return f"{nombre_texto} presenta algunos aspectos del desarrollo que conviene vigilar de cerca. {recomendacion}"
    return f"{nombre_texto} presenta hallazgos que requieren una valoración más detallada del desarrollo. {recomendacion}"

def limpiar_estado():
    claves_a_borrar = []
    for clave in list(st.session_state.keys()):
        if clave.startswith("chk_") or clave in {
            "nombre_paciente",
            "edad_cronologica",
            "prematuro",
            "edad_gestacional"
        }:
            claves_a_borrar.append(clave)

    for clave in claves_a_borrar:
        del st.session_state[clave]

    st.session_state.evaluar = False
    st.session_state.reset_counter += 1

# =========================
# ENCABEZADO
# =========================
st.markdown("""
<div class="main-header">
    <div class="main-title">🧠 App de Hitos del Neurodesarrollo</div>
    <div class="main-subtitle">Apoyo clínico para vigilancia del desarrollo infantil, desde lactante hasta 5 años.</div>
</div>
""", unsafe_allow_html=True)

# =========================
# CONTROLES SUPERIORES
# =========================
top1, top2, top3 = st.columns([1, 1, 1.2])

with top1:
    if st.button("🆕 Nueva evaluación", use_container_width=True):
        limpiar_estado()
        st.rerun()

with top2:
    if st.button("📋 Evaluar", use_container_width=True):
        st.session_state.evaluar = True

with top3:
    modo = st.radio(
        "Modo",
        ["Médico", "Padres"],
        horizontal=True,
        key=f"modo_{st.session_state.reset_counter}"
    )

# =========================
# PANEL SUPERIOR
# =========================
col_izq, col_der = st.columns([1.15, 1])

with col_izq:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Datos del paciente</div>', unsafe_allow_html=True)

    nombre = st.text_input(
        "Nombre del paciente",
        placeholder="Opcional",
        key="nombre_paciente"
    )

    edad_cronologica = st.number_input(
        "Edad cronológica (meses)",
        min_value=0,
        max_value=60,
        value=12,
        key="edad_cronologica"
    )

    prematuro = st.checkbox(
        "Antecedente de prematuridad",
        key="prematuro"
    )

    edad_gestacional = None
    if prematuro:
        edad_gestacional = st.number_input(
            "Edad gestacional al nacimiento (semanas)",
            min_value=22,
            max_value=36,
            value=34,
            key="edad_gestacional"
        )

    st.markdown('</div>', unsafe_allow_html=True)

with col_der:
    edad_utilizada = edad_cronologica
    texto_edad = f"{edad_cronologica} meses"

    if prematuro and edad_gestacional is not None:
        edad_corregida = calcular_edad_corregida(edad_cronologica, edad_gestacional)
        edad_utilizada = int(round(edad_corregida))
        texto_edad = f"{edad_cronologica} meses cronológicos / {edad_corregida} meses corregidos"

    edad_ref = buscar_edad_referencia(edad_utilizada)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Referencia de evaluación</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="small-label">Edad evaluada</div><div>{texto_edad}</div>', unsafe_allow_html=True)

    if prematuro and edad_gestacional is not None:
        st.markdown(f'<div class="small-label" style="margin-top:0.6rem;">Edad corregida usada</div><div>{edad_utilizada} meses</div>', unsafe_allow_html=True)

    st.markdown(f'<div class="small-label" style="margin-top:0.6rem;">Edad de referencia</div><div>{edad_ref if edad_ref is not None else "No disponible"} meses</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

if edad_ref is None:
    st.warning("No hay hitos cargados para esa edad todavía.")
    st.stop()

datos = hitos_desarrollo[edad_ref]

# =========================
# EVALUACIÓN
# =========================
st.markdown("## Evaluación por áreas")

tabs = st.tabs([
    "Motor grueso",
    "Motor fino-adaptativo",
    "Audición y lenguaje",
    "Personal-social",
    "Signos de alarma"
])

for idx, area in enumerate(AREAS):
    with tabs[idx]:
        titulo = area.replace("_", " ").title()
        st.markdown(f"### {titulo}")
        st.caption("Deje marcado si el niño cumple el hito.")
        for i, item in enumerate(datos[area]):
            st.checkbox(
                item,
                value=True,
                key=f"chk_{edad_ref}_{area}_{i}_{st.session_state.reset_counter}"
            )

with tabs[4]:
    st.markdown("### Signos de alarma")
    st.caption("Marque solo los signos de alarma presentes.")
    for i, item in enumerate(datos["alarma"]):
        st.checkbox(
            item,
            value=False,
            key=f"chk_{edad_ref}_alarma_{i}_{st.session_state.reset_counter}"
        )

# =========================
# RESULTADOS
# =========================
if st.session_state.evaluar:
    total_items = 0
    fallas = 0
    detalle_areas = {}

    for area in AREAS:
        total_area = len(datos[area])
        fallas_area = 0

        for i, _ in enumerate(datos[area]):
            total_items += 1
            valor = st.session_state.get(
                f"chk_{edad_ref}_{area}_{i}_{st.session_state.reset_counter}",
                True
            )
            if not valor:
                fallas += 1
                fallas_area += 1

        detalle_areas[area] = {
            "fallas": fallas_area,
            "total": total_area
        }

    alarmas_marcadas = 0
    for i, _ in enumerate(datos["alarma"]):
        valor = st.session_state.get(
            f"chk_{edad_ref}_alarma_{i}_{st.session_state.reset_counter}",
            False
        )
        if valor:
            alarmas_marcadas += 1

    area_mas_comprometida = None
    max_fallas = 0
    for area, info in detalle_areas.items():
        if info["fallas"] > max_fallas:
            max_fallas = info["fallas"]
            area_mas_comprometida = area

    tipo_resultado, interpretacion_texto = interpretar_resultado_global(fallas, alarmas_marcadas)
    banderas = detectar_banderas_orientativas(detalle_areas, alarmas_marcadas)
    recomendacion = generar_recomendacion_global(tipo_resultado, area_mas_comprometida, banderas)

    st.markdown("---")
    st.markdown("## Resultado clínico")

    if tipo_resultado == "ok":
        st.success(interpretacion_texto)
    elif tipo_resultado == "vigilar":
        st.warning(interpretacion_texto)
    else:
        st.error(interpretacion_texto)

    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric("Edad ref.", f"{edad_ref} m")
    with m2:
        st.metric("No cumplidos", f"{fallas}/{total_items}")
    with m3:
        st.metric("Alarmas", alarmas_marcadas)
    with m4:
        st.metric(
            "Área más afectada",
            area_mas_comprometida.replace("_", " ").title() if area_mas_comprometida else "Ninguna"
        )

    st.markdown("### Análisis por áreas")
    c1, c2 = st.columns(2)
    lista_areas = list(detalle_areas.items())

    for idx, (area, info) in enumerate(lista_areas):
        estado_texto, clase = interpretar_area(info["fallas"], info["total"])
        css_class = "area-ok" if clase == "ok" else "area-mid" if clase == "mid" else "area-bad"

        bloque = f"""
        <div class="{css_class}">
            <strong>{area.replace('_', ' ').title()}</strong><br>
            Estado: {estado_texto}<br>
            Ítems no cumplidos: {info['fallas']}/{info['total']}
        </div>
        """

        if idx % 2 == 0:
            with c1:
                st.markdown(bloque, unsafe_allow_html=True)
        else:
            with c2:
                st.markdown(bloque, unsafe_allow_html=True)

    st.markdown("### Banderas orientativas")
    if banderas:
        for bandera in banderas:
            st.markdown(f'<div class="flag-box">{bandera}</div>', unsafe_allow_html=True)
    else:
        st.success("Sin banderas orientativas específicas con la lógica actual de la app.")

    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.markdown("**Conducta sugerida**")
    st.write(recomendacion)
    st.markdown('</div>', unsafe_allow_html=True)

    if modo == "Médico":
        resumen = generar_resumen_medico(
            nombre=nombre,
            edad_ref=edad_ref,
            texto_edad=texto_edad,
            fallas=fallas,
            total_items=total_items,
            alarmas_marcadas=alarmas_marcadas,
            interpretacion=interpretacion_texto,
            recomendacion=recomendacion,
            banderas=banderas
        )
        st.markdown("### Resumen para historia clínica")
        st.text_area("Texto copiable", value=resumen, height=240)

    else:
        resumen_padres = generar_resumen_padres(
            nombre=nombre,
            tipo_resultado=tipo_resultado,
            recomendacion=recomendacion
        )
        st.markdown("### Resumen explicativo para padres")
        st.text_area("Texto explicativo", value=resumen_padres, height=220)

    st.markdown(
        '<div class="footer-note">Herramienta de apoyo clínico para vigilancia del desarrollo. '
        'No reemplaza la valoración integral ni una escala validada de tamizaje.</div>',
        unsafe_allow_html=True
    )
else:
    st.info("Complete la evaluación y pulse **Evaluar** para generar el análisis clínico.")
