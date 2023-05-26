from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

new_user_info = {
    "username": "hyegyo",
    "password": "Fastapi123@",
    "name": "송혜교",
    "registration_no": "8411101033456",
    "address": "서울시 삼성동 111-22",
    "phone": "01011111133",
    "email": "hye@email.com",
    "user_type" : "회원",
    "is_deleted": False
}

def test_create_user():
    response = client.post(
        "/user/signup", 
        json = new_user_info
    )

    assert response.status_code == 201

def test_fail_signup_with_duplication():
    response = client.post(
        "/user/signup",
        json = new_user_info
    )

    assert response.status_code == 400
    assert '이미 존재하는' in response.text

def test_fail_signup_with_invalid_username():
    new_user_info['username'] = '이순신'
    response = client.post(
        "/user/signup",
        json = new_user_info
    )

    assert response.status_code == 422
    assert '유효하지 않은 양식의 ID' in response.text

def test_fail_signup_with_invalid_password():
    new_user_info['password'] = '12345'
    response = client.post(
        "/user/signup",
        json = new_user_info
    )

    assert response.status_code == 422
    assert '유효하지 않은 양식의 비밀번호' in response.text

def test_fail_signup_with_invalid_email():
    new_user_info['email'] = 'email.com'
    response = client.post(
        "/user/signup",
        json = new_user_info
    )

    assert response.status_code == 422
    assert '유효하지 않은 이메일 양식' in response.text


new_user_info['id'] = 1000

def test_user_login():
    login_user_info = {"username":"hyegyo", "password":"Fastapi123@"}
    response = client.post(
        "user/login",
        json = login_user_info
    )

    assert response.status_code == 201
    assert 'SUCCESS' in response.text

def test_fail_login_with_invalid_username():
    login_user_info = {"username":"hye", "password":"Fastapi123@"}
    response = client.post(
        "user/login",
        json = login_user_info
    )

    assert response.status_code == 401
    assert '존재하지 않는 ID' in response.text

def test_fail_login_with_invalid_password():
    login_user_info = {"username":"hyegyo", "password":"Fastapi1@"}
    response = client.post(
        "user/login",
        json = login_user_info
    )

    assert response.status_code == 401
    assert '비밀번호가 일치하지' in response.text

def test_delete_user():
    response = client.request(
        "DELETE",
        "/user/delete",
        json = {'user_id': new_user_info['id']}
    )
    assert response.status_code == 204
    assert '' in response.text

