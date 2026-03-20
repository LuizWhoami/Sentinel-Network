import requests

class alertamen:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id

    def enviar(self, dispositivo):
        ip = dispositivo["IP"]
        mac = dispositivo["MAC"]

        mensagem = f'Dispositivo desconhecido \n IP: {ip} \n MAC: {mac}'
        url = f'https://api.telegram.org/bot{self.token}/sendMessage'

        print("enviando Alerta...", mensagem)
        r = requests.get(url, params={
        "chat_id": self.chat_id,
        "text": mensagem})

        print("Status: ", r.status_code)
        print("Resposta: ", r.text)