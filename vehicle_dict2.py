vehicles = {
    1 : ['Kamion', 'Iveco', 'OS 001 ZZ', 2015, 45_000.00],
    2 : ['Kamion', 'Iveco', 'OS 002 ZZ', 2015, 47_000.00],
    3 : ['Tegljac', 'MAN', 'RI 001 ZZ', 2018, 78_000],
    4 : ['Tegljac', 'MAN', 'RI 002 ZZ', 2020, 97_000],
    5 : ['Kombi', 'Mercedes Benz', 'ST 001 ZZ', 2013, 12_000],
    6 : ['Kombi', 'Volkswagen', 'ST 002 ZZ', 2021, 35_000],
    7 : ['Dostavno vozilo', 'Volkswagen', 'ZG 001 ZZ', 2010, 9_000],
    8 : ['Dostavno vozilo', 'Volkswagen', 'ZG 002 ZZ', 2010, 9_300]
}

print()
print('-'*92)
table_header_row_1 = f'|{"ID":<5}|{"Tip":<20}|{"Proizvodac":<20}|{"Registarska":<15}|{"Godina prve":>15}|{"Cijena u":>10}|'
table_header_row_2 = f'|{"":<5}|{"":<20}|{"":<20}|{"oznaka":<15}|{"registracije":>15}|{"EUR":>10}|'
print(table_header_row_1)
print(table_header_row_2)
print('-'*92)

for key, value in vehicles.items():
    print(f'|{key:<5}|', end='')
    for element in value:
        print(f'{element:<20}|', end='')
        print(f'{value[0]:<20}|', end='')
        print(f'{value[1]:<20}|', end='')
        print(f'{value[2]:<15}|', end='')
        print(f'{value[3]:>15}|', end='')
        print(f'{value[4]:>10.2f}|', end='')

    print() # end='\n'
print('-'*92)
print()