liga_mx_teams = [
    'Club América',
    'Atlas F. C.',
    'Atlético de San Luis',
    'C. D. Cruz Azul',
    'C. D. Guadalajara',
    'Club León',
    'F. C. Juárez',
    'Mazatlán F. C.',
    'C. F. Monterrey',
    'Club Necaxa',
    'C. F. Pachuca',
    'Club Puebla',
    'Querétaro F. C.',
    'Santos Laguna',
    'Tigres de la UANL',
    'Club Tijuana',
    'Deportivo Toluca F. C.',
    'Universidad Nacional'
]
print(len(liga_mx_teams))
print(liga_mx_teams[3])
print(liga_mx_teams[-2].lower())
print(f"{liga_mx_teams[3]} was born great.")
# liga_mx_teams[-3] = 'Xolos'
# print(liga_mx_teams)
# liga_mx_teams.append('Gambeta FC')
# print(liga_mx_teams)
# liga_mx_teams.insert(0, 'real Madrid')
# print(liga_mx_teams)
# del liga_mx_teams[0]
# print(liga_mx_teams)
# del liga_mx_teams[-1]
popped_liga_mx_team = liga_mx_teams.pop()
print(popped_liga_mx_team)
print(liga_mx_teams)
print(len(liga_mx_teams))
liga_mx_teams.append(popped_liga_mx_team)
print(liga_mx_teams)
print(len(liga_mx_teams))
# too_good = 'C. D. Cruz Azul'
# liga_mx_teams.remove(too_good)
# print(liga_mx_teams)
print("\nHere's the sorted list)


