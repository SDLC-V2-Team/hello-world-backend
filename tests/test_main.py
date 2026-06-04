import pytest
from main import main

def test_main_prints_hello_world(capsys):
    """Happy path: main prints the expected greeting to stdout."""
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello World\n"

def test_main_returns_zero():
    """Edge case: main returns zero as exit code."""
    assert main() == 0

def test_main_does_not_raise():
    """Edge case: main runs without raising any exception."""
    try:
        main()
    except Exception as e:
        pytest.fail(f"main() raised an unexpected exception: {e}")