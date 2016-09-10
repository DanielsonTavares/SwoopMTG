import urllib.request
from bs4 import BeautifulSoup
import os
from SwoopLib import *
import sys

# idioma das imagens e dos textos
cod_idioma = 'en'

# Sigla da edição
#cod_edicao_list = ['emn', 'soi', 'ogw', 'bfz', 'dtk', 'frf', 'ktk', 'ori', 'm15', 'ths', 'jou', 'bng']
cod_edicao_list = ['ULG', 'ARN', 'FUT', 'pMGD', 'WTH', 'UGL', 'RAV', 'DD3_EVG', 'JOU', 'M11', 'ALL', 'WWK', 'MOR', 'pGRU', 'DKA', 'DD3_DVD', 'CNS', 'THS', 'pCMP', 'DGM', 'MD1', 'pWCQ', 'ZEN', 'VIS', 'TSP', 'CHK', 'V10', 'V14', 'CON', 'pMPR', 'S00', 'MMQ', 'TSB', 'pGPX', 'VAN', 'DDF', 'BTD', 'OGW', 'V09', 'C13', 'DDE', 'ODY', 'HML', 'MM2', '5ED', 'RTR', 'pPOD', 'TMP', 'ISD', 'ATH', 'p2HG', 'ICE', 'EMA', 'NPH', 'VMA', 'W16', 'CN2', '9ED', 'FRF', 'DD3_JVC', 'SOI', 'C15', 'DDH', 'C14', 'ROE', 'STH', 'DDD', 'ONS', 'pPRO', 'CPK', 'BNG', 'GPT', 'M14', 'DDP', 'ATQ', 'pELP', 'FRF_UGIN', 'DST', 'MBS', 'DRB', 'JUD', 'PLC', 'DDI', 'DDJ', 'ITP', 'pHHO', 'pSUM', 'INV', 'DD2', 'pFNM', 'PO2', 'pLPA', 'SCG', 'M15', 'DD3_GVL', 'DRK', 'DDM', '10E', 'UDS', 'MMA', 'DDG', 'LEA', 'PLS', 'ME2', 'pGTW', 'BFZ', 'EVG', 'LEB', 'SOM', 'ORI', 'ME3', 'HOP', 'MIR', 'pDRC', 'CHR', 'DDK', 'p15A', 'TOR', 'pWOR', 'DDO', 'ARC', 'pWOS', 'EXO', 'CMD', 'EMN', 'M12', 'pPRE', 'FEM', 'pREL', '6ED', 'MRD', '7ED', 'LEG', 'M13', 'SHM', 'DDN', 'DKM', 'V12', 'UNH', 'PCY', 'V11', 'pJGP', 'DDQ', '8ED', '4ED', 'AVR', 'KTK', 'LRW', 'V13', 'SOK', 'pALP', 'DTK', 'ARB', 'TPR', 'RQS', '5DN', 'POR', 'DDL', 'APC', 'M10', 'ME4', 'V15', 'PD3', 'BRB', 'CEI', 'CED', 'EXP', 'V16', 'CST', 'pARL', 'DDC', 'pCEL', '2ED', 'pMEI', 'DIS', 'S99', 'H09', 'BOK', 'ALA', 'CSP', 'LGN', 'pSUS', 'MGB', 'pLGM', 'USG', 'DPA', 'MED', 'EVE', 'GTC', 'CM1', 'NMS', 'PC2', 'PD2', 'PTK', 'pWPN', '3ED']

# flag para indicar se as imagens serão salvas ou não. S-Sim; N-Não
fl_salva_img = 'N'

# flag para indicar se os dados das cartas serão salvos. S-Sim; N-Não
fl_salva_txt = 'S'

