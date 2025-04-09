import json

rovnice = "Fe + O₂ ⟶ Fe₂O₃"

with open("prvky.json", "r", encoding="utf-8") as file:
    prvky = json.load(file)
oxidacni_cisla = {
    'O' : -2,
    'H' : -1,
    'F': -1,
    'Cl': -1,
    'Br' : -1,
    'I' : -1
}
prvky.txt
