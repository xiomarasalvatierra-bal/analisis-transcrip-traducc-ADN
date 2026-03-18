from dna_toolkit import dna_analysis, dna_transcription, translate_codons, detect_mutations

#---------------------GENERAL DNA ANALYSIS-----------------
while True:
    dna = input("Enter the DNA sequence: ").upper()

    if set(dna).issubset({"A", "C", "G", "T"}):
        break
    else:
        print("Error: Enter only A, C, G, or T.")

print("Accepted sequence:", dna)

#--------GC CONTENT---------
gc_content, a, c, t, g, dna_length = dna_analysis(dna)

print("DNA length:", dna_length)
print("A:", a)
print("C:", c)
print("T:", t)
print("G:", g)
print("GC Content:", gc_content)


#---------------------DNA TO RNA TRANSCRIPTION---------------------
rna = dna_transcription(dna)
print("DNA transcription:", rna)


#---------------------CODON TRANSLATION---------------------------
protein = translate_codons(rna)
print("Proteins:", protein)


#-------------------MUTATION DETECTION-----------------------

reference = dna
print("Reference sequence:", reference)

while True:
    sample = input("Enter the sequence to compare: ").upper()

    if not set(sample).issubset({"A", "C", "G", "T"}):
        print("Error: Enter only A, C, G, or T.")
        continue

    break

print("Sequence to compare:", sample)

mutations = detect_mutations(reference, sample)

print("Mutations:", mutations)
