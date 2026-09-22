import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]))
import pytest
from app import create_app
@pytest.fixture
def app(tmp_path):
 return create_app({'TESTING':True,'DATABASE':str(tmp_path/'tasks.sqlite')})
@pytest.fixture
def client(app):
 return app.test_client()
