# This is the Python script for your project
# INTERSEÇÃO TAD - 2.1.1

def cria_intersecao(col, lin):
    try:
        int(str(lin))
        str(col)
        if type(col) != str or len(col) != 1 or (not (64 < ord(col) < 84))\
         or type(lin) != int or (not (0 < int(lin) < 20)):
            raise ValueError("cria_intersecao: argumentos invalidos")
        return {"col": col, "lin": lin}
    except ValueError:
        raise ValueError("cria_intersecao: argumentos invalidos")

def obtem_col(inter):
    return inter["col"]

def obtem_lin(inter):
    return inter["lin"]

def eh_intersecao(dic):
    if type(dic) != dict or len(dic) != 2 or not("col", "lis" in dic.keys())\
        or type(obtem_col(dic)) != str or len(obtem_col(dic)) != 1 or not (64 < ord(obtem_col(dic)) < 85)\
            or type(obtem_lin(dic)) != int or  not (0 < obtem_lin(dic) < 20):
        return False
    return True

def intersecoes_iguais(dic1, dic2):
    if obtem_col(dic1) == obtem_col(dic2) and obtem_lin(dic1) == obtem_lin(dic2):
        return True
    return False

def intersecao_para_str(inter):
    return str(obtem_col(inter)) + str(obtem_lin(inter))

def str_para_intersecao(string):
    if len(string) == 2:
        return cria_intersecao(str(string[0]), int(string[1]))
    if len(string) == 3:
        return cria_intersecao(str(string[0]), int(string[1:]))

def obtem_intersecoes_adjacentes(inter, canto):
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
    return "B"

def cria_pedra_preta():
    return "P"

def cria_pedra_neutra():
    return "N"

def eh_pedra(p):
    if type(p) == str and p in ("B", "P", "N"):
        return True
    return False

def eh_pedra_branca(p):
    if type(p) == str and p == "B":
        return True
    return False

def eh_pedra_preta(p):
    if type(p) == str and p == "P":
        return True
    return False
    
def eh_pedra_neutra(p):
    if type(p) == str and p == "N":
        return True
    return False
    
def pedras_iguais(p1, p2):
    if (eh_pedra_branca(p1) and eh_pedra_branca(p2)) or (eh_pedra_preta(p1) and eh_pedra_preta(p2))\
          or (eh_pedra_neutra(p1) and eh_pedra_neutra(p2)):
        return True
    return False

def pedra_para_str(p):
    if eh_pedra_branca(p):
        return "O"
    if eh_pedra_preta(p):
        return "X"
    if eh_pedra_neutra(p):
        return "."
    
def eh_pedra_jogador(p):
    if eh_pedra_preta(p) or eh_pedra_branca(p):
        return True
    return False


#TAD GOBAN

def cria_goban_vazio(n):
    if n is None or not (type(n) == int and n in (9, 13, 19)):
        raise ValueError("cria_goban_vazio: argumento invalido")
    return {"n": n, "B": (), "P": ()}

def cria_goban(n, B, P):
    if not (type(B) == tuple and type(P) == tuple):
        raise ValueError("cria_goban_vazio: argumento invalido")
    geral = []
    for inter in B:
        if inter is None or not (len(inter) == 2 and "col" in inter  and "lin" in inter \
                and type(obtem_col(inter)) == str and len(obtem_col(inter)) == 1 and type(obtem_lin(inter)) == int\
                and chr(65) <= obtem_col(inter) <= chr(64+n) and 0 < obtem_lin(inter) <= n) or inter in geral:
            raise ValueError("cria_goban: argumentos invalidos")
        else:
            geral += [inter,]
    for inter in P:
        if inter is None or not (len(inter) == 2 and "col" in inter and "lin" in inter \
                and type(obtem_col(inter)) == str and len(obtem_col(inter)) == 1 and type(obtem_lin(inter)) == int\
                and chr(65) <= obtem_col(inter) <= chr(64+n) and 0 < obtem_lin(inter) <= n) or inter in geral:
            raise ValueError("cria_goban: argumentos invalidos")
        else:
            geral += [inter,]
    try:
        goban_vazio = cria_goban_vazio(n)
        goban_vazio.update({"B": B, "P": P})
    except ValueError:
        raise ValueError("cria_goban: argumentos invalidos")
    return goban_vazio

def cria_copia_goban(gob):
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
    return {"col": chr(gob["n"]+64), "lin": gob["n"]}

def obtem_pedra(gob, inter):
    if inter in gob["B"]:
        return "B"
    if inter in gob["P"]:
        return "P"
    return "N"

def obtem_cadeia(gob, inter):
    cadeia = [inter,] 
    b = False
    p = False
    if inter in gob["B"]:
        b = True
    if inter in gob["P"]:
        p = True
    for dic in cadeia:
        dic_adj = obtem_intersecoes_adjacentes(dic, obtem_ultima_intersecao(gob))  #cria um tuplo para as interseções adjacentes
        for adj in dic_adj:
            if (((b and (adj in gob["B"])) or (p and adj in gob["P"]) or (not(adj in gob["B"]) and not(adj in gob["P"]) and not p and not b))\
                 and not adj in cadeia):
                    #Verifica se as interseções adjacentes são do mesmo tipo (livres ou ocupadas) que 
                    #a original e também se já estão contidas na lista
                    cadeia += [adj,] #Se for o caso são adicionadas à lista
                    #O ciclo repete-se para todos os elementos da lista
    return ordena_intersecoes(cadeia)

