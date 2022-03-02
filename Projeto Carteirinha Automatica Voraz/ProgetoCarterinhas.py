from decimal import Clamped
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()

auto = Image.open('.\Carteirinha-do-Cliente-Voraz.jpeg')
auto = auto.resize((2600 , 3600))

myFont = ImageFont.truetype('NewsGothicBT.ttf', 70)

cTipo = input('A Carterinha Sera \n (1) Auto, (2) Residencial ou (3) Empresarial ? \n \n')

clearConsole()

# Definindo Função que Vai Adicionar o Texto Na Imagem
def cMaker(img) :

    #Area que Vai Receber a Informação 
    if True :
        nome = input('Qual o Nome ? \n \n')
        clearConsole()
        cpf = input('Qual o CPF ? \n \n')
        clearConsole()
        seguradora = input('Qual a Seguradora ? \n \n')
        clearConsole()
        nApolice = input('Qual o Numero da Apolice \n \n')
        clearConsole()
        cResponsavel = input('Qual o Coretor Responsavel ? \n (1) Vera    (2) Renata \n \n')
        clearConsole()
        mVeiculo = input('Qual o Modelo do Veiculo ? \n \n')
        clearConsole()
        pVeiculo = input('Qual a Placa do Veiculo ? \n \n')
        clearConsole()
        cep = input('Qual o CEP de Pernoite ? \n \n')
        clearConsole()
        codC = input('Qual o Código do Cliente ? \n \n')
        clearConsole()
        codDoc = input('Qual o Código do Documento ? \n \n')
        clearConsole()
        vigencia = input('Qual a Vigencia ? \n \n ')
    
    
    
    
    img.text((330, 430), "Cliente: " + nome.title(), font=myFont, fill=(255, 255, 255))
    
    img.text((330, 630), "CPF: " + cpf.title(), font=myFont, fill=(255, 255, 255))
    
    img.text((330, 830), "Seguradoura: " + seguradora.title(), font=myFont, fill=(255, 255, 255))
    
    img.text((330, 1030), "Ramo: Veículo" , font=myFont, fill=(255, 255, 255))
    
    img.text((1530, 630), "Código do Cliente: " + codC.title(), font=myFont, fill=(255, 255, 255))
    
    img.text((1530, 830), "Vigência: " + vigencia.upper(), font=myFont, fill=(255, 255, 255))
    
    img.text((1530, 1030), "Apólice: " + nApolice.title(), font=myFont, fill=(255, 255, 255))
    
    img.text((330, 2550), "Coretora Responsavel: " + cResponsavel.title(), font=myFont, fill=(1, 70, 185))
    
    img.text((330, 2700), "Veículo: " + mVeiculo.title(), font=myFont, fill=(1, 70, 185))
    
    img.text((330, 2850), "Placa: " + pVeiculo.upper(), font=myFont, fill=(1, 70, 185))
    
    img.text((330, 3000), "CEP de Pernoite: " + cep.title(), font=myFont, fill=(1, 70, 185))
    
    img.text((1530, 2850), "Código de Doc.: " + codDoc.title(), font=myFont, fill=(1, 70, 185))
    



if cTipo in '1' or "auto" in cTipo.lower():

    imgDr = ImageDraw.Draw(auto)
    
    cMaker(imgDr)
    
    auto.show()
    
    auto.save("#30.Carteirinha-do-Cliente.png")
    
