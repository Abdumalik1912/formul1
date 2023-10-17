from championship import Championship


tournament = Championship()

tournament.create_driver("Lewis Hamilton")
tournament.create_driver("Michael Schumacher")
tournament.create_driver("Sebastian Vettel")
tournament.create_driver("Ali Valiyev")

for d in tournament.get_drivers():
    print(d.get_name)

print()
dr = tournament.get_driver("Lewis Hamilton")
if dr != -1.0:
    print(dr.get_name)

print(tournament.define_grand_pri("55th annual grand pri tournament"))
print(tournament.define_grand_pri("Mayor's Special Grand Pri Tournament"))

print(tournament.get_grand_pri("Mayor's Special Grand Pri Tournament"))
print(tournament.get_grand_pri("Formula-1"))
