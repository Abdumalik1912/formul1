from championship import Championship


tournament = Championship()

tournament.create_driver("Lewis Hamilton")
tournament.create_driver("Michael Schumacher")
tournament.create_driver("Sebastian Vettel")
tournament.create_driver("Alain Rost")

for d in tournament.get_drivers():
    print(d.get_name)

print()
dr = tournament.get_driver("Lewis Hamilton")
dr2 = tournament.get_driver("Michael Schumacher")
dr3 = tournament.get_driver("Sebastian Vettel")
if dr != -1.0:
    print(dr.get_name)

gp1 = tournament.define_grand_pri("55th annual grand pri tournament")
print(tournament.define_grand_pri("Mayor's Special Grand Pri Tournament"))

print(tournament.get_grand_pri("Mayor's Special Grand Pri Tournament"))
print(tournament.get_grand_pri("Formula-1"))

tournament.enter_driver(gp1, dr)
tournament.enter_driver(gp1, dr2)
tournament.enter_driver(gp1, dr3)

print(tournament.set_time(gp1, dr, 1, 0, 0, 0))
print(tournament.set_time(gp1, dr2, 0, 40, 0, 0))
print(tournament.set_time(gp1, dr3, 0, 20, 0, 0))

print(tournament.gp_ranking(gp1))
print(tournament.get_position(dr3, gp1))

print(tournament.get_championship_ranking())

