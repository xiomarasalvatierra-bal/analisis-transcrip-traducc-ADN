# Análisis de Secuencias Genéticas en Python

**Algoritmo básico en Python para analizar secuencias de ADN, transcribir a ARN, traducir codones y detectar mutaciones.**

---

## Descripción

Este proyecto implementa un pipeline básico de bioinformática que permite:

- Analizar secuencias de ADN.
- Transcribir ADN a ARN.
- Traducir codones a proteínas.
- Reconocer mutaciones comparando secuencias de referencia y secuencias de prueba.

Es ideal para aprender cómo funcionan los procesos fundamentales de la biología molecular en un contexto computacional.

---

## Funcionalidades

- `analisis_adn(adn)` – valida y procesa la secuencia de ADN.  
- `transcripcion_adn(adn)` – convierte ADN a ARN.  
- `traducir_codones(arn)` – genera la cadena de proteínas correspondiente.  
- `detectar_mutaciones(ref, muestra)` – compara secuencias y reporta diferencias.
