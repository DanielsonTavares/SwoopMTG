def Busca_dados(texto):

    sep_traco = texto.find('—')
    sep_virgula = texto.find(',')
    sep_parentese = texto.find('(')

    # fl_pr: Se houver poder e resistencia, fl_pr será > -1
    fl_pr = texto[0:].find('/')

    # fl_cm: Se houver custo de mana, fl_cm será > -1
    fl_cm = texto.find('(')

    # verificando se possui poder/resistencia
    if fl_pr > -1:
        sep_virgulaaux = sep_virgula - 4
    else:
        sep_virgulaaux = sep_virgula

    # verificando se tem o separador '—' (Separador de tipo e sub-tipo)
    if sep_traco > -1:
        tipo = texto[0:texto.find('—')].strip()
        sep_traco = sep_traco + 2
        sub_tipo = texto[sep_traco:sep_virgulaaux]
    else:
        sep_traco = 0
        tipo = texto[sep_traco:sep_virgulaaux]
        sub_tipo = ''


    if fl_pr > -1:
        poder_resistencia = texto[sep_virgula-3:sep_virgula]
    else:
        poder_resistencia = '   '

    if fl_cm > -1:
        custo_mana = texto[sep_virgula:sep_parentese].strip().replace(', ','')
        custo_convertido = texto[sep_parentese+1:].replace(')','')
    else:
        custo_mana = ' '
        custo_convertido = ' '

    dict = {
        'tipo': tipo,
        'sub_tipo': sub_tipo,
        'poder_resistencia': poder_resistencia,
        'custo_mana': custo_mana,
        'custo_convertido':custo_convertido
    }


    return dict