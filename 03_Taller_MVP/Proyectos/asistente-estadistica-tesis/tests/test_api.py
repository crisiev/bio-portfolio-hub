from fastapi.testclient import TestClient
from src.main import app

# Cliente de pruebas que simula un navegador o Postman
client = TestClient(app)

def test_tm_endpoint():
    """
    Prueba que el endpoint /tm devuelva un HTTP 200 y el JSON correcto.
    """
    # Hacemos una petición GET pasándole la secuencia por la URL (Query Params)
    response = client.get("/tm?secuencia=ATGC")
    
    # 1. El estatus debe ser 200 OK
    assert response.status_code == 200
    # 2. El cuerpo JSON debe contener la respuesta esperada
    assert response.json() == {"secuencia": "ATGC", "tm_wallace": 12.0}
