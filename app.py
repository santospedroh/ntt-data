from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Inicializando o tabuleiro
tabuleiro = [" " for _ in range(9)]
jogador_atual = "X"

# Função para verificar o vencedor
def verificar_vencedor():
    combinacoes = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontais
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Verticais
        (0, 4, 8), (2, 4, 6)              # Diagonais
    ]
    
    for a, b, c in combinacoes:
        if tabuleiro[a] == tabuleiro[b] == tabuleiro[c] and tabuleiro[a] != " ":
            return tabuleiro[a]
    
    if " " not in tabuleiro:
        return "Empate"
    
    return None

@app.route('/')
def index():
    return render_template('index.html', tabuleiro=tabuleiro, jogador_atual=jogador_atual)

@app.route('/jogada/<int:posicao>')
def jogada(posicao):
    global jogador_atual
    if tabuleiro[posicao] == " ":
        tabuleiro[posicao] = jogador_atual
        vencedor = verificar_vencedor()
        if vencedor:
            return jsonify({"vencedor": vencedor})
        
        # Troca de jogador
        jogador_atual = "O" if jogador_atual == "X" else "X"
    
    return jsonify({"tabuleiro": tabuleiro, "jogador_atual": jogador_atual})

@app.route('/reiniciar')
def reiniciar():
    global tabuleiro, jogador_atual
    tabuleiro = [" " for _ in range(9)]
    jogador_atual = "X"
    return jsonify({"tabuleiro": tabuleiro, "jogador_atual": jogador_atual})

@app.route("/hello")
def hello():
    try:       
        print("Hello World") 
        return print("Hello World") 
    except Exception as e:
        print(e)

if __name__ == "__main__":
    app.run(debug=True)
