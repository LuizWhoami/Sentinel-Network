import json

class gerenciar:
    def __init__(self, arquivo="dispositivos.json"):
        self.arquivo = arquivo

    def salvar_dispositivos(lista):
        with open("dispositivos.json", 'w') as f:
            json.dump(lista, f, indent=4)


    def carregar_dispositivos():
        try:
            with open("dispositivos.json", 'r') as f:
                return json.load(f)
        except:
            return []
