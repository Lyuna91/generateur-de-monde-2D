import random

# Liste de 100 préfixes
prefixes = [
    "Al", "Bel", "Car", "Dor", "El", "Fal", "Gar", "Hor", "Ith", "Jer", "Kor", "Lir", "Mor", "Nor", "Or",
    "Pal", "Quor", "Ran", "Sel", "Tor", "Ul", "Vor", "Xan", "Yar", "Zor", "Ald", "Ber", "Cal", "Dur", "End",
    "Fur", "Gal", "Har", "Ill", "Jon", "Kel", "Lin", "Mal", "Nem", "Oth", "Per", "Quen", "Ral", "Sim", "Tal",
    "Un", "Vur", "Wen", "Xor", "Yer", "Zun", "As", "Bor", "Cer", "Del", "Eld", "Fer", "Gil", "Hal", "Ith",
    "Jan", "Kam", "Lor", "Mil", "Nir", "Olar", "Pel", "Qual", "Ril", "Sul", "Tar", "Ur", "Ven", "Wal", "Xal",
    "Yil", "Zir", "Ant", "Bar", "Cen", "Dol", "Em", "Fen", "Gir", "Hum", "Is", "Jal", "Kal", "Lan", "Med",
    "Nar", "Ol", "Par", "Quon", "Ris", "Sond", "Thal"
]

# Liste de 100 syllabes intermédiaires
middles = [
    "an", "el", "on", "ir", "ul", "or", "ur", "in", "al", "un", "er", "ol", "en", "ir", "as", "il", "or", "is",
    "ar", "il", "as", "om", "et", "ul", "id", "em", "os", "er", "as", "ur", "od", "al", "er", "ir", "um", "en",
    "in", "il", "or", "et", "in", "al", "un", "om", "at", "ur", "es", "ir", "on", "ar", "an", "al", "or", "ar",
    "is", "am", "el", "al", "os", "en", "ir", "om", "ul", "il", "am", "er", "ul", "ur", "om", "as", "in", "ir",
    "an", "et", "ul", "al", "es", "om", "ir", "as", "er", "um", "al", "on", "in", "an", "el", "ul", "in", "as",
    "er", "am", "om", "et", "an", "ar", "il", "on", "ar", "il", "as", "om"
]

# Liste de 100 suffixes
suffixes = [
    "ia", "ara", "on", "ar", "us", "tan", "lan", "den", "dor", "lia", "via", "mar", "ton", "ra", "na", "ca",
    "ri", "da", "lia", "lor", "kar", "thia", "gon", "nor", "pol", "min", "sha", "via", "mon", "gar", "nia",
    "dor", "nia", "tan", "bel", "ora", "ram", "zar", "tal", "din", "nia", "mar", "sha", "dia", "ran", "vor",
    "ton", "ir", "sia", "los", "per", "lum", "lar", "tor", "dan", "zar", "sar", "nia", "ron", "ton", "gar",
    "lia", "dal", "mor", "son", "tur", "na", "lir", "nia", "dor", "ron", "zon", "nar", "la", "pha", "bir",
    "gar", "nia", "tor", "mia", "dar", "ron", "nia", "mar", "sa", "dar", "tir", "lor", "zar", "nar", "ion",
    "tar", "bar", "sol", "lon", "mir", "tor", "tin"
]

# Liste des titres de pays
country_titles = [
    "Royaume de", "Principauté de", "République de", "Confédération de", "Union de", "Empire de"
]

# Fonction de génération de noms de pays
def generate_country_name():
    title = random.choice(country_titles)
    name = random.choice(prefixes) + random.choice(middles) + random.choice(suffixes)
    return f"{title} {name}"

# Générer quelques exemples de noms de pays
for _ in range(10):
    print(generate_country_name())
