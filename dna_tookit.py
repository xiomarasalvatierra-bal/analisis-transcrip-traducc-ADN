# --------------------- DNA ANALYSIS -----------------
def dna_analysis(dna):
    dna_length = len(dna)
    a = dna.count('A')
    c = dna.count('C')
    t = dna.count('T')
    g = dna.count('G')

    gc_content = ((g + c) / dna_length) * 100
    return gc_content, a, c, t, g, dna_length


# --------------------- DNA TO RNA -----------------
def dna_transcription(dna):
    return dna.replace('T', 'U')


# --------------------- CODON TABLE -----------------
codon_table = {
    "AUG": "Met",
    "UUU": "Phe", "UUC": "Phe",
    "UUA": "Leu", "UUG": "Leu", "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
    "AUU": "Ile", "AUC": "Ile", "AUA": "Ile",
    "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
    "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser", "AGU": "Ser", "AGC": "Ser",
    "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
    "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
    "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
    "UAU": "Tyr", "UAC": "Tyr",
    "CAU": "His", "CAC": "His",
    "CAA": "Gln", "CAG": "Gln",
    "AAU": "Asn", "AAC": "Asn",
    "AAA": "Lys", "AAG": "Lys",
    "GAU": "Asp", "GAC": "Asp",
    "GAA": "Glu", "GAG": "Glu",
    "UGU": "Cys", "UGC": "Cys",
    "UGG": "Trp",
    "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg", "AGA": "Arg", "AGG": "Arg",
    "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly",
    "UAA": "STOP", "UAG": "STOP", "UGA": "STOP"
}


# --------------------- TRANSLATE ONE CODON -----------------
def translate_codon(dna_codon):
    rna_codon = dna_transcription(dna_codon)
    return codon_table.get(rna_codon, "Unknown")


# --------------------- CLASSIFY SUBSTITUTION -----------------
def classify_substitution(codon_ref, codon_mut):
    aa_ref = translate_codon(codon_ref)
    aa_mut = translate_codon(codon_mut)

    if aa_ref == aa_mut:
        return "silent", aa_ref, aa_mut
    elif aa_mut == "STOP":
        return "nonsense", aa_ref, aa_mut
    else:
        return "missense", aa_ref, aa_mut


# --------------------- DETECT POINT MUTATIONS -----------------
def detect_point_mutations(reference, sample):

    if len(reference) != len(sample):
        return "Sequences must have the same length (not a substitution)"

    if len(reference) % 3 != 0:
        return "Sequence length must be multiple of 3"

    mutations = []

    for i in range(0, len(reference), 3):
        codon_ref = reference[i:i+3]
        codon_mut = sample[i:i+3]

        if codon_ref != codon_mut:
            mutation_type, aa_ref, aa_mut = classify_substitution(codon_ref, codon_mut)

            mutations.append({
                "codon_position": i//3 + 1,
                "codon_ref": codon_ref,
                "codon_mut": codon_mut,
                "aa_ref": aa_ref,
                "aa_mut": aa_mut,
                "type": mutation_type
            })

    return mutations
