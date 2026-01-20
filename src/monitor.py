# Chamar todos os scrapers
# Receber os preços
# Comparar com o histórico
# Decidir o que fazer

from scraper.amazon import get_amazon_price
from utils import load_prices, save_prices
from notifier.email_sender import send_email_alert

DATA_FILE = "src/data/prices.json"
AMAZON_URL = "https://www.amazon.com.br/Apple-iPhone-15-128-GB/dp/B0CP6CVJSG"


def main():
    print("Iniciando monitoramento de preços")

    prices = load_prices(DATA_FILE)

    current_price = get_amazon_price(AMAZON_URL)

    if current_price is None:
        print("Não foi possível obter o preço atual")
        return

    old_price = prices.get("amazon")

    if old_price is None:
        print(f"Primeiro registro de preço: R$ {current_price}")

    elif current_price < old_price:
        print(f"📉 Preço caiu! R$ {old_price} → R$ {current_price}")

        send_email_alert(
            old_price=old_price,
            new_price=current_price,
            product_url=AMAZON_URL
        )

    elif current_price > old_price:
        print(f"📈 Preço subiu! R$ {old_price} → R$ {current_price}")

    else:
        print(f"Preço mantido: R$ {current_price}")

    prices["amazon"] = current_price
    save_prices(DATA_FILE, prices)

    print("Preço salvo com sucesso")


if __name__ == "__main__":
    main()
