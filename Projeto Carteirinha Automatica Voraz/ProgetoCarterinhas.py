from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

auto = Image.open('./Carteirinha-do-Cliente-Voraz.jpeg')

myFont = ('FreeMono.ttf', 65)

cTipo = input('A Carterinha Sera (1) Auto, (2) Residencial ou (3) Empresarial ?')

# Definindo Função que Vai Adicionar o Texto Na Imagem
def cMaker(img) :

    #Area que Vai Receber a Informação
    
    nome = input('Qual o Nome ?')
    cpf = input('Qual o CPF ?')
    seguradora = input('Qual a Seguradora ?')
    nApolice = input('Qual o Numero da Apolice')
    cResponsavel = input('Qual o Coretor Responsavel ? \n (1) Vera    (2) Renata')
    mVeiculo = input('Qual o Modelo do Veiculo ?')
    pVeiculo = input('Qual a Placa do Veiculo ?')
    cep = input('Qual o CEP de Pernoite ?')
    codC = input('Qual o Código do Cliente ?')
    codDoc = input('Qual o Código do Documento ?')
    
    
    img.text((28, 36), "nice Car", fill=(255, 0, 0))


if cTipo in '1' or "auto" in cTipo.lower():

    imgDr = ImageDraw.Draw(auto)
    
    cMaker(imgDr)
    

