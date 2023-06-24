# pylint: disable=redefined-outer-name

from pathlib import Path
import time
from codector.file import File
from tests.conftest import pytest


@pytest.fixture
def repo_folder(repo):
    with open(Path(repo.working_dir) / "hello.md", "w", encoding="utf-8") as hello_file:
        hello_file.write("Hello world!")
    yield Path(repo.working_dir)


# pylint: disable-next=too-few-public-methods
class Commit:
    def __init__(self, message, committed_date=0):
        self.message = message
        self.committed_date = committed_date


def test_file_returns_global_metadata_1(repo_folder, snapshot):
    my_file = File("hello.md", repo_folder / "hello.md")
    my_file.add_commit(Commit("First commit for this"))
    my_file.add_commit(Commit("Another commit for this"))

    assert my_file.get_metadata() == snapshot


def test_file_returns_global_metadata_2(repo_folder, snapshot):
    my_file = File("hello.md", repo_folder / "hello.md")
    my_file.add_commit(Commit("Unrelated commit"))

    assert my_file.get_metadata() == snapshot


def test_handles_files_that_were_edited_today(repo_folder, snapshot):
    my_file = File("hello.md", repo_folder / "hello.md")
    my_file.add_commit(Commit("Unrelated commit", int(time.time())))

    assert my_file.get_metadata() == snapshot
