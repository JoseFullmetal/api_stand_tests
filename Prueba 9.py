import sender_stand_request
from create_user_test import get_user_body

def negative_assert_no_firstname(user_body):
    response = sender_stand_request.post_new_user(user_body)

    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos"


# Prueba 9 - firstName vacío (debe fallar con error 400)
print("--- Probando test con firstName vacío ---")
def test_create_user_empty_first_name_get_error_response():
    user_body = get_user_body("")
    negative_assert_no_firstname(user_body)