import streamlit as st

# ============================================================
# CONFIGURACIÓN GENERAL
# ============================================================

st.set_page_config(
    page_title="Asistente de Deprescripción",
    layout="wide"
)

st.title("🧠 Asistente de Deprescripción y Conciliación")
st.markdown(
    "Sistema de apoyo a la decisión clínica basado en criterios BEERS, STOPP y guías clínicas. "
    "**Requiere siempre validación por el clínico.**"
)

# ============================================================
# DEFINICIÓN DE REGLAS CLÍNICAS (EJEMPLO REPRESENTATIVO)
# ============================================================

reglas = [
    {
        "id": "BEERS_01",
        "nombre": "Benzodiacepinas de vida media larga",
        "condiciones": {
            "edad_min": 65,
            "farmacos": ["diazepam", "clorazepato", "flurazepam"]
        },
        "problema": "Riesgo aumentado de caídas, sedación y deterioro cognitivo",
        "recomendacion": "Evitar benzodiacepinas de vida media larga. Considerar retirada progresiva.",
        "fuente": "Criterios Beers"
    },
    {
        "id": "STOPP_01",
        "nombre": "AINEs crónicos en insuficiencia renal",
        "condiciones": {
            "edad_min": 65,
            "egfr_max": 60,
            "farmacos": ["ibuprofeno", "diclofenaco", "naproxeno"]
        },
        "problema": "Riesgo de deterioro renal y sangrado gastrointestinal",
        "recomendacion": "Evitar AINEs crónicos.",
        "fuente": "STOPP"
    },
    {
        "id": "BEERS_02",
        "nombre": "Hipnóticos tipo Z en pacientes ancianos",
        "condiciones": {
            "edad_min": 65,
            "farmacos": ["zolpidem", "zopiclona", "zaleplon"]
    },
    "problema": "Riesgo aumentado de caídas, fracturas y deterioro cognitivo",
    "recomendacion": "Evitar hipnóticos tipo Z en ancianos.",
    "fuente": "Criterios Beers"
    },
    {
    "id": "BEERS_03",
    "nombre": "Alta carga anticolinérgica en ≥65 años",
    "condiciones": {
        "edad_min": 65,
        "farmacos": ["amitriptilina", "clorfeniramina", "oxibutinina"]
    },
    "problema": "Confusión, estreñimiento, retención urinaria y deterioro cognitivo",
    "recomendacion": "Evitar fármacos con alta carga anticolinérgica.",
    "fuente": "Beers / STOPP"
    },
    {
    "id": "BEERS_04",
    "nombre": "Uso prolongado de inhibidores de la bomba de protones",
    "condiciones": {
        "edad_min": 65,
        "farmacos": ["omeprazol", "pantoprazol", "lansoprazol"]
    },
    "problema": "Riesgo de fracturas, infecciones y déficits de micronutrientes",
    "recomendacion": "Reevaluar indicación del IBP y considerar retirada progresiva.",
    "fuente": "Beers / STOPP"
    },
    {
    "id": "BEERS_05",
    "nombre": "Sulfonilureas de larga duración en ancianos",
    "condiciones": {
        "edad_min": 65,
        "farmacos": ["glibenclamida", "glimepirida"]
    },
    "problema": "Riesgo elevado de hipoglucemia prolongada",
    "recomendacion": "Evitar sulfonilureas de larga duración.",
    "fuente": "Criterios Beers"
    },
  {
    "id": "STOPP_SRAA_01",
    "nombre": "Doble bloqueo del sistema renina-angiotensina",
    "condiciones": {
        "farmacos": [
            "enalapril", "lisinopril",
            "losartan", "valsartan",
            "candesartan", "irbesartan",
            "aliskiren"
        ],
        "minimo_coincidencias": 2
    },
    "problema": "Riesgo aumentado de insuficiencia renal, hiperpotasemia e hipotensión",
    "recomendacion": "Evitar el doble bloqueo del sistema renina-angiotensina.",
    "fuente": "STOPP"

    },
    {
    "id": "BEERS_AD_01",
    "nombre": "Antidepresivos tricíclicos en ≥65 años",
    "condiciones": {
        "edad_min": 65,
        "farmacos": [
            "amitriptilina",
            "imipramina",
            "clomipramina",
            "doxepina"
        ]
    },
    "problema": "Alta carga anticolinérgica, sedación, hipotensión ortostática y riesgo de caídas",
    "recomendacion": "Evitar antidepresivos tricíclicos en pacientes ancianos. Considerar alternativas más seguras.",
    "fuente": "Criterios Beers"
    },
    {
    "id": "BEERS_AD_02",
    "nombre": "Paroxetina en pacientes ≥65 años",
    "condiciones": {
        "edad_min": 65,
        "farmacos": ["paroxetina"]
    },
    "problema": "Efecto anticolinérgico elevado con riesgo de confusión y caídas",
    "recomendacion": "Evitar paroxetina en ancianos. Considerar ISRS con mejor perfil de seguridad.",
    "fuente": "Criterios Beers"
    },
    {
    "id": "BEERS_AD_03",
    "nombre": "ISRS y riesgo de caídas en ≥65 años",
    "condiciones": {
        "edad_min": 65,
        "farmacos": [
            "sertralina",
            "fluoxetina",
            "paroxetina",
            "citalopram",
            "escitalopram",
            "fluvoxamina"
        ]
    },
    "problema": "Mayor riesgo de caídas y fracturas en pacientes ancianos",
    "recomendacion": "Reevaluar balance beneficio-riesgo del ISRS y vigilar riesgo de caídas.",
    "fuente": "Criterios Beers"
    },
    {
    "id": "BEERS_AD_04",
    "nombre": "Citalopram y escitalopram en ≥65 años",
    "condiciones": {
        "edad_min": 65,
        "farmacos": ["citalopram", "escitalopram"]
    },
    "problema": "Riesgo de prolongación del intervalo QT y arritmias",
    "recomendacion": "Usar con precaución en ancianos y reevaluar necesidad.",
    "fuente": "Criterios Beers"
    },
    {
    "id": "STOPP_AD_01",
    "nombre": "ISRS combinados con AINEs",
    "condiciones": {
        "farmacos": [
            "sertralina",
            "fluoxetina",
            "paroxetina",
            "citalopram",
            "escitalopram"
        ],
        "farmacos_combinados": [
            "ibuprofeno",
            "diclofenaco",
            "naproxeno"
        ]
    },
    "problema": "Aumento del riesgo de hemorragia gastrointestinal",
    "recomendacion": "Evitar la combinación o valorar gastroprotección.",
    "fuente": "STOPP"
    },
    {
    "id": "STOPP_DIU_02",
    "nombre": "Diuréticos tiazídicos con insuficiencia renal",
    "condiciones": {
        "edad_min": 65,
        "egfr_max": 30,
        "farmacos": ["hidroclorotiazida", "indapamida", "clortalidona"]
    },
    "problema": "Escasa eficacia y mayor riesgo de toxicidad en insuficiencia renal",
    "recomendacion": "Evitar diuréticos tiazídicos en eGFR <30 ml/min.",
    "fuente": "STOPP"
    },
    {
    "id": "STOPP_DIU_03",
    "nombre": "Diuréticos ahorradores de potasio combinados con IECA/ARA II",
    "condiciones": {
        "farmacos": ["espironolactona", "eplerenona"],
        "farmacos_combinados": [
            "enalapril", "lisinopril",
            "losartan", "valsartan"
        ]
    },
    "problema": "Riesgo elevado de hiperpotasemia e insuficiencia renal",
    "recomendacion": "Evitar la combinación o monitorizar estrechamente potasio y función renal.",
    "fuente": "STOPP"
    },
    {
    "id": "STOPP_DIU_05",
    "nombre": "Uso simultáneo de múltiples diuréticos",
    "condiciones": {
        "farmacos": [
            "furosemida", "torasemida",
            "hidroclorotiazida", "indapamida",
            "espironolactona"
        ],
        "minimo_coincidencias": 2
    },
    "problema": "Mayor riesgo de deshidratación, alteraciones electrolíticas e hipotensión",
    "recomendacion": "Reevaluar combinación de diuréticos y ajustar tratamiento.",
    "fuente": "STOPP"
    },
 {
    "id": "IND_OAC_01",
    "tipo": "conciliacion",
    "nombre": "Anticoagulante sin indicación documentada",
    "condiciones": {
        "farmacos": [
            "apixaban",
            "rivaroxaban",
            "dabigatran",
            "edoxaban",
            "warfarina",
            "acenocumarol"
        ],
        "diagnosticos_ausentes": [
            "fibrilacion auricular",
            "fa",
            "tromboembolismo venoso",
            "embolia pulmonar"
        ]
    },
    "problema": "Tratamiento anticoagulante sin indicación registrada",
    "recomendacion": "Revisar y documentar la indicación clínica del anticoagulante.",
    "fuente": "Conciliación",
    "prioridad": "media"

    },
    {
    "id": "CRIT_HEM_01",
    "nombre": "Anticoagulante oral combinado con AINE",
    "condiciones": {
        "farmacos": [
            "apixaban", "rivaroxaban", "dabigatran",
            "warfarina", "acenocumarol"
        ],
        "farmacos_combinados": [
            "ibuprofeno", "diclofenaco", "naproxeno"
        ]
    },
    "problema": "Riesgo muy elevado de hemorragia gastrointestinal y sangrados graves",
    "recomendacion": "Evitar la combinación. Considerar alternativas analgésicas o gastroprotección.",
    "fuente": "STOPP"
    },
    {
    "id": "CRIT_CNS_01",
    "nombre": "Benzodiacepina combinada con opioide",
    "condiciones": {
        "farmacos": [
            "diazepam", "lorazepam", "alprazolam",
            "clonazepam", "zolpidem"
        ],
        "farmacos_combinados": [
            "morfina", "oxicodona", "fentanilo",
            "tramadol"
        ]
    },
    "problema": "Riesgo elevado de sedación profunda, depresión respiratoria y muerte",
    "recomendacion": "Evitar la combinación. Reevaluar necesidad de ambos tratamientos.",
    "fuente": "Beers / STOPP"
    },
    {
    "id": "CRIT_CARD_01",
    "nombre": "Digoxina sin indicación documentada",
    "condiciones": {
        "farmacos": ["digoxina"],
        "diagnosticos_requeridos": [
            "fibrilacion auricular",
            "insuficiencia cardiaca"
        ]
    },
    "problema": "Uso de digoxina sin indicación clara con riesgo de toxicidad",
    "recomendacion": "Revisar indicación y valorar deprescripción.",
    "fuente": "Conciliación / STOPP"
    },
    {
    "id": "CRIT_CNS_02",
    "nombre": "Antipsicótico sin indicación documentada",
    "condiciones": {
        "edad_min": 65,
        "farmacos": [
            "quetiapina", "risperidona",
            "haloperidol", "olanzapina"
        ],
        "diagnosticos_requeridos": [
            "psicosis",
            "esquizofrenia",
            "trastorno bipolar"
        ]
    },
    "problema": "Uso de antipsicóticos sin indicación clara con aumento de mortalidad",
    "recomendacion": "Revisar indicación y considerar retirada progresiva.",
    "fuente": "Beers / STOPP"
    },
    {
    "id": "CRIT_ELECT_01",
    "nombre": "ISRS combinado con diurético",
    "condiciones": {
        "farmacos": [
            "sertralina", "citalopram",
            "escitalopram", "fluoxetina"
        ],
        "farmacos_combinados": [
            "furosemida", "hidroclorotiazida",
            "indapamida"
        ]
    },
    "problema": "Riesgo elevado de hiponatremia y síndrome confusional",
    "recomendacion": "Monitorizar sodio y reevaluar la combinación.",
    "fuente": "Beers"
    },
    {
    "id": "CRIT_DM_01",
    "nombre": "Metformina en insuficiencia renal avanzada",
    "condiciones": {
        "egfr_max": 30,
        "farmacos": ["metformina"]
    },
    "problema": "Riesgo de acidosis láctica en insuficiencia renal avanzada",
    "recomendacion": "Suspender metformina en eGFR <30 ml/min.",
    "fuente": "Guías clínicas / STOPP"
    },
    {
    "id": "CRIT_HEM_03",
    "nombre": "Anticoagulante combinado con doble antiagregación",
    "condiciones": {
        "farmacos": [
            "apixaban", "rivaroxaban", "dabigatran",
            "warfarina", "acenocumarol"
        ],
        "farmacos_combinados": [
            "aspirina",
            "clopidogrel"
        ],
        "minimo_coincidencias": 2
    },
    "problema": "Riesgo muy elevado de sangrado con escaso beneficio en la mayoría de casos",
    "recomendacion": "Reevaluar necesidad de antiagregación asociada a anticoagulación.",
    "fuente": "STOPP"
    },
    {
    "id": "CRIT_NEURO_01",
    "nombre": "Antiepiléptico sin diagnóstico documentado de epilepsia",
    "condiciones": {
        "farmacos": [
            "levetiracetam",
            "valproico",
            "carbamazepina"
        ],
        "diagnosticos_requeridos": ["epilepsia"]
    },
    "problema": "Uso de antiepilépticos sin indicación clara con riesgo de sedación y deterioro cognitivo",
    "recomendacion": "Revisar indicación del antiepiléptico y valorar deprescripción.",
    "fuente": "Conciliación / STOPP"
    },
    {
    "id": "CRIT_NEURO_02",
    "nombre": "Tramadol combinado con ISRS o IRSN",
    "condiciones": {
        "farmacos": ["tramadol"],
        "farmacos_combinados": [
            "sertralina", "fluoxetina", "paroxetina",
            "citalopram", "escitalopram", "venlafaxina"
        ]
    },
    "problema": "Riesgo de síndrome serotoninérgico y convulsiones",
    "recomendacion": "Evitar la combinación y considerar alternativas analgésicas.",
    "fuente": "STOPP"
    },
    {
    "id": "CRIT_NEURO_03",
    "nombre": "Linezolid combinado con ISRS o IRSN",
    "condiciones": {
        "farmacos": ["linezolid"],
        "farmacos_combinados": [
            "sertralina", "fluoxetina", "paroxetina",
            "citalopram", "escitalopram", "venlafaxina"
        ]
    },
    "problema": "Riesgo de síndrome serotoninérgico y convulsiones",
    "recomendacion": "Evitar la combinación y considerar alternativas analgésicas.",
    "fuente": "STOPP"
    },
    {
    "id": "CRIT_GI_01",
    "nombre": "Uso prolongado de corticoides sistémicos",
    "condiciones": {
        "farmacos": [
            "prednisona",
            "metilprednisolona",
            "dexametasona"
        ]
    },
    "problema": "Riesgo de osteoporosis, infecciones, diabetes y sangrado digestivo",
    "recomendacion": "Reevaluar indicación y duración del tratamiento corticoide.",
    "fuente": "STOPP"
    },
    {
    "id": "CRIT_RESP_01",
    "nombre": "Benzodiacepinas en pacientes con EPOC",
    "condiciones": {
        "farmacos": [
            "diazepam", "lorazepam", "alprazolam"
        ],
        "diagnosticos_requeridos": ["epoc"]
    },
    "problema": "Riesgo de depresión respiratoria y exacerbaciones",
    "recomendacion": "Evitar benzodiacepinas en pacientes con EPOC.",
    "fuente": "Beers / STOPP"
    },
    {
    "id": "HF_01",
    "nombre": "AINEs en insuficiencia cardíaca",
    "condiciones": {
        "diagnosticos_requeridos": ["insuficiencia cardiaca"],
        "farmacos": ["ibuprofeno", "diclofenaco", "naproxeno"]
    },
    "problema": "Empeoramiento de la insuficiencia cardíaca y riesgo de descompensación",
    "recomendacion": "Evitar AINEs en pacientes con insuficiencia cardíaca.",
    "fuente": "STOPP / Guías de IC"
    },
    {
    "id": "HF_02",
    "nombre": "Calcioantagonistas no dihidropiridínicos en IC",
    "condiciones": {
        "diagnosticos_requeridos": ["insuficiencia cardiaca"],
        "farmacos": ["verapamilo", "diltiazem"]
    },
    "problema": "Efecto inotrópico negativo y aumento del riesgo de descompensación",
    "recomendacion": "Evitar verapamilo y diltiazem en insuficiencia cardíaca.",
    "fuente": "STOPP / Guías de IC"
    },
    {
    "id": "HF_10",
    "nombre": "Fibrilación auricular sin anticoagulación en IC",
    "condiciones": {
        "diagnosticos_requeridos": [
            "insuficiencia cardiaca",
            "fibrilacion auricular"
        ],
        "farmacos_ausentes": [
            "apixaban", "rivaroxaban",
            "dabigatran", "warfarina",
            "acenocumarol"
        ]
    },
    "problema": "Riesgo elevado de ictus por ausencia de anticoagulación",
    "recomendacion": "Valorar anticoagulación según balance riesgo-beneficio.",
    "fuente": "START / Guías de IC"
    },
    {
    "id": "COPD_06",
    "nombre": "Uso de teofilina en EPOC",
    "condiciones": {
        "diagnosticos_requeridos": ["epoc"],
        "farmacos": ["teofilina"]
    },
    "problema": "Alto riesgo de toxicidad con beneficio limitado",
    "recomendacion": "Reevaluar uso de teofilina y considerar alternativas inhaladas.",
    "fuente": "STOPP / Guías GOLD"
    },
    {
    "id": "COPD_07",
    "nombre": "Betabloqueantes no cardioselectivos en EPOC",
    "condiciones": {
        "diagnosticos_requeridos": ["epoc"],
        "farmacos": [
            "propranolol",
            "nadolol"
        ]
    },
    "problema": "Riesgo de broncoespasmo y deterioro respiratorio",
    "recomendacion": "Evitar betabloqueantes no cardioselectivos en EPOC.",
    "fuente": "STOPP / Guías clínicas"
    },
    {
    "id": "COPD_08",
    "nombre": "EPOC sin tratamiento broncodilatador",
    "condiciones": {
        "diagnosticos_requeridos": ["epoc"],
        "farmacos_ausentes": [
            "salbutamol",
            "formoterol",
            "salmeterol",
            "tiotropio"
        ]
    },
    "problema": "Ausencia de tratamiento broncodilatador esencial",
    "recomendacion": "Valorar inicio de broncodilatador inhalado.",
    "fuente": "START / Guías GOLD"
}    
]

