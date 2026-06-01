# Contributing to Research to Midjourney

Thank you for your interest in contributing! This document provides guidelines.

## Getting Started

1. Fork the repository
2. Clone: `git clone https://github.com/YOUR-USERNAME/research-to-midjourney-skill.git`
3. Create branch: `git checkout -b feat/your-feature`
4. Make changes and test
5. Commit: `git commit -m "feat: description"`
6. Push: `git push -u origin feat/your-feature`
7. Create Pull Request

## Code Guidelines

- Use Python 3.8+
- Follow PEP 8
- Add docstrings to functions and classes
- Include type hints
- Add comments for complex logic

## Data Files

CSV files use pipe (`|`) delimiters.

### Adding Metaphors

Edit `src/research-to-mj/data/metaphor_database.csv`

### Adding Visual Styles

Edit `src/research-to-mj/data/visual_styles.csv`

## Testing

```bash
python3 src/research-to-mj/scripts/research.py
```

## Report Issues

Use GitHub Issues for bugs and feature requests.

## License

MIT License
