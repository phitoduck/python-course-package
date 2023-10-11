from uuid import uuid4

import pytest

from tests.consts import PROJECT_DIR


@pytest.fixture(scope="session")
def test_session_id() -> str:
    test_session_id: str = str(PROJECT_DIR.name) + str(uuid4())[:6]
    return test_session_id
