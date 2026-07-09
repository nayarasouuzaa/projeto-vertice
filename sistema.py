import requests

# 1. BANCO DE DADOS FAKE DO ESTREITAMENTO DE STOCK
estoque_da_loja = [
    {"produto": "Teclado Mecânico", "quantidade": 10},
    {"produto": "Mouse Sem Fio", "quantidade": 2},        # Vai disparar alerta (menor que 3)
    {"produto": "Monitor 24 polegadas", "quantidade": 5},
    {"produto": "Cabo HDMI 2m", "quantidade": 1},         # Vai disparar alerta (menor que 3)
]

# 2. CONFIGURAÇÕES DO TELEGRAM
# Substitui o texto dentro das aspas pelas chaves que guardaste no bloco de notas:
TELEGRAM_TOKEN = "8988190052:AAEySeXa49fh8ILIP2oiz844kOLwrr6gIgg"
CHAT_ID = "7203561602"


def enviar_alerta_telegram(mensagem):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    dados = {
        "chat_id": CHAT_ID,
        "text": mensagem
    }
    try:
        resposta = requests.post(url, data=dados)
        if resposta.status_code == 200:
            print("Sucesso: Alerta enviado para o Telegram!")
        else:
            print(f"Erro no Telegram: {resposta.status_code}. Verifica os teus tokens.")
    except Exception as erro:
        print(f"Falha de internet: {erro}")


def verificar_estoque():
    print("A analisar o stock da loja...")
    for item in estoque_da_loja:
        nome_produto = item["produto"]
        qtd_atual = item["quantidade"]
        
        # Regra de negócio: quantidade menor que 3 é crítica
        if qtd_atual < 3:
            texto = f"⚠ ALERTA DE RUPTURA!\nO produto '{nome_produto}' está a acabar. Restam apenas {qtd_atual} unidades no stock!"
            enviar_alerta_telegram(texto)
    print("Verificação concluída!")

if __name__ == "__main__":
    verificar_estoque()