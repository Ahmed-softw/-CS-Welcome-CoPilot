import streamlit as st
import pypdf
import json
from google import genai
from google.genai import types

# 1. إعداد وتأمين واجهة الويب لتبدو كمنصة جامعية رسمية
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

# 2. ضع مفتاح الـ API الخاص بك هنا مباشرة بين علامتي التنصيص بدلاً من النص المؤقت
API_KEY = "AQ.Ab8RN6KQ-6opXfamf01lQR5rh78tm2NVcGB3xR558KrmNzXLxQ"

@st.cache_resource
def init_ai_client(api_key):
    try:
        if api_key and api_key != "AQ.Ab8RN6KQ-6opXfamf01lQR5rh78tm2NVcGB3xR558KrmNzXLxQ":
            return genai.Client(api_key=api_key)
        return None
    except Exception as e:
        return None

client = init_ai_client(API_KEY)

if "quiz_data" not in st.session_state:
    st.session_state.quiz_data = None
if "merged_text" not in st.session_state:
    st.session_state.merged_text = ""

# 3. تقسيم الواجهة وتعديل المسميات حسب طلبك بدقة
tab_intro_videos, tab_roadmap, tab_syllabus, tab_quiz = st.tabs([
    "🎥 الفيديوهات التوجيهية والشرح",
    "🚀 مسار المهندس الناجح", 
    "📚 pdf ارفع ملفك وخلني اللخصه لك ", 
    "🧠 pdf اختبارات تفاعلية بس ارسل "
])

# ==================== التبويب الأول: الفيديوهات التوجيهية والشرح ====================
with tab_intro_videos:
    st.subheader("🎥 الفيديوهات التوجيهية والشرح")
    st.write("شاهد الفيديوهات التالية للتعرف على المنصة وكيفية البدء في التخصص بشكل مثالي:")
    
    col_vid1, col_vid2 = st.columns(2)
    
    with col_vid1:
        st.markdown('<div class="video-header">👋 1. فيديو المقدمة والتعريف بالفكرة</div>', unsafe_allow_html=True)
        st.write("في هذا الفيديو أُعرفك بنفسي كطالب هندسة برمجيات، وأشرح لك كيف جاءتني فكرة المشروع بناءً على الصعوبات والضياع الذي واجهته في سنتي الأولى.")
        st.video("https://youtube.com") 
        
    with col_vid2:
        st.markdown('<div class="video-header">🛠️ 2. كيف تسجل دخول علي منصة سطر التعليمية</div>', unsafe_allow_html=True)
        st.write("كيف تنزل الملف في الموقع وكيف تدخل دوراة سطر ")
        st.video("https://youtube.com")

