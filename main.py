import os
import tempfile

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from typing import List

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile):
    try:
        # Verificar si el archivo es válido
        if not file.filename.endswith(".txt"):
            return JSONResponse(content={
                "error": "El archivo debe tener extensión .txt"}, status_code=400)

        # Crear un archivo temporal para procesar los datos
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(file.file.read())
            temp_file_path = temp_file.name

        # Procesar el archivo para determinar el código secreto más corto
        shortest_code = find_shortest_code(temp_file_path)

        # Eliminar el archivo temporal
        os.remove(temp_file_path)

        return {"shortest_code": shortest_code}

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

# Función para encontrar el código secreto más corto
def find_shortest_code(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    code_set = set()

    for line in lines:
        # Validar el formato de 3 caracteres
        if len(line) == 3:
            code_set.add(line.strip())

    # Encontrar el código secreto más corto
    shortest_code = "".join(sorted(code_set, key=lambda x: len(x))[0])

    # Imprimir el código secreto más corto
    print("Código secreto más corto encontrado:", shortest_code)

    return shortest_code

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
