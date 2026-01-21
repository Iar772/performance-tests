import httpx
from faker import Faker
from starlette import status

CREATE_USER_URL = "http://localhost:8003/api/v1/users"
CREATE_CREDIT_ACCOUNT_URL = "http://localhost:8003/api/v1/accounts/open-credit-card-account"
CREATE_PURCHASE_OPERATION_URL = "http://localhost:8003/api/v1/operations/make-purchase-operation"
GET_OPERATION_RECEIPT_URL = "http://localhost:8003/api/v1/operations/operation-receipt/{operation_id}"

fake_data = Faker()
email = fake_data.email()
last_name = fake_data.last_name()
first_name = fake_data.first_name()
middle_name = fake_data.last_name()
phone_number = fake_data.phone_number()

create_user_payload = {
    "email": email,
    "lastName": last_name,
    "firstName": first_name,
    "middleName": middle_name,
    "phoneNumber": phone_number,
}

with httpx.Client() as client:
    create_user_http_response = client.post(CREATE_USER_URL, json=create_user_payload)
    assert create_user_http_response.status_code == status.HTTP_200_OK, (
        f"Expected 200 status code, got {create_user_http_response.status_code}"
    )
    create_user_response_data = create_user_http_response.json()

    user_id = create_user_response_data.get("user")["id"]

    create_credit_account_http_response = client.post(CREATE_CREDIT_ACCOUNT_URL, json={"userId": user_id})
    assert create_credit_account_http_response.status_code == status.HTTP_200_OK, (
        f"Expected 200 status code, got {create_credit_account_http_response.status_code}"
    )
    create_credit_account_response_data = create_credit_account_http_response.json()

    create_purchase_operation_payload = {
        "status": "IN_PROGRESS",
        "amount": 77.99,
        "cardId": create_credit_account_response_data.get("account")["cards"][0]["id"],
        "accountId": create_credit_account_response_data.get("account")["id"],
        "category": "taxi",
    }
    create_purchase_operation_http_response = client.post(
        CREATE_PURCHASE_OPERATION_URL, json=create_purchase_operation_payload
    )
    assert create_purchase_operation_http_response.status_code == status.HTTP_200_OK, (
        f"Expected 200 status code, got {create_purchase_operation_http_response.status_code}"
    )
    create_purchase_operation_response_data = create_purchase_operation_http_response.json()

    operation_id = create_purchase_operation_response_data.get("operation")["id"]
    operation_receipt_http_response = client.get(GET_OPERATION_RECEIPT_URL.format(operation_id=operation_id))
    assert operation_receipt_http_response.status_code == status.HTTP_200_OK, (
        f"Expected 200 status code, got {operation_receipt_http_response.status_code}"
    )

    operation_receipt_response_data = operation_receipt_http_response.json()
    print("Get operation receipt response:", operation_receipt_response_data)
