import sys
import subprocess
from pathlib import Path
import pytest

from main import main


def test_main_prints_hello_world(capsys):
    """Happy path: calling main should print 'hello world'."""
    main()
    captured = capsys.readouterr()
    assert captured.out == "hello world\n"


def test_main_returns_zero():
    """Edge case: main should return 0 as exit code."""
    exit_code = main()
    assert exit_code == 0


def test_script_execution():
    """Integration test: running the script directly produces the correct output and exit code."""
    script_path = Path(__file__).parent.parent / "main.py"
    result = subprocess.run(
        [sys.executable, str(script_path)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert result.stdout.rstrip("\n") == "hello world"