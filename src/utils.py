# Traduzir preço 
# Formatar texto
# Ler e escrever JSON

import json
import os


def load_prices(filepath):
    if not os.path.exists(filepath):
        return {}

    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)


def save_prices(filepath, data):
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
