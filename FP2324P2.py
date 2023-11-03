# This is the Python script for your project
# INTERSEÇÃO TAD - 2.1.1

def cria_intersecao(col, lin):
    '''cria intersecao: str x int → intersecao
    cria intersecao(col,lin) recebe um caracter e um inteiro correspondentes à
    coluna col e `a linha lin e devolve a interseção correspondente.'''

    try:
        int(str(lin))
        str(col)
        if type(col) != str or len(col) != 1 or (not (64 < ord(col) < 84))\
         or type(lin) != int or (not (0 < int(lin) < 20)):
            raise ValueError("cria_intersecao: argumentos invalidos")
        return {"col": col, "lin": lin}
    except ValueError:
        raise ValueError("cria_intersecao: argumentos invalidos")
    except TypeError as e:
        if "unhashable type: dict" in str(e):
            raise ValueError("cria_intersecao: argumentos invalidos")

def obtem_col(inter):
    '''obtem col: intersecao → str
    obtem col(i) devolve a coluna col da interseção i'''

    return inter["col"]

def obtem_lin(inter):
    '''obtem lin: intersecao → int
    obtem lin(i) devolve a linha lin da interseção i.'''

    return inter["lin"]

def eh_intersecao(dic):
    '''eh intersecao: universal → booleano
    eh intersecao(arg) devolve True caso o seu argumento seja um TAD intersecao
    e False caso contrário.'''

    if type(dic) != dict or len(dic) != 2 or not("col", "lis" in dic)\
        or type(obtem_col(dic)) != str or len(obtem_col(dic)) != 1 or not (64 < ord(obtem_col(dic)) < 85)\
            or type(obtem_lin(dic)) != int or  not (0 < obtem_lin(dic) < 20):
        return False
    return True

def intersecoes_iguais(dic1, dic2):
    '''intersecoes iguais: universal × universal → booleano
    intersecoes iguais(i1, i2) devolve True apenas se i1 e i2 são interseções e são
    iguais, e False caso contrário.'''

    if obtem_col(dic1) == obtem_col(dic2) and obtem_lin(dic1) == obtem_lin(dic2):
        return True
    return False

def intersecao_para_str(inter):
    '''intersecao para str : intersecao → str
    intersecao para str(i) devolve a cadeia de caracteres que representa o seu
    argumento.'''

    return str(obtem_col(inter)) + str(obtem_lin(inter))

def str_para_intersecao(string):
    '''str para intersecao: str → intersecao
    str para intersecao(s) devolve a interseção representada pelo seu argumento.'''

    if len(string) == 2:
        return cria_intersecao(str(string[0]), int(string[1]))
    if len(string) == 3:
        return cria_intersecao(str(string[0]), int(string[1:]))

def obtem_intersecoes_adjacentes(inter, canto):
    '''obtem intersecoes adjacentes: intersecao × intersecao → tuplo
    obtem intersecoes adjacentes(i, l) devolve um tuplo com as interseções adjacentes
    à interseção i de acordo com a ordem de leitura em que l corresponde à interseção
    superior direita do tabuleiro de Go.'''

    intersecoes = ()
    if obtem_lin(inter) != 1:
        intersecoes += ({"col": obtem_col(inter), "lin": obtem_lin(inter) - 1},)
    if obtem_col(inter) != "A":
        intersecoes += ({"col": chr(ord(obtem_col(inter)) - 1), "lin": obtem_lin(inter)},)
    if obtem_col(inter) != obtem_col(canto):
        intersecoes += ({"col": chr(ord(obtem_col(inter)) + 1), "lin": obtem_lin(inter)},)
    if obtem_lin(inter) != obtem_lin(canto):
        intersecoes += ({"col": obtem_col(inter), "lin": obtem_lin(inter) + 1},)
    
    return intersecoes

