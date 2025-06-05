## Run Fit6_Backend
Puerto 8080
uvicorn main:app --reload --port 8080
docker compose up --build -d

## Run Fit6_Backend_Alimentos
Puerto 8000
docker compose up --build -d

## Run Fit6_Backend_ActividadFisica
Puerto 8081
uvicorn main:app --reload --port 8081

## Run Fit6_ui
Puerto 5173
npm install
npm run dev

## Run Fit6_Backend_Receta
Puerto 8082
docker compose up --build -d
