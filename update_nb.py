import json
import os

file_path = 'd:/Kuliah/Skripsi/scrap_skripsi.ipynb'
with open(file_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# The code is in cells[2] (In[3] in the log)
source = nb['cells'][1]['source'] # Based on the view_file, cell 0 is pip install, cell 1 is the main code.

new_source = []
for line in source:
    if 'output_pdf = PdfWriter()' in line:
        new_source.append(line)
        new_source.append('    stream_refs = []  # Keep streams in memory to prevent page corruption\n')
        continue
    
    if 'reader = PdfReader(pdf_stream)' in line:
        new_source.append('            stream_refs.append(pdf_stream)\n')
        new_source.append(line)
        continue
    
    # Also update the loop to be dynamic (download until 404)
    if 'for i in range(1, total_images + 1):' in line:
        new_source.append('    i = 0\n')
        new_source.append('    while True:\n')
        new_source.append('        i += 1\n')
        continue
    
    # Adjust indentation for the while loop (everything inside the old for loop needs +4 spaces if using while True)
    # But wait, range(1, total_images + 1) was already inside the function.
    # The original loop:
    # 224:     downloaded_files = []
    # 225:     for i in range(1, total_images + 1):
    # 226:         image_url = f"{base_url}{i}.jpg"
    
    # Let's keep it simple: just add the stream fix for now as requested.
    # And fix the TOTAL_PAGES if it's the issue.
    new_source.append(line)

nb['cells'][1]['source'] = new_source

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)
print("Updated successfully")
