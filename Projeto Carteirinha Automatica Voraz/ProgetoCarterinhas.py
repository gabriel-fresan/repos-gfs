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

def compareStr(str1, str2):
    count1 = 0
    count2 = 0
      
    for i in range(len(str1)):
        if str1[i] >= "0" and str1[i] <= "9":
            count1 += 1
      
    for i in range(len(str2)):
        if str2[i] >= "0" and str2[i] <= "9":
            count2 += 1
      
    return count1 == count2

myFont = ImageFont.truetype('NewsGothicBT.ttf', 87)

cTipo = easygui.get_choice('A Carterinha Sera ? \n ' , 'tipo de carteirinha' , ['1. Auto' , '2. Residencial' , '3. Empresarial'])

clearConsole()
# Definindo Função que Vai Adicionar o Texto Na Imagem
def cMakerRes(img) :

    #Area que Vai Receber a Informação 
    if True :
        
        endosso = easygui.get_choice('É Um Endosso ? \n ','Endosso ?' , ['1- Sim, É um Endosso' , '2- Não, É uma Apolice'])
        endosso = endosso.replace('1- Sim, É um ', '')
        endosso = endosso.replace('2- Não, É uma ', '')
        
        nome = easygui.get_string('Qual o Nome ? \n ')
        
        cpfin = easygui.get_string('Qual o CPF/CNPJ ? \n ')
        cpfin = cpfin.replace('.' , '')
        cpfin = cpfin.replace('/' , '')
        
        
        
        if compareStr(cpfin  , '00000000000'):
                cpfin = cpfin.replace('a','')
                cpfps = '.'.join(cpfin[i:i + 3] for i in range(0, len(cpfin), 3))
                cpfps2 = '.'.join(cpfps[i:i + 12] for i in range(0, len(cpfps), 12))
                cpf = cpfps2.replace('..' , '-')
                cpf = 'CPF: ' + cpf
        
        elif compareStr(cpfin , '00000000000000'):
                cpfin = cpfin.replace('a','')
                cpfps = '.'.join(cpfin[i:i + 2] for i in range(2, len(cpfin), 2))
                cpfps2 = '-'.join(cpfps[i:i + 5] for i in range(0, len(cpfps), 4))
                cpfps3 = '-'.join(cpfps2[i:i + 10] for i in range(0, len(cpfps2), 10))
                cpfps3 = cpfps3.replace('-.' , '')
                cpf = cpfps2.replace('.-' , '/')
                cpf = 'CNPJ: ' + cpf
        else:
                cpf = 'ERROR'
        
        
        seguradora = easygui.get_choice('Qual a Seguradora ? \n ' , 'Seguradoras' , ['1- Porto Seguro' , '2- Liberty Seguros' ,   '3- HDI Seguros' , '4- Alianz'  , '5- Sompo Seguros' , '6- Tokio Seguros' , '7- Bradesco Seguros' ])
        
        nSeguradora = ''
        if True :
                
                if '1' in seguradora :
                        nSeguradora = '3004 6268'
                        seguradora = seguradora.replace('1-' , '')
                elif '2' in seguradora :
                        nSeguradora = '0800 702 5100'
                        seguradora = seguradora.replace('2-' , '')
                elif '3' in seguradora :
                        nSeguradora = '3003 5390'
                        seguradora = seguradora.replace('3-' , '')
                elif '4' in seguradora :
                        nSeguradora = '0800 177 178'
                        seguradora = seguradora.replace('4-' , '')
                elif '5' in seguradora :
                        nSeguradora = '0800 77 19 719'
                        seguradora = seguradora.replace('5-' , '')
                elif '6' in seguradora :
                        nSeguradora = '0800 30 86546'
                        seguradora = seguradora.replace('6-' , '')
                elif '7' in seguradora :
                        nSeguradora = '4004 0237'
                        seguradora = seguradora.replace('7-' , '')
        
        
        


        nApolice = easygui.get_string('Qual o Numero da Apolice \n ')
        
        vigencia = easygui.get_string('Qual a Vigencia ? \n  ')
        
        cResponsavel = easygui.get_choice('Qual o Coretor Responsavel ? \n ','Coretor' , ['1- Vera Viana' , '2- Renata Dutra'])
        cResponsavel = cResponsavel.replace('1- ','')
        cResponsavel = cResponsavel.replace('2- ','')
        
        cep = easygui.get_string('Qual o CEP ? \n ')
        
        lRisco = easygui.get_string('Qual o Local De Risco ? \n ')
        
        # cep = easygui.get_string('Qual o CEP de Pernoite ? \n ')
        
        codC = easygui.get_string('Qual o Código do Cliente ? \n ')
        
        rTipo = easygui.get_string('Qual o Tipo de Seguro ? \n ')
        
        
        
    
    
    if True :
        img.text((330, 480), "Cliente: " + nome.title(), font=myFont, fill=(255, 255, 255))
        
        img.text((330, 680), cpf.title(), font=myFont, fill=(255, 255, 255))
        
        img.text((330, 880), "Seguradora: " + seguradora.title(), font=myFont, fill=(255, 255, 255))
        
        img.text((330, 1080), "Ramo: Automóvel" , font=myFont, fill=(255, 255, 255))
        
        img.text((1530, 680), "Código do Cliente: " + codC.title(), font=myFont, fill=(255, 255, 255))
        
        img.text((1530, 880), "Vigência: " + vigencia.upper(), font=myFont, fill=(255, 255, 255))
        
        img.text((1530, 1080), endosso + ": " + nApolice.title(), font=myFont, fill=(255, 255, 255))
        
        img.text((300, 2615), "Coretora Responsável: " + cResponsavel.title(), font=myFont, fill=(104, 149, 59), stroke_width=2)
        
        img.text((300, 2765), "Telefone Seguradora: " + nSeguradora.title(), font=myFont, fill=(104, 149, 59))
        
        img.text((300, 2885), "CEP: " + cep, font=myFont, fill=(104, 149, 59))
        
        img.text((300, 3005), "Local De Risco : " + lRisco.title(), font=myFont, fill=(104, 149, 59))
        
        # img.text((300, 3125), "CEP de Pernoite: " + cep.title(), font=myFont, fill=(104, 149, 59))
        
        img.text((1500, 2885), "Residência : " + rTipo.title(), font=myFont, fill=(104, 149, 59))
    
    


