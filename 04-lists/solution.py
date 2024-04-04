# Erweitert:
orte = [
    "Bern",
    "Zürich",
    "Basel",
    "Luzern",
    "Aarberg",
    "St. Gallen",
    "Genf",
    "Lausanne",
    "Winterthur",
    "Lugano",
]
wohnort = "Aarberg"

i = 0
while i < len(orte):
    ort = orte[i]

    if wohnort == ort:
        print("------------------")
        print("Ich wohne in " + ort)
        print("------------------")
    else:
        print("Ich wohne nicht in " + ort)