for cod_edicao in cod_edicao_list:
    try:
        # diretório para salvar as informacoes - imagens
        dir_imagem = 'dados/imagens/' + cod_edicao + '/' + cod_idioma

        # diretório para salvar as informacoes - textos em sql
        dir_export = 'dados/export/'

        if fl_salva_img == 'S':
            if not os.path.exists(dir_imagem):
                os.makedirs(dir_imagem)

        if fl_salva_txt == 'S':
            if not os.path.exists(dir_export):
                os.makedirs(dir_export)
            arquivo_txt = open(dir_export+'/' + cod_edicao + '_' + cod_idioma + '.sql', 'wb')

            table_name = 'cartas'

        url = 'http://magiccards.info/query?q=%2B%2Be%3A'+cod_edicao+'%2F'+cod_idioma+'&v=spoiler&s=issue'

        # acessando o link
        htmlfile = urllib.request.urlopen(url)
        # definindo a codificação do site
        htmltext = htmlfile.read().decode('utf-8')
        # parseando o html do site
        soup = BeautifulSoup(htmltext, 'html.parser')


        table_list = soup.find_all('table')

        td_list = table_list[3].find_all('td')

        k = 0

        while k < len(td_list):
            dados_carta = td_list[k].find_all('p')
            link_carta = td_list[k].find_all('a')
            url_home = 'http://magiccards.info'

            if link_carta != []:
                link = link_carta[0].get('href')
                arq_link = os.path.split(link)
                id_card = arq_link[1].replace('.html','')

                '''
                print('**************',k)
                print('Edição', cod_edicao.upper())
                print('Nome: '+link_carta[0].text, url_home+link)
                print('Tipo: '+dados_carta[1].text.replace('\n            ',''))
                print('Descrição: '+dados_carta[2].text)
                print('Flavor: '+dados_carta[3].text)
                print('Artista: '+dados_carta[4].text)
                '''

                caminho_img = 'http://magiccards.info/scans/'+cod_idioma+'/'+cod_edicao+'/'+id_card+'.jpg'
                #print('Imgagem: ' + caminho_img)

                if fl_salva_img == 'S':
                    figura = urllib.request.urlopen(caminho_img).read()
                    arquivo = open(dir + '/' + link_carta[0].text + '.jpg', 'wb')
                    arquivo.write(figura)
                    arquivo.close()

                if fl_salva_txt == 'S':

                    #Tratando o tipo, sub-tipo, poder/resistencia e custo
                    dict_dados = Busca_dados(dados_carta[1].text.replace('\n            ',' ').replace('\'','´'))

                    tipo = dict_dados['tipo']
                    sub_tipo = dict_dados['sub_tipo']
                    poder_resistencia = dict_dados['poder_resistencia']
                    custo_mana = dict_dados['custo_mana']
                    custo_convertido = dict_dados['custo_convertido']

                    # Dictionary com os campos da tabela
                    export_cartas = {'edicao': cod_edicao.upper(),
                                     'nome': link_carta[0].text.replace('\'','´'),
                                     #'tipo': dados_carta[1].text.replace('\n            ','').replace('\'','´'),
                                     'tipo': tipo,
                                     'sub_tipo': sub_tipo,
                                     'poder': poder_resistencia[0],
                                     'resistencia': poder_resistencia[2],
                                     'custo_mana': custo_mana,
                                     'custo_convertido': custo_convertido,
                                     'descricao': dados_carta[2].text.replace('\'','´'),
                                     'flavor': dados_carta[3].text.replace('\'','´'),
                                     'artista': dados_carta[4].text.replace('\'','´'),
                                     'imagem': caminho_img
                    }

                    keys = str(export_cartas.keys())[9:].replace('[', '').replace(']', '')
                    vals = str(export_cartas.values())[11:].replace('[', '').replace(']', '')

                    insert = 'Insert Into ' + table_name + keys + ' values' + vals

                    arquivo_txt.write(insert.encode('utf-8')+'\n'.encode('utf-8'))
                    #print('Insert Into Table ' + keys + ' values' + vals)

            k += 1

        if fl_salva_txt == 'S':
            arquivo_txt.close()

        print(cod_edicao + '/' + cod_idioma + ': [OK]')
    except:
        print(cod_edicao + '/' + cod_idioma + ': [ERRO]')

input('Pressione qualquer tecla para encerrar...')