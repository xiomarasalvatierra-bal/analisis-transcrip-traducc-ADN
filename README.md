# Genetic Sequence Analysis in Python

**Basic Python algorithm to analyze DNA sequences, transcribe them into RNA, translate codons, and detect mutations.**

---

## Description

This project implements a basic bioinformatics pipeline that allows:

- Analysis of DNA sequences
- DNA to RNA transcription
- Codon-to-protein translation
- Mutation detection by comparing reference and sample sequences

It is designed as an educational project to understand how fundamental molecular biology processes can be implemented in a computational context.

---

## Features

- `analisis_adn(adn)` – validates and processes a DNA sequence  
- `transcripcion_adn(adn)` – converts DNA into RNA  
- `traducir_codones(arn)` – generates the corresponding protein sequence  
- `detectar_mutaciones(ref, muestra)` – compares sequences and reports mutations

---

## Technologies Used

- Python

---

## Learning Objectives

- Understand the computational representation of DNA sequences
- Implement basic bioinformatics concepts using Python
- Practice string manipulation and algorithmic thinking applied to biology

---

## New Features

* Automatic classification of mutations into:

  * Silent
  * Missense
  * Nonsense
* Evaluation of the potential impact on the protein
* Provides an estimation of the biological impact of each mutation on the resulting protein, enabling deeper insights into genetic data.
