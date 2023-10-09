import json
import shutil
import subprocess
from copy import deepcopy
from pathlib import Path
from typing import Dict

import pytest

THIS_DIR = Path(__file__).parent
PROJECT_DIR = (THIS_DIR / "../").resolve()


@pytest.fixture(scope="function")
def project_dir() -> Path:
    template_values = {
        "repo_name": "test-repo",
    }
    generated_repo_dir: Path = generate_project(template_values=template_values)
    yield generated_repo_dir
    shutil.rmtree(path=generated_repo_dir)


def generate_project(template_values: Dict[str, str]) -> Path:
    template_values: Dict[str, str] = deepcopy(template_values)
    cookiecutter_config = {"default_context": template_values}
    cookiecutter_config_fpath = PROJECT_DIR / "cookiecutter-test-config.json"
    cookiecutter_config_fpath.write_text(json.dumps(cookiecutter_config))

    command = [
        "cookiecutter",
        str(PROJECT_DIR),
        "--output-dir",
        str(PROJECT_DIR / "sample"),
        "--no-input",
        "--config-file",
        str(cookiecutter_config_fpath),
    ]
    print(f"Command: {' '.join(command)}")

    subprocess.run(args=command, check=True)

    generated_repo_dir = PROJECT_DIR / "sample" / template_values["repo_name"]
    return generated_repo_dir


def test__can_generate_project(project_dir: Path):
    """
    execute: `cookiecutter <template directory> ...`
    """

    assert project_dir.exists()
