import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from fastapi.testclient import TestClient
from api_server import app

client = TestClient(app)

def test_root():
    resp = client.get('/')
    assert resp.status_code == 200
    assert resp.json()['message'] == 'AdvancedChatbot API is running'


def test_chat():
    resp = client.post('/chat', json={'message': 'hello'})
    assert resp.status_code == 200
    assert 'Hello' in resp.json()['reply']
