from PIL import Image
import PIL
import os
import glob

images = [file for file in os.listdir() if file.endswith(('jpg', 'png' ))]
print(f"Imagens no diretório: {images}");

file_name = input("Qual arquivo será comprimido: ")
picture = Image.open(file_name)

picture.save("comprimida_"+file_name,optimize=True,quality=60)
print("A imagem foi otimizada com sucesso!")
