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

wiederholung = 0
while wiederholung < len(orte):
    ort = orte[wiederholung]

    if wohnort == ort:
        print("Ich wohne in " + ort)
    else:
        print("Ich wohne nicht in " + ort)