def ordena_intersecoes(tup):
    '''ordena intersecoes: tuplo → tuplo
    ordena intersecoes(t) devolve um tuplo de interseções com as mesmas interseções
    de t ordenadas de acordo com a ordem de leitura do tabuleiro de Go.'''

    a = 0
    lis = list(tup) #Torna o tuplo numa lista
    while a != 1:   #Verifica se houveram alterações no tuplo, se não for o caso termina o ciclo
        a = 1
        for i in range (len(lis) -1):  
            #Verifica se, para cada interseção, se a interseção seguinte 
            #tem linha de ordem menor, se for o caso, trocam de ordem no tuplo 
            if obtem_lin(lis[i]) > obtem_lin(lis[i+1]):
                    lis[i], lis[i+1] = lis[i+1], lis[i]
                    a=0
            elif obtem_lin(lis[i]) == obtem_lin(lis[i+1]):
                #Se tiverem a mesma linha verifica se a seguinte tem coluna de menor ordem,
                #se for o caso, trocam de ordem no tuplo
                if obtem_col(lis[i]) > obtem_col(lis[i+1]):
                    lis[i], lis[i+1] = lis[i+1], lis[i]
                    a=0
    tup = tuple(lis) #Torna a lista num tuplo
    return tup

#  PEDRA TAD - 2.1.2

def cria_pedra_branca():
    '''cria pedra branca: {} → pedra
    cria pedra branca() devolve uma pedra pertencente ao jogador branco.'''

    return "B"

def cria_pedra_preta():
    '''cria pedra preta: {} → pedra
    cria pedra preta() devolve uma pedra pertencente ao jogador preto.'''

    return "P"

def cria_pedra_neutra():
    '''cria pedra neutra: {} → pedra
    cria pedra neutra() devolve uma pedra neutra'''

    return "N"

def eh_pedra(p):
    '''eh pedra: universal → booleano
    eh pedra(arg) devolve True caso o seu argumento seja um TAD pedra e False
    caso contrário.'''

    if type(p) == str and p in ("B", "P", "N"):
        return True
    return False

def eh_pedra_branca(p):
    '''eh pedra branca: pedra → booleano
    eh pedra branca(p) devolve True caso a pedra p seja do jogador branco e False
    caso contrário'''

    if type(p) == str and p == "B":
        return True
    return False

def eh_pedra_preta(p):
    '''eh pedra: universal → booleano
    eh pedra preta(p) devolve True caso a pedra p seja do jogador preto e False
    caso contrário.'''

    if type(p) == str and p == "P":
        return True
    return False
    
def eh_pedra_neutra(p):
    '''pedras iguais: universal x universal → booleano
    pedras iguais(p1, p2) devolve True apenas se p1 e p2 são pedras e são iguais.'''

    if type(p) == str and p == "N":
        return True
    return False
    
def pedras_iguais(p1, p2):
    '''pedras iguais: universal x universal → booleano
    pedras iguais(p1, p2) devolve True apenas se p1 e p2 são pedras e são iguais.'''

    if (eh_pedra_branca(p1) and eh_pedra_branca(p2)) or (eh_pedra_preta(p1) and eh_pedra_preta(p2))\
          or (eh_pedra_neutra(p1) and eh_pedra_neutra(p2)):
        return True
    return False

def pedra_para_str(p):
    '''pedra para str : pedra → str
    pedra para str(p) devolve a cadeia de caracteres que representa o jogador dono
    da pedra, isto é, "O", "X" ou "." para pedras do jogador branco, preto ou neutra
    respetivamente.'''

    if eh_pedra_branca(p):
        return "O"
    if eh_pedra_preta(p):
        return "X"
    if eh_pedra_neutra(p):
        return "."
    
def eh_pedra_jogador(p):
    '''eh pedra jogador : pedra → booleano
    eh pedra jogador(p) devolve True caso a pedra p seja de um jogador e False caso
    contrário.'''

    if eh_pedra_preta(p) or eh_pedra_branca(p):
        return True
    return False


