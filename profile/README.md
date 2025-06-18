# .github
## Run Fit6_Backend
Puerto 8080
uvicorn main:app --reload --port 8080
docker compose up --build -d

## Run Fit6_Backend_Alimentos
Puerto 8000
docker compose up --build -d

## Run Fit6_Backend_ActividadFisica
Puerto 8081
docker compose up --build -d
uvicorn main:app --reload --port 8081

## Run Fit6_ui
Puerto 5173
npm install
npm run dev

![image](https://github.com/user-attachments/assets/bf35af04-f266-4f92-a8a1-4f99bd66d6a4)
![image](https://github.com/user-attachments/assets/160a0ab4-69fa-49c6-bacb-f9c4116e868c)
