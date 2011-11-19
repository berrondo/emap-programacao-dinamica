olá, pessoal!

para quem estiver a fim de ler um loooongo (gigantesco mesmo) relato de uma experiência iterativa e incremental! :D

nesta segunda, depois da aula (e da entrega da prova de algoritmo que deixou a todos arrasados) tivemos, na minha opinião, uma de nossas melhores experiências coletivas pós-aula até agora! e olha que eu acho que vínhamos num crescendo, infelizmente compartilhado por poucos...

bom, depois da debandada da maioria do pessoal, sobramos eu, Débora e Ariel e tudo começou com a Débora dizendo que não conseguiu ir muito longe quando tentou sozinha encarar o exercicio 6.1 do Papadimitriou, que aqui transcrevo:

"""
    6.1. A contiguous subsequence of a list S is a subsequence made up of consecutive elements of S. For instance, if S is 

    5; 15; -30; 10; -5; 40; 10;

    then 15; 30; 10 is a contiguous subsequence but 5; 15; 40 is not. Give a linear-time algorithm for the following task:

    Input: A list of numbers, a1; a2; . . . ; an.
    Output: The contiguous subsequence of maximum sum (a subsequence of length zero has sum zero).

    For the preceding example, the answer would be 10; -5; 40; 10, with a sum of 55.

    (Hint: For each j in {1; 2; . . . ; n}, consider contiguous subsequences ending exactly at position j.)
"""

que é muito semelhante (exatamente igual?) - como ela percebeu - a este exercício, da lista 2:

"""
    7. Escreva um algoritmo para, dado um vetor de números reais, computar a soma máxima dentre todos os possíveis subvetores contínuos do vetor entrada. Por exemplo, no vetor X abaixo, o intervalo X[3...7] tem a maior soma, 187. O algoritmo deve devolver a maior soma, não o intervalo que a define.


    31, -41, 59, 26, -53, 58, 97, -93, -23, 84
              ^                ^
              3                7
              
    O problema é fácil quando todos os números são positivos. Neste caso, a maior soma é claramente a soma do vetor de entrada inteiro. A dificuldade aparece quando alguns números são negativos. Devemos considerar os números negativos na esperança de que os positivos selecionados conjuntamente compensem a contribuição negativa? Para completar a definição do problema, quando todos os números são negativos, a máxima soma é zero, obtida com a escolha do intervalo vazio.
    (a) Desenvolva um algoritmo com complexidade O(n³).
    (b) Desenvolva um algoritmo com complexidade O(n²).
    (c) Seria possível encontrar um algoritmo com complexidade menor que O(n²)? Qual a menor complexidade possível para um algoritmo que resolva este problema? Argumente. 
"""

começamos a pensar e falar juntos: ah! era aquele exercício que - em tese - não tinha solução melhor do que n²! mas, peraí, é o primeiro exercício do capítulo sobre programação dinâmica e tínhamos acabado de ver (eu e a Débora, pelo menos) o Alexandre falando exaustivamente sobre o tema com aquele problema da "distância de edição"!

então eu li a fala do Alexandre que anotei no papel, definindo programação dinâmica (com minhas palavras):

"""
    A programação dinâmica se aproveita da ordenação apropriada (correta) de instâncias menores do problema. Ou, a solução n depende de n-1...
"""

hummm... mais ou menos isso...

voltando ao nosso problema, será que era isso de que se tratava?... sim! vamos aplicar a tal da programação dinâmica:

em primeiro lugar, não se trata de ordenar a entrada. a ordem da entrada é parte do problema... humm, mas e aquele negócio de sair calculando cada passo e guardando em uma matriz para utilizar de novo ao calcular o passo seguinte e obter a resposta na última célula da matriz como no  caso do problema da distância de edição?

volte lá no problema... sacou a hint "Para cada j pertencente a [1, 2, ..., n], considere subsequências contíguas terminando exatamente na posição j"?

hummm... será que é isso? se tomarmos um j qualquer, basta ver que subsequência terminando em j produz a maior soma até ali?

