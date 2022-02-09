from unittest.mock import patch

from organize.actions import Shell
from pathlib import Path


def test_shell_basic():
    shell = Shell("echo 'Hello World'")
    result = shell.run(simulate=True)
    assert not result

    result = shell.run(simulate=False)
    result = result["shell"]
    assert "Hello World" in result["output"]  # windows escapes the string
    assert result["returncode"] == 0


def test_shell_template_simulation():
    shell = Shell("echo '{msg}'", run_in_simulation=True)
    result = shell.run(msg="Hello", simulate=True)
    result = result["shell"]
    assert "Hello" in result["output"]
    assert result["returncode"] == 0
