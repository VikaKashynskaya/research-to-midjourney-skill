# Research to Midjourney - Claude Development Guide

This file provides guidance to Claude Code when working with this research-to-midjourney-skill repository.

## Project Overview

Research to Midjourney is an AI-powered skill that transforms technical briefs into comprehensive creative research documents, complete with:
- Deep concept exploration and idea generation
- Metaphor discovery and semantic analysis
- Historical context and cultural references
- Visual style recommendations
- Intelligent Midjourney prompt generation

## Workflow

### 1. Research Phase
```bash
python3 src/research-to-mj/scripts/research.py "<tech-brief>" --deep
```

**Analysis domains:**
- `concept` - Core idea extraction and refinement
- `history` - Historical context and precedents
- `metaphor` - Metaphor and analogy discovery
- `cultural` - Cultural and artistic references
- `semantic` - Semantic field analysis

### 2. Metaphor Discovery
```bash
python3 src/research-to-mj/scripts/metaphor_finder.py "<concept>" --sources all
```

**Metaphor sources:**
- `nature` - Natural phenomena and biology
- `technology` - Tech and future concepts
- `art` - Artistic and cultural movements
- `history` - Historical periods and events
- `psychology` - Psychological and behavioral patterns

### 3. Visual Style Analysis
```bash
python3 src/research-to-mj/scripts/style_analyzer.py "<concept>" --depth full
```

**Output:**
- Visual style recommendations
- Mood board keywords
- Color and composition suggestions
- Historical style references

### 4. Midjourney Prompt Generation
```bash
python3 src/research-to-mj/scripts/mj_prompt_generator.py "<research-file>" --variations 5
```

**Generates:**
- Multiple MJ prompt variations
- Style descriptors
- Technical parameters
- Fallback options

## Architecture

```
src/research-to-mj/                    # Source of Truth
├── data/
│   ├── research_frameworks.csv        # Research analysis frameworks
│   ├── metaphor_database.csv          # Metaphor library
│   ├── visual_styles.csv              # Visual style database
│   ├── mj_templates.csv               # MJ prompt templates
│   └── historical_references.csv      # Historical context database
├── scripts/
│   ├── research.py                    # Main research analyzer
│   ├── metaphor_finder.py             # Metaphor extraction
│   ├── style_analyzer.py              # Visual style recommendation
│   ├── mj_prompt_generator.py         # MJ prompt creation
│   ├── web_search.py                  # Web research integration
│   └── report_generator.py            # Document generation
├── templates/
│   ├── research_report.md             # Research template
│   └── mj_prompts.md                  # MJ prompts template
└── utils/
    ├── semantic_search.py             # Semantic analysis
    ├── web_scraper.py                 # Research sources
    └── formatter.py                   # Output formatting

.claude/skills/research-to-mj/         # Claude skill (symlinks)
docs/                                   # Documentation
examples/                               # Example outputs
```

## Key Features

1. **Multi-source Research**
   - Web search integration
   - Academic sources
   - Cultural databases
   - Historical archives

2. **Metaphor Engine**
   - Semantic similarity matching
   - Cross-domain associations
   - Cultural metaphor libraries
   - Emotional mapping

3. **Visual Style Intelligence**
   - Historical style analysis
   - Mood and emotion mapping
   - Color psychology
   - Composition recommendations

4. **Intelligent MJ Prompts**
   - Context-aware generation
   - Style consistency
   - Technical precision
   - Creative variations

## Usage Examples

### Basic Research
```
Research a modern fintech app with emphasis on trust and innovation
```

### With Style Preference
```
Research a sustainable fashion brand with focus on organic, nature-inspired aesthetics
```

### Full Pipeline
```
I need deep research for a cybersecurity platform for gamers. 
Include metaphors, historical context, and generate 5 Midjourney prompts for the hero image.
```

## Prerequisites

Python 3.x with no external dependencies required for core functionality.
Optional: requests library for web search integration.

## Git Workflow

Never push directly to `main`:

1. Create a branch: `git checkout -b feat/feature-name` or `fix/bug-name`
2. Make changes and commit: `git commit -m "type: description"`
3. Push branch: `git push -u origin <branch>`
4. Create PR: `gh pr create`

## Data Files Format

All CSV files use UTF-8 encoding with pipe (|) delimiters for better semantic content handling.

### research_frameworks.csv
```
domain|framework|questions|key_areas
concept|Five Whys|Why does this exist?|Purpose,Value,Impact
history|Timeline Analysis|What came before?|Origins,Evolution,Trends
```

### metaphor_database.csv
```
metaphor|source_domain|target_domain|description|emotional_weight
lighthouse|nature|guidance|illuminating path through darkness|hope,trust
```

### mj_templates.csv
```
category|template|parameters|weight
style|"[concept], [style], [mood]"|style,mood,era|high
composition|"[layout], [perspective], [focus]"|layout,perspective|medium
```

## Search Implementation

Uses BM25 ranking with semantic enrichment:
- Keyword extraction from research data
- Semantic similarity for metaphor discovery
- Contextual matching for style recommendations
- Cross-reference pattern matching

## Output Generation

Reports are generated in Markdown with:
- Executive summary
- Research findings with sources
- Metaphor exploration
- Visual style recommendations
- 5-10 Midjourney prompt variations
- Glossary and references