# ============================================================
# MOTOR DE EVALUACIÓN
# ============================================================
def evaluar_regla(regla, paciente):

    cond = regla["condiciones"]

    # =====================================================
    # 0. CONCILIACIÓN: fármaco presente + diagnóstico AUSENTE
    # =====================================================
    if "diagnosticos_ausentes" in cond:

        # Debe tomar el fármaco
        if "farmacos" in cond:
            toma_farmaco = any(
                f in paciente["medicamentos"]
                for f in cond["farmacos"]
            )
            if not toma_farmaco:
                return False

        # NO debe tener ninguno de los diagnósticos que justifican el fármaco
        tiene_indicacion = any(
            d in paciente.get("diagnosticos", [])
            for d in cond["diagnosticos_ausentes"]
        )

        return not tiene_indicacion

    # =====================================================
    # 1. START: diagnóstico presente + fármaco AUSENTE
    # =====================================================
    if "farmacos_ausentes" in cond:

        if "diagnosticos_requeridos" in cond:
            tiene_dx = any(
                d in paciente.get("diagnosticos", [])
                for d in cond["diagnosticos_requeridos"]
            )
            if not tiene_dx:
                return False

        toma_alguno = any(
            f in paciente["medicamentos"]
            for f in cond["farmacos_ausentes"]
        )

        return not toma_alguno

    # =====================================================
    # 2. COMBINACIONES (A + B)
    # =====================================================
    if "farmacos_combinados" in cond:
        grupo_a = cond.get("farmacos", [])
        grupo_b = cond.get("farmacos_combinados", [])

        hay_a = any(f in paciente["medicamentos"] for f in grupo_a)
        hay_b = any(f in paciente["medicamentos"] for f in grupo_b)

        return hay_a and hay_b

    # =====================================================
    # 3. CONTEO (≥ X fármacos)
    # =====================================================
    if "minimo_coincidencias" in cond:
        contador = sum(
            1 for f in cond.get("farmacos", [])
            if f in paciente["medicamentos"]
        )
        return contador >= cond["minimo_coincidencias"]

    # =====================================================
    # 4. STOPP / BEERS
    # =====================================================
    if "edad_min" in cond:
        if paciente["edad"] < cond["edad_min"]:
            return False

    if "egfr_max" in cond:
        if paciente["egfr"] >= cond["egfr_max"]:
            return False

    if "diagnosticos_requeridos" in cond:
        tiene_dx = any(
            d in paciente.get("diagnosticos", [])
            for d in cond["diagnosticos_requeridos"]
        )
        if not tiene_dx:
            return False

    if "farmacos" in cond:
        if not any(f in paciente["medicamentos"] for f in cond["farmacos"]):
            return False

    return True

