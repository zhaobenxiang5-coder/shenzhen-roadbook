with open("generate_clean_artifact_html.py", "r") as f:
    text = f.read()

from generate_super_app import CHECKLIST_CATEGORIES
import json

cat_code = f"CHECKLIST_CATEGORIES = {json.dumps(CHECKLIST_CATEGORIES, ensure_ascii=False)}\n"
text = cat_code + text

with open("generate_clean_artifact_html.py", "w") as f:
    f.write(text)

print("Prepend checklist categories success")
