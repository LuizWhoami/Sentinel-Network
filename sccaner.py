from scapy.all import ARP, Ether, srp
import json
import time

class scannerrede:
    def __init__(self, rede):
        self.rede = rede

    def scan_rede(self, rede):
        arp = ARP(pdst=self.rede)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        pacote = ether / arp

        resultado = srp(pacote, timeout=2, verbose=False)[0]

        dispositivos = []

        for enviado, recebido in resultado:
            dispositivos.append({"IP": recebido.psrc, "MAC": recebido.hwsrc})

        return dispositivos

