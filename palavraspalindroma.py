if __name__ == "__main__":
    palavra = str(input(("Digite a palavra: ")))
    print (palavra)
    if str(palavra.upper()) == str(palavra.upper())[::-1]:
        
        print("A palavra " + palavra + " é palindroma")
    else:
        print("A palavra " + palavra + " não é palindroma")
        