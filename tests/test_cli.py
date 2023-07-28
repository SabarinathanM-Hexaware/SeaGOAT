from click.testing import CliRunner

from seagoat import __version__
from seagoat.cli import seagoat
from tests.conftest import pytest


@pytest.mark.usefixtures("server")
def test_integration_test_with_color(snapshot, repo, mocker):
    mocker.patch("os.isatty", return_value=True)
    runner = CliRunner()
    query = "JavaScript"
    result = runner.invoke(seagoat, [query, repo.working_dir])

    assert result.output == snapshot
    assert result.exit_code == 0


@pytest.mark.usefixtures("server")
def test_integration_test_without_color(snapshot, repo, mocker):
    mocker.patch("os.isatty", return_value=True)
    runner = CliRunner()
    query = "JavaScript"
    result = runner.invoke(seagoat, [query, repo.working_dir, "--no-color"])

    assert result.output == snapshot
    assert result.exit_code == 0


def test_version_option():
    runner = CliRunner()
    result = runner.invoke(seagoat, ["--version"])

    assert result.exit_code == 0
    assert result.output.strip() == f"seagoat, version {__version__}"