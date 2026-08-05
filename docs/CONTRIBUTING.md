# 🤝 Contributing to spark

Thank you for your interest in contributing to `spark`!

## 🛠️ Development Setup

1. Fork and clone the repository:
   ```bash
   git clone https://github.com/G10DC/spark.git
   cd spark
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -e .
   ```

3. Run the test suite:
   ```bash
   python -m unittest discover tests
   ```

## 📝 Guidelines

- Keep code clean, well-tested, and documented.
- All new features or lenses should include unit tests in `tests/`.
- Maintain compatibility with Python 3.10+.
