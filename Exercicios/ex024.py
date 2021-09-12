# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "Santo"
city = str(input('Em que cidade você nasceu? ')).strip()
print(city[:5].lower() == 'santo')