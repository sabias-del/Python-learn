# 'ab' - сокращение от 'a'ddress'b'ook

ad = {
    'Sparow': "sparow@gmail.com",
    "Jesika": "jesika@gmail.com",
    "Mak": "makk@gmail.com",
    "Spammer": "spamer@hotmail.com"
}
print("Адрес Sparow'a:", ad['Sparow'])

del ad["Spammer"]
print('\nВ адресной книге {0} контакта\n'.format(len(ad)))

for name, address in ad.items():
    print('Контакт {0} с адресом {1}'.format(name, address))

ad['Gudio'] = "guido@gmail.com"
if 'Guidio' in ad:
    print("\nАндрес Gudio:", ad['Gudio'])