#TAD GOBAN

def cria_goban_vazio(n):
    '''cria goban vazio: int → goban
    cria goban vazio(n) devolve um goban de tamanho nxn, sem interseções ocupadas.
    Também verifica a validade dos argumentos dados'''

    if n is None or not (type(n) == int and n in (9, 13, 19)):
        raise ValueError("cria_goban_vazio: argumento invalido")
    return {"n": n, "B": (), "P": ()}

def cria_goban(n, B, P):
    '''cria goban: int x tuplo x tuplo → goban
    cria goban(n, ib, ip) devolve um goban de tamanho n x n, com as interseções
    do tuplo ib ocupadas por pedras brancas e as interseções do tuplo ip ocupadas
    por pedras pretas. Também verifica se os argumentos dados são válidos'''

    if not (type(B) == tuple and type(P) == tuple):
        raise ValueError("cria_goban: argumentos invalidos")
    geral = []
    for inter in B:
        if inter is None or not (len(inter) == 2 and "col" in inter  and "lin" in inter \
                and type(obtem_col(inter)) == str and len(obtem_col(inter)) == 1 \
                and type(obtem_lin(inter)) == int and chr(65) <= obtem_col(inter) <= chr(64+n) \
                and 0 < obtem_lin(inter) <= n) or inter in geral:
            raise ValueError("cria_goban: argumentos invalidos")
        else:
            geral += [inter,]
    for inter in P:
        if inter is None or not (len(inter) == 2 and "col" in inter and "lin" in inter \
                and type(obtem_col(inter)) == str and len(obtem_col(inter)) == 1 \
                and type(obtem_lin(inter)) == int and chr(65) <= obtem_col(inter) <= chr(64+n) \
                and 0 < obtem_lin(inter) <= n) or inter in geral:
            raise ValueError("cria_goban: argumentos invalidos")
        else:
            geral += [inter,]
    try:
        goban_vazio = cria_goban_vazio(n)
        goban_vazio.update({"B": B, "P": P})

    except ValueError:
        raise ValueError("cria_goban: argumentos invalidos")
    except AttributeError:
        raise ValueError("cria_goban: argumentos invalidos")
    except TypeError:
        raise ValueError("cria_goban: argumentos invalidos")
    
    return goban_vazio

def cria_copia_goban(gob):
    '''cria copia goban: goban → goban
    cria copia goban(t) recebe um goban e devolve uma cópia do goban.'''

    copia = {}
    if isinstance(gob, dict):
        for key, objeto in gob.items():
            copia[key] = cria_copia_goban(objeto)
    elif isinstance(gob, tuple):
        return tuple(cria_copia_goban(objeto) for objeto in gob)
    else:
        return gob
    return copia

def obtem_ultima_intersecao(gob):
    '''obtem ultima intersecao: goban → intersecao
    obtem ultima intersecao(g) devolve a interseção que corresponde ao 
    canto superior direito do goban g.'''

    return {"col": chr(gob["n"]+64), "lin": gob["n"]}

def obtem_pedra(gob, inter):
    '''obtem pedra: goban x intersecao → pedra
    obtem pedra(g, i) devolve a pedra na interseção i do goban g. Se a posição
    não estiver ocupada, devolve uma pedra neutra'''

    if inter in gob["B"]:
        return "B"
    if inter in gob["P"]:
        return "P"
    return "N"

