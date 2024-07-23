votos = []
sistema_operacional = [
'Windows Server',
'Unix',
'Linux',
'Netware',
'Mac OS',
'Outro',
]


print("Qual o melhor Sistema Operacional para uso em servidores?")
print("""
1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
""")

while True: 
    voto = input('Informe seu voto [1-6] [0-sair] : ')
    if not voto.isnumeric() or int(voto) < 0 or int(voto) > 6:
        print('Opção inválida !!')
        continue
    elif voto == '0':
        print('TCHAU TCHAU :P')
        break
    votos.append(voto)


print('Sistema Operacional     Votos   %')
print('-------------------     -----   ---')