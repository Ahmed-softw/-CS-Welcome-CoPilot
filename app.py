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

# جلب مفتاح Cohere بطريقة آمنة من إعدادات الـ Secrets السحابية
try:
    COHERE_API_KEY = st.secrets["COHERE_API_KEY"]
except Exception:
    COHERE_API_KEY = ""

if "all_extracted_text" not in st.session_state:
    st.session_state.all_extracted_text = ""
if "jef_response" not in st.session_state:
    st.session_state.jef_response = ""

tab1, tab2, tab3 = st.tabs([
    "🎥 القسم الأول: الفيديوهات التعليمية", 
    "🚀 القسم الثاني: خارطة الطريق التقنية", 
    "🤖 القسم الثالث: المساعد الذكي جفري"
])

with tab1:
    st.subheader("🎥 الفيديوهات التوجيهية والشرح المدمج")
    col_vid1, col_vid2 = st.columns(2)

    with col_vid1:
        st.markdown('<div class="video-card">', unsafe_allow_html=True)
        st.markdown('<div class="video-title">👋 1. فيديو مقدمة المشروع والتعريف بالفكرة</div>', unsafe_allow_html=True)
        st.write("عرض مرئي مدمج ومباشر يسرد فكرة وتفاصيل مشروع التخرج.")
        
        video_path_1 = "Recording 2026-10-28 161523.mp4" 
        if os.path.exists(video_path_1):
            st.video(video_path_1)
        else:
            st.warning("⚠️ تأكد من رفع الفيديو الأول على GitHub")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_vid2:
        st.markdown('<div class="video-card">', unsafe_allow_html=True)
        st.markdown('<div class="video-title">🛠️ 2. فيديو الشرح والتعلم المدمج</div>', unsafe_allow_html=True)
        st.write("فيديو إرشادي تكميلي يشرح المادة التعليمية وطريقة التفاعل.")

        video_path_2 = "Screen Recording 2026-10-28 162939.mp4"
        if os.path.exists(video_path_2):
            st.video(video_path_2)
        else:
            st.warning("⚠️ تأكد من رفع الفيديو الثاني على GitHub")
        st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.subheader("🚀 خارطة طريق طالب هندسة البرمجيات وعلوم الحاسب")
    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown("""
            <div class="roadmap-card">
                <div class="card-title">🐙 1. منصة GitHub وبناء المعرض</div>
                <div class="card-text">
                    GitHub هي منصة استضافة لمشاريع البرمجيات.
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
                    التخصص لا يقتصر على المذاكرة فقط، بل يحتاج بناء شبكة علاقات قوية.
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
                    منصة سطر هي الخيار المثالي والمجاني بالكامل باللغة العربية.
                    <br><br>
                    🔗 <b>رابط الموقع الرسمي:</b> <a class="link-style-satr" href="https://satr.codes" target="_blank">اضغط هنا للانتقال إلى منصة سطر</a>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.checkbox("سجلت في منصة سطر وبدأت أول مسار برمجي", key="chk_satr")
        
        st.markdown("""
            <div class="roadmap-card">
                <div class="card-title">📝 4. التوثيق الرقمي المستمر (Dev Journal)</div>
                <div class="card-text">
                    وثق واكتب وسجل كل لغة برمجة في مفكرة رقمية مثل Notion.
                    <br><br>
                    🔗 <b>رابط الأداة المقترحة:</b> <a class="link-style" href="https://notion.so" target="_blank">اضغط هنا للانتقال إلى Notion</a>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.checkbox("أنشأت مفكرتي الرقمية الخاصة لتوثيق كل مهارة أتعلمها", key="chk_journal")

with tab3:
    st.markdown("""
    <div class="info-box">
        🤖 <b>مرحباً بك! أنا جفري مساعدك الذكي:</b> لمساعدتك، يرجى رفع ملفات الـ PDF الدراسية, 
        ثم وجه لي الأمر في الصندوق السفلي. <br><b>تنبيه صارم:</b> أنا لا أستجيب للأوامر إلا إذا بدأت بـ مناداتي باسمي أولاً! 
        <br><i>مثال صحيح: "جفري لخص لي هذه المحاضرة واصنع منها أسئلة صح وخطأ"</i>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("📚 1. أرفق المواد الدراسية (PDF)")
    uploaded_files = st.file_uploader(
        "اسحب وأفلت ملفات الـ PDF هنا (الحد الأقصى 15 ملفاً)", 
        type=["pdf"], 
        accept_multiple_files=True
    )

    if uploaded_files:
        if len(uploaded_files) > 15:
            st.error("⚠️ تنبيه: تجاوزت الحد الأقصى المسموح به!")
            st.session_state.all_extracted_text = ""
        else:
            st.success("تم رفع الملفات بنجاح! جاري معالجة واستخراج النصوص...")
            
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
            st.info("تم تجهيز نصوص الملفات بنجاح وجاهزة للتنفيذ والاستعلام.")

    st.write("---")

    st.subheader("🤖 2. صندوق أوامر واستفسارات المساعد جفري")

    user_command = st.text_area(
        "اكتب أمرك المركب الموجه للمساعد هنا (ابدأ بكلمة جفري):", 
        placeholder="مثال: جفري لخص لي هذه المحاضرة واصنع منها 10 أسئلة خيارات متعددة...",
        height=100
    )

    if st.button("🚀 إرسال الأمر المباشر إلى جفري"):
        clean_command = user_command.strip()
        
        if not COHERE_API_KEY:
            st.error("⚠️ مفتاح الـ API غير معرف في إعدادات Secrets الخاصة بـ Streamlit Cloud.")
        elif not st.session_state.all_extracted_text:
            st.warning("⚠️ يرجى رفع ملفات PDF أولاً ليتمكن جفري من قراءتها وتحليلها.")
        elif not clean_command:
            st.warning("⚠️ صندوق الأوامر فارغ، يرجى كتابة التوجيه المطلوب أولاً.")
        elif not clean_command.startswith("جفري"):
            st.error("⛔ جفري يرفض الاستجابة! التنبيه الصارم ينص على ضرورة مناداته بـ 'جفري'.")
        else:
            with st.spinner("جاري التواصل مع الخادم وتحليل المواد الدراسية... برجاء الانتظار"):
                try:
                    url = "https://api.cohere.ai/v1/chat"
                    headers = {
                        "Authorization": f"Bearer {COHERE_API_KEY.strip()}",
                        "Content-Type": "application/json",
                        "Accept": "application/json"
                    }
                    
                    system_prompt = (
                        "أنت مساعد أكاديمي ذكي جداً وخبير ومتخصص في علوم الحاسب وهندسة البرمجيات، واسمك الشخصي هو 'جفري'.\n"
                        "مهمتك تنفيذ كافة الأوامر الموجهة لك من الطالب بناءً على نصوص الـ PDF المرفقة.\n"
                    )
                    
                    full_prompt = f"محتوى الملفات الدرا
