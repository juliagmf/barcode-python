from email.mime import image
import barcode
from barcode.writer import ImageWriter
from PIL import Image

#definindo o conteúdo do código de barras como uma string
numeros = input("Digite o código para criar: ")

#formato do código de barras necessário
barcode_formato = barcode.get_barcode_class('upc')

#gerando um código de barras e renderizando como imagem
my_barcode = barcode_formato(numeros, writer=ImageWriter())

#salvando o código de barras como imagem
my_barcode.save("barcode")

Image.open('barcode.png')