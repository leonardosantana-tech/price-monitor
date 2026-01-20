# Acessar a URL do produto
# Receber o HTML
# Procurar o elemento do preço
# Extrair o texto
# Retornar esse texto

import requests
import os


def get_amazon_price(product_url: str):
    print("🌐 Buscando preço via RapidAPI (Axesso)")

    api_key = os.getenv("RAPIDAPI_KEY")

    if not api_key:
        print("❌ RAPIDAPI_KEY não encontrada")
        return None

    url = "https://axesso-axesso-amazon-data-service-v1.p.rapidapi.com/amz/amazon-lookup-product"

    querystring = {
        "url": product_url
    }

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "axesso-axesso-amazon-data-service-v1.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring, timeout=20)
        print("📡 Status code:", response.status_code)

        response.raise_for_status()
        data = response.json()

        price = data.get("price")
        title = data.get("productTitle")

        if not price:
            print("❌ Preço não encontrado no JSON")
            return None

        print(f"✅ Produto: {title}")
        print(f"💰 Preço encontrado: R$ {price}")

        return float(price)

    except requests.exceptions.RequestException as e:
        print("❌ Erro na requisição:")
        print(response.text if "response" in locals() else e)
        return None


if __name__ == "__main__":
    print("▶️ Teste RapidAPI Amazon")

    test_url = "https://www.amazon.com.br/Apple-iPhone-15-128-GB/dp/B0CP6CVJSG"
    price = get_amazon_price(test_url)

    print("💰 Preço retornado:", price)

