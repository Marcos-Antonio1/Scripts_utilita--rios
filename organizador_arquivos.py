# -*- coding: utf-8 -*- 
import shutil
import os 
import platform
import glob
def main(): 
    print ("Organizador de arquivos")
    print ("1- Para organizar o diretório onde está o script ")
    print ("0- ou Qualquer outra tecla para passar o diretório ")
    opcao=int(input())
    if opcao==1:
        arquivos=listarArquivos()
        pastas_para_serem_criadas=verificarDiretorioAseremCriados(arquivos)
        if (platform.system()=="Linux"):
            local=os.getcwd()+'/'
        else:
            local=os.getcwd()+'\\'
        preparacaoCriarPasta(pastas_para_serem_criadas,local)
        SeparandoArquivos(arquivos,local)
    else:
        diretorio=input("informe o diretório completo: ")
        arquivos=listarArquivos(diretorio)
        pastas_para_serem_criadas=verificarDiretorioAseremCriados(arquivos)
        preparacaoCriarPasta(pastas_para_serem_criadas,diretorio)
        SeparandoArquivos(arquivos,diretorio)
    
def listarArquivos(diretorio=''):
    newdiretorio=[]
    if diretorio=='':
        diretorio =glob.glob('*')
        for i in diretorio:
            if os.path.isfile(i):
                newdiretorio.append(i)
        return newdiretorio
    else:
        diretorio= glob.glob(diretorio+ '*')
        for i in diretorio:
            if os.path.isfile(i):
                newdiretorio.append(i)
        return newdiretorio

def criardiretorio(caminho):
        os.mkdir(caminho)

def verificarDiretorioAseremCriados(listarArquivos):
    diretorios=[]
    for i in listarArquivos:
        if os.path.isfile(i):
            dire=i.rpartition('.')
            if not diretorios.count(dire[2]):
                diretorios.append(dire[2])
    return diretorios

def preparacaoCriarPasta(diretorios,diretorio):        
    if len(diretorios)>0:
        for i in diretorios:
                if not os.path.isdir(diretorio+"Arquivos"+i):
                    criardiretorio(diretorio+"Arquivos"+i)

def SeparandoArquivos(arquivos,diretorio):
    if len(arquivos)>0:    
        for i in arquivos:
            arq=i.rpartition('.')
            destino=diretorio+"Arquivos"+arq[2]
            moverArquivo(i,destino)
                    
def moverArquivo(origem,destino):
    shutil.move(origem,destino)

main()