def evaluar_paciente(paciente):
    alertas = []
    for regla in reglas:
        if evaluar_regla(regla, paciente):
            alertas.append(regla)
    return alertas

# ============================================================
# INTERFAZ – ENTRADA DE DATOS
# ============================================================

st.header("📋 Datos del paciente")

col1, col2 = st.columns(2)

with col1:
    edad = st.number_input("Edad", min_value=0, max_value=120, value=75)
    egfr = st.number_input("eGFR (ml/min)", min_value=0.0, value=45.0)

with col2:
    diagnosticos = st.multiselect(
        "Diagnósticos",
        [
            "insuficiencia cardiaca",
            "fibrilacion auricular",
            "epoc",
            "diabetes",
            "demencia",
        ]
    )

st.subheader("💊 Medicación activa")

medicacion_texto = st.text_area(
    "Introduce los medicamentos (uno por línea o separados por comas):",
    placeholder="Ejemplo:\napixaban\nibuprofeno\nenalapril"
)

# Procesar el texto introducido
medicamentos = []
if medicacion_texto:
    medicamentos = [
        m.strip().lower()
        for m in medicacion_texto.replace(",", "\n").split("\n")
        if m.strip()
    ]
# ANÁLISIS
# ------------------------------
with st.form("form_analisis"):
    submit = st.form_submit_button("🔍 Analizar medicación")

if submit:
    paciente = {
        "edad": edad,
        "egfr": egfr,
        "diagnosticos": diagnosticos,
        "medicamentos": medicamentos
    }

    alertas = evaluar_paciente(paciente)

    st.header("📊 Resultados del análisis")

    if not alertas:
        st.success("✅ No se detectan problemas de medicación relevantes.")
    else:
        for a in alertas:
            prioridad = a.get("prioridad", "media")

            if prioridad == "critica":
                st.error(f"🔴 {a['nombre']}")
            elif prioridad == "alta":
                st.warning(f"🟠 {a['nombre']}")
            else:
                st.info(f"🔵 {a['nombre']}")

            st.markdown(f"**Problema:** {a['problema']}")
            st.markdown(f"**Recomendación:** {a['recomendacion']}")
            st.markdown(f"_Fuente: {a['fuente']}_")
            st.markdown("---")
