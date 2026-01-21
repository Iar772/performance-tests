import httpx
from faker import Faker

CREATE_USER_URL = "http://localhost:8003/api/v1/users"
CREATE_DEPOSIT_ACCOUNT_URL = "http://localhost:8003/api/v1/accounts/open-deposit-account"

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
    assert create_user_http_response.status_code == 200, (
        f"Expected 200 status code, got {create_user_http_response.status_code}"
    )
    create_user_response_data = create_user_http_response.json()

    user_id = create_user_response_data.get("user")["id"]

    create_deposit_account_response = client.post(CREATE_DEPOSIT_ACCOUNT_URL, json={"userId": user_id})
    assert create_deposit_account_response.status_code == 200, (
        f"Expected 200 status code, got {create_deposit_account_response.status_code}"
    )
    create_deposit_account_response_data = create_deposit_account_response.json()
    print("Create deposit account status code:", create_deposit_account_response.status_code)
    print("Create deposit account response:", create_deposit_account_response_data)