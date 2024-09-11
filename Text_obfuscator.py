import random

# Same dictionaries as before
identical_group_replacements = {
    "**": ["ᕯ", "★", "✪"],
    "!!": ["‼", "❗"],
    "!?": ["⁉", "‽"],
    "??": ["⁇", "❓"],
    "?!": ["⁈", "⁉"],
    "...": ["…", "⋯"],
    " ": ["     ", " ", " "],

    "DZ": ["Ǳ", "Ꜩ"],
    "Dz": ["ǲ", "ǅ"],
    "LJ": ["Ǉ", "Љ"],
    "Lj": ["ǈ", "Љ"],
    "NJ": ["Ǌ", "Њ"],
    "Nj": ["ǋ", "Њ"],

    "dz": ["ǳ", "ʣ"],
    "lj": ["ǉ", "љ"],
    "nj": ["ǌ", "њ"]
}

approximate_group_replacements = {
    "II": ["Ⅱ", "IІ"],
    "III": ["Ⅲ", "III"],
    "IV": ["Ⅳ", "IV"],
    "VI": ["Ⅵ", "VI"],
    "VII": ["Ⅶ", "VII"],
    "VIII": ["Ⅷ", "VIII"],
    "IX": ["Ⅸ", "IX"],
    "XI": ["Ⅺ", "XI"],
    "XII": ["Ⅻ", "XII"],

    "ii": ["ⅱ", "ii"],
    "iii": ["ⅲ", "iii"],
    "iv": ["ⅳ", "iv"],
    "vi": ["ⅵ", "vi"],
    "vii": ["ⅶ", "vii"],
    "viii": ["ⅷ", "viii"],
    "ix": ["ⅸ", "ix"],
    "xi": ["ⅺ", "xi"],
    "xii": ["ⅻ", "xii"],

    "IJ": ["Ĳ", "IJ"],

    "ae": ["æӕ", "æ"],
    "bl": ["Ы", "bl"],
    "dz": ["ʣ", "dz"],
    "ij": ["ĳ", "ij"],
    "lm": ["㏐", "lm"],
    "ln": ["㏑", "ln"],
    "log": ["㏒", "log"],
    "ls": ["ʪ", "ls"],
    "lx": ["㏓", "lx"],
    "lz": ["ʫ", "lz"],
    "mb": ["㏔", "mb"],
    "mil": ["㏕", "mil"],
    "mol": ["㏖", "mol"],
    "Oy": ["Ѹ", "Oy"],
    "oy": ["ѹ", "oy"],
    "ts": ["ʦ", "ts"]
}

identical_replacements = {
    "`": ["՝", "`"],
    ",": ["͵", ","],
    ":": ["։", ":"],
    ";": [";", ";"],
    "|": ["ǀ", "|"],
    "/": ["⁄", "⧸"],
    "\\": ["⧵", "⧹"],
    "-": ["‐", "–"],
    "+": ["𖫵", "+"],
    "<": ["ᐸ", "𖫬", "ⵦ"],
    ">": ["ᐳ", ">"],
    "3": ["З", "3"],
    "6": ["Ꮾ", "6"],
    "Æ": ["Ӕ", "Æ"],
    "a": ["а", "a"],
    "e": ["е", "e"],
    "o": ["о", "o"],
    "i": ["і", "i"],
    "p": ["р", "p"],
    "s": ["ѕ", "s"],
    "t": ["т", "t"],
    "u": ["у", "u"],
    "x": ["х", "x"],
    "y": ["у", "y"],
    "z": ["ꮓ", "z"]
}

approximate_replacements = {
    "3": ["Ӡ", "3"],
    "5": ["Ƽ", "5"],
    "6": ["б", "6"],
    "A": ["ᗅ", "A"],
    "B": ["ᗷ", "B"],
    "C": ["Ꮯ", "C"],
    "D": ["Ⅾ", "D"],
    "I": ["Ⅰ", "I"],
    "O": ["ⵔ", "O"],
    "P": ["ꓑ", "P"],
    "R": ["Ꭱ", "R"],
    "S": ["ꓢ", "S"],
    "T": ["ㄒ", "T"],
    "V": ["ᐯ", "V"],
    "W": ["Ꮤ", "W"],
    "X": ["χ", "X"],
    "g": ["ɡ", "g"],
    "k": ["к", "k"],
    "m": ["ⅿ", "m"],
    "p": ["ρ", "p"],
    "s": ["տ", "s"],
    "u": ["υ", "u"],
    "x": ["ⅹ", "x"]
}


def replace_group(text, replacements):
    for group, candidates in replacements.items():
        if random.randint(1, 10) <= 6:  # 60% chance of replacing
            text = text.replace(group, random.choice(candidates))
    return text


def obfuscate_text(input_text, use_approximate=False):
    # Step 1: Replace groups from identicalGroupReplacements
    input_text = replace_group(input_text, identical_group_replacements)

    if use_approximate:
        # Step 2: Replace groups from approximateGroupReplacements if enabled
        input_text = replace_group(input_text, approximate_group_replacements)

    output_text = ""

    # Step 3: Replace individual characters from identicalReplacements and approximateReplacements
    for char in input_text:
        candidates = identical_replacements.get(char, [char])  # Use original char if no replacement

        if use_approximate:
            candidates += approximate_replacements.get(char, [])

        # Randomly choose a replacement character if possible
        if random.randint(1, 10) <= 6:  # 60% chance of obfuscating a character
            output_text += random.choice(candidates)
        else:
            output_text += char

    return output_text


def obfuscate_file(input_file, output_file, use_approximate=False):
    # Read the input sentences from the file
    with open(input_file, 'r', encoding='utf-8') as infile:
        sentences = infile.readlines()

    # Open the output file to write obfuscated sentences using UTF-8 encoding
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for sentence in sentences:
            obfuscated_sentence = obfuscate_text(sentence.strip(), use_approximate)
            outfile.write(obfuscated_sentence + '\n')

# Example usage
input_file = 'word_list.txt'  # Your file with 100 different sentences
output_file = 'obfuscated_output.txt'  # Output file for obfuscated sentences

# Obfuscate the sentences and save them to a new file
obfuscate_file(input_file, output_file, use_approximate=True)

print(f"Obfuscated sentences saved to {output_file}.")

