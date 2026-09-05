from app import app

def test_health():
    # Crea un cliente de pruebas simulado
    client = app.test_client()
    # Hace una petición GET a la ruta /health
    response = client.get('/health')
    # Verifica que devuelva código 200 (OK)
    assert response.status_code == 200
    