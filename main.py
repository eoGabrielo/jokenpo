import random

pontosMaquina = 0
pontosUsuario = 0
pontosEmpate = 0

print("Bem vindo ao JOKENPO")
while True:
    pedraPepelTesouraMaquina = random.randint(1,3)
    try:
        pedraPepelTesouraUsuario = int(input("Escolha Pedra(1), Papel(2), Tesoura(3) ou Finalizar o Jogo(0): "))

        #USUARIO PEDRA
        if pedraPepelTesouraUsuario == 1 and pedraPepelTesouraMaquina == 1:
            print("")
            print("Vc jogou 'Pedra' a maquina 'Pedra'")
            print("JOGO EMPATADO!")
            pontosEmpate = pontosEmpate + 1
        elif pedraPepelTesouraUsuario == 1 and pedraPepelTesouraMaquina == 2:
            print("")
            print("Vc jogou 'Pedra' a maquina 'Papel'")
            print("VOCE PERDEU!")
            pontosMaquina = pontosMaquina + 1
        elif pedraPepelTesouraUsuario == 1 and pedraPepelTesouraMaquina == 3:
            print("")
            print("Vc jogou 'Pedra' a maquina 'Tesoura'")
            print("VOCE GANHOU!")
            pontosUsuario = pontosUsuario + 1
        #USUARIO PAPEL
        elif pedraPepelTesouraUsuario == 2 and pedraPepelTesouraMaquina == 1:
            print("")
            print("Vc jogou 'Papel' a maquina 'Pedra'")
            print("VOCE GANHOU!")
            pontosUsuario = pontosUsuario + 1
        elif pedraPepelTesouraUsuario == 2 and pedraPepelTesouraMaquina == 2:
            print("")
            print("Vc jogou 'Papel' a maquina 'Papel'")
            print("JOGO EMPATOU!")
            pontosEmpate = pontosEmpate + 1
        elif pedraPepelTesouraUsuario == 2 and pedraPepelTesouraMaquina == 3:
            print("")
            print("Vc jogou 'Papel' a maquina 'Tesoura'")
            print("VOCE PERDEU!")
            pontosMaquina = pontosMaquina + 1
        #USUARIO TESOURA
        elif pedraPepelTesouraUsuario == 3 and pedraPepelTesouraMaquina == 1:
            print("")
            print("Vc jogou 'Tesoura' a maquina 'Pedra'")
            print("VOCE PERDEU!")
            pontosMaquina = pontosMaquina + 1
        elif pedraPepelTesouraUsuario == 3 and pedraPepelTesouraMaquina == 2:
            print("")
            print("Vc jogou 'Tesoura' a maquina 'Papel'")
            print("VOCE GANHOU!")
            pontosUsuario = pontosUsuario + 1
        elif pedraPepelTesouraUsuario == 3 and pedraPepelTesouraMaquina == 3:
            print("")
            print("Vc jogou 'Tesoura' a maquina 'Tesoura'")
            print("JOGO EMPATOU!")
            pontosEmpate = pontosEmpate + 1
        #NUMERO MAIOR QUE 3, bate aqui.
        elif pedraPepelTesouraUsuario > 3:
            print("SOMENTE DIGITOS DE 1 A 3, TENTE NOVAMENTE!")
        elif pedraPepelTesouraUsuario == 0:
            break
    #Junto com try, se o valor for diferente do try "int", bate aqui.
    except ValueError:
        print("SOMENTE DIGITOS NUMERICOS DE 1 A 3!!!")
        
print("")
print("JOGO FINALIZADO")
print(f"PONTRUACAO DA MAQUINA: {pontosMaquina}")
print(f"PONTUACAO DO USUARIO: {pontosUsuario}")
if pontosMaquina > pontosUsuario:
    print(f"Maquina venceu com uma pontuanção de {pontosMaquina} contra {pontosUsuario}.")
elif pontosUsuario == pontosMaquina:
    print(f"Jogo empatado, maquina com {pontosMaquina} pontos e usuario com {pontosUsuario} pontos.")
else:
    print(f"Usuario venceu com uma pontuanção de {pontosUsuario} contra {pontosMaquina}.")







