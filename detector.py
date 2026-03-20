class detectorint:
    def __init__(self):
        self.alertados = set()

    def detectar(self, atual, conhecidos):
        conhecidos_macs = [dispositivos["MAC"] for dispositivos in conhecidos] 
        novos = []
        for dispositivos in atual:
            if dispositivos["MAC"] not in conhecidos_macs and dispositivos["MAC"] not in self.alertados:
                print("Dispositivos DesConhecidos")
                print(f"IP: {dispositivos['IP']} | MAC {dispositivos['MAC']}")

                novos.append(dispositivos)
                self.alertados.add(dispositivos['MAC'])

        return novos