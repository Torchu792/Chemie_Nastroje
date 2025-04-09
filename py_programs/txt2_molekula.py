dict_tabulka = {
    "vod": "H", "hel": "He", "lit": "Li", "ber": "Be", "bor": "B", "uhl": "C", "dus": "N", "kys": "O", "flu": "F", "neo": "Ne", "sod": "Na", "hoř": "Mg", "hli": "Al", "kře": "Si", "fos": "P", "sír": "S", "cho": "Cl", "arg": "Ar", "dra": "K", "váp": "Ca", "ska": "Sc", "tit": "Ti", "van": "V", "chr": "Cr", "má": "Mn", "žel": "Fe", "kob": "Co", "nik": "Ni", "měď": "Cu", "zin": "Zn", "gal": "Ga", "ger": "Ge", "ars": "As", "sel": "Se", "bro": "Br", "kry": "Kr", "rub": "Rb", "str": "Sr", "ytt": "Y", "zir": "Zr", "nio": "Nb", "mol": "Mo", "tec": "Tc", "rut": "Ru", "rho": "Rh", "pal": "Pd", "stř": "Ag", "kad": "Cd", "ind": "In", "cín": "Sn", "ant": "Sb", "tel": "Te", "jód": "I", "xen": "Xe", "ces": "Cs", "bar": "Ba", "lan": "La", "cer": "Ce", "pra": "Pr", "neo": "Nd", "pro": "Pm", "sam": "Sm", "eur": "Eu", "gad": "Gd", "ter": "Tb", "dys": "Dy", "hol": "Ho", "erb": "Er", "thu": "Tm", "ytt": "Yb", "lut": "Lu", "haf": "Hf", "tan": "Ta", "wol": "W", "rhe": "Re", "osm": "Os", "iri": "Ir", "pla": "Pt", "zla": "Au", "rtu": "Hg", "tha": "Tl", "olo": "Pb", "bis": "Bi", "pol": "Po", "ast": "At", "rad": "Rn", "fra": "Fr", "rad": "Ra", "act": "Ac", "tho": "Th", "pro": "Pa", "urá": "U", "nep": "Np", "plu": "Pu", "ame": "Am", "cur": "Cm", "ber": "Bk", "cal": "Cf", "ein": "Es", "fer": "Fm", "men": "Md", "nob": "No", "law": "Lr", "rut": "Rf", "dub": "Db", "sea": "Sg", "boh": "Bh", "has": "Hs", "mei": "Mt", "dar": "Ds", "roe": "Rg", "cop": "Cn", "nih": "Nh", "fle": "Fl", "mos": "Mc", "liv": "Lv", "ten": "Ts", "oga": "Og"
}
dict_idy = {
 'o': ['O', -2],
 's': ['S', -2],
 'h': ['H', -1],
 'b': ['Br', -1],
 'c': ['Cl', -1],
 'j': ['I', -1],
 'f': ['F', -1]
}
koncovka = 'ý'
dict_oxidacnicisla = {
    "ičit"+ koncovka: 4,
    "ičel"+ koncovka: 8,
    "nat"+ koncovka: 2,
    "ist"+ koncovka: 7,
    "ičn"+ koncovka: 5,
    "ečn"+ koncovka: 5,
    "ov"+ koncovka: 6,
    "it"+ koncovka: 3,
    "n"+ koncovka: 1
}




indexy = ['₀', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉']
gigavzorec = [[1, 2, 1],[4, 5, 1]]



molekula_nazev = (str(input('Tvoje molekula? '))).lower()
id_nazev, druhyprvek_nazev = molekula_nazev.split() 

def jakyprvek(prvek):

    try:
        return dict_tabulka[prvek[:3]]
    except KeyError:
        for klice in dict_tabulka:
            if prvek[:2] in klice:
                return dict_tabulka[klice]
def jakyoxcislo(prvek):
    for klice in dict_oxidacnicisla:     
        if prvek[-len(klice):] in klice:
            return dict_oxidacnicisla[klice]


gigavzorec[1][0] = jakyprvek(druhyprvek_nazev)
gigavzorec[1][1] = jakyoxcislo(druhyprvek_nazev)
        
gigavzorec[0][0] = dict_idy[id_nazev[0]][0]
gigavzorec[0][1] = dict_idy[id_nazev[0]][1]

print(gigavzorec)

xx = gigavzorec[0][1]  #0- nayev prvku 1-ox cislo 2-pocet
zz = gigavzorec[1][1]

while gigavzorec[0][1] + gigavzorec[1][1] != 0:
    if abs(gigavzorec[0][1]) < gigavzorec[1][1]:
        gigavzorec[0][1] += xx
        gigavzorec[0][2] += 1               
    if abs(gigavzorec[0][1]) > gigavzorec[1][1]:
        gigavzorec[1][1] += zz
        gigavzorec[1][2] += 1


# def rovnovahameziprvky(list)
#     CelkOxCislo = 1
#     while CelkOxCislo != 0:
#         for x in len(list):
#             list[CelkOxCislo][1]





if gigavzorec[1][2] == '₁':
    gigavzorec[1][2] = ''
if gigavzorec[0][2] == '₁':
    gigavzorec[0][2] = ''

print(''.join([gigavzorec[1][0], gigavzorec[1][2]]) + ''.join([gigavzorec[0][0], gigavzorec[0][2]]))
