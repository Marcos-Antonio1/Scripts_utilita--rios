# -*- coding: utf-8 -*- 
import shutil
import os 
import glob # listar arquivos

def main():
    print ("Organizador de arquivos")
    print ("1- Para organizar o diretório onde está o script ")
    print ("0- ou Qualquer outra tecla para passar o diretório ")
    opcao=int(input())
    if opcao==1:
        arquivos=listarArquivos()
        pastas_para_serem_criadas=verificarDiretorioAseremCriados(arquivos)
        local=os.getcwd()+'/'
        preparacaoCriarPasta(pastas_para_serem_criadas,local)
        SeparandoArquivos(arquivos,local)
    else:
        diretorio=input("informe o diretório completo: ")
        arquivos=listarArquivos(diretorio)
        pastas_para_serem_criadas=verificarDiretorioAseremCriados(arquivos)
        preparacaoCriarPasta(pastas_para_serem_criadas,diretorio)
        SeparandoArquivos(arquivos,diretorio)
    
def listarArquivos(diretorio=''):
    if diretorio=='':
        return glob.glob('*')
    else:
        return glob.glob(diretorio+ '*')

def criardiretorio(caminho):
        os.mkdir(caminho)

def verificarDiretorioAseremCriados(listarArquivos):
    diretorios={
        "pdfs" : False,
        "Imagens": False,
        "ArquivosIsos":False,
        "Songs": False,
        "Documentos":False,
        "Videos": False,
        "Pacotes/exe":False
    }
    for i in listarArquivos:
        if i.count(".pdf"):
            diretorios["pdfs"]=True
        elif i.count(".jpeg") or i.count(".jpg") or i.count(".png"):
            diretorios["Imagens"]=True
        elif i.count(".iso"):
            diretorios["ArquivosIsos"]=True
        elif i.count(".doc") or i.count(".docx") or i.count(".odt") or i.count(".pttx") or i.count(".odp") or i.count(".odp"):
            diretorios["Documentos"]=True
        elif i.count(".mp4") or i.count(".avi") or i.count(".mkv") or i.count(".MPG"):
              diretorios["Videos"]=True
        elif i.count(".exe") or i.count(".deb"):
            diretorios["Pacotes/exe"]=True
        elif i.count(".mp3") or i.count(".WAV"):
            diretorios["Songs"]=True
    return diretorios;

def preparacaoCriarPasta(diretorios,diretorio):        
    for i in diretorios.items():
        if i[1]==True:
            if not os.path.isdir(diretorio+i[0]):
                criardiretorio(diretorio+i[0])

def SeparandoArquivos(arquivos,diretorio):
    for i in arquivos:
        if i.count(".pdf"):
            destino=diretorio+"pdfs"
            moverArquivo(i,destino)
        elif i.count(".jpeg") or i.count(".jpg") or i.count(".png"):
            destino=diretorio+"Imagens"
            moverArquivo(i,destino)
        elif i.count(".iso"):
            destino=diretorio+"ArquivosIsos"
            moverArquivo(i,destino)
        elif i.count(".doc") or i.count(".docx") or i.count(".odt") or i.count(".pttx") or i.count(".odp") or i.count(".odp"):
            destino=diretorio+"Documentos"
            moverArquivo(i,destino)
        elif i.count(".mp4") or i.count(".avi") or i.count(".mkv") or i.count(".MPG"):
            destino=diretorio+"Videos"
            moverArquivo(i,destino)
        elif i.count(".exe") or i.count(".deb"):
            destino=diretorio+"Videos"
            moverArquivo(i,destino)
        elif i.count(".mp3") or i.count(".WAV"):
            destino=diretorio+"Songs"
            moverArquivo(i,destino)
                

def moverArquivo(origem,destino):
    shutil.move(origem,destino)

main()