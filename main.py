from dna_tookit import analisis_adn, transcripcion_adn, traducir_codones, detectar_mutaciones

#---------------------ANÁLISIS GENERAL DEL ADN-----------------
adn = input("Ingrese la secuencia ADN: ").upper()

contenido_gc, a, c, t, g, tamanio_adn = analisis_adn(adn)

print("Tamaño del ADN: ", tamanio_adn)
print("A: ", a)
print("C: ", c)
print("T: ", t)
print("G: ", g)
print("Contenido de GC: ", contenido_gc)


#---------------------TRANSCRIPCIÓN ADN A ARN---------------------
arn = transcripcion_adn(adn)
print("Transcripción del ADN: ", arn)


#---------------------TRADUCIR CODONES ---------------------------
proteina = traducir_codones(arn)
print("Proteínas: ", proteina)


#-------------------RECONOCER MUTACIONES-----------------------

ref = input("Ingrese la secuencia de referencia: ").upper()
muestra = input("Ingrese la secuencia a comparar: ").upper()

mutaciones = detectar_mutaciones(ref, muestra)

print("Mutaciones: ", mutaciones)