from datetime import datetime, timedelta, time
import random
import asyncio
import httpx

# Lista de alimentos con sus IDs tal como te devolvió la API
alimentos = [
  {
    "name": "Banana",
    "description": "Es una banana común",
    "kcal": 89,
    "protein": 1.1,
    "fat": 0.3,
    "carbs": 22.8,
    "id": "682a9f65d78e82f8e0ee47ad"
  },
  {
    "name": "Manzana",
    "description": "Es una manzana roja",
    "kcal": 52,
    "protein": 0.3,
    "fat": 0.2,
    "carbs": 14,
    "id": "682a9f65d78e82f8e0ee47ae"
  },
  {
    "name": "Huevo duro",
    "description": "Es una huevo de gallina",
    "kcal": 155,
    "protein": 13,
    "fat": 11,
    "carbs": 1.1,
    "id": "682a9f65d78e82f8e0ee47af"
  },
  {
    "name": "Pollo",
    "description": "Es un pollo",
    "kcal": 165,
    "protein": 31,
    "fat": 3.6,
    "carbs": 0,
    "id": "682a9f65d78e82f8e0ee47b0"
  },
  {
    "name": "Carne de vaca",
    "description": "Carne de vaca",
    "kcal": 250,
    "protein": 26,
    "fat": 15,
    "carbs": 0,
    "id": "682a9f65d78e82f8e0ee47b1"
  },
  {
    "name": "Cerdo",
    "description": "Carne de cerdo",
    "kcal": 297,
    "protein": 26,
    "fat": 21,
    "carbs": 0,
    "id": "682a9f65d78e82f8e0ee47b2"
  },
  {
    "name": "Zanahoria",
    "description": "Es una zanahoria cruda",
    "kcal": 41,
    "protein": 0.9,
    "fat": 0.2,
    "carbs": 10,
    "id": "682a9f65d78e82f8e0ee47b3"
  },
  {
    "name": "Papa",
    "description": "Es una papa cruda",
    "kcal": 77,
    "protein": 2,
    "fat": 0.1,
    "carbs": 17,
    "id": "682a9f65d78e82f8e0ee47b4"
  },
  {
    "name": "Batata",
    "description": "Tubérculo dulce",
    "kcal": 336.5,
    "protein": 24.6,
    "fat": 20.7,
    "carbs": 17.4,
    "id": "6853125c5438ecf16992e90e"
  },
  {
    "name": "Empanada",
    "description": "Masa rellena",
    "kcal": 267.4,
    "protein": 2.4,
    "fat": 27.5,
    "carbs": 14.4,
    "id": "6853125c5438ecf16992e910"
  },
  {
    "name": "Pescado",
    "description": "Rico en omega-3",
    "kcal": 129,
    "protein": 22.9,
    "fat": 4.7,
    "carbs": 39.2,
    "id": "6853125c5438ecf16992e912"
  },
  {
    "name": "Pasas",
    "description": "Fruta deshidratada",
    "kcal": 217.5,
    "protein": 15.7,
    "fat": 3.6,
    "carbs": 32.3,
    "id": "6853125c5438ecf16992e913"
  },
  {
    "name": "Galletitas",
    "description": "Dulces horneados",
    "kcal": 304,
    "protein": 18.5,
    "fat": 10.3,
    "carbs": 49.7,
    "id": "6853125d5438ecf16992e915"
  },
  {
    "name": "Frutilla",
    "description": "Fruta roja",
    "kcal": 193,
    "protein": 4.1,
    "fat": 28.5,
    "carbs": 21.4,
    "id": "6853125c5438ecf16992e906"
  },
  {
    "name": "Crema",
    "description": "Producto lácteo espeso",
    "kcal": 59.8,
    "protein": 9.6,
    "fat": 13.5,
    "carbs": 19.9,
    "id": "6853125c5438ecf16992e907"
  },
  {
    "name": "Pan",
    "description": "Producto de harina horneado",
    "kcal": 131,
    "protein": 0.2,
    "fat": 3.3,
    "carbs": 24.7,
    "id": "6853125c5438ecf16992e90a"
  },
  {
    "name": "Yogur",
    "description": "Lácteo fermentado",
    "kcal": 101.1,
    "protein": 23.3,
    "fat": 12.3,
    "carbs": 3.2,
    "id": "6853125c5438ecf16992e909"
  },
  {
    "name": "Leche",
    "description": "Bebida láctea",
    "kcal": 213.6,
    "protein": 18.5,
    "fat": 27.2,
    "carbs": 41.7,
    "id": "6853125c5438ecf16992e908"
  },
  {
    "name": "Café",
    "description": "Bebida con cafeína",
    "kcal": 346.5,
    "protein": 27.4,
    "fat": 1,
    "carbs": 14.2,
    "id": "6853125c5438ecf16992e90b"
  },
  {
    "name": "Pera",
    "description": "Fruta jugosa",
    "kcal": 187.5,
    "protein": 18,
    "fat": 11.3,
    "carbs": 10.7,
    "id": "6853125c5438ecf16992e90c"
  },
  {
    "name": "Nueces",
    "description": "Fruto seco",
    "kcal": 79.3,
    "protein": 25.8,
    "fat": 23.5,
    "carbs": 1.1,
    "id": "6853125c5438ecf16992e90f"
  },
  {
    "name": "Aceite de oliva",
    "description": "Aceite saludable para cocinar",
    "kcal": 187.3,
    "protein": 6.3,
    "fat": 6.5,
    "carbs": 1.4,
    "id": "6853125d5438ecf16992e91b"
  },
  {
    "name": "Queso",
    "description": "Derivado lácteo",
    "kcal": 143.4,
    "protein": 2.2,
    "fat": 7.9,
    "carbs": 14.8,
    "id": "6853125c5438ecf16992e90d"
  },
  {
    "name": "Lechuga",
    "description": "Vegetal de hoja verde",
    "kcal": 85.4,
    "protein": 28,
    "fat": 19.6,
    "carbs": 42.5,
    "id": "6853125d5438ecf16992e91e"
  },
  {
    "name": "Pasta",
    "description": "Fideos de trigo",
    "kcal": 327.3,
    "protein": 19.2,
    "fat": 12.4,
    "carbs": 26.6,
    "id": "6853125d5438ecf16992e91f"
  },
  {
    "name": "Manteca",
    "description": "Grasa láctea",
    "kcal": 358.1,
    "protein": 26.9,
    "fat": 9.1,
    "carbs": 28.8,
    "id": "6853125c5438ecf16992e905"
  },
  {
    "name": "Helado",
    "description": "Postre congelado",
    "kcal": 264.4,
    "protein": 25.8,
    "fat": 28.5,
    "carbs": 48.2,
    "id": "6853125d5438ecf16992e920"
  },
  {
    "name": "Jugo de naranja",
    "description": "Bebida de frutas",
    "kcal": 442,
    "protein": 11.9,
    "fat": 22.4,
    "carbs": 3.3,
    "id": "6853125d5438ecf16992e918"
  },
  {
    "name": "Cereal",
    "description": "Desayuno",
    "kcal": 184.1,
    "protein": 14.5,
    "fat": 21,
    "carbs": 17.5,
    "id": "6853125d5438ecf16992e917"
  },
  {
    "name": "Aceite de coco",
    "description": "Aceite vegetal",
    "kcal": 305.5,
    "protein": 16.1,
    "fat": 23.5,
    "carbs": 6.8,
    "id": "6853125c5438ecf16992e914"
  },
  {
    "name": "Lentejas",
    "description": "Legumbre rica en hierro",
    "kcal": 52.4,
    "protein": 4.8,
    "fat": 9.2,
    "carbs": 20.1,
    "id": "6853125d5438ecf16992e921"
  },
  {
    "name": "Ajo",
    "description": "Condimento natural",
    "kcal": 141.1,
    "protein": 27.2,
    "fat": 28.6,
    "carbs": 9.5,
    "id": "6853125d5438ecf16992e91c"
  },
  {
    "name": "Brócoli",
    "description": "Vegetal verde",
    "kcal": 177.8,
    "protein": 29.8,
    "fat": 7.2,
    "carbs": 29.1,
    "id": "6853125d5438ecf16992e91d"
  },
  {
    "name": "Espinaca",
    "description": "Rica en hierro",
    "kcal": 85.7,
    "protein": 19.2,
    "fat": 11.1,
    "carbs": 46.3,
    "id": "6853125d5438ecf16992e91a"
  },
  {
    "name": "Agua",
    "description": "Bebida esencial",
    "kcal": 71.1,
    "protein": 16.5,
    "fat": 16.1,
    "carbs": 1.7,
    "id": "6853125d5438ecf16992e926"
  },
  {
    "name": "Mermelada",
    "description": "Dulce de frutas",
    "kcal": 418.7,
    "protein": 30,
    "fat": 16.3,
    "carbs": 9,
    "id": "6853125d5438ecf16992e916"
  },
  {
    "name": "Huevos",
    "description": "Ricos en proteínas",
    "kcal": 303.7,
    "protein": 24.1,
    "fat": 29,
    "carbs": 16.5,
    "id": "6853125d5438ecf16992e922"
  },
  {
    "name": "Porotos",
    "description": "Legumbres variadas",
    "kcal": 68.8,
    "protein": 29,
    "fat": 9,
    "carbs": 34,
    "id": "6853125d5438ecf16992e923"
  },
  {
    "name": "Naranja",
    "description": "Cítrico",
    "kcal": 346.5,
    "protein": 11.9,
    "fat": 2,
    "carbs": 2.1,
    "id": "6853125d5438ecf16992e919"
  },
  {
    "name": "Garbanzos",
    "description": "Legumbre energética",
    "kcal": 416.9,
    "protein": 12,
    "fat": 29.4,
    "carbs": 32.7,
    "id": "6853125d5438ecf16992e924"
  },
  {
    "name": "Cebolla",
    "description": "Verdura aromática",
    "kcal": 216.3,
    "protein": 26,
    "fat": 21.8,
    "carbs": 6.4,
    "id": "6853125d5438ecf16992e92a"
  },
  {
    "name": "Tomate",
    "description": "Fruto rojo",
    "kcal": 73.5,
    "protein": 8.7,
    "fat": 25.9,
    "carbs": 14.3,
    "id": "6853125d5438ecf16992e927"
  },
  {
    "name": "Carne de cerdo",
    "description": "Carne roja",
    "kcal": 396.8,
    "protein": 18.1,
    "fat": 25.4,
    "carbs": 35.2,
    "id": "6853125c5438ecf16992e911"
  },
  {
    "name": "Zapallo",
    "description": "Verdura anaranjada",
    "kcal": 428.6,
    "protein": 12,
    "fat": 3.4,
    "carbs": 17.7,
    "id": "6853125d5438ecf16992e928"
  },
  {
    "name": "Té",
    "description": "Infusión caliente",
    "kcal": 464.8,
    "protein": 1.4,
    "fat": 15.3,
    "carbs": 33.9,
    "id": "6853125d5438ecf16992e92c"
  },
  {
    "name": "Almendras",
    "description": "Fruto seco",
    "kcal": 306.5,
    "protein": 8,
    "fat": 3.3,
    "carbs": 17.5,
    "id": "6853125d5438ecf16992e929"
  },
  {
    "name": "Chocolate",
    "description": "Dulce de cacao",
    "kcal": 375.1,
    "protein": 15.7,
    "fat": 14.5,
    "carbs": 43.2,
    "id": "6853125d5438ecf16992e92d"
  },
  {
    "name": "Miel",
    "description": "Endulzante natural",
    "kcal": 283.2,
    "protein": 16.9,
    "fat": 19.6,
    "carbs": 18.5,
    "id": "6853125d5438ecf16992e92b"
  },
  {
    "name": "Pizza",
    "description": "Comida con queso y salsa",
    "kcal": 61.6,
    "protein": 7.3,
    "fat": 14.1,
    "carbs": 23.9,
    "id": "6853125d5438ecf16992e925"
  },
  {
    "name": "Uvas",
    "description": "Fruta pequeña y dulce",
    "kcal": 128.2,
    "protein": 6.2,
    "fat": 25.7,
    "carbs": 25.2,
    "id": "6853125d5438ecf16992e92e"
  },
  {
    "name": "Arroz",
    "description": "Grano cocido común en comidas",
    "kcal": 427.7,
    "protein": 6.8,
    "fat": 11.6,
    "carbs": 44,
    "id": "6853125e5438ecf16992e92f"
  },
  {
    "name": "Tarta",
    "id": "6853125e5438ecf16992e930"
  }
]