def obtem_cadeia(gob, inter):
    '''obtem cadeia: goban x intersecao 7→ tuplo
    obtem cadeia(g, i) devolve o tuplo formado pelas interseções (em ordem de
    leitura) das pedras da cadeia que passa pela interseção i. Se a posição não
    estiver ocupada, devolve a cadeia de posições livres.'''

    cadeia = [inter,] 
    b = False
    p = False
    if inter in gob["B"]:
        b = True
    if inter in gob["P"]:
        p = True
    for dic in cadeia:
        dic_adj = obtem_intersecoes_adjacentes(dic, obtem_ultima_intersecao(gob))  
        #cria um tuplo para as interseções adjacentes
        for adj in dic_adj:
            if (((b and (adj in gob["B"])) or (p and adj in gob["P"]) or \
                 (not(adj in gob["B"]) and not(adj in gob["P"]) and not p and not b))\
                 and not adj in cadeia):
                    #Verifica se as interseções adjacentes são do mesmo tipo (livres ou ocupadas) que 
                    #a original e também se já estão contidas na lista
                    cadeia += [adj,] #Se for o caso são adicionadas à lista
                    #O ciclo repete-se para todos os elementos da lista
    return ordena_intersecoes(cadeia)

def coloca_pedra(gob, inter, p):
    '''coloca pedra: goban x intersecao x pedra → goban
    coloca pedra(g, i, p) modifica destrutivamente o goban g colocando a pedra
    do jogador p na interseção i, e devolve o próprio goban.'''

    if eh_pedra_jogador(p):
        if eh_pedra_branca(p):
            conj_inter = list(gob["B"])
            conj_inter.append(inter)
            gob.update({p: tuple(conj_inter)})
        if eh_pedra_preta(p):
            conj_inter = list(gob["P"])
            conj_inter.append(inter)
            gob.update({p: tuple(conj_inter)})
    return gob

def remove_pedra(gob, inter):
    '''remove pedra: goban x intersecao 7→ goban
    remove pedra(g, i) modifica destrutivamente o goban g removendo a pedra
    da interseção i, e devolve o próprio goban.'''

    if inter in gob["B"]:
        new_B = tuple(i for i in gob["B"] if i != inter)
        gob.update({"B": new_B})
    if inter in gob["P"]:
        new_P = tuple(i for i in gob["P"] if i != inter)
        gob.update({"P": new_P})
    return gob

def remove_cadeia(gob, cadeia):
    '''remove cadeia: goban x tuplo → goban
    remove cadeia(g, t) modifica destrutivamente o goban g removendo as pedras
    nas interseções to tuplo t, e devolve o próprio goban.'''

    for inter in cadeia:
        if inter in gob["B"]:
            novo_gob_B = tuple(i for i in gob["B"] if i != inter)
            gob.update({"B": novo_gob_B})
        if inter in gob["P"]:
            novo_gob_P = tuple(i for i in gob["P"] if i != inter)
            gob.update({"P": novo_gob_P})
    return gob

def eh_goban(gob):
    '''eh goban: universal → booleano
    eh goban(arg) devolve True caso o seu argumento seja um TAD goban e False
    caso contrário.'''
    try:
        if not (type(gob) == dict and len(gob) == 3 and "n", "B", "P" in gob\
                and gob["n"] in (9, 13, 19)):
            return False
        for inter in gob["B"]:
            if not eh_intersecao_valida(gob, inter):
                return False
        for inter in gob["P"]:
            if not eh_intersecao_valida(gob, inter):
                return False
        return True
    except AttributeError:
        return False
        
def eh_intersecao_valida(gob, inter):
    '''eh intersecao valida: goban x intersecao → booleano
    eh intersecao valida(g, i) devolve True se i é uma interseção válida dentro do
    goban g e False caso contrário.'''

    if not (eh_intersecao(inter) and 0 < ord(obtem_col(inter)) - 64 <= gob["n"] \
            and 0 < obtem_lin(inter) <= gob["n"]):
        return False
    return True

def gobans_iguais(gob1, gob2):
    '''gobans iguais: universal x universal → booleano
    gobans iguais(g1, g2) devolve True apenas se g1 e g2 forem gobans e forem iguais.'''

    if gob1["n"] == gob2["n"]:
        if ordena_intersecoes(gob1["B"]) == ordena_intersecoes(gob2["B"]) and \
            ordena_intersecoes(gob1["P"]) == ordena_intersecoes(gob2["P"]):
            return True
        
