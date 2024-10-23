import fitz

my_path = r'C:\nai_localgpt\localGPT\SOURCE_DOCUMENTS\Attachment B1 - DFLR0000277_Micro_Mini_RIU_SSOW_Rev_New.pdf'

doc = fitz.open(my_path)

i = 0
for page in doc:
    if (i > 30):
        break
    text = page.get_text()
    print('page ', i)
    print(text)
    i += 1
