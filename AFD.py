estados = ["q1", "q2"]
inicial = "q1"
aceitação = ["q2"]
alfabeto = ["0", "1"]

transicao = {
    "q1" : {"0":"q1", "1":"q2"},
    "q2" : {"0":"q1", "1":"q2"},
}

cadeia = input("Digite uma palavra: ")
estadoAtual = inicial
for c in cadeia:
    if c not in alfabeto:
        estadoAtual = None
        print("VTNC PORRA")
        break
    else:
        estadoAtual = transicao[estadoAtual][c]

if estadoAtual in aceitação:
    print("aceita!!!!!!!!!!!!!!!")
else:
    print("rejeita uhhhhhha")