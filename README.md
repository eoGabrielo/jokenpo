# Jokenpo em Python

Bem-vindo ao Jokenpo! Este é um simples jogo de pedra, papel e tesoura implementado em Python.

## Como Jogar

1. Execute o script Python.
2. Escolha Pedra(1), Papel(2), Tesoura(3) ou Finalizar o Jogo(0) quando solicitado.
3. Veja o resultado do round e continue jogando.

## Pontuação

- Cada rodada resulta em pontos para o jogador, a máquina ou empate.
- O jogo finaliza quando o usuário escolhe finalizar o jogo.

## Explicação do codigo

Este código é uma implementação simples do jogo "Pedra, Papel e Tesoura" (ou "Jokenpo") em Python.

1. Importar a biblioteca `random` para gerar números aleatórios.
   
   ```python
   import random
   ```

2. Inicializar variáveis para armazenar os pontos da máquina (`pontosMaquina`), pontos do usuário (`pontosUsuario`) e pontos de empate (`pontosEmpate`).

   ```python
   pontosMaquina = 0
   pontosUsuario = 0
   pontosEmpate = 0
   ```

3. Iniciar o jogo exibindo uma mensagem de boas-vindas e um loop `while` que continuará executando até que o usuário decida finalizar o jogo.

   ```python
   print("Bem vindo ao JOKENPO")
   while True:
   ```

4. Gerar a jogada da máquina aleatoriamente entre 1 e 3 (1 representa Pedra, 2 representa Papel e 3 representa Tesoura) usando `random.randint(1, 3)`.

   ```python
   pedraPapelTesouraMaquina = random.randint(1, 3)
   ```

5. Solicitar ao usuário que faça sua jogada digitando 1 para Pedra, 2 para Papel, 3 para Tesoura ou 0 para finalizar o jogo.

   ```python
   pedraPapelTesouraUsuario = int(input("Escolha Pedra(1), Papel(2), Tesoura(3) ou Finalizar o Jogo(0): "))
   ```

6. Avaliar as jogadas do usuário e da máquina e determinar o resultado do jogo com base nas regras do Jokenpo.

   ```python
   if pedraPapelTesouraUsuario == 1 and pedraPapelTesouraMaquina == 1:
       # Empate
   elif pedraPapelTesouraUsuario == 1 and pedraPapelTesouraMaquina == 2:
       # Máquina vence (Papel cobre Pedra)
   elif ...
   ```

   O mesmo padrão é seguido para as demais combinações de jogadas.

7. Verificar se o número digitado pelo usuário está dentro do intervalo esperado (1 a 3). Se não estiver, exibir uma mensagem de erro.

   ```python
   elif pedraPapelTesouraUsuario > 3:
       print("SOMENTE DIGITOS DE 1 A 3, TENTE NOVAMENTE!")
   ```

8. Tratar exceções se o valor inserido pelo usuário não puder ser convertido para um número inteiro.

   ```python
   except ValueError:
       print("SOMENTE DIGITOS NUMERICOS DE 1 A 3!!!")
   ```

9. Finalizar o jogo quando o usuário digitar 0.

   ```python
   elif pedraPapelTesouraUsuario == 0:
       break
   ```

10. Após o loop, exibir a pontuação final e determinar o vencedor.

   ```python
   print("JOGO FINALIZADO")
   print(f"PONTRUACAO DA MAQUINA: {pontosMaquina}")
   print(f"PONTUACAO DO USUARIO: {pontosUsuario}")
   ```

   Comparar as pontuações da máquina e do usuário para determinar o vencedor ou se o jogo terminou em empate.

   ```python
   if pontosMaquina > pontosUsuario:
       print(f"Maquina venceu com uma pontuanção de {pontosMaquina} contra {pontosUsuario}.")
   elif pontosUsuario == pontosMaquina:
       print(f"Jogo empatado, maquina com {pontosMaquina} pontos e usuario com {pontosUsuario} pontos.")
   else:
       print(f"Usuario venceu com uma pontuanção de {pontosUsuario} contra {pontosMaquina}.")
   ```

Esse é o funcionamento básico do jogo implementado neste código Python. Ele continua executando até que o usuário decida finalizar o jogo digitando 0. Durante cada iteração do loop, o usuário faz sua escolha e o programa determina o vencedor com base nas regras do Jokenpo.
