rios = {'nilo': 'Egito', 'amazonas': 'brasil', 'reno': 'holanda'}
print()
for r, p in rios.items():
    print(f'O rio {r.title()} atravessa {p.title()}!')
print()
for rio in rios.keys():
    print(f'Rio {rio.title()}')
print()
for pais in rios.values():
    print(pais.title())