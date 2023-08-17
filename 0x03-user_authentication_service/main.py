#!/usr/bin/env python3
"""the test file for the app.py file"""
import requests


def register_user(email: str, password: str) -> None:
    """test the register_user function"""
    payload = {"email": email, "password": password}
    response = requests.post('http://localhost:5000/users', data=payload)
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """test the log_in function"""
    payload = {"email": email, "password": password}
    response = requests.post('http://localhost:5000/sessions', data=payload)
    assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    """tests the log_in function"""
    payload = {"email": email, "password": password}
    response = requests.post('http://localhost:5000/sessions', data=payload)
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "logged in"}
    session_id = response.cookies.get('session_id')
    return session_id


def profile_unlogged() -> None:
    """tests the profile function"""
    response = requests.get('http://localhost:5000/profile')
    assert response.status_code == 403


def profile_logged(session_id: str) -> None:
    """tests the profile function"""
    response = requests.get('http://localhost:5000/profile',
                            cookies={'session_id': session_id})
    assert response.status_code == 200
    assert response.json() == {"email": "guillaume@holberton.io"}


def log_out(session_id: str) -> None:
    """tests the log_out function"""
    response = requests.delete('http://localhost:5000/sessions',
                               cookies={'session_id': session_id})
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenue"}


def reset_password_token(email: str) -> str:
    """tests the reset_password_token function"""
    payload = {"email": email}
    response = requests.post('http://localhost:5000/reset_password',
                             data=payload)
    assert response.status_code == 200
    assert response.json() == {"email": email, "reset_token": "token"}
    reset_token = response.json().get('reset_token')
    return reset_token


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """tests the update_password function"""
    payload = {"email": email, "reset_token": reset_token,
               "new_password": new_password}
    response = requests.put('http://localhost:5000/reset_password',
                            data=payload)
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "Password updated"}
