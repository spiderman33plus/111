a = "111"
b = a * 1000
c = b * 1000
d = c * 1000
nombre_base = "111"
veces = 10
resultado = d
for i in range(veces):
    nombre_archivo = f"{nombre_base}_{i+1}.txt"
    
    with open(nombre_archivo, "w") as f:
        f.write("Resultado: " + str(resultado))

print("Archivos creados")