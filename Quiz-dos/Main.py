# Datos de entrada
nombre = "Oscar"
dias = 7
salario = 785000

# Cálculos
prima = (salario / 360) * dias
cesantia = (salario / 360) * dias
intereses_cesantia = cesantia * 0.12 / 360 * dias
vacaciones = (salario / 360) * dias / 720

# Liquidación total
liquidacion = prima + cesantia + intereses_cesantia + vacaciones

# Mostrar resultados
print(f"Señor {nombre} para los {dias} días laborados y")
print(f"salario ${salario}, su liquidación se compone así:")
print(f"Prima: ${prima:.2f}")
print(f"Cesantía: ${cesantia:.2f}")
print(f"Intereses cesantías: ${intereses_cesantia:.2f}")
print(f"Vacaciones: ${vacaciones:.2f}")
print(f"Liquidación: ${liquidacion:.2f}")




