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
            print(f'Vaga {vagas} Disponivel.')
        else:
            print(f'Vaga {vagas} Indisponivel, carro de placa {cars[vagas]}.')
    print()
slots = {0: False, 1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: True, 9: False}
cars  = {0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: 'AAA', 9: ''}


slot = 4
placa   = 'ABC'
letter_1_value = ord(placa[0]) - 65
letter_2_value = ord(placa[1]) - 65
letter_3_value = ord(placa[2]) - 65

#print(letter_1_value,letter_2_value,letter_3_value)
print_slots(slots,cars)

estacionar(slots,4,placa,cars)
estacionar(slots,4,'AGF',cars)