def goban_para_str(gob):
    '''goban para str : goban → str
    goban para str(g) devolve a cadeia de caracteres que representa o goban.'''

    string = " "
    mid = ""
    a = True
    b = int(obtem_lin(obtem_ultima_intersecao(gob)))
    n = 0
    while not obtem_col(obtem_ultima_intersecao(gob)) in string: #Adiciona as letras
        string += " " + chr(a + 64)
        a += 1
    while b != 0:  #Adiciona o número da linha correspondente no início de cada linha da string
        if b >= 10:
            mid += "\n" + str(b)
        else:
            mid += "\n " + str(b)
        while n != gob["n"]:
             #Adiciona um "." de a interseção correspondente for livre e um "X" caso contrário
            for inter in gob["B"]:
                if intersecoes_iguais(cria_intersecao(str(chr(n+65)), b), inter):
                    mid += " O"
                    a = False
            if a:
                for inter in gob["P"]:
                    if intersecoes_iguais(cria_intersecao(str(chr(n+65)), int(b)), inter):
                        mid += " X"
                        a = False
            if a:
                mid += " ."
            a = True
            n += 1
        if b > 9:   #Adiciona o número da linha correspondente no fim de cada linha da string
            mid += " " + str(b)
        else:
            mid += "  " + str(b)
        b -= 1
        n = 0
    
    return " " + string + mid + "\n " + string

def obtem_territorios(gob):
    '''obtem territorios: goban 7→ tuplo
    obtem territorios(g) devolve o tuplo formado pelos tuplos com as interseções de
    cada território de g. A função devolve as interseções de cada território ordenadas
    em ordem de leitura do tabuleiro de Go, e os territórios ordenados em ordem de
    leitura da primeira interseção do território.'''

    geral = []
    territorios = []
    def aux(geral, territorios, inter):
        if inter not in geral:
            tup = []
            for inter1 in obtem_cadeia(gob, inter):
                tup.append(inter1)
                geral += [inter1,]
            territorios += [tuple(tup),]

    for inter in gob["B"]:
        aux(geral, territorios, inter)
    for inter in gob["P"]:
        aux(geral, territorios, inter)
    for n in range(gob["n"]-1):
        aux(geral, territorios, cria_intersecao(chr(65+n), n+1))
    for tup in territorios:
        ordena_intersecoes(tup)
    return tuple(sorted(territorios, key=lambda x: obtem_lin(x[0])*10000+ord(obtem_col(x[0]))))

def obtem_adjacentes_diferentes(gob, tup):
    '''obtem adjacentes diferentes: goban x tuplo → tuplo
    obtem adjacentes diferentes(g, t) devolve o tuplo ordenado formado pelas interseções
    adjacentes às interseções do tuplo t correspondente às liberdades de uma cadeia de pedras,
    enquanto que o segundo corresponde à fronteira de um território'''

    interes = []
    if eh_pedra_branca(obtem_pedra(gob, tup[0])):
        for inter in tup:
            for inter1 in obtem_intersecoes_adjacentes(inter, obtem_ultima_intersecao(gob)):
                if not inter1 in interes and not inter1 in tup and not eh_pedra_preta(obtem_pedra(gob, inter1)):
                    interes += [inter1]
    elif eh_pedra_preta(obtem_pedra(gob, tup[0])):
        for inter in tup:
            for inter1 in obtem_intersecoes_adjacentes(inter, obtem_ultima_intersecao(gob)):
                if not inter1 in interes and not inter1 in tup and not eh_pedra_branca(obtem_pedra(gob, inter1)):
                    interes += [inter1]
    else:
        for inter in tup:
            for inter1 in obtem_intersecoes_adjacentes(inter, obtem_ultima_intersecao(gob)):
                if not inter1 in interes and not inter1 in tup:
                    interes += [inter1]
    return tuple(ordena_intersecoes(interes))