# Definindo Função que Vai Adicionar o Texto Na Imagem
def cMakerAuto(img) :

    #Area que Vai Receber a Informação 
    if True :
        
        endosso = easygui.get_choice('É Um Endosso ? \n ','Endosso ?' , ['1- Sim, É um Endosso' , '2- Não, É uma Apolice'])
        endosso = endosso.replace('1- Sim, É um ', '')
        endosso = endosso.replace('2- Não, É uma ', '')
        
        
        nome = easygui.get_string('Qual o Nome ? \n ')
        
        
        cpfin = easygui.get_string('Qual o CPF/CNPJ ? \n ') + 'a'
        cpfin = cpfin.replace('.' , '')
        cpfin = cpfin.replace('/' , '')
        
        
        if cpfin < 'a000.000.000-00' and cpfin >= 'a00000000000':
                
                cpfps = '.'.join(cpfin[i:i + 3] for i in range(0, len(cpfin), 3))
                cpfps2 = '.'.join(cpfps[i:i + 12] for i in range(0, len(cpfps), 12))
                cpf = cpfps2.replace('..' , '-')
                cpcj = 'CPF'
                cpfin = cpfin.replace('a','')
                
        elif cpfin < 'a00.000.000/0000-00' and cpfin >= 'a00000000000000':
                
                cpcj = 'CNPJ'
                cpfin = cpfin.replace('a','')
        
        
        seguradora = easygui.get_choice('Qual a Seguradora ? \n ' , 'Seguradoras' , ['1- Azul Seguros' , '2- Porto Seguro' , '3- Liberty Seguros' ,   '4- HDI Seguros' , '5- Suhai Seguros'  , '6- Alianz'  , '7- Sompo Seguros' , '8- Tokio Seguros' , '9- Bradesco Seguros' , '10- Aliro Seguros' ])
        
        nSeguradora = ''
        if True :
                
                if '1' in seguradora :
                        nSeguradora = '4004 3700'
                        seguradora = seguradora.replace('1-' , '')
                elif '2' in seguradora :
                        nSeguradora = '0300 337 6786'
                        seguradora = seguradora.replace('2-' , '')
                elif '3' in seguradora :
                        nSeguradora = '0800 701 4120'
                        seguradora = seguradora.replace('3-' , '')
                elif '4' in seguradora :
                        nSeguradora = '3003 5390'
                        seguradora = seguradora.replace('4-' , '')
                elif '5' in seguradora :
                        nSeguradora = '3003 0335'
                        seguradora = seguradora.replace('5-' , '')
                elif '6' in seguradora :
                        nSeguradora = '4090 1110'
                        seguradora = seguradora.replace('6-' , '')
                elif '7' in seguradora :
                        nSeguradora = '0800 77 19 719'
                        seguradora = seguradora.replace('7-' , '')
                elif '8' in seguradora :
                        nSeguradora = '0800 318 6546'
                        seguradora = seguradora.replace('8-' , '')
                elif '9' in seguradora :
                        nSeguradora = '4004 2757'
                        seguradora = seguradora.replace('9-' , '')
                elif '10' in seguradora :
                        nSeguradora = '0800 220 2128'
                        seguradora = seguradora.replace('10-' , '')



        nApolice = easygui.get_string('Qual o Numero da Apolice \n ')
        
        cResponsavel = easygui.get_choice('Qual o Coretor Responsavel ? \n ','Coretor' , ['1- Vera Viana' , '2- Renata Dutra'])
        cResponsavel = cResponsavel.replace('1- ','')
        cResponsavel = cResponsavel.replace('2- ','')
        
        mVeiculo = easygui.get_string('Qual o Modelo do Veiculo ? \n ')
        
        pVeiculo = easygui.get_string('Qual a Placa do Veiculo ? \n ')
        
        cep = easygui.get_string('Qual o CEP de Pernoite ? \n ')
        
        codC = easygui.get_string('Qual o Código do Cliente ? \n ')
        
        codDoc = easygui.get_string('Qual o Código do Documento ? \n ')
        
        vigencia = easygui.get_string('Qual a Vigencia ? \n  ')
    
    
    def drawImage() :
        img.text((330, 480), "Cliente: " + nome.title(), font=myFont, fill=(255, 255, 255))
        
        img.text((330, 680), "CPF: " + cpf.title(), font=myFont, fill=(255, 255, 255))
        
        img.text((330, 880), "Seguradora: " + seguradora.title(), font=myFont, fill=(255, 255, 255))
        
        img.text((330, 1080), "Ramo: Automóvel" , font=myFont, fill=(255, 255, 255))
        
        img.text((1530, 680), "Código do Cliente: " + codC.title(), font=myFont, fill=(255, 255, 255))
        
        img.text((1530, 880), "Vigência: " + vigencia.upper(), font=myFont, fill=(255, 255, 255))
        
        img.text((1530, 1080), endosso + ": " + nApolice.title(), font=myFont, fill=(255, 255, 255))
        
        img.text((330, 2515), "Coretora Responsável: " + cResponsavel.title(), font=myFont, fill=(1, 70, 185), stroke_width=2)
        
        img.text((330, 2665), "Telefone Seguradora: " + nSeguradora.title(), font=myFont, fill=(1, 70, 185))
        
        img.text((330, 2785), "Veículo: " + mVeiculo.title(), font=myFont, fill=(1, 70, 185))
        
        img.text((330, 2905), "Placa: " + pVeiculo.upper(), font=myFont, fill=(1, 70, 185))
        
        img.text((330, 3025), "CEP de Pernoite: " + cep.title(), font=myFont, fill=(1, 70, 185))
        
        img.text((1530, 2905), "Código de Doc.: " + codDoc.title(), font=myFont, fill=(1, 70, 185))
    
    drawImage()



if '1' in cTipo or "auto" in cTipo.lower():

        auto = Image.open('Carteirinha-do-Cliente-Voraz-auto.png')
        auto = auto.resize((2600 , 3600))

        imgDrAuto = ImageDraw.Draw(auto)
        
        cMakerAuto(imgDrAuto)
        
        #onde = easygui.get_save_file_name()
        
        auto.save('./#30.Carteirinha-do-Cliente.png')
        
        auto.show()

elif '2' in cTipo or "res" in cTipo.lower():

        res = Image.open('Carteirinha-do-Cliente-Voraz-res.png')
        res = res.resize((2600 , 3600))
        
        
        imgDrRes = ImageDraw.Draw(res)
        
        cMakerRes(imgDrRes)
        
        #onde = easygui.get_save_file_name()
        
        res.save('./#40.Carteirinha-do-Cliente.png')
        
        res.show()
