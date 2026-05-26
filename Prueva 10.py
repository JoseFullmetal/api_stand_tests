# Prueba 10 - firstName es número entero, no string (debe fallar con error 400)
import sender_stand_request
from create_user_test import get_user_body

print("--- Probando test con tipo número en firstName ---")
def test_create_user_number_type_first_name_get_error_response():
    user_body = get_user_body(12)
    response = sender_stand_request.post_new_user(user_body)

    assert response.status_code == 400