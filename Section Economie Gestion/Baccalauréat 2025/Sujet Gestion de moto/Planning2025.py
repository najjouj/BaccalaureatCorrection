from pandas import *
plan = read_csv("Planning.csv",sep=";")
#print(plan)
#b
print(plan.columns)
#c
#print(plan [["NomPrenApp","Immat","Cylindre"]].groupby("DateSeance"))
print(plan.groupby("DateSeance").sum())
#d
print(plan[plan["NomPrenApp"]=="Mondher SOUSSI"]["DateSeance"].count())
#e
plan["PrixSeance"] = (plan["HeureFin"] - plan["HeureDebut"]) * 30
#print(plan)
plan_tri=plan.sort_values(by=["NomPrenMon"],ascending=[True])
print(plan_tri)
