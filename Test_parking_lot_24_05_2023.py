from datetime import datetime,timedelta
from time import sleep
import os
import math
from termcolor import colored

def entrar(placa):
    for i in range (20):
        if i in time and not placa in time:
            time.pop(i)  
            time[placa] = datetime.now()
            print(f'\nCarro {placa} tem 20 min de tolerancia.')
            break
        elif placa in time:
            print(f'\nCarro {placa} já está no estacionamento')
            break

def sair_estacionamento(placa):
    enter_time = time.pop(placa, None)
    if enter_time is not None:
        exit_time = datetime.now()
        duration = exit_time - enter_time
        if not duration<=timedelta(0):
            hours = math.ceil(duration.total_seconds() / 3600) 
            conta = hours * 5
            print(f'\nO carro {placa} ficou um total de {duration} e deve pagar {conta}$')
    return duration

def estacionar(slots,slot,placa,cars):
    if slots[slot] == False:
        slots[slot] = True
        cars[slot] = placa
        print(f'Carro {placa} estacionou na vaga {slot}')
        print_slots(slots,cars)

    else: 
        print(f'Vaga {slot} já está ocupada pelo carro {cars[slot]}')
        print_slots(slots,cars)
def print_slots(slots,cars):
    print()
    for vagas in slots:
        if slots[vagas] == False:
            print(colored(f'Vaga {vagas} Disponivel.','green'))
        else:
            print(colored(f'Vaga {vagas} Indisponivel, carro de placa {cars[vagas]}.','red'))
    print()

def sair_vaga(slots,slot,cars):
    if slots[slot]:
        print(f'Carro {cars[slot]} saiu da vaga {slot}')
        slots[slot] = False
        cars[slot] = ''
    else:
        print(f'Não há carros na vaga {slot}')

slots = {0: False, 1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: True, 9: False}
cars  = {0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: 'AAA', 9: ''}
time = {0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}


placa = 'AAA'
letter_1_value = ord(placa[0]) - 65
letter_2_value = ord(placa[1]) - 65
letter_3_value = ord(placa[2]) - 65

#print(letter_1_value,letter_2_value,letter_3_value)
print_slots(slots,cars)

estacionar(slots,4,"ABC",cars)
estacionar(slots,4,'AGF',cars)

os.system('cls')

entrar('BBB')
entrar('HUN')
entrar('OOO')
entrar('BBB')
sleep(5)
sair_estacionamento('BBB')
estacionar(slots,5,'HUN',cars)

while True:
    func = input('[1] Entrar no estacionamento \n[2] Sair do estacionamento \n[3] estacionar\n[4] sair da vaga \n[5] print slots\n')
    if func ==   '1':
        placa = input('Insira a placa do carro no padrão "AAA1A11"\n')
        entrar(placa)
    elif func == '2':
        placa = input('Insira a placa do carro no padrão "AAA1A11"\n')
        sair_estacionamento(placa)
    elif func == '3':
        placa = input('Insira a placa do carro no padrão "AAA1A11"\n')
        while True:
            vaga = input('Insira o numero da vaga\n')
            try:
                vaga = int(vaga)
                break
            except Exception as e:
                print(e)
        estacionar(slots,vaga,placa[0:3],cars)

    elif func == '4':
        pass
    elif func == '5':
        pass
    else:
        print('Opção inválida')