inspirados pelo distância de edição do Alexandre, escrevemos no quadro uma bizarrice mais ou menos assim (numa mistura de pseudo-código e Python):

    maior_sequencia = max{maior_sequencia(S[0:j]), maior_sequencia(S[1:j]), ..., S[j]}

perceberam a tentativa?... de escrever o problema da vez (em j) dependente dos subproblemas anteriores?

começou a saltar aos olhos uma série de coisas: "você vai calcular tudo de novo a cada vez?", "isso é recursivo?", "isso é linear?"

e se guardássemos os valores calculados anteriormente para calcular o próximo? a Débora sugeriu que usássemos um dicionário. a Débora adora dicionários!

tá... e que cara teria esse dicionário? mais ou menos isso:

    D = { a_maior_soma_ate_o_momento : (indice_inicial_do_intervalo_que_a_produz, indice_final) }

ou: guardaríamos em cada chave o valor da maior soma que tivéssemos no intervalo considerado. esta chave teria como seu valor uma tupla com os dois índices do início e do final da subsequência que gera essa maior soma (por que o problema quer exatamente a subsequência).

então precisaríamos de um for para percorrer a sequência de entrada e ir calculando a cada passo, de j em j:

    for j in range(len(S)):
        MS = max(maior_sequencia(S[0:j]), maior_sequencia(S[1:j]), ..., S[j])
        D[MS] = (    ???    , j)
    
entenderam a ideia??? muito esquisito (e muito errado!)... mas no caminho!... por outro lado, como conseguimos o primeiro item da sequência para colocar no lugar do ??? ?

é preciso parar um momento e chamar atenção para o fato de que o que descrevi até aqui se deu em forma de brainstorming: a cada momento cada um de nós deu um palpite que foi nos colocando na direção certa. cada insight (ou chute...) que contei até agora veio de um de nós em um ou outro momento, em zigue-zague e não linearmente como narrado aqui!

neste momento, mais dois insights foram fundamentais: o Ariel chamou atenção para o fato que bastava realmente comparar o problema da vez com o imediatamente anterior "já solucionado" (usando mesmo a definição de programação dinâmica!) e a Débora resolveu fazer um chinês com o que tínhamos até ali, o que nos deu a ideia de como ficaria o dicionário que queríamos montar, iteração a iteração:

    maior soma até então, inicio da sequencia, fim da sequencia:  (indices começam em 1)
    5                     1                    1
    20                    1                    2
    -10                   1                    3
    10                    4                    4
    5                     4                    5
    45                    4                    6
    55                    4                    7

se conseguíssemos montar este dicionário, a resposta seria dada diretamente pela maior chave do dicionário, a qual indicaria a subsequência de maior soma, ou, em Python:

    D[max(D.keys())] !!!

e parece realmente que é possível montar este dicionário em uma passada pela sequência, a nossa tão desejada solução linear!!!

bom, vamos colocar tudo dentro de uma função:

    def MAX(S):
        somas_e_sequencias = {}                               # o dicionario que vamos montar
        soma = 0                                              # uma soma para comecar
        
        for indice, da_vez in enumerate(S):                   # enumerate retorna o indice do elemento e o proprio elemento
        
            anterior_e_da_vez = soma + da_vez
            soma = max(anterior_e_da_vez, da_vez)             # quem eh maior?
            
            somas_e_sequencias[soma] = (   ???   , indice)
             
        maior_soma = max(somas_e_sequencias.keys())           # qual a maior chave? a maior de todas as somas?
        i_incial, i_final = somas_e_sequencias[maior_soma]    # entre quais indices estah a maior soma?


dá para entender? o dicionário é montado dentro do for onde são consideradas a soma anterior e o elemento da vez. depois do for, pegamos a maior chave e vemos que índices guardamos para ela...

opa! tá faltando coisa aí ainda... é... ainda não está certo, mas a ideia geral já se consolidou. só que ainda não sabemos como pegar o primeiro indice das subsequências...

a descoberta de quem é esse cara está na linha:

            soma = max(anterior_e_da_vez, da_vez)             # quem eh maior?

