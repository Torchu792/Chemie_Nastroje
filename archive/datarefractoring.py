import sqlite3, os

#TODO - assign datatypes if necesarry, the data needs to be refractored as its not justr intereger theres also some text form
#TODO - clean data

# try:
#     os.remove("prvky.db")
# except:
#     pass
conn = sqlite3.connect('../py_programs/prvky.db')
c = conn.cursor()
# c.execute("""CREATE TABLE prvky (
#             protonove_cislo integer,
#             symbol text,
#             latinsky_nzv text,
#             anglicky_nzv text,
#             cesky_nzv text,
#             skupina,
#             perioda,
#             blok text,
#             ar_hmotnost,
#             density,
#             melting_point,
#             boiling_point,
#             specific_heat_capacity,
#             elektronegativita,
#             abundance_in_earth_crust,
#             origin text,
#             phase_roomtempeture,
#             rok_objevu
#             )""")
# conn.commit()


with open("prvky.txt", "r", encoding="utf-8") as fileen:
    with open("prvkycz.txt", "r", encoding="utf-8") as filecz:
        for linecz, lineen in zip(filecz, fileen):
            joined_line = (lineen.strip() + "	" + linecz.strip()).split("	")
            try:
                c.execute("""INSERT INTO prvky VALUES (
                        :protonove_cislo,
                        :symbol,
                        :latinsky_nzv,
                        :anglicky_nzv,
                        :cesky_nzv,
                        :skupina,
                        :perioda,
                        :blok,
                        :ar_hmotnost,
                        :density,
                        :melting_point,
                        :boiling_point,
                        :specific_heat_capacity,
                        :elektronegativita,
                        :abundance_in_earth_crust,
                        :origin,
                        :phase_roomtempeture,
                        :rok_objevu
                        )""",
                          {
                          'protonove_cislo': joined_line[0],
                          'symbol': joined_line[1],
                          'latinsky_nzv': joined_line[17],
                          'anglicky_nzv': joined_line[2],
                          'cesky_nzv': joined_line[16],
                          'skupina': joined_line[4],
                          'perioda': joined_line[5],
                          'blok': joined_line[6],
                          'ar_hmotnost': joined_line[20],
                          'density': joined_line[8],
                          'melting_point': joined_line[9],
                          'boiling_point': joined_line[10],
                          'specific_heat_capacity': joined_line[11],
                          'elektronegativita': joined_line[12],
                          'abundance_in_earth_crust': joined_line[13],
                          'origin': joined_line[14],
                          'phase_roomtempeture': joined_line[15],
                          'rok_objevu': joined_line[21]
                      })
            except IndexError as e:
                print(e, '; ' ,joined_line)
        conn.commit()
conn.close()
