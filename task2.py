import os
from langchain_text_splitters import CharacterTextSplitter, MarkdownHeaderTextSplitter


document_text = """
# دليل خدمات الاتصالات والإنترنت

## قسم الفواتير والاشتراكات
يمكن للعميل الاعتراض على الفاتورة خلال 30 يومًا من تاريخ صدورها. في حال ثبوت الخطأ يتم إضافة الرصيد لحساب العميل تلقائيًا.

## قسم الدعم الفني والأعطال
في حال انقطاع الخدمة بشكل كامل، يتم تعويض العميل برصيد مجاني بشرط رفع تذكرة دعم خلال 24 ساعة من الانقطاع.
"""


basic_splitter = CharacterTextSplitter(chunk_size=200,chunk_overlap=20,length_function=len )
basic_chunks = basic_splitter.split_text(document_text)


headers_to_split_on = [("#", "Header 1"), ("##", "Header 2")]
markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
advanced_chunks = markdown_splitter.split_text(document_text)


with open("task2_output.txt", "w", encoding="utf-8") as f:
    f.write("=== 1. التقطيع التقليدي (Character Text Splitter) ===\n")
    for idx, chunk in enumerate(basic_chunks, 1):
        f.write(f"الجزء {idx}:\n{chunk}\n{'-'*30}\n")
    
    f.write("\n" + "="*50 + "\n\n")
    
    f.write("=== 2. التقطيع المتقدم (MarkdownHeaderTextSplitter) ===\n")
    for idx, chunk in enumerate(advanced_chunks, 1):
        f.write(f"الجزء {idx}:\nالمحتوى: {chunk.page_content}\nالقسم: {chunk.metadata}\n{'-'*30}\n")

print("تم حفظ نتائج Task 2 بنجاح في ملف task2_output.txt!")