a pergunta é: quem ganha esse max? se a soma anterior mais o da vez ganha, continuamos a considerar a subsequência em que estamos... se ganha o elemento da vez... opa, começa uma nova subsequência então!! mas precisamos começar com algum indice_inicial e atualizá-lo sempre que o elemento da vez ganhar o max!... vamos colocar essas linhas na nossa função:

    def MAX(S):
        somas_e_sequencias = {}                               # o dicionario que vamos montar
        soma = 0                                              # uma soma para comecar
        
        for indice, da_vez in enumerate(S):                   # enumerate retorna o indice do elemento e o proprio elemento
        
            anterior_e_da_vez = soma + da_vez
            soma = max(anterior_e_da_vez, da_vez)             # quem eh maior?
            
            if soma == da_vez:                                # se o max eh o elemento da vez...
                primeiro_indice = indice                      # eh hora de trocar o indice inicial. temos o indice inicial!!
                                                              # claro que na primeira passagem, soma == da_vez, logo, primeiro_indice = 0
                
            somas_e_sequencias[soma] = (primeiro_indice, indice)
             
        maior_soma = max(somas_e_sequencias.keys())           # qual a maior chave? a maior de todas as somas?
        i_incial, i_final = somas_e_sequencias[maior_soma]    # entre quais indices estah a maior soma?
    

e então terminou o nosso tempo e corri para escrever um código quase exatamente assim, que rodamos e nos satisfez (pelo menos para o que tínhamos considerado até então):
        
    def MAX_SEQ(s):
        max_seq = {}; ultimo = 0; soma_max = 0;     # tinhamos chamado o primeiro de ultimo :D
        for i in range(len(s)):
            soma = max((soma_max + s[i]), s[i])
            if soma == s[i]:
                ultimo = i
            max_seq[soma] = (ultimo, i)
            soma_max = soma
        return max_seq
        
para escrever isso aqui eu mudei um pouco a cara dele, de um modo que - acho eu - deixa ele mais compreensível. também estávamos experimentando, então nada estava muito polido...  mas...
    
não, a Débora não está satisfeita... (ela é pessimista...) se utilizarmos um valor inicial negativo tudo vai dar errado... se todos os itens da sequência forem negativos tudo vai dar errado...

humm... de fato, nos dois enunciados temos a questão da sequência vazia que dá soma 0 e para a sequência toda negativa a soma é zero... hummm... 

Ah!... calma, Débora! primeiro aquela inicialização da soma = 0 não é para comparar com nada, já que aquele 0 é somado com o primeiro elemento da sequência de cara... o 0 só inicializa "soma" de forma neutra pra não ter influência em nada mesmo... 

quanto a sequência de negativos e a soma 0 da subsequência vazia, veja se essa nova inicialização do nosso dicionário não resolve: (é, você pensou nisso... ;-) )

    somas_e_sequencias = {0 : (0, 0)}                        # o dicionario que vamos montar
    
e temos a soma 0 produzida pela sequência vazia!!! no caso da sequência toda negativa, as sub-somas negativas são comparadas com o 0 no final e o 0 ganha!!!  \o/

