from math import sqrt

x1 = float(input("Digite coordenada x (P1):"))
y1 = float(input("Digite coordenada y (P1):"))

x2 = float(input("Digite coordenada x (P2):"))
y2 = float(input("Digite coordenada y (P2):"))

soma = (x2 - x1)**2 + (y2 - y1)**2
resultado = soma ** 0.5

print(f"O resultado é = {soma: .2f}")
print(f"O resultado é = {resultado: .2f}")