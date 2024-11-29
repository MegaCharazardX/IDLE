from prettytable import PrettyTable
table = PrettyTable()
table.add_row(["Hari", "Dhejus"])
table.add_row([17, 20])
table.border = False
table.header = False
print(table)