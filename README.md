# Hello World Script

A minimal Python service that prints "Hello World" to standard output.

## Quick Start

1. Ensure Python 3.11+ is installed.
2. Run the script:
   ```bash
   python main.py
   ```

## Running Tests

```bash
python -m unittest tests/test_main.py
```

## Docker

Build and run:
```bash
docker build -t hello-world .
docker run --rm hello-world
```
