import math
from PIL import Image
from tqdm import tqdm

image = Image.open("Curva.png")
curva = image.convert("RGB")

width, height = image.size
areaTotal = width * height

black = (0, 0, 0)
areaCurva = 0

loop = tqdm(total=height, position=0, leave=False)
for i in range(height):
    loop.set_description("Calculating... ".format(i))
    loop.update(1)
    for j in range(width):
        color = curva.getpixel((j, i))

        if color == black:
            areaCurva += 1
loop.close()

areaReal = 15.392 * 16.180

imgReal = areaReal * areaCurva/areaTotal
Calculo = 56*math.pi

print(f"Método Computacional: {imgReal:.2f}u")
print(f"Cálculo na mão: {Calculo:.2f}u")

erroPercentual = 100-((imgReal*100)/Calculo)
print(f"Erro Percentil: {erroPercentual:.2f}%")
