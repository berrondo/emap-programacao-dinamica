def MAX(S):
    somas_e_sequencias = {0:(0,0)}
    # primeiro_indice = 0
    soma = 0
    
    print
    for indice, da_vez in enumerate(S):
        anterior_e_da_vez = soma + da_vez
        soma = max(anterior_e_da_vez, da_vez)
        print soma,
        if soma == da_vez:
            primeiro_indice = indice
        somas_e_sequencias[soma] = (primeiro_indice, indice)
         
    maior_soma = max(somas_e_sequencias.keys())
    i_incial, i_final = somas_e_sequencias[maior_soma]
    
    i_final = i_final and i_final + 1
         
    print
    print somas_e_sequencias
    return i_incial, i_final, S[i_incial:i_final], maior_soma
    
    
S =  [-5, 15, -30, 10, -5, 40, 10]
S1 = [5, 15, 30, 10, 5, 40, 10]
S2 = [-5, -15, -30, -10, -5, -40, -10]
S3 = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
S4 = [0, 5, 15, -30, 10, -5, 40, 10]
S5 = [5, 15, -30, 10, -5, 40, -10]
print MAX(S)
print MAX(S1)
print MAX(S2)
print MAX(S3)
print MAX(S4)
print MAX(S5)