# ==================== التبويب الثاني: مسار المهندس الناجح ====================
with tab_roadmap:
    st.subheader("🎯 خطوات جوهرية بناءً على تجربتي الشخصية لحمايتك من الضياع المعرفي:")
    st.write("هذه الأدوات والمنصات هي رأس مالك في الكلية، والبدء فيها مبكراً يختصر عليك سنوات من الحيرة:")
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.markdown(f"""
        <div class="roadmap-card">
            <div class="card-title">🐙 1. منصة GitHub وبناء المعرض البرمجي</div>
            <div class="card-text">
                أولاً_ اصنع حساب GitHub لأنه هو بيكون المعرض الخاص بك بحيث تسجل فيه جميع انجازاتك الدراسية 
                زي اللابات اللي تأخذها من الدكاترة في المواد لازم تسجلها وتسجل إنجازاتك زي حق سطر وكذا.
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.checkbox("أنشأت حساب في GitHub وربطته بـ Git بنجاح", key="chk_github")
        
        st.markdown(f"""
        <div class="roadmap-card">
            <div class="card-title">💼 2. منصة LinkedIn وبناء العلاقات المهنية</div>
            <div class="card-text">
                التخصص لا يقتصر على المذاكرة فقط، بل يحتاج بناء شبكة علاقات قوية. أنشئ حسابك الآن، 
                أضف دكاترة القسم، الخريجين المتميزين، وتابع مهندسي البرمجيات في الشركات الكبرى 
                لتتعرف على التوجهات الحالية والتقنيات المطلوبة في السوق السعودي قبل التخرج بوقت كافٍ.
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.checkbox("أنشأت حساب LinkedIn احترافي ورابطته بتخصصي", key="chk_linkedin")

    with col_right:
        st.markdown(f"""
        <div class="satr-card">
            <div class="card-title">🚀 3. منصة سطر التعليمية (Satr.codes)</div>
            <div class="card-text">
                بناءً على تجربتي الشخصية، الدراسة الأكاديمية تحتاج دائماً لجانب تطبيقي مكمل. منصة سطر 
                (التابعة للأكاديمية السعودية الرقمية) هي الخيار المثالي والمجاني بالكامل باللغة العربية. 
                أنصحك بالبدء فوراً في مسارات لغة <b>Python</b> والتقدم نحو مسارات الـ <b>Full-Stack</b> 
                لتمتلك أساساً برمجياً خارقاً وشهادات معتمدة تدعم ملفك الجامعي والمهني بقوة.
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.checkbox("سجلت في منصة سطر وبدأت أول مسار برمي تطبيقي", key="chk_satr")

        st.markdown(f"""
        <div class="roadmap-card">
            <div class="card-title">📝 4. التوثيق الرقمي المستمر (Dev Journal)</div>
            <div class="card-text">
                <b>أهم نصيحة لحمايتك عند اقتراب التدريب التعاوني (COOP):</b> وثق واكتب وسجل كل لغة برمجة، 
                أداة، أو خوارزمية تفهمها في مفكرة رقمية مثل (Notion أو Obsidian). عدم تسجيل هذه المهارات 
                اليومية سيجعلك تنسى المبادئ الأساسية عند الوصول لسنوات التخرج والتدريب العملي.
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.checkbox("أنشأت مفكرتي الرقمية الخاصة لتوثيق كل مهارة أتعلمها", key="chk_journal")

# ==================== التبويب الثالث: pdf ارفع ملفك وخلني اللخصه لك ====================
with tab_syllabus:
    st.subheader("📚 pdf ارفع ملفك وخلني اللخصه لك")
    st.write("يمكنك رفع ملف أو عدة ملفات (تتحمل أكثر من 15 ملف دفعة واحدة) ليقوم النظام بدمجها وتلخيصها فوراً بلمح البصر.")
    
    uploaded_files = st.file_uploader("ارفع ملفات الـ PDF الخاصة بالمواد الدراسية هنا", type=["pdf"], accept_multiple_files=True)

    if uploaded_files:
        st.success(f"🔒 تم رفع {len(uploaded_files)} ملفات بنجاح وجاري دمج النصوص وإعداد محرك البث الفوري!")
        all_text = ""
        for uploaded_file in uploaded_files:
            try:
                pdf_reader = pypdf.PdfReader(uploaded_file)
                for page in pdf_reader.pages:
                    text = page.extract_text()
                    if text:
                        all_text += text + "\n"
            except Exception as e:
                pass
        
        st.session_state.merged_text = all_text[:20000]

        if st.session_state.merged_text and st.button("📝 استخراج ملخص فوري شامل"):
            if client is None:
                st.error("⚠️ لم يتم العثور على مفتاح API Key سليم داخل الكود في السطر رقم 25.")
            else:
                st.markdown("### 📌 التلخيص الأكاديمي المباشر (بث حي كلمة بكلمة):")
                try:
                    prompt = f"قم بتلخيص المحتوى التالي تلخيصاً أكاديمياً احترافياً شاملاً على شكل نقاط وعناوين رئيسية باللغة العربية:\n\n{st.session_state.merged_text}"
                    response_stream = client.models.generate_content_stream(model='gemini-2.5-flash', contents=prompt)
                    st.write_stream(response_stream)
                except Exception as e:
                    st.error(f"حدث خطأ في الاتصال")

# ==================== التبويب الرابع: pdf اختبارات تفاعلية بس ارسل ====================
with tab_quiz:
    st.subheader("🧠 pdf اختبارات تفاعلية بس ارسل")
    st.write("اكتب نوع الأسئلة بدقة وحدد صعوبتها وعددها (حتى 100 سؤال) ليقوم النظام بصياغتها تفاعلياً.")

    if not st.session_state.merged_text:
        st.warning("⚠️ يرجى رفع ملفات الـ PDF من التبويب السابق أولاً لتتمكن من تخصيص وصناعة الاختبار التفاعلي.")
    else:
        col_type, col_diff, col_num = st.columns(3)
        with col_type:
            quiz_type = st.text_input("اكتب نوع الأسئلة المطلوب بيدك:", value="خيارات متعددة تفصيلية")
        with col_diff:
            quiz_difficulty = st.selectbox("مستوى الصعوبة المتوقع:", ["سهل (Easy)", "متوسط (Medium)", "صعب (Hard)"])
        with col_num:
            quiz_count = st.slider("عدد الأسئلة المطلوبة:", min_value=1, max_value=100, value=5)

        if st.button("🎲 صياغة الاختبار التفاعلي المخصص"):
            if client is None:
                st.error("⚠️ لم يتم العثور على مفتاح API Key سليم داخل الكود في السطر رقم 25.")
            else:
                with st.spinner("جاري صياغة وهندسة بنك الأسئلة المتقدم بالمعايير المكتوبة..."):
                    try:
                        prompt = f"قم بتوليد عدد {quiz_count} أسئلة من نوع {quiz_type} ومستوى الصعوبة هو {quiz_difficulty} بناءً على المحتوى الدراسي التالي. يجب أن تكون الاستجابة بصيغة JSON فقط كقائمة مصفوفة، وتتبع الهيكل التالي تماماً بدون تغيير أو إضافة أي نصوص خارج الجيسون:\n [{{\n\"question\": \"السؤال هنا\",\n\"options\": [\"الخيار أ أو النص المساعد هنا\", \"الخيار ب أو النص المساعد هنا\"],\n\"answer\": \"الإجابة الصحيحة المطابقة تماماً لخياراتك لغرض التصحيح الأوتوماتيكي\"\n}}]\n\nالمحتوى الدراسي المرفوع:\n{st.session_state.merged_text}"
                        response = client.models.generate_content(
                            model='gemini-2.5-flash',
                            contents=prompt,
