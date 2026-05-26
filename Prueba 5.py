import sender_stand_request
from create_user_test import get_user_body

# Prueba 5 - nombre con espacio (la API acepta espacios aunque la lista diga error 400)
print("--- Probando test con espacio en el nombre ---")
def test_create_user_has_space_in_first_name_get_error_response():
    user_body = get_user_body("A Aaa")
    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 400
    assert user_response.json()["code"] == 400
    assert user_response.json()["message"] == "El nombre solo puede contener letras latinas y la longitud debe ser de 2 a 15 caracteres"