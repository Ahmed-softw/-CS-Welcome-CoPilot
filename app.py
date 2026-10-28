import streamlit as st
import pypdf
import os 
import requests

# 1. إعداد واجهة الويب الفخمة لتناسب تخصصات الحاسب
st.set_page_config(page_title="CS Academic Assistant", page_icon="💻", layout="wide")

st.markdown("""
  <style>
    .main-title { font-size: 34px; font-weight: bold; color: #38BDF8; text-align: center; margin-bottom: 5px; }
    .sub-title { font-size: 18px; color: #475569; text-align: center; margin-bottom: 25px; }
    .stButton>button { width: 100%; background-color: #0284C7; color: white; border-radius: 8px; font-weight: bold; height: 45px; }
    .info-box { background-color: #1E293B; padding: 15px; border-radius: 12px; border-right: 5px solid #38BDF8; margin-bottom: 20px; color: #CBD5E1; }
    .video-card { background-color: #0F172A; padding: 15px; border-radius: 10px; border: 1px solid #334155; margin-bottom: 15px; }
    .video-title { font-size: 16px; font-weight: bold; color: #38BDF8; margin-bottom: 8px; }
    .response-box { background-color: #1E293B; padding: 25px; border-radius: 12px; border: 1px solid #334155; color: #F8FAFC; line-height: 1.7; font-size: 16px; }
    .roadmap-card, .satr-card { background-color: #1E293B; padding: 15px; border-radius: 10px; margin-bottom: 15px; border: 1px solid #334155; }
    .card-title { font-size: 18px; font-weight: bold; color: #38BDF8; margin-bottom: 5px; }
    .card-text { color: #CBD5E1; font-size: 14px; }
    .link-style, .link-style-satr { color: #38BDF8; font-weight: bold; text-decoration: none; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">💻 Jeffrey المساعد الذكي</div>', unsafe_allow_html=True)    
st.markdown('<div class="sub-title">مساعد مرئي وملخص للمواد ومرشد جامعي لأقسام الحاسب وبناء القدرات التقنية</div>', unsafe_allow_html=True)

# 2. إعدادات مفاتيح ربط سيرفر الـ AI لـ Groq
GROQ_API_KEY = "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"
GROQ_URL = "https://groq.com"  # تم تصحيح الرابط إلى الرابط الفعلي لـ API البنية التحتية

# تهيئة متغيرات الذاكرة التخزينية داخل الجلسة (Session State)
if "all_extracted_text" not in st.session_state:
    st.session_state.all_extracted_text = ""
if "jef_response" not in st.session_state:
    st.session_state.jef_response = ""

# عرض طريقة الاستخدام والتنبيه الخاص باسم المساعد
st.markdown("""
<div class="info-box">
    🤖 <b>مرحباً بك! أنا جفري مساعدك الذكي:</b> لمساعدتك، يرجى رفع ملفات الـ PDF الدراسية (بحد أقصى 15 ملفاً)، 
    ثم وجه لي الأمر في الصندوق السفلي. <br><b>تنبيه صارم:</b> أنا لا أستجيب للأوامر إلا إذا بدأت بـ مناداتي باسمي أولاً! 
    <br><i>مثال صحيح: "جفري لخص لي هذه المحاضرة واصنع منها أسئلة صح وخطأ"</i>
</div>
""", unsafe_allow_html=True)

# ==================== القسم الأول: الفيديوهات التعليمية الخاصة بك ====================
st.subheader("🎥 الفيديوهات التوجيهية والشرح المدمج")
col_vid1, col_vid2 = st.columns(2)

with col_vid1:
    st.markdown('<div class="video-card">', unsafe_allow_html=True)
    st.markdown('<div class="video-title">👋 1. فيديو مقدمة المشروع والتعريف بالفكرة</div>', unsafe_allow_html=True)
    st.write("عرض مرئي مدمج ومباشر يسرد فكرة وتفاصيل مشروع التخرج.")
    
    video_path_1 = "Screen Recording 2026-10-28 161512.mp4" 
    if os.path.exists(video_path_1):
        st.video(video_path_1)
    else:
        st.warning(f"⚠️ تأكد من وجود الفيديو الأول باسم: '{video_path_1}'")
        st.video("https://w3schools.com")
    st.markdown('</div>', unsafe_allow_html=True)

with col_vid2:
    st.markdown('<div class="video-card">', unsafe_allow_html=True)
    st.markdown('<div class="video-title">🛠️ 2. فيديو الشرح والتعلم المدمج</div>', unsafe_allow_html=True)
    st.write("فيديو إرشادي تكميلي يشرح المادة التعليمية وطريقة التفاعل.")

    video_path_2 = "فديو تعلم.mp4"
    if os.path.exists(video_path_2):
        st.video(video_path_2)
    else:
        st.warning(f"⚠️ تأكد من وجود الفيديو الثاني باسم: '{video_path_2}'")
        st.video("https://w3schools.com")
    st.markdown('</div>', unsafe_allow_html=True)

st.write("---")

# ==================== القسم الثاني: مسار المهندس الناجح مع الروابط المدمجة ==============
st.subheader("🚀 خارطة طريق طالب هندسة البرمجيات وعلوم الحاسب")
col_left, col_right = st.columns(2)  # تم إصلاح الخطأ: إنشاء الأعمدة المفقودة لكي لا ينهار التطبيق

with col_left:
    st.markdown("""
        <div class="roadmap-card">
            <div class="card-title">🐙 1. منصة GitHub وبناء المعرض</div>
            <div class="card-text">
                GitHub هي منصة استضافة لمشاريع البرمجيات، حيث يمكن للمهندسين مشاركة مشاريعهم وبناء معرض أعمالهم. 
                للبدء، قم بإنشاء حساب على GitHub وابدأ برفع مشاريعك البرمجية.
                <br><br>
                🔗 <b>رابط الموقع الرسمي:</b> <a class="link-style" href="https://github.com" target="_blank">اضغط هنا للانتقال إلى GitHub</a>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.checkbox("أنشأت حساب في GitHub وربطته بـ Git بنجاح", key="chk_github")
    
    st.markdown("""
        <div class="roadmap-card">
            <div class="card-title">💼 2. منصة LinkedIn وبناء العلاقات</div>
            <div class="card-text">
                التخصص لا يقتصر على المذاكرة فقط، بل يحتاج بناء شبكة علاقات قوية وتتبع التقنيات والوظائف المطلوبة بالسوق المهني.
                <br><br>
                🔗 <b>رابط الموقع الرسمي:</b> <a class="link-style" href="https://linkedin.com" target="_blank">اضغط هنا للانتقال إلى LinkedIn</a>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.checkbox("أنشأت حساب LinkedIn احترافي وربطته بتخصصي", key="chk_linkedin")

with col_right:
    st.markdown("""
        <div class="satr-card">
            <div class="card-title">🚀 3. منصة سطر التعليمية (Satr.codes)</div>
            <div class="card-text">
                منصة سطر هي الخيار المثالي والمجاني بالكامل باللغة العربية. أنصحك بالبدء فوراً في مسارات لغة Python ومسارات الـ Full-Stack لدعم دراستك الجامعية.
                <br><br>
                🔗 <b>رابط الموقع الرسمي:</b> <a class="link-style-satr" href="https://satr.codes" target="_blank">اضغط هنا للانتقال إلى منصة سطر</a>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.checkbox("سجلت في منصة سطر وبدأت أول مسار برمي تطبيقي", key="chk_satr")
    
    st.markdown("""
        <div class="roadmap-card">
            <div class="card-title">📝 4. التوثيق الرقمي المستمر (Dev Journal)</div>
            <div class="card-text">
                وثق واكتب وسجل كل لغة برمجة، أداة، أو خوارزمية تفهمها في مفكرة رقمية مثل Notion لكي لا تنسى عند التقديم على التدريب التعاوني (COOP).
                <br><br>
                🔗 <b>رابط الأداة المقترحة:</b> <a class="link-style" href="https://notion.so" target="_blank">اضغط هنا للانتقال إلى Notion</a>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.checkbox("أنشأت مفكرتي الرقمية الخاصة لتوثيق كل مهارة أتعلمها", key="chk_journal")

st.write("---")

# ==================== القسم الثالث: منطقة إدراج المواد الدراسية ====================
st.subheader("📚 1. أرفق المواد الدراسية (PDF)")
uploaded_files = st.file_uploader(
    "اسحب وأفلت ملفات الـ PDF هنا (الحد الأقصى 15 ملفاً)", 
    type=["pdf"], 
    accept_multiple_files=True
)

if uploaded_files:
    if len(uploaded_files) > 15:
        st.error("⚠️ تنبيه: تجاوزت الحد الأقصى المسموح به! يرجى رفع 15 ملفاً أو أقل فقط.")
        st.session_state.all_extracted_text = ""
    else:
        st.success(f"🔒 تم رفع {len(uploaded_files)} ملفات بنجاح! جاري معالجة واستخراج النصوص...")
        
        combined_text = ""
        for uploaded_file in uploaded_files:
            try:
                pdf_reader = pypdf.PdfReader(uploaded_file)
                for page in pdf_reader.pages:
                    text = page.extract_text()
                    if text:
                        combined_text += text + "\n"
            except Exception as e:
                pass
        st.session_state.all_extracted_text = combined_text[:40000]
        st.info("✅ تم تجهيز نصوص الملفات بنجاح وجاهزة للتنفيذ والاستعلام.")

st.write("---")

# ==================== القسم الرابع: صندوق الأوامر الموحد والربط بالذكاء الاصطناعي ====================
st.subheader("🤖 2. صندوق أوامر واستفسارات المساعد جفري")

user_command = st.text_area(
    "اكتب أمرك المركب الموجه للمساعد هنا (ابدأ بكلمة جفري):", 
    placeholder="مثال: جفري لخص لي هذه المحاضرة واصنع منها 10 أسئلة خيارات متعددة و 5 أسئلة مقالية...",
    height=100
)

if st.button("🚀 إرسال الأمر المباشر إلى جفري"):
    clean_command = user_command.strip()
    
    if not st.session_state.all_extracted_text:
        st.warning("⚠️ يرجى رفع ملفات PDF أولاً ليتمكن جفري من قراءتها وتحليلها.")
    elif not clean_command:
        st.warning("⚠️ صندوق الأوامر فارغ، يرجى كتابة التوجيه المطلوب أولاً.")
    elif not clean_command.startswith("جفري"):  # تم إصلاح وإكمال شرط التحقق المقصوص
        st.error("⛔ جفري يرفض الاستجابة! التنبيه الصارم ينص على ضرورة مناداته بـ 'جفري' أول جملة الأمر المباشر.")
    else:
        with st.spinner("جاري التواصل مع الخادم وتحليل المواد الدراسية... برجاء الانتظار"):
            try:
                # إعداد الهيدرز والبيانات (Headers & Payload) لتتوافق مع معايير الحوسبة الفورية
                headers = {
                    "Authorization": f"Bearer {GROQ_API_KEY.strip()}",
                    "Content-Type": "application/json"
                }
                
                system_instruction = """أنت مساعد أكاديمي ذكي جداً وخبير ومتخصص في علوم الحاسب وهندسة البرمجيات، واسمك الشخصي هو 'جفري'.
مهمتك تنفيذ كافة الأوامر الموجهة لك من الطالب بمرونة فائقة بناءً على نصوص الـ PDF المرفقة مع الالتزام التام بالقواعد التالية:
1. يمكنك دمج عدة طلبات معاً (ملخص، شرح جزئية، صياغة أسئلة متنوعة) في رد واحد منسق أكاديمياً بعناوين واضحة.
2. إذا تضمن طلب الطالب توليد أسئلة (خيارات، صح وخطأ، أو مقالي)، فيجب وبشكل صارم ألا يتجاوز إجمالي عدد الأسئلة المصنوعة 60 سؤالاً كحد أقصى مهما كانت صيغة الطلب.
