from decimal import Clamped
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import easygui_qt as easygui

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()

auto = Image.open('Carteirinha-do-Cliente-Voraz.png')
auto = auto.resize((2600 , 3600))

myFont = ImageFont.truetype('NewsGothicBT.ttf', 87)

cTipo = easygui.get_choice('A Carterinha Sera ? \n \n' , 'tipo de carteirinha' , ['1. Auto' , '2. Residencial' , '3. Empresarial'])

clearConsole()

# Definindo Função que Vai Adicionar o Texto Na Imagem
def cMaker(img) :

    #Area que Vai Receber a Informação 
    if True :
        nome = easygui.get_string('Qual o Nome ? \n \n')
        clearConsole()
        cpf = easygui.get_string('Qual o CPF ? \n \n')
        clearConsole()
        seguradora = easygui.get_string('Qual a Seguradora ? \n \n')
        clearConsole()
        nSeguradora = easygui.get_string('Qual o Numero da Seguradora ? \n \n')
        clearConsole()
        nApolice = easygui.get_string('Qual o Numero da Apolice \n \n')
        clearConsole()
        cResponsavel = easygui.get_choice('Qual o Coretor Responsavel ? \n \n','Coretor' , ['1. Vera Viana' , '2. Renata Dutra'])
        cResponsavel = cResponsavel.replace('1. ','')
        cResponsavel = cResponsavel.replace('2. ','')
        clearConsole()
        mVeiculo = easygui.get_string('Qual o Modelo do Veiculo ? \n \n')
        clearConsole()
        pVeiculo = easygui.get_string('Qual a Placa do Veiculo ? \n \n')
        clearConsole()
        cep = easygui.get_string('Qual o CEP de Pernoite ? \n \n')
        clearConsole()
        codC = easygui.get_string('Qual o Código do Cliente ? \n \n')
        clearConsole()
        codDoc = easygui.get_string('Qual o Código do Documento ? \n \n')
        clearConsole()
        vigencia = easygui.get_string('Qual a Vigencia ? \n \n ')
    
    
    def drawImage() :
        img.text((330, 480), "Cliente: " + nome.title(), font=myFont, fill=(255, 255, 255))
        
        img.text((330, 680), "CPF: " + cpf.title(), font=myFont, fill=(255, 255, 255))
        
        img.text((330, 880), "Seguradora: " + seguradora.title(), font=myFont, fill=(255, 255, 255))
        
        img.text((330, 1080), "Ramo: Automóvel" , font=myFont, fill=(255, 255, 255))
        
        img.text((1530, 680), "Código do Cliente: " + codC.title(), font=myFont, fill=(255, 255, 255))
        
        img.text((1530, 880), "Vigência: " + vigencia.upper(), font=myFont, fill=(255, 255, 255))
        
        img.text((1530, 1080), "Apólice: " + nApolice.title(), font=myFont, fill=(255, 255, 255))
        
        img.text((330, 2515), "Coretora Responsável: " + cResponsavel.title(), font=myFont, fill=(1, 70, 185), stroke_width=2)
        
        img.text((330, 2665), "Telefone Seguradora: " + nSeguradora.title(), font=myFont, fill=(1, 70, 185))
        
        img.text((330, 2785), "Veículo: " + mVeiculo.title(), font=myFont, fill=(1, 70, 185))
        
        img.text((330, 2905), "Placa: " + pVeiculo.upper(), font=myFont, fill=(1, 70, 185))
        
        img.text((330, 3025), "CEP de Pernoite: " + cep.title(), font=myFont, fill=(1, 70, 185))
        
        img.text((1530, 2905), "Código de Doc.: " + codDoc.title(), font=myFont, fill=(1, 70, 185))
    
    drawImage()



if '1' in cTipo or "auto" in cTipo.lower():

    imgDr = ImageDraw.Draw(auto)
    
    cMaker(imgDr)
    
    onde = easygui.get_save_file_name()
    
    auto.save(onde)
    
    auto.show()
    