def jogada(gob, inter, p):
    '''jogada: goban x intersecao x pedra → goban
    jogada(g, i, p) modifica destrutivamente o goban g colocando a pedra de jogador
    p na interseção i e remove todas as pedras do jogador contrário pertencentes a
    cadeias adjacentes à i sem liberdades, devolvendo o próprio goban'''

    if not eh_pedra_branca(obtem_pedra(gob, inter)) and not eh_pedra_preta(obtem_pedra(gob, inter)):
        coloca_pedra(gob, inter, p)
    if eh_pedra_branca(p):
        for adj in obtem_intersecoes_adjacentes(inter, obtem_ultima_intersecao(gob)):
            if eh_pedra_preta(obtem_pedra(gob, adj)) and obtem_adjacentes_diferentes(gob, obtem_cadeia(gob, adj)) == ():
                remove_cadeia(gob, obtem_cadeia(gob, adj))
    if eh_pedra_preta(p):
        for adj in obtem_intersecoes_adjacentes(inter, obtem_ultima_intersecao(gob)):
            if eh_pedra_branca(obtem_pedra(gob, adj)) and obtem_adjacentes_diferentes(gob, obtem_cadeia(gob, adj)) == ():
                remove_cadeia(gob, obtem_cadeia(gob, adj))
    return gob

def obtem_pedras_jogadores(gob):
    '''obtem pedras jogadores: goban 7→ tuplo
    obtem pedras jogadores(g) devolve um tuplo de dois inteiros que correspondem ao
    número de interseções ocupadas por pedras do jogador branco e preto, respetivamente.'''

    return (len(gob["B"]), len(gob["P"]))

#Funções adicionais

def calcula_pontos(gob):  #2.2.1
    '''calcula pontos: goban → tuple
    calcula pontos(g) é uma função auxiliar que recebe um goban e devolve o tuplo de dois
    inteiros com as pontuações dos jogadores branco e preto, respetivamente.'''

    count_b = len(gob["B"])
    count_p = len(gob["P"])
    if count_b == 0 and count_p == 0:
        return (count_b, count_p)
    for interes in obtem_territorios(gob):
        if not eh_pedra_branca(obtem_pedra(gob, interes[0])) and not eh_pedra_preta(obtem_pedra(gob, interes[0])):
            if all(eh_pedra_branca(obtem_pedra(gob, inter)) for inter in obtem_adjacentes_diferentes(gob, interes)):
                count_b += len(interes)
            if all(eh_pedra_preta(obtem_pedra(gob, inter)) for inter in obtem_adjacentes_diferentes(gob, interes)):
                count_p += len(interes)
    return (count_b, count_p)

def eh_jogada_legal(gob, inter, p, copgob):
    '''eh jogada legal: goban x intersecao x pedra x goban 7→ booleano 
    eh jogada legal(g, i, p, l) é uma função auxiliar que recebe um goban g, uma interseção
    i, uma pedra de jogador p e um outro goban l e devolve True se a jogada for legal ou
    False caso contrário, sem modificar g ou l. Para a deteção de repetição, considere que l
    representa o estado de tabuleiro que não pode ser obtido após a resolução completa da
    jogada.'''

    g_copia = cria_copia_goban(gob)
    if eh_goban(gob) and eh_intersecao_valida(gob, inter) and not eh_pedra_preta(obtem_pedra(gob, inter)) and not eh_pedra_branca(obtem_pedra(gob, inter)):
        if obtem_adjacentes_diferentes(jogada(g_copia, inter, p), obtem_cadeia(jogada(g_copia, inter, p), inter)) == ():
            return False
        if jogada(g_copia, inter, p) != copgob:
            return True
    return False
        
