import data_post
import sender_stand_request


# esta función cambia los valores en el parámetro "firstName"
def get_user_body(first_name):
    # el diccionario que contiene el cuerpo de solicitud se copia del archivo "data" (datos) para conservar los datos del diccionario de origen
    current_body = data_post.user_body.copy()
    # Se cambia el valor del parámetro firstName
    current_body["firstName"] = first_name
    # Se devuelve un nuevo diccionario con el valor firstName requerido
    return current_body


# Prueba 1. Creación de un nuevo usuario o usuaria
# El parámetro "firstName" contiene dos caracteres

print("--- Probando test con nombre de 2 letras ---")
def test_create_user_2_letter_in_first_name_get_success_response():
    # La versión actualizada del cuerpo de solicitud con el nombre "Aa" se guarda en la variable "user_body"
    user_body = get_user_body("Aa")
    # El resultado de la solicitud relevante se guarda en la variable "user_response"
    user_response = sender_stand_request.post_new_user(user_body)

    # Comprueba si el código de estado es 201
    assert user_response.status_code == 201
    # Comprueba que el campo authToken está en la respuesta y contiene un valor
    assert user_response.json()["authToken"] != ""


# Prueba 2. Creacion de usuario con firstName de 15 caracteres
print("--- Probando test con nombre de 15 letras ---")
def test_create_user_15_letter_in_first_name_get_success_response():
    user_body = get_user_body("Aaaaaaaaaaaaaaa")
    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""


# Prueba 4. Creacion de usuario con firstName de 16 caracteres
print("--- Probando test con nombre de 16 letras ---")
def test_create_user_16_letter_in_first_name_get_error_response():
    user_body = get_user_body("Aaaaaaaaaaaaaaaa")
    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 400
    assert user_response.json()["code"] == 400


# Prueba 5. Creacion de usuario con firstName de mas de 16 caracteres
print("--- Probando test con nombre de 17 letras ---")
def test_create_user_17_letter_in_first_name_get_error_response():
    user_body = get_user_body("Aaaaaaaaaaaaaaaaa")
    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 400
    assert user_response.json()["code"] == 400


# Prueba 8 - sin el parámetro firstName (debe fallar con error 400)
print("--- Probando test sin firstName ---")


def negative_assert_no_firstname(user_body):
    pass


def test_create_user_no_first_name_get_error_response():
    user_body = data_post.user_body.copy()
    user_body.pop("firstName")
    negative_assert_no_firstname(user_body)

