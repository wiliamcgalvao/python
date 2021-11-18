def TorreHanoi(n , TorreA, TorreB, TorreC):
    if n==1:
        print("Disco 1 de",TorreA,"para",TorreB)
        return 
    TorreHanoi(n-1, TorreA, TorreC, TorreB)
    print("Disco",n,"de",TorreA,"para",TorreB)
    TorreHanoi(n-1, TorreC, TorreB, TorreA)
          
TorreHanoi(3,'Torre A','Torre B','Torre C')