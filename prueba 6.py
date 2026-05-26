
import sender_stand_request
from create_user_test import get_user_body

# Prueba 6 - nombre con caracteres especiales (debe fallar con error 400)
print("--- Probando test con caracteres especiales en el nombre ---")
def test_create_user_has_special_symbol_in_first_name_get_error_response():
    user_body = get_user_body("\"№%@\"")  # \\ antes de las comillas dobles
    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 400
    assert user_response.json()["code"] == 400
    assert user_response.json()["message"] == "Has introducido un nombre de usuario no válido. El nombre solo puede contener letras del alfabeto latino, la longitud debe ser de 2 a 15 caracteres."
