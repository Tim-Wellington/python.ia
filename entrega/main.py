distancia = float(input("Informe a distância em km: "))
chovendo = input("Está chovendo? (S/N): ")

if distancia <= 5:
    taxa = 5
elif distancia <= 10:
    taxa = 8
else:
    taxa = 10

if chovendo.upper() == "S":
    taxa += 2

print(f"Taxa de entrega: R$ {taxa:.2f}")