import subprocess
from pathlib import Path


def test__linting_passes(project_dir: Path):
    subprocess.run(
        [
            "make",
            "lint-ci",
        ],
        cwd=project_dir,
        check=True,
    )


def test__tests_pass():
    ...


def test__install_succeeds():
    ...
