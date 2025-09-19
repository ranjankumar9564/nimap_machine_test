import requests

BASE_URL = "http://127.0.0.1:8000/api/"

login_data = {"username": "muna", "password": "1234"}
r = requests.post(BASE_URL + "token/", json=login_data)
if r.status_code != 200:
    print("Login failed:", r.text)
    exit()

token = r.json()["access"]
headers = {"Authorization": f"Bearer {token}"}

print("✅ JWT Token acquired")

client_data = {"client_name": "Test Client"}
r = requests.post(BASE_URL + "clients/", json=client_data, headers=headers)
print("✅ Create Client Response:", r.json())
client_id = r.json()["id"]

r = requests.get(BASE_URL + "clients/", headers=headers)
print("✅ All Clients:", r.json())

r = requests.get(BASE_URL + f"clients/{client_id}/", headers=headers)
print(f"✅ Client {client_id} Details:", r.json())

update_data = {"client_name": "Updated Test Client"}
r = requests.put(BASE_URL + f"clients/{client_id}/", json=update_data, headers=headers)
print(f"✅ Client {client_id} Updated:", r.json())

r = requests.get(BASE_URL + "projects/", headers=headers)
users = [user['id'] for user in r.json()] if r.status_code == 200 else [1]
print("✅ Users available:", users)

project_data = {"project_name": "Test Project", "users": users, "client": client_id}
r = requests.post(BASE_URL + f"clients/{client_id}/projects/", json=project_data, headers=headers)
print("✅ Create Project Response:", r.json())

r = requests.get(BASE_URL + "projects/", headers=headers)
print("✅ Projects assigned to logged-in user:", r.json())

r = requests.delete(BASE_URL + f"clients/{client_id}/", headers=headers)
print(f"✅ Delete Client {client_id} Status Code:", r.status_code)
