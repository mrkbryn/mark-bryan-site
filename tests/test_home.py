import pytest
from app.db import get_db


def test_index(client, auth):
    response = client.get('/')
    # Verify public links
    assert b"About" in response.data
    assert b"Home" in response.data
    assert b"Resume" in response.data
    assert b"Research" in response.data

    # Verify private links
    assert b"Blog" not in response.data


def test_admin_links(client, auth):
    auth.login()
    response = client.get('/')
    # Verify private links
    assert b"Logout" in response.data
    assert b"Blog" in response.data
