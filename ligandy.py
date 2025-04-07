from traceback import print_tb

oxidacnicisla = {
    "ičit": 4,
    "ičel":8,
    "nat":2,
    "ist":7,
    "ičn":5,
    "ečn":5,
    "ov":6,
    "it":3,
    "n":1
}
indexy = ['₀', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉']
tabulka = {
    "vod": "H", "hel": "He", "lit": "Li", "ber": "Be", "bor": "B", "uhl": "C", "dus": "N", "kys": "O", "flu": "F", "neo": "Ne", "sod": "Na", "hoř": "Mg", "hli": "Al", "kře": "Si", "fos": "P", "sír": "S", "cho": "Cl", "arg": "Ar", "dra": "K", "váp": "Ca", "ska": "Sc", "tit": "Ti", "van": "V", "chr": "Cr", "má": "Mn", "žel": "Fe", "kob": "Co", "nik": "Ni", "měď": "Cu", "zin": "Zn", "gal": "Ga", "ger": "Ge", "ars": "As", "sel": "Se", "bro": "Br", "kry": "Kr", "rub": "Rb", "str": "Sr", "ytt": "Y", "zir": "Zr", "nio": "Nb", "mol": "Mo", "tec": "Tc", "rho": "Rh", "pal": "Pd", "stř": "Ag", "kad": "Cd", "ind": "In", "cín": "Sn", "ant": "Sb", "tel": "Te", "jód": "I", "xen": "Xe", "ces": "Cs", "bar": "Ba", "lan": "La", "cer": "Ce", "pra": "Pr", "pro": "Pm", "sam": "Sm", "eur": "Eu", "gad": "Gd", "ter": "Tb", "dys": "Dy", "hol": "Ho", "erb": "Er", "thu": "Tm", "lut": "Lu", "haf": "Hf", "tan": "Ta", "wol": "W", "rhe": "Re", "osm": "Os", "iri": "Ir", "pla": "Pt", "zla": "Au", "rtu": "Hg", "tha": "Tl", "olo": "Pb", "bis": "Bi", "pol": "Po", "ast": "At", "rado": "Rn", "fra": "Fr", "rad": "Ra", "act": "Ac", "tho": "Th", "prot": "Pa", "urá": "U", "nep": "Np", "plu": "Pu", "ame": "Am", "cur": "Cm", "berk": "Bk", "cal": "Cf", "ein": "Es", "fer": "Fm", "men": "Md", "nob": "No", "law": "Lr", "rut": "Rf", "dub": "Db", "sea": "Sg", "boh": "Bh", "has": "Hs", "mei": "Mt", "dar": "Ds", "roe": "Rg", "cop": "Cn", "nih": "Nh", "fle": "Fl", "mos": "Mc", "liv": "Lv", "ten": "Ts", "oga": "Og"
} #compromised tabulka
ciselne_predpony = {
# "mono":1,
"di":2,
"tri":3,
"tetra":4,
"penta":5,
"hexa":6,
"hepta":7,
"okta":8,
"nona":9,
"deka":10,
"undeka":11,
"dodeka":12,
'trideka':13,
'tetradeka':14,
'pentadeka':15,
'hexadeka':16,
}
ligandy = {
'fluorido':'F',
'chlorido':'Cl',
'bromido':'Br',
'jodido':'I',
'hydroxido':'OH',
'kyanido':'CN',
'rhodanido':'SCN',
'peroxido':'O₂',
'aqua':'H₂O',
'ammin':'NH₃',
'karbonyl':'CO',
'nitrosyl':'NO',
'oxido':'O',
'thio':'S',
'sulfato':'SO₄',
'nitrato':'NO₃',
'hydrido':'H',
'nitro':'NO₂',
'hydroperoxo':'O₂H',
'imido':'NH',
'nitrito':'ONO',
'fosfato':'PO₄',
'amido':'NH₂',
'sulfito':'SO₃',
'karbonato':'CO₃',
}
# for key, value in ligandy.items():
#     print(f"'{key.lower()}':'{value}',")
# for item in ligandy.keys():
#     x = item
#     for i in range(10):
#         item = item.replace(str(i), indexy[i])
#     print(f"'{item}':'{ligandy[x]}',")


####################
def jakyprvek(prvek):
    try:
        return tabulka[prvek[:3]]
    except KeyError:
        return tabulka[prvek[:3]]

molekula_nazev = "dikyanidostříbrnan sodný" #(str(input('Tvoje molekula? '))).lower()
# koncovka = 'ý'
# print(jakyprvek(molekula_nazev.split(' ')[-1]))
ligand_nazev = molekula_nazev.split(' ')[0]
ligand_vzorec = str()
for key in ciselne_predpony.keys():
    if ligand_nazev.startswith(key):
        ligand_vzorec += str(ciselne_predpony[key])
        ligand_nazev = ligand_nazev[len(key):]

for key in ligandy.keys():
    if ligand_nazev.startswith(key):
        if ligand_vzorec and ligand_vzorec[-1].isdigit():
            ligand_vzorec += f"({str(ligandy[key])})"
        else:
            ligand_vzorec += str(ligandy[key])
        ligand_nazev = ligand_nazev[len(key):]


koncovka = "an"
for key in oxidacnicisla.keys():
    if ligand_nazev.endswith(key + koncovka):
        print(oxidacnicisla[key])


ligand_vzorec = f"{jakyprvek(molekula_nazev.split(' ')[-1])}[{jakyprvek(ligand_nazev) + ligand_vzorec}]"
# print(jakyprvek(ligand_nazev))
#
# print(ligand_nazev)
print(ligand_vzorec)

