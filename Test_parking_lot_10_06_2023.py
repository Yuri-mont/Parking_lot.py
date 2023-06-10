from datetime import datetime,timedelta
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

def sair_estacionamento(slots,slot,placa,cars):
    if placa in time:
        enter_time = time.pop(placa, None)
        if enter_time is not None:
            exit_time = datetime.now()
            duration = exit_time - enter_time
            if not duration<=timedelta(0):
                hours = math.ceil(duration.total_seconds() / 3600) 
                conta = hours * 5
                print(f'\nO carro {placa} ficou um total de {duration} e deve pagar {conta}$')
            if slots[slot]:
                slots[slot] = False
                cars[slot] = ''
        return duration
    else:
        print(f'Carro {placa} não está no estacionamento!!!')
    

def estacionar(slots,slot,placa,cars):
    if placa in time:
        if slots[slot] == False:
            slots[slot] = True
            cars[slot] = placa
            print(f'Carro {placa} estacionou na vaga {slot}')
            print_slots(slots,cars)

        else: 
            print(f'Vaga {slot} já está ocupada pelo carro {cars[slot]}')
            print_slots(slots,cars)
    else:
        print(f'Carro {placa} não está no estacionamento!!!')

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
        print(f'\nNão há carros na vaga {slot}\n')

def check_state(placa):
    placa = placa[0:3]
    ranges_SC = [
        ("LWR", "MMM"),
        ("OKD", "OKH"),
        ("QHA", "QJZ"),
        ("QTK", "QTM"),
        ("RAA", "RAJ"),
        ("RDS", "REB"),
        ("RKW", "RLP"),
        ("RXK", "RYI")
    ]

    prompt_value = sum((ord(c) - ord('A')) * (26 ** (2 - i)) for i, c in enumerate(placa))

    lower_bound_range_parana_1 = sum((ord(c) - ord('A')) * (26 ** (2 - i)) for i, c in enumerate("AAA"))
    upper_bound_range_parana_1 = sum((ord(c) - ord('A')) * (26 ** (2 - i)) for i, c in enumerate("BEZ"))

    lower_bound_range_parana_2 = sum((ord(c) - ord('A')) * (26 ** (2 - i)) for i, c in enumerate("RHA"))
    upper_bound_range_parana_2 = sum((ord(c) - ord('A')) * (26 ** (2 - i)) for i, c in enumerate("RHZ"))

    lower_bound_range_GREMIO = sum((ord(c) - ord('A')) * (26 ** (2 - i)) for i, c in enumerate("IAQ"))
    upper_bound_range_GREMIO = sum((ord(c) - ord('A')) * (26 ** (2 - i)) for i, c in enumerate("JDO"))

    valor_SC = sum((ord(c) - ord('A')) * (26 ** (len(placa) - 1 - i)) for i, c in enumerate(placa))

    for range_start, range_end in ranges_SC:
        lower_bound = sum((ord(c) - ord('A')) * (26 ** (len(range_start) - 1 - i)) for i, c in enumerate(range_start))
        upper_bound = sum((ord(c) - ord('A')) * (26 ** (len(range_end) - 1 - i)) for i, c in enumerate(range_end))

        if lower_bound_range_parana_1 <= prompt_value <= upper_bound_range_parana_1 or lower_bound_range_parana_2 <= prompt_value <= upper_bound_range_parana_2:
            return "Paraná", True

        elif lower_bound_range_GREMIO <= prompt_value <= upper_bound_range_GREMIO:
            return "GREMIO", True

        elif lower_bound <= valor_SC <= upper_bound:
            return "SANTA CATARINA", True

    return False



def check_pattern():  
    license_plate = input('Insira a placa do carro no padrão "AAA1A11"\n')
    #THIS CODE ABOVE CHECK THE PATTERN OF LICENSE PLATE
    if len(license_plate) ==7:
        if not license_plate[0].isnumeric() and not license_plate[1].isnumeric() and not license_plate[2].isnumeric() :
            if license_plate[3].isnumeric() and not license_plate[4].isnumeric() and license_plate[5].isnumeric() and license_plate[6].isnumeric():   
                return license_plate
    else:
        print('Follow the instructions')
    
slots = {0: False, 1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False}
cars  = {0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
time = {0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}


while True:
    func = input('\n[1] Entrar no estacionamento \n[2] Sair do estacionamento \n[3] estacionar\n[4] sair da vaga \n[5] print slots\n[X] Sair do programa\n')
    if func ==   '1':
        
        while True:
            placa = check_pattern()
            if placa != None:
                break
        if check_state(placa):
            print(check_state(placa)[0])
            entrar(placa)
        else:
            print("Carros desse estado não pode entrar no estacionamento")
    elif func == '2':
        while True:
            placa = check_pattern()
            if placa != None:
                break
        while True:
            vaga = input('Insira o numero da vaga\n')
            try:
                vaga = int(vaga)
                break
            except Exception as e:
                print(f'{vaga} precisa ser um numero')
        sair_estacionamento(slots,vaga,placa[0:3],cars)
    elif func == '3':
        while True:
            placa = check_pattern()
            if placa != None:
                break
        while True:
            vaga = input('Insira o numero da vaga\n')
            try:
                vaga = int(vaga)
                break
            except Exception as e:
                print(e)
        estacionar(slots,vaga,placa[0:3],cars)

    elif func == '4':
        while True:
            placa = check_pattern()
            if placa != None:
                break
        if placa in time:
            while True:
                vaga = input('Insira o numero da vaga\n')
                try:
                    vaga = int(vaga)
                    break
                except Exception as e:
                    print(e)
            sair_vaga(slots,vaga,cars)
        else:
            print(f'Carro {placa} não está no estacionamento!!!')

    elif func == '5':
        print_slots(slots,cars)
    elif func == '6':
        print()
        print(time)
        print()
    elif func == 'X' or func =='x':
        break
    else:
        print('Opção inválida')

#if carro in vaga carro needs to leave vaga to leave parking lot
