""" Módulo para treinar com a biblioteca OS"""


import os, os.path


def listando_arquivos():
    global path_escolhido, lista_geral, so_arquivos, so_dir
    path_escolhido = str(input('??? preencha com o caminho do diretório escolhido >>  '))

    lista_geral = os.listdir(path_escolhido)

    #descobrindo o que são arquivos e o que são diretórios
    so_arquivos = [i.name for i in os.scandir(path_escolhido) if i.is_file()]
    so_dir = [i.name for i in os.scandir(path_escolhido) if i.is_dir()]

    print(f'Seu diretório escolhido tem {len(lista_geral)} arquivos, sendo {len(so_arquivos)} arquivos e {len(so_dir)} diretórios')

    #posicionando o script no diretorio escolhido para futura interação
    os.chdir(path_escolhido)
    print("________" * 10)

def relacionar_arquivos():
    while True:
        resposta = input('??? Você gostaria de listar seus arquivos e diretórios? (Y/N)').upper()
        if resposta not in ('Y', 'N'):
            print('>>> Você precisa escolher uma das opções possíveis (Y/N)')
        elif resposta == 'Y':
            for i in lista_geral:
                print(i)
            break
        else:
            break

def finding_extentions():
    global lista_extensoes
    lista_extensoes = []
    for i in so_arquivos:
        ext = i.split('.')[-1].lower()
        if ext not in lista_extensoes:
        #lista_extencoes.append(i.split('.')[-1])
            lista_extensoes.append(ext)
    print(f'>>>você tem arquivos em {len(lista_extensoes)} extenções diferentes')
    print(f'>>>sendo elas {lista_extensoes}')
    print("________" * 10)


def deseja_organizar_arquivos():
    while True:
        resposta = input('??? Você gostaria de ORGANIZAR seus arquivos em diretórios por extenção? (Y/N)').upper()
        if resposta not in ('Y', 'N'):
            print('>>> Você precisa escolher uma das opções possíveis (Y/N)')
        elif resposta == 'Y':
            dir_atual = os.getcwd()  #<class 'str'>
            for i in lista_extensoes: #criando 1 pasta para cada tipo de extencao
                nova_dir = dir_atual + "/" + i
                os.mkdir(nova_dir)
            for i in so_arquivos: #movendo os arquivos para as novas pastas
                atual = os.getcwd() + "/" + i
                destino = os.getcwd() + "/" + i.split('.')[-1] + "/" + i
                os.rename(atual, destino)
            print(f'>>> Seus arquivos foram ORGANIZADOS!!')
            break
        else:
            break


if __name__ == "__main__":
    listando_arquivos()
    relacionar_arquivos()
    finding_extentions()
    deseja_organizar_arquivos()

    #print(f'seu local atual é {os.getcwd()}')
    #print(f'o diretório escolhido é {path_escolhido}')


# c:/users/dan_g/teste_desktop