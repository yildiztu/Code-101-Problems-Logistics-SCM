# Contributing to Code - 101 Problems

Thank you for your interest in contributing to this project! This document provides guidelines for contributors.

## How to Contribute

### Reporting Issues
- Use GitHub Issues to report bugs or request features
- Provide clear descriptions and steps to reproduce
- Include relevant screenshots and error messages

### Submitting Changes
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Code Standards

### General Guidelines
- Write clear, readable code with meaningful variable names
- Add comments for complex logic
- Follow existing code style and patterns
- Ensure all notebooks run without errors

### Jupyter Notebook Standards
- Include clear markdown explanations
- Use proper headings and structure
- Add visualizations where appropriate
- Test all code cells before submission

### Python Code
- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Write docstrings for functions and classes
- Keep functions focused and single-purpose

## Pull Request Process

### Before Submitting
- [ ] Test your changes thoroughly
- [ ] Update documentation if needed
- [ ] Check for existing issues/PRs
- [ ] Ensure all tests pass

### PR Requirements
- Clear description of changes
- Link to related issues
- Screenshots for UI changes
- Testing instructions if applicable

## Development Setup

### Prerequisites
- Python 3.8 or higher
- Git
- Jupyter Notebook

### Installation
```bash
# Clone the repository
git clone https://github.com/yildiztu/Code-101-Problems-Logistics-SCM.git
cd Code-101-Problems-Logistics-SCM

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Project Structure

```
Code-101-Problems-Logistics-SCM/
├── Part I - The Port & Container Terminal (Problems 1-46)/
├── Part II - The End-to-End Supply Chain (Problems 47-101)/
├── README.md
├── TODO.md
├── CONTRIBUTING.md
├── LICENSE
├── requirements.txt
└── infrastructure/
```

## Getting Help

- Check existing issues and documentation
- Ask questions in GitHub Discussions
- Review existing code for patterns
- Contact maintainers for guidance

## License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.
