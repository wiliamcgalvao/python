# Programa para impressão da sequecia de Fibonacci

ntermos = int(input("Quantos termos deseja? "))

# Primeiros 2 termos
n1, n2 = 0, 1
contador = 0

# verifique se o número de termos é válido
if ntermos <= 0:
   print("Por favor, insira um número inteiro positivo")
# se houver apenas um termo, retorna n1
elif ntermos == 1:
   print("Seqüência de Fibonacci até",ntermos,":")
   print(n1)
# gerar sequência de fibonacci
else:
   print("Sequência de Fibonacci:")
   while contador < ntermos:
       print(n1)
       nth = n1 + n2
       # atualizar valores
       n1 = n2
       n2 = nth
       contador += 1