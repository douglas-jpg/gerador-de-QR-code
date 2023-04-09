# autor: douglas de lima bezerra
# data: 09/04/2023
# cria um qr code atravez de um link
import os  # criar e/ou mover os arquivos
import pyqrcode

# so ira receber links com o protocolo http
while True:
    url = str(input('Digite o seu link: '))
    if url.startswith('http'):
        break
    else:
        print('Link invalido'
              'Por favor insira o protocolo http:// ou https://')
# cria o qrcode
qr = pyqrcode.create(url)

# colocar o nome do arquivo e aadicionar o .png
nome = str(input('Digite o nome do arquivo: '))
nome += '.png'

# guarda o arquivo na pasta qrcodes
# caso nao exista cria um
caminho = "qrcodes"
if not os.path.exists(caminho):
    os.makedirs(caminho)

# cria o arquivo no formato imagem .png
qr.png(os.path.join(caminho, nome.replace(' ', '_')), scale=10)

# mensagem de confirmacao
print(f'O seu qrcode {nome} no formato foi criado com sucesso')
