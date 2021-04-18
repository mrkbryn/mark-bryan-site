import pytest
from app.db import get_db


def test_research(client, auth):
    response = client.get('/research/')
    assert b"Publications" in response.data
    assert b"Presentations" in response.data
    assert b"Awards" in response.data
