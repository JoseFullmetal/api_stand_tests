import data_post
import sender_stand_request
from create_user_test import get_user_body

# Prueba 4 - nombre con 16 letras (debe fallar con error 400)
print("--- Probando test con nombre de 16 letras ---")
def test_create_user_16_letter_in_first_name_get_error_response():
    user_body = get_user_body("Aaaaaaaaaaaaaaa")  # exactamente 16 caracteres
    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 400
    assert user_response.json()["code"] == 400
    assert user_response.json()["message"] == "El nombre solo puede contener letras latinas y la longitud debe ser de 2 a 15 caracteres"