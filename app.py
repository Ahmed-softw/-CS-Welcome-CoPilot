import streamlit as st
import pypdf
import json
import requests

# 1. إعداد واجهة الويب الفخمة لتناسب تخصصات الحاسب
st.set_page_config(page_title="CS Welcome Co-Pilot", page_icon="💻", layout="wide")

st.markdown("""
    <style>
    .main-title { font-size: 34px; font-weight: bold; color: #38BDF8; text-align: center; margin-bottom: 5px; }
    .sub-title { font-size: 18px; color: #475569; text-align: center; margin-bottom: 25px; }
    .stButton>button { width: 100%; background-color: #0284C7; color: white; border-radius: 8px; font-weight: bold; }
    .roadmap-card { background-color: #1E293B; padding: 22px; border-radius: 12px; border-top: 4px solid #38BDF8; margin-bottom: 20px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); }
    .satr-card { background-color: #1E293B; padding: 22px; border-radius: 12px; border-top: 4px solid #F59E0B; margin-bottom: 20px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); }
    .card-title { font-size: 22px; font-weight: bold; color: #F8FAFC; margin-bottom: 10px; display: flex; align-items: center; gap: 10px; }
    .card-text { font-size: 15px; color: #CBD5E1; line-height: 1.6; margin-bottom: 15px; }
    .video-header { font-size: 20px; font-weight: bold; color: #38BDF8; margin-top: 15px; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">💻 المساعد الرقمي للطلاب الجدد في تخصصات الحاسب</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">منصة الإرشاد الذكي وأتمتة المحاضرة الأولى بالجامعة</div>', unsafe_allow_html=True)

# 2. ضع مفتاحك الجديد المبتدئ بـ gsk_ هنا مباشرة بيدك بين علامتي التنصيص
GROQ_API_KEY = "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"

if "quiz_data" not in st.session_state:
    st.session_state.quiz_data = None
if "merged_text" not in st.session_state:
    st.session_state.merged_text = ""

# 3. تقسيم الواجهة والتبويبات المعتمدة بطلبك دقة
tab_intro_videos, tab_roadmap, tab_syllabus, tab_quiz = st.tabs([
    "🎥 الفيديوهات التوجيهية والشرح",
    "🚀 مسار المهندس الناجح", 
    "📚 pdf ارفع ملفك وخلني اللخصه لك ", 
    "🧠 pdf اختبارات تفاعلية بس ارسل "
])

# ==================== التبويب الأول ====================
with tab_intro_videos:
    st.subheader("🎥 الفيديوهات التوجيهية والشرح")
    col_vid1, col_vid2 = st.columns(2)
    with col_vid1:
        st.markdown('<div class="video-header">👋 1. فيديو المقدمة والتعريف بالفكرة</div>', unsafe_allow_html=True)
        st.write("في هذا الفيديو أُعرفك بنفسي كطالب هندسة برمجيات، وأشرح لك كيف جاءتني فكرة المشروع بناءً على الصعوبات التي عشتها.")
        st.video("https://youtube.com") 
    with col_vid2:
        st.markdown('<div class="video-header">🛠️ 2. كيف تسجل دخول علي منصة سطر التعليمية</div>', unsafe_allow_html=True)
        st.write("كيف تنزل الملف في الموقع وكيف تدخل دوراة سطر ")
        st.video("https://youtube.com")

# ==================== التبويب الثاني ====================
with tab_roadmap:
    st.subheader("🎯 خطوات جوهرية بناءً على تجربتي الشخصية لحمايتك من الضياع المعرفي:")
    col_left, col_right = st.columns(2)
    with col_left:
        st.markdown("""<div class="roadmap-card"><div class="card-title">🐙 1. منصة GitHub وبناء المعرض</div><div class="card-text">أولاً_ اصنع حساب GitHub لأنه هو بيكون المعرض الخاص بك بحيث تسجل فيه جميع انجازاتك الدراسية زي اللابات.</div></div>""", unsafe_allow_html=True)
        st.checkbox("أنشأت حساب في GitHub وربطته بـ Git بنجاح", key="chk_github")
        st.markdown("""<div class="roadmap-card"><div class="card-title">💼 2. منصة LinkedIn وبناء العلاقات</div><div class="card-text">التخصص لا يقتصر على المذاكرة فقط، بل يحتاج بناء شبكة علاقات قوية وتتبع التقنيات المطلوبة بالسوق.</div></div>""", unsafe_allow_html=True)
        st.checkbox("أنشأت حساب LinkedIn احترافي ورابطته بتخصصي", key="chk_linkedin")
    with col_right:
        st.markdown("""<div class="satr-card"><div class="card-title">🚀 3. منصة سطر التعليمية (Satr.codes)</div><div class="card-text">منصة سطر هي الخيار المثالي والمجاني بالكامل باللغة العربية. أنصحك بالبدء فوراً في مسارات لغة Python ومسارات الـ Full-Stack.</div></div>""", unsafe_allow_html=True)
        st.checkbox("سجلت في منصة سطر وبدأت أول مسار برمي تطبيقي", key="chk_satr")
        st.markdown("""<div class="roadmap-card"><div class="card-title">📝 4. التوثيق الرقمي المستمر (Dev Journal)</div><div class="card-text">وثق واكتب وسجل كل لغة برمجة، أداة، أو خوارزمية تفهمها في مفكرة رقمية مثل Notion لكي لا تنسى عند التدريب.</div></div>""", unsafe_allow_html=True)
        st.checkbox("أنشأت مفكرتي الرقمية الخاصة لتوثيق كل مهارة أتعلمها", key="chk_journal")

# ==================== التبويب الثالث ====================
with tab_syllabus:
    st.subheader("📚 pdf ارفع ملفك وخلني اللخصه لك")
    uploaded_files = st.file_uploader("ارفع ملفات الـ PDF الخاصة بالمواد الدراسية هنا", type=["pdf"], accept_multiple_files=True)
    if uploaded_files:
        st.success(f"🔒 تم رفع {len(uploaded_files)} ملفات بنجاح وجاري إعداد معالج البث الفوري!")
        all_text = ""
        for uploaded_file in uploaded_files:
            try:
                pdf_reader = pypdf.PdfReader(uploaded_file)
                for page in pdf_reader.pages:
                    text = page.extract_text()
                    if text: all_text += text + "\n"
            except: pass
        st.session_state.merged_text = all_text[:15000]

        if st.session_state.merged_text and st.button("📝 استخراج ملخص فوري شامل"):
            if GROQ_API_KEY == "ضع_مفتاح_GROQ_الخاص_بك_هنا" or GROQ_API_KEY == "":
                st.error("⚠️ الرجاء وضع مفتاح Groq API Key الصحيح داخل الكود في السطر رقم 25.")
            else:
                with st.spinner("جاري التلخيص الفوري الشامل عبر خوادم Groq الخارقة..."):
                    try:
                        url = "https://groq.com"
                        headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
                        payload = {
                            "model": "llama-3.1-8b-instant",
                            "messages": [{"role": "user", "content": f"قم بتلخيص المحتوى التالي تلخيصاً أكاديمياً احترافياً شاملاً على شكل نقاط وعناوين رئيسية باللغة العربية واضحة ومباشرة:\n\n{st.session_state.merged_text}"}]
                        }
                        res = requests.post(url, json=payload, headers=headers)
                        st.markdown("### 📌 التلخيص الأكاديمي الشامل:")
                        st.info(res.json()['choices']['message']['content'])
                    except:
                        st.error("حدث خطأ في الاتصال بسيرفر الذكاء الاصطناعي، يرجى المحاولة مجدداً.")

# ==================== التبويب الرابع ====================
with tab_quiz:
    st.subheader("🧠 pdf اختبارات تفاعلية بس ارسل")
    if not st.session_state.merged_text:
        st.warning("⚠️ يرجى رفع ملفات الـ PDF من التبويب السابق أولاً.")
    else:
        col_type, col_diff, col_num = st.columns(3)
        with col_type: quiz_type = st.text_input("اكتب نوع الأسئلة المطلوب بيدك:", value="خيارات متعددة تفصيلية")
        with col_diff: quiz_difficulty = st.selectbox("مستوى الصعوبة المتوقع:", ["سهل", "متوسط", "صعب"])
        with col_num: quiz_count = st.slider("عدد الأسئلة المطلوبة:", min_value=1, max_value=100, value=3)

        if st.button("🎲 صياغة الاختبار التفاعلي المخصص"):
            if GROQ_API_KEY == "ضع_مفتاح_GROQ_الخاص_بك_هنا" or GROQ_API_KEY == "":
                st.error("⚠️ الرجاء وضع مفتاح Groq API Key الصحيح داخل الكود في السطر رقم 25.")
            else:
                with st.spinner("جاري صياغة بنك الأسئلة بالمعايير المطلوبة..."):
                    try:
                        url = "https://groq.com"
                        headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
                        prompt = f"قم بتوليد عدد {quiz_count} أسئلة من نوع {quiz_type} وصعوبة {quiz_difficulty} بناءً على النص التالي. يجب أن تكون الاستجابة بصيغة JSON فقط كقائمة مصفوفة نظيفة تماماً بدون أي نصوص خارج الأقواس، وتتبع الهيكل التالي تماماً:\n [{{\n\"question\": \"السؤال\",\n\"options\": [\"أ\", \"ب\", \"ج\", \"د\"],\n\"answer\": \"الإجابة الصحيحة\"\n}}]\n\nالمحتوى:\n{st.session_state.merged_text}"
                        payload = {
                            "model": "llama-3.1-8b-instant",
                            "messages": [{"role": "user", "content": prompt}],
                            "response_format": {"type": "json_object"}
                        }
                        res = requests.post(url, json=payload, headers=headers)
                        data = json.loads(res.text)
                        if "questions" in data: st.session_state.quiz_data = data["questions"]
                        elif isinstance(data, list): st.session_state.quiz_data = data
                        else: st.session_state.quiz_data = list(data.values())
                        st.session_state.user_answers = {}
                    except:
                        st.error("حدث خطأ في معالجة بنك الأسئلة، يرجى إعادة الضغط على زر الصياغة.")

        if st.session_state.quiz_data:
            st.markdown("### 📝 بنك الاختبار المخصص الجاهز:")
            with st.form("quiz_form"):
                for idx, q in enumerate(st.session_state.quiz_data):
                    if isinstance(q, dict) and "question" in q and "options" in q:
                        st.markdown(f"**س{idx+1}: {q['question']}**")
                        st.session_state.user_answers[idx] = st.radio("اختر الإجابة:", q['options'], key=f"q_{idx}")
                        st.write("---")
                if st.form_submit_button("📥 إرسال الإجابات للتصحيح التلقائي"):
                    correct_count = 0
                    st.markdown("### 📊 تقرير الأداء المباشر:")
                    for idx, q in enumerate(st.session_state.quiz_data):
                        if isinstance(q, dict) and "answer" in q:
