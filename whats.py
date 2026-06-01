import pandas as pd
import pywhatkit as kit
import time
from datetime import datetime

# Configuração
ARQUIVO_CSV = "campo Junho 2026.csv"

# Dicionário com telefones (você precisa preencher com os números reais)
CONTATOS = {
    "Everton G.": "+55119XXXXXXXXX",  # Substitua pelos números reais
    "Thiago": "+5553984473607",
    "João": "+55119XXXXXXXXX",
    "Alexandre": "+55119XXXXXXXXX",
    "Marco": "+55119XXXXXXXXX",
    "Rodrigo": "+55119XXXXXXXXX",
    "Dinalva": "+55119XXXXXXXXX",
    # Adicione mais contatos conforme necessário
}

def extrair_dados_escala():
    """Extrai os dados da escala manualmente (pois o CSV tem formato irregular)"""
    
    escala = {
        "Carta Zoom": {
            "dia": "Quarta-feira",
            "hora": "19:00",
            "responsaveis": [
                ("03/06/2026", "Everton G."),
                ("10/06/2026", "Thiago"),
                ("17/06/2026", "João"),
                ("24/06/2026", "Alexandre"),
            ]
        },
        "Salão": {
            "dia": "Sábado",
            "hora": "09:15",
            "responsaveis": [
                ("06/06/2026", "Alexandre"),
                ("13/06/2026", "Marco"),
                ("20/06/2026", "Rodrigo"),
                ("27/06/2026", "João"),
            ]
        },
        "Salão/Casa": {
            "dia": "Domingo",
            "hora": "09:15",
            "responsaveis": [
                ("07/06/2026", "Marco"),
                ("14/06/2026", "Thiago"),
                ("21/06/2026", "João"),
                ("28/06/2026", "Grupos Alexandre / Rodrigo"),
            ]
        },
        "Carrinho": {
            "responsaveis": [
                ("Terça", "14:00", "Centro/Rodoviário", "Dinalva/convite"),
                ("Terça", "14:00", "Centro frente cinema", "Dinalva/convite"),
                ("Quinta", "08:00", "Loja Americanas", "Marco/convite"),
            ]
        }
    }
    
    return escala

def gerar_mensagem(atividade, data, hora, pessoa):
    """Gera a mensagem personalizada"""
    mensagem = f"""Olá {pessoa}! 👋

Lembrete de Responsabilidade - JUNHO/2026

📋 Atividade: {atividade}
📅 Data: {data}
🕐 Hora: {hora}

Você está escalado(a) para esta data!
Confirme sua presença. Obrigado! ✨"""
    
    return mensagem

def enviar_mensagens(debug=True):
    """Envia mensagens via WhatsApp"""
    
    escala = extrair_dados_escala()
    contador = 0
    
    print("=" * 60)
    print("ENVIADOR DE LEMBRETES - ESCALA JUNHO/2026")
    print("=" * 60)
    
    # Processa Carta Zoom
    print("\n📨 CARTA ZOOM (Quartas à noite):")
    for data, pessoa in escala["Carta Zoom"]["responsaveis"]:
        if pessoa in CONTATOS:
            mensagem = gerar_mensagem(
                "Carta Zoom",
                data,
                escala["Carta Zoom"]["hora"],
                pessoa
            )
            
            telefone = CONTATOS[pessoa]
            print(f"\n→ {pessoa} ({telefone})")
            print(f"  Mensagem:\n{mensagem}\n")
            
            if not debug:
                kit.sendwhatmsg(telefone, mensagem, 19, 0)  # Envia 19:00
                time.sleep(2)
            
            contador += 1
    
    # Processa Salão
    print("\n📨 SALÃO (Sábados de manhã):")
    for data, pessoa in escala["Salão"]["responsaveis"]:
        if pessoa in CONTATOS:
            mensagem = gerar_mensagem(
                "Salão",
                data,
                escala["Salão"]["hora"],
                pessoa
            )
            
            telefone = CONTATOS[pessoa]
            print(f"\n→ {pessoa} ({telefone})")
            print(f"  Mensagem:\n{mensagem}\n")
            
            if not debug:
                kit.sendwhatmsg(telefone, mensagem, 9, 15)  # Envia 09:15
                time.sleep(2)
            
            contador += 1
    
    # Processa Salão/Casa
    print("\n📨 SALÃO/CASA (Domingos de manhã):")
    for data, pessoa in escala["Salão/Casa"]["responsaveis"]:
        if pessoa in CONTATOS:
            mensagem = gerar_mensagem(
                "Salão/Casa",
                data,
                escala["Salão/Casa"]["hora"],
                pessoa
            )
            
            telefone = CONTATOS[pessoa]
            print(f"\n→ {pessoa} ({telefone})")
            print(f"  Mensagem:\n{mensagem}\n")
            
            if not debug:
                kit.sendwhatmsg(telefone, mensagem, 9, 15)  # Envia 09:15
                time.sleep(2)
            
            contador += 1
    
    print("=" * 60)
    print(f"✅ Total de mensagens a enviar: {contador}")
    print(f"⚠️  Modo DEBUG: {debug} (não envia de verdade)")
    print("=" * 60)

if __name__ == "__main__":
    # Execute em modo debug=True primeiro para verificar
    enviar_mensagens(debug=True)
    
    # Após verificar, mude para debug=False para enviar de verdade
    # enviar_mensagens(debug=False)
    