URL = "http://localhost:8000/consumptions"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJjYXJsb3Mucm9kcmlndWV6QGV4YW1wbGUuY29tIiwiZXhwIjoxNzUwMjc2NDA5fQ.o0cXNn6deOfMJjV4AJ2b7ZJSgRQDQ4PMgYm_-jvGoik"
cookies = {"access_token": TOKEN}



def fechas_ultimos_2_meses_con_hora():
    hoy = datetime.utcnow().date()
    fechas_con_hora = []
    for i in range(60):
        fecha = hoy - timedelta(days=i)
        # Generar hora aleatoria
        hora = random.randint(0, 23)
        minuto = random.randint(0, 59)
        segundo = random.randint(0, 59)
        dt_con_hora = datetime.combine(fecha, time(hora, minuto, segundo))
        fechas_con_hora.append(dt_con_hora)
    return fechas_con_hora

async def registrar_consumo(client, alimento, fecha_hora, gramos=100):
    payload = {
        "food_id": alimento["id"],
        "grams": gramos,
        "consumed_at": fecha_hora.isoformat() + "Z"  # ISO 8601 con Z de UTC
    }
    response = await client.post(URL, json=payload, cookies=cookies)
    print(f"{fecha_hora} - {alimento['name']} ({alimento['id']}): {response.status_code} - {response.text}")

async def main():
    fechas = fechas_ultimos_2_meses_con_hora()
    async with httpx.AsyncClient() as client:
        tasks = []
        for fecha_hora in fechas:
            alimento = random.choice(alimentos)
            gramos = random.randint(50, 300)
            tasks.append(registrar_consumo(client, alimento, fecha_hora, gramos))
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())