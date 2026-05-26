# create_user_test.py

import data_post
import sender_stand_request


def get_user_body(first_name):
    current_body = data_post.user_body.copy()
    current_body["firstName"] = first_name
    return current_body


# Prueba 1 - nombre con 2 letras
print("--- Probando test con nombre de 2 letras ---")
def test_create_user_2_letter_in_first_name_get_success_response():
    user_body = get_user_body("Aa")
    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""


# Prueba 2 - nombre con 15 letras
print("--- Probando test con nombre de 15 letras ---")
def test_create_user_15_letter_in_first_name_get_success_response():
    user_body = get_user_body("Aaaaaaaaaaaaaaa")  # exactamente 15 caracteres
    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""