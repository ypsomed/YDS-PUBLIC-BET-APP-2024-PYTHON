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

for ort in orte:
    if wohnort == ort:
        print("------------------")
        print("Ich wohne in " + ort)
        print("------------------")
    else:
        print("Ich wohne nicht in " + ort)
