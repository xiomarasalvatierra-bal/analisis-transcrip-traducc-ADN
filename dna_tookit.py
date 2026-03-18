#---------------------GENERAL DNA ANALYSIS-----------------
def dna_analysis(dna):

    dna_length = len(dna)

    a = dna.count('A')
    c = dna.count('C')
    t = dna.count('T')
    g = dna.count('G')

    gc_content = ((g + c) / dna_length) * 100

    return gc_content, a, c, t, g, dna_length


#---------------------DNA TO RNA TRANSCRIPTION---------------------
def dna_transcription(dna):

    rna = dna.replace('T', 'U')

    return rna


#---------------------CODON TRANSLATION---------------------------
def translate_codons(rna):

    codon_table = {

        "AUG": "Methionine",

        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",

        "UUA": "Leucine",
        "UUG": "Leucine",

        "CUU": "Leucine",
        "CUC": "Leucine",
        "CUA": "Leucine",
        "CUG": "Leucine",

        "AUU": "Isoleucine",
        "AUC": "Isoleucine",
        "AUA": "Isoleucine",

        "GUU": "Valine",
        "GUC": "Valine",
        "GUA": "Valine",
        "GUG": "Valine",

        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",

        "CCU": "Proline",
        "CCC": "Proline",
        "CCA": "Proline",
        "CCG": "Proline",

        "ACU": "Threonine",
        "ACC": "Threonine",
        "ACA": "Threonine",
        "ACG": "Threonine",

        "GCU": "Alanine",
        "GCC": "Alanine",
        "GCA": "Alanine",
        "GCG": "Alanine",

        "UAU": "Tyrosine",
        "UAC": "Tyrosine",

        "CAU": "Histidine",
        "CAC": "Histidine",

        "CAA": "Glutamine",
        "CAG": "Glutamine",

        "AAU": "Asparagine",
        "AAC": "Asparagine",

        "AAA": "Lysine",
        "AAG": "Lysine",

        "GAU": "Aspartic Acid",
        "GAC": "Aspartic Acid",

        "GAA": "Glutamic Acid",
        "GAG": "Glutamic Acid",

        "UGU": "Cysteine",
        "UGC": "Cysteine",

        "UGG": "Tryptophan",

        "CGU": "Arginine",
        "CGC": "Arginine",
        "CGA": "Arginine",
        "CGG": "Arginine",

        "AGU": "Serine",
        "AGC": "Serine",

        "AGA": "Arginine",
        "AGG": "Arginine",

        "GGU": "Glycine",
        "GGC": "Glycine",
        "GGA": "Glycine",
        "GGG": "Glycine",

        "UAA": "STOP",
        "UAG": "STOP",
        "UGA": "STOP"
    }

    proteins = []

    for i in range(0, len(rna), 3):

        codon = rna[i:i+3]      # read every 3 bases
        amino_acid = codon_table.get(codon, "Unknown")

        if amino_acid == "STOP":
            break

        proteins.append(amino_acid)

    return proteins


#-------------------MUTATION DETECTION-----------------------
def detect_mutations(reference, sample):
    mutations = []

    for i in range(len(reference)):
        if reference[i] != sample[i]:
            mutations.append((i + 1, reference[i], sample[i]))

    return mutations
