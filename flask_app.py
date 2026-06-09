from flask import Flask, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app) # Permite que a página do GitHub Pages acesse este servidor na nuvem

@app.route('/api/catalogar', methods=['GET'])
def api_catalogar():
    # Captura os parâmetros enviados pela sua página HTML
    try:
        dias = int(request.args.get('dias', 30))
        timeframe = request.args.get('timeframe', 'M5')
        minimo = float(request.args.get('minimo', 80))
    except ValueError:
        return jsonify({"erro": "Parâmetros inválidos"}), 400
    
    # Lista de múltiplos ativos analisados simultaneamente
    lista_ativos = ['EUR/USD', 'GBP/USD', 'USD/JPY', 'EUR/GBP', 'AUD/USD', 'BTC/USD', 'ETH/USD']
    sinais_gerados = []
    
    for ativo in lista_ativos:
        # Simulação do cálculo probabilístico de assertividade do passado
        assertividade = round(random.uniform(75, 98), 1)
        
        # Filtro: só entra na lista se atingir a assertividade mínima da tela
        if assertividade >= minimo:
            direcao = "CALL" if random.random() > 0.5 else "PUT"
            vitorias = int(dias * (assertividade / 100))
            derrotas = dias - vitorias
            
            # Gera horários fictícios simulando os melhores padrões encontrados
            horas = str(random.randint(6, 22)).zfill(2)
            minutos = str(random.choice([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])).zfill(2)
            horario = f"{horas}:{minutos}"
            
            sinais_gerados.append({
                "ativo": ativo,
                "horario": horario,
                "timeframe": timeframe,
                "operacao": direcao,
                "vitorias": vitorias,
                "derrotas": derrotas,
                "assertividade": assertividade
            })
            
    # Retorna a lista de sinais ordenando da maior assertividade para a menor
    sinais_gerados = sorted(sinais_gerados, key=lambda k: k['assertividade'], reverse=True)
    return jsonify(sinais_gerados)