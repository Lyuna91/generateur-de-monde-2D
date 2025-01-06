import random

# Liste de 100 préfixes
prefixes = [
    "Bel", "San", "Port", "New", "Saint", "Mont", "Fort", "Wood", "Brook", "Lake", "Green", "Nor", "East", "West",
    "South", "North", "Oak", "El", "River", "Ash", "Burn", "Low", "Gold", "Silver", "Red", "Blue", "Iron", "High",
    "Holly", "Hill", "Fair", "Rock", "Wind", "Gran", "White", "Black", "Clif", "Wood", "Sky", "Moor", "Rain", "Sun",
    "Bright", "Crest", "Rose", "Thorn", "Fern", "Snow", "Salt", "Clear", "Deep", "Shadow", "Star", "Pine", "Fox",
    "Wolf", "Bear", "Lion", "Eagle", "Hawk", "Tide", "Sage", "King", "Spring", "Peak", "Val", "Gold", "Maple",
    "Cherry", "Vine", "Elm", "Bluff", "Crow", "Briar", "Green", "Flat", "Meadow", "Oak", "Wild", "Cross", "Sun",
    "Stone", "Shade", "Dawn", "Swift", "Field", "River", "Elder", "Moss", "Birch", "Dark", "Lark", "Fox", "Horn",
    "Ash", "Storm"
]

# Liste de 100 syllabes intermédiaires
middles = [
    "ford", "ham", "ston", "wich", "ing", "ley", "ton", "bury", "wood", "field", "well", "shire", "port", "haven",
    "water", "view", "brook", "land", "mill", "park", "wood", "cliff", "vale", "more", "stead", "stone", "crest",
    "pine", "ford", "bridge", "creek", "ridge", "shore", "hall", "moor", "hill", "grove", "bourne", "hollow",
    "ridge", "haven", "field", "meadow", "pond", "ford", "oak", "cross", "gate", "end", "side", "fall", "wood",
    "cove", "light", "mouth", "rock", "wall", "pine", "vale", "lake", "berry", "fort", "ridge", "village",
    "worth", "edge", "bridge", "shore", "glen", "dale", "end", "port", "moor", "hill", "cape", "stone", "valley",
    "mark", "path", "vail", "grove", "hill", "mouth", "bank", "ford", "moor", "rose", "lynn", "dell", "run", "more"
]

# Liste de 100 suffixes
suffixes = [
    "ville", "ton", "burg", "berg", "worth", "stead", "view", "stone", "field", "port", "shore", "water", "wood",
    "ford", "wood", "shire", "wick", "well", "hill", "crest", "dale", "rock", "fall", "mark", "brook", "haven",
    "mouth", "cove", "grove", "brook", "bank", "ridge", "ford", "cape", "val", "stone", "town", "mont", "wood",
    "wall", "dale", "ford", "burn", "hall", "field", "gate", "mount", "ridge", "pool", "mill", "side", "port",
    "land", "pond", "mead", "hill", "fort", "view", "mount", "shire", "cross", "way", "more", "lea", "valley",
    "vale", "mere", "house", "run", "side", "hollow", "den", "park", "ridge", "bury", "point", "field", "well",
    "wood", "stone", "green", "ford", "moore", "holm", "worth", "mill", "field", "worth", "mark", "worth", "light"
]

# Liste des introductions (optionnelles)
introductions = [
    "", "Ville de", "Commune de", "Municipalité de", "Cité de", "", "Fort de", "Nouveau", "Vieux"
]



