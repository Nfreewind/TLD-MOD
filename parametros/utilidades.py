import os


caminho = '/home/hugo/Documents/Mestrado/alov_dataset/alov300/anotacao/01-Light/'
arquivo = '01-Light_video00001.ann'
file = open(os.path.join(caminho,arquivo),'r')
linhas = file.readlines()
file.close()
linhaEspaco = []
listaDeFrames = []
for linha,i in zip(linhas,range(len(linhas))):
    linhaEspaco.append(linha.split(' '))
    listaDeFrames.append(linhaEspaco[i][0]) # lista que contem apenas os numeros da linhas das anotaçoes

print(linhaEspaco)
print(listaDeFrames)


