if st.button("🚀 إرسال الأمر المباشر إلى جفري"):
    clean_command = user_command.strip()
    
    if not st.session_state.all_extracted_text:
        st.warning("⚠️ يرجى رفع ملفات PDF أولاً ليتمكن جفري من قراءتها وتحليلها.")
    elif not clean_command:
        st.warning("⚠️ صندوق الأوامر فارغ، يرجى كتابة التوجيه المطلوب أولاً.")
    elif not clean_command.startswith("جفري"):
        st.error("⛔ جفري يرفض الاستجابة! التنبيه الصارم ينص على ضرورة مناداته بـ 'جفري' أول جملة الأمر المباشر.")
    else:
        with st.spinner("جاري التواصل مع الخادم وتحليل المواد الدراسية... برجاء الانتظار"):
            try:
                headers = {
                    "Authorization": f"Bearer {GROQ_API_KEY.strip()}",
                    "Content-Type": "application/json"
                }
                
                # تم تحويل النص لسطر واحد مستمر لمنع أخطاء الترميز والمحاذاة في السيرفر السحابي
                system_instruction = "أنت مساعد أكاديمي ذكي جداً وخبير ومتخصص في علوم الحاسب وهندسة البرمجيات، واسمك الشخصي هو 'جفري'.\nمهمتك تنفيذ كافة الأوامر الموجهة لك من الطالب بمرونة فائقة بناءً على نصوص الـ PDF المرفقة مع الالتزام التام بالقواعد التالية:\n1. يمكنك دمج عدة طلبات معاً (ملخص، شرح جزئية، صياغة أسئلة متنوعة) في رد واحد منسق أكاديمياً بعناوين واضحة.\n2. إذا تضمن طلب الطالب توليد أسئلة (خيارات، صح وخطأ، أو مقالي)، فيجب وبشكل صارم ألا يتجاوز إجمالي عدد الأسئلة المصنوعة 60 سؤالاً كحد أقصى مهما كانت صيغة الطلب.\n3. لغة الرد يجب أن تكون العربية الفصحى الواضحة والمنظمة للمذاكرة مباشرة."
                
                payload = {
                    "model": "llama3-8b-8192",
                    "messages": [
                        {"role": "system", "content": system_instruction},
                        {"role": "user", "content": f"نص مراجع المواد المرفوعة:\n{st.session_state.all_extracted_text}\n\nتوجيه وأمر الطالب لك: {clean_command}"}
                    ],
                    "temperature": 0.4
                }

                # إرسال الطلب إلى السيرفر
                res = requests.post(GROQ_URL, json=payload, headers=headers)

                # التحقق من نجاح الاستجابة
                if res.status_code == 200:
                    result_json = res.json()
                    st.session_state.jef_response = result_json['choices'][0]['message']['content']
                else:
                    st.error(f"خطأ في الاستجابة من سيرفر جفري: {res.status_code}")

            except Exception as e:
                st.error(f"حدث خطأ أثناء معالجة الطلب: {e}")