def turno_jogador(gob, p, copgob):
    '''turno jogador: goban x pedra x goban → booleano
    turno jogador(g, p, l) é uma função auxiliar que recebe um goban g, uma pedra de
    jogador p e um outro goban l, e oferece ao jogador que joga com pedras p a opção de
    passar ou de colocar uma pedra própria numa interseção. Se o jogador passar, a função
    devolve False sem modificar os argumentos. Caso contrário, a função devolve True e
    modifica destrutivamente o tabuleiro g de acordo com a jogada realizada.'''

    arg = ""
    while arg == "":
        if eh_pedra_branca(p):
            arg = str(input("Escreva uma intersecao ou 'P' para passar [O]:"))
        else:
            arg = str(input("Escreva uma intersecao ou 'P' para passar [X]:"))
    while not eh_jogada_legal(gob, str_para_intersecao(arg), p, copgob):
        if arg == "P":
            return False
        if eh_pedra_branca(p):
            arg = str(input("Escreva uma intersecao ou 'P' para passar [O]:"))
        else:
            arg = str(input("Escreva uma intersecao ou 'P' para passar [X]:"))
    try:
        gob = jogada(gob, str_para_intersecao(arg), p)
        return True
    except ValueError:
        turno_jogador(gob, p, copgob)
    

def go(n, ib, ip):
    '''go: int x tuple x tuple 7→ booleano (1,5 valores)
    go(n, tb, tn) é a função principal que permite jogar um jogo completo do Go de dois
    jogadores. A função recebe um inteiro correspondente `a dimensão do tabuleiro, e dois
    tuplos (potencialmente vazios) com a representação externa das interseções ocupadas
    por pedras brancas (tb) e pretas (tp) inicialmente. O jogo termina quando os dois
    jogadores passam a vez de jogar consecutivamente. A função devolve True se o jogador
    com pedras brancas conseguir ganhar o jogo, ou False caso contrário. A função deve
    verificar a validade dos seus argumentos, gerando um ValueError com a mensagem
    'go: argumentos invalidos' caso os seus argumentos não sejam válidos.'''

    passcount = 0
    if not(isinstance(ib, tuple) and isinstance(ip, tuple) and isinstance(n, int) and n in (9, 13, 19)):
        raise ValueError("go: argumentos invalidos")
    if len(ib) > 0 or len(ip) > 0:
        try:
            for i in ib:
                if type(i) != str:
                    raise ValueError("go: argumentos invalidos")
            for i in ip:
                if type(i) != str:
                    raise ValueError("go: argumentos invalidos")
            ib = tuple(str_para_intersecao(i) for i in ib)
            ip = tuple(str_para_intersecao(i) for i in ip)
            gob = cria_goban(n, ib, ip)
        except ValueError or TypeError:
            raise ValueError("go: argumentos invalidos")
    else:
        gob = cria_goban_vazio(n)
    b = cria_pedra_preta()
    while passcount < 2:
        print ("Branco (O) tem", calcula_pontos(gob)[0], "pontos\nPreto (X) tem", calcula_pontos(gob)[1], "pontos") 
        print(goban_para_str(gob))
        a = turno_jogador(gob, b, cria_copia_goban(gob))
        if not a:
            passcount += 1
        else:
            passcount = 0
        if passcount < 2:
            b = cria_pedra_branca()
            print ("Branco (O) tem", calcula_pontos(gob)[0], "pontos\nPreto (X) tem", calcula_pontos(gob)[1], "pontos") 
            print(goban_para_str(gob))
            a = turno_jogador(gob, b, cria_copia_goban(gob))
            if not a:
                passcount += 1
            else:
                passcount = 0
            b = cria_pedra_preta()
    print ("Branco (O) tem", calcula_pontos(gob)[0], "pontos\nPreto (X) tem", calcula_pontos(gob)[1], "pontos") 
    print(goban_para_str(gob))
    if calcula_pontos(gob)[0] > calcula_pontos(gob)[1]:
        return True
    return False

