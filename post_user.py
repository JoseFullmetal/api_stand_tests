import configuration
import requests
import data_post


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
    print("--- Probando post_new_user ---")
    response = post_new_user(data_post.user_body)
    print(response.status_code)
    print(response.json())

    print("--- Probando post_products_kits ---")
    response = post_products_kits(data_post.product_ids)
    print(response.status_code)
    print(response.json())
