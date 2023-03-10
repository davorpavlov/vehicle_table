import os

os.system('cls')
vehicles = [
    {"ID": 1, "Tip": "Kamion", "Proizvođač": "Iveco", "Registarska oznaka": "OS 001 ZZ", "Godina prve registracije": 2015, "Cijena u EUR": 45000},
    {"ID": 2, "Tip": "Kamion", "Proizvođač": "Iveco", "Registarska oznaka": "OS 002 ZZ", "Godina prve registracije": 2015, "Cijena u EUR": 47000},
    {"ID": 3, "Tip": "Tegljač", "Proizvođač": "MAN", "Registarska oznaka": "RI 001 ZZ", "Godina prve registracije": 2018, "Cijena u EUR": 78000},
    {"ID": 4, "Tip": "Tegljač", "Proizvođač": "MAN", "Registarska oznaka": "RI 002 ZZ", "Godina prve registracije": 2020, "Cijena u EUR": 97000},
    {"ID": 5, "Tip": "Kombi", "Proizvođač": "Mercedes Benz", "Registarska oznaka": "ST 001 ZZ", "Godina prve registracije": 2013, "Cijena u EUR": 12000},
    {"ID": 6, "Tip": "Kombi", "Proizvođač": "Volkswagen", "Registarska oznaka": "ST 002 ZZ", "Godina prve registracije": 2021, "Cijena u EUR": 35000},    
    {"ID": 7, "Tip": "Dostavno vozilo", "Proizvođač": "Volkswagen", "Registarska oznaka": "ZG 001 ZZ", "Godina prve registracije": 2010, "Cijena u EUR": 9000},    
    {"ID": 8, "Tip": "Dostavno vozilo", "Proizvođač": "Volkswagen", "Registarska oznaka": "ZG 002 ZZ", "Godina prve registracije": 2010, "Cijena u EUR": 9300}
]

print("ID  | Tip             | Proizvođač      | Registarska oznaka  | Godina prve registracije | Cijena u EUR")
print("-------------------------------------------------------------------------------------------------------")

for vehicle in vehicles:
    print(f"{vehicle['ID']:2}  | {vehicle['Tip']:15} | {vehicle['Proizvođač']:15} | {vehicle['Registarska oznaka']:19} | {vehicle['Godina prve registracije']:24} | {vehicle['Cijena u EUR']:9}")

