#Programa desafio final java to python

if __name__ == "__main__":
     with open('c:\\desafio\\morse.in') as fin:
        with open('c:\\desafio\\texto.out', 'r+') as fout:
            fout.truncate(0)
        with open('c:\\desafio\\texto.out', 'a') as fout:
            morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
            linhas = fin.readlines()
            for linha in linhas:
                temp = linha.rstrip('\n').split(" ");
                palavra = ""
                for t in temp:
                    contador = 0 
                    for p in morse:
                        if t == p:
                            palavra += chr(65 + contador)
                            break;
                        contador+=1
                fout.write(palavra+'\n')
                if linha =="..-. .. --":
                    break
            
            
            
#            char = fin.read(1)
#            while char != "":
#               fout.write(char)
#               char = fin.read(1)


#          texto = fin.readline()
#          with open('c:\\desafio\\texto.out', 'w') as fout:
#          fout.write(texto)
