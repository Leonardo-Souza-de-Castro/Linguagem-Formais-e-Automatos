estados = input("Digite os estados: ").split()
inicial = input("Digite o estado inicial: ")
aceitação = input("Digite o estado de aceitação: ").split()
alfabeto = input("Digite o algabeto: ").split()
transicao = {}
print("Digite as transições (ex: q0 q1 q0). Enter vazio para parar:")

while True:
    linha = input().strip()
    if not linha:
        break

    partes = linha.split()
    estado_atual = partes[0]
    transicao[estado_atual] = {}

    for i, simbolo in enumerate(alfabeto):
        transicao[estado_atual][simbolo] = partes[i+1]

cadeia = input("Digite uma palavra: ").split()
estadoAtual = inicial

for palavra in cadeia:
    estadoAtual = inicial  # sempre começa do inicial para cada palavra

    for simbolo in palavra:   # percorre caractere por caractere
        if simbolo not in alfabeto:
            estadoAtual = None
            break
        else:
            estadoAtual = transicao[estadoAtual][simbolo]

    if estadoAtual in aceitação:
        print("aceita")
    else:
        print("rejeita")