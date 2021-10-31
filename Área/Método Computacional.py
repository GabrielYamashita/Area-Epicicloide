from PIL import Image
from tqdm import tqdm

image = Image.open("./CurvaTratada.png")
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

areaReal = 31.28 * 20.47 # Dimensões da Imagem
imgReal = areaReal * areaCurva/areaTotal
Calculo = 228.79 # Resultado do Cálculo Numérico

print(f"Método Computacional: {imgReal:.2f}u")
print(f"Cálculo na mão: {Calculo:.2f}u")

erroPercentual = abs(100-((imgReal*100)/Calculo))
print(f"Erro Percentil: {erroPercentual:.2f}%")
