import json

file_path = 'd:/Kuliah/Skripsi/scrap_skripsi.ipynb'

with open(file_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = cell['source']
        new_source = []
        for line in source:
            if 'verify=certifi.where()' in line:
                line = line.replace('verify=certifi.where()', 'verify=False')
            new_source.append(line)
            if 'from requests.exceptions import SSLError, RequestException' in line:
                new_source.append('import urllib3\n')
                new_source.append('urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)\n')
        cell['source'] = new_source

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Notebook updated successfully.")
