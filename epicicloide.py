import math
from PIL import Image
from tqdm import tqdm

image = Image.open("Epicicloide.png")
epicicloide = image.convert("RGB")

width, height = image.size
areaTotal = width * height

black = (0, 0, 0)
areaEpicicloide = 0

loop = tqdm(total=height, position=0, leave=False)
for i in range(height):
    loop.set_description("Calculating... ".format(i))
    loop.update(1)
    for j in range(width):
        color = epicicloide.getpixel((j, i))

        if color == black:
            areaEpicicloide += 1
loop.close()

areaReal = 15.392 * 16.180

epiReal = areaReal * areaEpicicloide/areaTotal
epiCalculo = 56*math.pi

print(f"Método Computacional: {epiReal:.2f}u")
print(f"Cálculo na mão: {epiCalculo:.2f}u")

erroPercentual = 100-((epiReal*100)/epiCalculo)
print(f"Erro Percentil: {erroPercentual:.2f}%")
