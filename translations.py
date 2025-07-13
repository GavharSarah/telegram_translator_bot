import json

def get_i18n(lang_code):
    try:
        with open(f"locales/{lang_code}.json", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