def coloca_pedra(gob, inter, p):
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

def remove_pedra(gob, inter): #nao sei se funciona
    if inter in gob["B"]:
        new_B = tuple(i for i in gob["B"] if i != inter)
        gob.update({"B": new_B})
    if inter in gob["P"]:
        new_P = tuple(i for i in gob["P"] if i != inter)
        gob.update({"P": new_P})
    return gob

def remove_cadeia(gob, cadeia): #nao sei se funciona
    for inter in cadeia:
        if inter in gob["B"]:
            novo_gob_B = tuple(i for i in gob["B"] if i != inter)
            gob.update({"B": novo_gob_B})
        if inter in gob["P"]:
            novo_gob_P = tuple(i for i in gob["P"] if i != inter)
            gob.update({"P": novo_gob_P})
    return gob

def eh_goban(gob):
    if not (type(gob) == dict and len(gob) == 3 and "n", "B", "P" in gob.keys() and gob["n"] in (9, 13, 19)):
        return False
    for inter in gob["B"]:
        if not eh_intersecao_valida(gob, inter):
            return False
    for inter in gob["P"]:
        if not eh_intersecao_valida(gob, inter):
            return False
    return True
        
def eh_intersecao_valida(gob, inter):
    if not (eh_intersecao(inter) and 0 < ord(obtem_col(inter)) - 64 <= gob["n"] and 0 < obtem_lin(inter) <= gob["n"]):
        return False
    return True

def gobans_iguais(gob1, gob2):
    if gob1["n"] == gob2["n"]:
        if ordena_intersecoes(gob1["B"]) == ordena_intersecoes(gob2["B"]) and \
            ordena_intersecoes(gob1["P"]) == ordena_intersecoes(gob2["P"]):
            return True
        
def goban_para_str(gob):
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
    interes = []
    if tup[0] in gob["B"]:
        for inter in tup:
            for inter1 in obtem_intersecoes_adjacentes(inter, obtem_ultima_intersecao(gob)):
                if not inter1 in interes and not inter1 in tup and not inter1 in gob["P"]:
                    interes += [inter1]
    elif tup[0] in gob["P"]:
        for inter in tup:
            for inter1 in obtem_intersecoes_adjacentes(inter, obtem_ultima_intersecao(gob)):
                if not inter1 in interes and not inter1 in tup and not inter1 in gob["B"]:
                    interes += [inter1]
    else:
        for inter in tup:
            for inter1 in obtem_intersecoes_adjacentes(inter, obtem_ultima_intersecao(gob)):
                if not inter1 in interes and not inter1 in tup:
                    interes += [inter1]
    return tuple(ordena_intersecoes(interes))

def jogada(gob, inter, p):
    if not inter in gob["P"] and not inter in gob["B"]:
        coloca_pedra(gob, inter, p)
    if p == "B":
        for adj in obtem_intersecoes_adjacentes(inter, obtem_ultima_intersecao(gob)):
            if adj in gob["P"] and obtem_adjacentes_diferentes(gob, obtem_cadeia(gob, adj)) == ():
                remove_cadeia(gob, obtem_cadeia(gob, adj))
    if p == "P":
        for adj in obtem_intersecoes_adjacentes(inter, obtem_ultima_intersecao(gob)):
            if adj in gob["B"] and obtem_adjacentes_diferentes(gob, obtem_cadeia(gob, adj)) == ():
                remove_cadeia(gob, obtem_cadeia(gob, adj))
    return gob

def obtem_pedras_jogadores(gob):
    return (len(gob["B"]), len(gob["P"]))

#Funções adicionais

def calcula_pontos(gob):  #2.2.1
    count_b = len(gob["B"])
    count_p = len(gob["P"])
    if count_b == 0 and count_p == 0:
        return (count_b, count_p)
    for interes in obtem_territorios(gob):
        if not interes[0] in gob["B"] and not interes[0] in gob["P"]:
            if all(inter in gob["B"] for inter in obtem_adjacentes_diferentes(gob, interes)):
                count_b += len(interes)
            if all(inter in gob["P"] for inter in obtem_adjacentes_diferentes(gob, interes)):
                count_p += len(interes)
    return (count_b, count_p)

def eh_jogada_legal(gob, inter, p, copgob):
    g_copia = cria_copia_goban(gob)
    if eh_goban(gob) and eh_intersecao_valida(gob, inter) and not inter in gob["P"] and not inter in gob["B"]:
        if obtem_adjacentes_diferentes(jogada(g_copia, inter, p), obtem_cadeia(jogada(g_copia, inter, p), inter)) == ():
            return False
        if jogada(g_copia, inter, p) != copgob:
            return True
    return False
        
def turno_jogador(gob, p, copgob):
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
    gob = jogada(gob, str_para_intersecao(arg), p)
    return True

def go(n, ib, ip):
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