mas é preciso outro truque para lidar com o fato de que em Python o segundo índice de uma fatia não retorna seu elemento correspondente. fatias de intervalos em Python são sempre fechadas no início e abertas no fim como em [i, j[

bizarramente, essa linha resolve:

    i_final = i_final and i_final + 1

que seria o equivalente a fazer:

    if i_final: i_final += 1
    
querendo dizer que se o i_final não for 0, a gente soma 1 a ele... é, é esquisito... mas é que queremos mantê-lo 0 quando ele for 0 para que a sequência produzida na resposta seja [], exceto quando houver um i_final, que para retornar o elemento ao qual corresponde precisa que somemos 1 a ele...

pondo tudo junto (e simplificando um pouco):
    

    def MAX(S):
        somas_e_sequencias = {0 : (0, 0)}                     # o dicionario que vamos montar
        soma = 0                                              # uma soma para comecar
        
        for indice, da_vez in enumerate(S):                   # enumerate retorna o indice do elemento e o proprio elemento
        
            soma = max( (soma + da_vez), da_vez )             # quem eh maior?
            
            if soma == da_vez:                                # se o max eh o elemento da vez...
                primeiro_indice = indice                      # eh hora de trocar o indice inicial. temos o indice inicial!!
                
            somas_e_sequencias[soma] = (primeiro_indice, indice)
             
        maior_soma = max(somas_e_sequencias.keys())           # qual a maior chave? a maior de todas as somas?
        i_incial, i_final = somas_e_sequencias[maior_soma]    # entre quais indices estah a maior soma?
        
        if i_final: i_final += 1                              # ou: i_final = i_final and i_final + 1
        
        return i_incial, i_final, S[i_incial:i_final], maior_soma   # retornando tudo!
    
    
alguns exemplos de uso e suas saídas correspondentes (o código que executei tem uns 'prints' estratégicos ;-) ):
(e lembrem-se: dicionários não possuem ordem determinada para suas chaves!)

    print MAX([5, 15, -30, 10, -5, 40, 10])
    5 20 -10 10 5 45 55
    {0: (0, 0), 5: (3, 4), 10: (3, 3), 45: (3, 5), 20: (0, 1), -10: (0, 2), 55: (3, 6)}
    (3, 7, [10, -5, 40, 10], 55)
    
    print MAX([-5, 15, -30, 10, -5, 40, 10])
    -5 15 -15 10 5 45 55
    {0: (0, 0), 5: (3, 4), 10: (3, 3), 45: (3, 5), 15: (1, 1), -15: (1, 2), 55: (3, 6), -5: (0, 0)}  # humm... esse -5 deveria retornar (0, 1)? serah que eh preciso ajustar isso?
    (3, 7, [10, -5, 40, 10], 55)
    
    print MAX([5, 15, -30, 10, -5, 40, -10])
    5 20 -10 10 5 45 35
    {0: (0, 0), 35: (3, 6), 5: (3, 4), 10: (3, 3), 45: (3, 5), 20: (0, 1), -10: (0, 2)}
    (3, 6, [10, -5, 40], 45)

    print MAX([0, 5, 15, -30, 10, -5, 40, 10])
    0 5 20 -10 10 5 45 55
    {0: (0, 0), 5: (4, 5), 10: (4, 4), 45: (4, 6), 20: (1, 2), -10: (1, 3), 55: (4, 7)}
    (4, 8, [10, -5, 40, 10], 55)
    
    print MAX([5, 15, 30, 10, 5, 40, 10])
    5 20 50 60 65 105 115
    {0: (0, 0), 65: (0, 4), 5: (0, 0), 105: (0, 5), 50: (0, 2), 115: (0, 6), 20: (0, 1), 60: (0, 3)}
    (0, 7, [5, 15, 30, 10, 5, 40, 10], 115)

    print MAX([-5, -15, -30, -10, -5, -40, -10])    # olha a sequência toda negativa aqui!
    -5 -15 -30 -10 -5 -40 -10
    {0: (0, 0), -30: (2, 2), -15: (1, 1), -10: (6, 6), -40: (5, 5), -5: (4, 4)}
    (0, 0, [], 0)

    print MAX([31, -41, 59, 26, -53, 58, 97, -93, -23, 84])
    31 -10 59 85 32 90 187 94 71 155
    {0: (0, 0), 32: (2, 4), 187: (2, 6), 71: (2, 8), 155: (2, 9), 85: (2, 3), -10: (0, 1), 90: (2, 5), 59: (2, 2), 94: (2, 7), 31: (0, 0)}
    (2, 7, [59, 26, -53, 58, 97], 187)

    
é, parece que restam alguns probleminhas... nem eu sei se cobrimos todas as alternativas... mas acho que vale o relato. o que eu fiz foi só dar uma polida no que fizemos e terminar o que faltou. seria bem interessante encarar de novo o mesmo problema, mas dessa vez em um dojo, com passos de bebê e casos de testes cobrindo todas as alternativas que quiséssemos imaginar, permitindo refatoração no código em qualquer momento...

era isso... let's do more of those! :D
><>Cláudio Berrondo
