import pytest
from app.db import get_db


def test_resume(client, auth):
    response = client.get('/resume/')
    assert b"Education" in response.data
    assert b"Experience" in response.data
    assert b"Skills" in response.data
