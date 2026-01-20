# 📱 Price-Monitor – Amazon iPhone 15 Tracker

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![Status](https://img.shields.io/badge/Status-Finalizado-green)

## 🎯 Objetivo do Projeto

Este projeto nasceu de uma necessidade pessoal de monitorar o preço do **iPhone 15 na Amazon Brasil** para comprar pelo menor valor possível.
Além disso, foi uma ótima oportunidade para explorar conceitos de Python, integração com APIs, manipulação de JSON e práticas de automação de monitoramento de preços.

## 🧠 Expectativa Inicial vs Solução Final

No início, esperava conseguir capturar o preço diretamente com web scraping usando `requests` e `BeautifulSoup`.
No entanto, a Amazon bloqueia muito scraping direto, retornando CAPTCHAs e páginas vazias. Para resolver isso, testei:

1. ❌ **Scraper com requests + BeautifulSoup** → bloqueado;
2. ⚠️ **Scraper com Selenium** → confiável, mas pesado, complexo e instável para rodar em background;
3. ✅ **Uso de API de terceiros (RapidAPI com Axesso)** → solução definitiva.

A terceira opção foi escolhida porque é mais estável, rápida e segura, sem precisar lidar com bloqueios da Amazon ou alteração constante de layout HTML.

## 🔧 Tecnologias e Elementos Utilizados

- **Linguagem:** Python 3.12+
- **Bibliotecas principais:**
  - `requests` → para chamadas HTTP à API.
  - `os` → para leitura segura de variáveis de ambiente.
  - `json` → para persistência de dados.
  - `smtplib` → envio de alertas por e-mail.
- **APIs externas:**
  - [Axesso Amazon Data Service](https://rapidapi.com/axesso/api/axesso-amazon-data-service) (via RapidAPI) → fornece preço atual, histórico e detalhes do produto.

### Estrutura de arquivos:

- `src/scraper/amazon.py` → captura preço via API.
- `src/utils.py` → funções de leitura/escrita em JSON (`load_prices`, `save_prices`).
- `src/notifier/email_sender.py` → envio de alertas por email.
- `src/monitor.py` → integra todas as partes e executa o monitoramento.

## 🪚 JSON (Armazenamento)

Utilizado para armazenar preços no arquivo `prices.json` em formato simples, permitindo futuras análises ou gráficos:

json
{
    "amazon": 4299.00
}

## 🏠 Arquitetura
O projeto é modular e escalável:

scraper → módulo de captura de dados.

utils → módulo de manipulação de arquivos.

notifier → módulo de envio de alertas.

monitor.py → orquestrador que coordena a execução.

## ⚙️ Como Rodar o Projeto
1. Clonar repositório
Bash

git clone <URL_DO_SEU_REPOSITORIO>
cd price-monitor
2. Instalar dependências
Bash

pip install -r requirements.txt
3. Configuração de Segurança (Variáveis de Ambiente)
Este projeto utiliza variáveis de ambiente para não expor senhas no código. Siga os passos:

Crie variáveis utilizando Windows Power Shell ou diretamente em Variáveis de Ambiente

# Chave da API (Obtenha em: "[https://rapidapi.com/axesso/api/axesso-amazon-data-service](https://rapidapi.com/axesso/api/axesso-amazon-data-service))"
RAPIDAPI_KEY=SUA_CHAVE_DO_RAPIDAPI_AQUI

# Configurações de E-mail (Para alertas)
EMAIL_USER=seuemail@gmail.com
EMAIL_PASS=senha_de_app_gerada_pelo_google
⚠️ Importante: O arquivo .env contém dados sensíveis e nunca deve ser enviado ao GitHub. Certifique-se de que o arquivo .gitignore contenha a linha .env para evitar vazamentos.

4. Executar o Monitor
Bash

python src/monitor.py

## ⏱ Para rodar em Segundo Plano
Para rodar de forma automatizada, você pode usar:

Windows: Task Scheduler (Agendador de Tarefas). Crie uma tarefa diária ou a cada hora para executar o script.

Linux/Mac: Cron jobs.

Python Puro: Opcionalmente, você pode transformar em serviço contínuo adicionando um loop while True + time.sleep(3600) no código para rodar a cada hora.

## 📝 Problemas e Resoluções
Web scraping bloqueado → resolvido com API oficial via RapidAPI.

Formato de preço → normalizado para float e salvo em prices.json.

Envio de alertas seguro → email via SMTP usando Senha de App (não a senha normal do e-mail).

Segurança de dados → implementação de leitura via variáveis de ambiente (os.getenv) para proteger chaves de API.

## 💡 Aprendizados
Integração real com APIs externas REST.

Manipulação de JSON para armazenar dados históricos.

Estruturação de projetos Python de forma modular (MVC simplificado).

Segurança no desenvolvimento (uso de .env e .gitignore).

Diferença prática entre scraping de HTML vs APIs oficiais.

## 📊 Possíveis Extensões
[ ] Monitoramento de mais produtos e sites simultaneamente.

[ ] Geração de gráficos de histórico de preços (Matplotlib/Pandas).

[ ] Envio de alertas via WhatsApp (Twilio) ou Telegram Bot.

```
