# Dados fictícios
dados_qualidade_agua = [
    {"localizacao": "Praia A", "ph": 7.5, "temperatura": 25, "poluentes": 3},
    {"localizacao": "Praia B", "ph": 8.2, "temperatura": 27, "poluentes": 5},
    {"localizacao": "Praia C", "ph": 6.8, "temperatura": 22, "poluentes": 1},
    {"localizacao": "Praia D", "ph": 9.1, "temperatura": 30, "poluentes": 4},
    {"localizacao": "Praia E", "ph": 7.0, "temperatura": 24, "poluentes": 2},
]

# Função para verificar a qualidade da água
def verificar_qualidade(dados):
    for ponto in dados:
        localizacao = ponto["localizacao"]
        ph = ponto["ph"]
        temperatura = ponto["temperatura"]
        poluentes = ponto["poluentes"]

        alerta = []

        if ph < 6.5 or ph > 8.5:
            alerta.append(f"pH fora do padrão seguro: {ph}")
        
        if temperatura < 20 or temperatura > 28:
            alerta.append(f"Temperatura fora do padrão seguro: {temperatura}°C")
        
        if poluentes > 3:
            alerta.append(f"Nível de poluentes alto: {poluentes}")

        if alerta:
            print(f"Alerta para {localizacao}:")
            for aviso in alerta:
                print(f"  - {aviso}")
        else:
            print(f"A qualidade da água em {localizacao} está dentro dos padrões seguros.")

# Verificar a qualidade da água
verificar_qualidade(dados_qualidade_agua)
