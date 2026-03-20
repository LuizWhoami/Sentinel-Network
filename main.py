import time
from sccaner import scannerrede
from detector import detectorint
from alerta import alertamen
from gerenciador import gerenciar

rede = '192.168.0.1/24'

token = "Insira seu token"
chat_id = 'Insira seu chat_ID'
alerta = alertamen(token, chat_id)

scannerrede = scannerrede(rede)
detector = detectorint()
db = gerenciar

conhecidos = db.carregar_dispositivos()

if not conhecidos:
    print("nenhum dispositivos conhecido")
    conhecidos = scannerrede.scan_rede(rede)
    print("Debug Scan:", conhecidos)
    db.salvar_dispositivos(conhecidos)


while True:
    print("Scaneando Rede.")
    atual = scannerrede.scan_rede(rede)
    conhecidos = db.carregar_dispositivos()

    novos = detector.detectar(atual, conhecidos)

    for dispositivos in novos:
        alerta.enviar(dispositivos)

    time.sleep(10)