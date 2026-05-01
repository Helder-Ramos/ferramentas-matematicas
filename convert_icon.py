from PIL import Image

img = Image.open("icone.png")
# Isso gera o arquivo .ico com os tamanhos necessários para o Windows
img.save("icone.ico", sizes=[(32, 32), (64, 64), (128, 128), (256, 256)])