from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokeymon Name", ["Combee", "Roserade", "Ledyba", "Ledian"])
table.add_column("Pokeymon Type", ["Flying", "Poison", "Flying", "Ledian"])
table.align = "l"

print(table)

