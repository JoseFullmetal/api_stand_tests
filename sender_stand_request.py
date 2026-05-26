import configuration
import requests
import data_post


def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)


def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)


def get_warehouses():
    return requests.get(configuration.URL_SERVICE + configuration.WAREHOUSES_PATH)


def post_new_user(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=body,
        headers=data_post.headers
    )


def post_products_kits(products_ids):
    return requests.post(
        configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
        json=products_ids,
        headers=data_post.headers
    )


if __name__ == "__main__":
    print("--- Probando get_docs ---")
    response = get_docs()
    print(response.status_code)
    print(response.headers)

    print("--- Probando get_users_table ---")
    response = get_users_table()
    print(response.status_code)

    print("--- Probando get_warehouses ---")
    response = get_warehouses()
    print(response.status_code)
    print(response.json())

    print("--- Probando post_new_user ---")
    response = post_new_user(data_post.user_body)
    print(response.status_code)
    print(response.json())

    print("--- Probando post_products_kits ---")
    response = post_products_kits(data_post.product_ids)
    print(response.status_code)
    print(response.json())
