import os
from google import genai
from google.genai import types
import arabic_reshaper
from bidi.algorithm import get_display
from dotenv import load_dotenv

load_dotenv()



def fix_arabic(text):
    reshaped_text = arabic_reshaper.reshape(text)
    return get_display(reshaped_text)


client = genai.Client()

user_question = "أريد إلغاء باقة الإنترنت الخاصة بي واسترجاع أموالي، كيف أفعل ذلك؟"

prompt_1 = "أنت موظف خدمة عملاء في شركة اتصالات. أجب عن سؤال العميل."

prompt_2 = """أنت موظف خدمة عملاء في شركة اتصالات. أجب عن سؤال العميل.
القيود السلبية:
- لا تقم بأي حال من الأحوال بوعد العميل باسترجاع الأموال.
- لا تستخدم مصطلحات تقنية معقدة."""

prompt_3 = """أنت موظف خدمة عملاء في شركة اتصالات. أجب عن سؤال العميل.
القيود السلبية:
- لا تعتذر أو تستخدم عبارات ترحيبية مطولة.
- لا تتجاوز إجابتك 20 كلمة فقط.
- لا تقدم أي وعود مالية، فقط وجهه لزيارة الفرع."""

prompts = [prompt_1, prompt_2, prompt_3]

for i, p in enumerate(prompts, 1):
    response = client.models.generate_content(
        model='gemini-3.6-flash',
        contents=user_question,
        config=types.GenerateContentConfig(
            system_instruction=p
        )
    )
    with open("output.txt", "a", encoding="utf-8") as f:
     f.write(f"=== التجربة رقم {i} ===\n{response.text}\n\n")

    print(f"=== التجربة رقم {i} ===")
   
    print(fix_arabic(response.text))
    print("-" * 40)