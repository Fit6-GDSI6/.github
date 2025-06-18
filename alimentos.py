import random
from datetime import datetime

# Lista base de alimentos con nombre y descripciones
base_alimentos = [
    ("Leche", "Bebida láctea"),
    ("Crema", "Producto lácteo espeso"),
    ("Aceite de oliva", "Aceite saludable para cocinar"),
    ("Pan", "Producto de harina horneado"),
    ("Queso", "Derivado lácteo"),
    ("Yogur", "Lácteo fermentado"),
    ("Arroz", "Grano cocido común en comidas"),
    ("Pasta", "Fideos de trigo"),
    ("Papa", "Tubérculo"),
    ("Batata", "Tubérculo dulce"),
    ("Carne de vaca", "Fuente de proteínas"),
    ("Carne de cerdo", "Carne roja"),
    ("Pollo", "Carne blanca"),
    ("Pescado", "Rico en omega-3"),
    ("Huevos", "Ricos en proteínas"),
    ("Manteca", "Grasa láctea"),
    ("Aceite de coco", "Aceite vegetal"),
    ("Galletitas", "Dulces horneados"),
    ("Cereal", "Desayuno"),
    ("Mermelada", "Dulce de frutas"),
    ("Miel", "Endulzante natural"),
    ("Agua", "Bebida esencial"),
    ("Jugo de naranja", "Bebida de frutas"),
    ("Té", "Infusión caliente"),
    ("Café", "Bebida con cafeína"),
    ("Chocolate", "Dulce de cacao"),
    ("Frutilla", "Fruta roja"),
    ("Banana", "Fruta amarilla"),
    ("Manzana", "Fruta fresca"),
    ("Pera", "Fruta jugosa"),
    ("Naranja", "Cítrico"),
    ("Uvas", "Fruta pequeña y dulce"),
    ("Tomate", "Fruto rojo"),
    ("Zanahoria", "Verdura naranja"),
    ("Lechuga", "Vegetal de hoja verde"),
    ("Espinaca", "Rica en hierro"),
    ("Brócoli", "Vegetal verde"),
    ("Zapallo", "Verdura anaranjada"),
    ("Cebolla", "Verdura aromática"),
    ("Ajo", "Condimento natural"),
    ("Lentejas", "Legumbre rica en hierro"),
    ("Garbanzos", "Legumbre energética"),
    ("Porotos", "Legumbres variadas"),
    ("Almendras", "Fruto seco"),
    ("Nueces", "Fruto seco"),
    ("Pasas", "Fruta deshidratada"),
    ("Helado", "Postre congelado"),
    ("Tarta", "Postre o salado horneado"),
    ("Empanada", "Masa rellena"),
    ("Pizza", "Comida con queso y salsa")
]

# Generar 50 alimentos con macros aleatorios
alimentos = []
for name, desc in base_alimentos[:50]:
    grams = 100
    kcal = round(random.uniform(50, 500), 1)
    protein = round(random.uniform(0, 30), 1)
    fat = round(random.uniform(0, 30), 1)
    carbs = round(random.uniform(0, 50), 1)
    alimentos.append({
        "name": name,
        "description": desc,
        "kcal": kcal,
        "protein": protein,
        "fat": fat,
        "carbs": carbs,
        "grams": grams,
    })

import asyncio
import httpx

URL = "http://localhost:8000/foods/create"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJjYXJsb3Mucm9kcmlndWV6QGV4YW1wbGUuY29tIiwiZXhwIjoxNzUwMjc2NDA5fQ.o0cXNn6deOfMJjV4AJ2b7ZJSgRQDQ4PMgYm_-jvGoik"

cookies = {"access_token": TOKEN}  # Nombre de la cookie que espera tu backend, cambia si es otro


async def crear_alimento(client, alimento):
    resp = await client.post(URL, json=alimento, cookies=cookies)
    print(f"{alimento['name']}: {resp.status_code} - {resp.text}")

async def main():
    async with httpx.AsyncClient() as client:
        tasks = [crear_alimento(client, alimento) for alimento in alimentos]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
