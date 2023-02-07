from prettytable import PrettyTable

# table = PrettyTable()

# table.field_names = ["Pokemon Name", "Type", "Population", "Annual Rainfall"]
# table.add_rows(
#     [
#         ["Adelaide", 1295, 1158259, 600.5],
#         ["Brisbane", 5905, 1857594, 1146.4],
#         ["Darwin", 112, 120900, 1714.7],
#         ["Hobart", 1357, 205556, 619.5],
#         ["Sydney", 2058, 4336374, 1214.8],
#         ["Melbourne", 1566, 3806092, 646.9],
#         ["Perth", 5386, 1554769, 869.4],
#     ]
# )
# print(table)

pokemon_table = PrettyTable()

pokemon_table.field_names = ['Pokemon Name', "Type"]
pokemon_table.add_rows(
    [
        ['Pikachu', 'Electric'], 
        ['Charmandar', 'Fire'], 
        ['Chikorita', 'Grass']
    ]
)
pokemon_table.align = 'l'
print(pokemon_table)