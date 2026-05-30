# Research to Midjourney Skill

> Transform technical briefs into comprehensive creative research with intelligent Midjourney prompt generation

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/python-3.x-yellow.svg?logo=python&logoColor=white)](https://python.org)
[![GitHub Stars](https://img.shields.io/github/stars/VikaKashynskaya/research-to-midjourney-skill?style=flat)](https://github.com/VikaKashynskaya/research-to-midjourney-skill)

## What It Does

An AI-powered research assistant that takes a technical brief or product description and delivers:

1. **Deep Concept Exploration** - Uncover the core idea, values, and implications
2. **Historical Context** - Discover relevant historical periods, movements, and precedents
3. **Metaphor Discovery** - Find powerful metaphors across nature, technology, art, history
4. **Cultural References** - Explore artistic, cultural, and psychological connections
5. **Visual Style Recommendations** - Define the visual language and mood
6. **Midjourney Prompts** - Generate 5-10 optimized MJ prompts ready to use

## Quick Start

### Installation

Clone and install locally:
```bash
git clone https://github.com/VikaKashynskaya/research-to-midjourney-skill.git
cd research-to-midjourney-skill
```

### Usage in Claude

Simply describe your project:

```
Research a modern fintech app that makes financial technology accessible to Gen Z. 
I need deep concept analysis, historical context, metaphors, and MJ prompts for the hero section.
```

Or for style exploration:

```
Deep research for a sustainable fashion brand. Focus on:
- How sustainability relates to historical movements
- Nature-inspired metaphors
- Visual style recommendations
- 5 Midjourney prompts for lookbooks
```

## Features

### 🔍 Research Domains

| Domain | What You Get |
|--------|------------|
| **Concept** | Core purpose, values, target audience, differentiation |
| **History** | Historical precedents, relevant periods, evolution of ideas |
| **Metaphor** | Cross-domain metaphors from nature, tech, art, history, psychology |
| **Cultural** | Artistic movements, cultural references, psychological patterns |
| **Semantic** | Word associations, emotional mapping, conceptual relationships |

### 🎨 Visual Style Intelligence

- Historical style analysis and recommendations
- Mood and emotional mapping
- Color psychology insights
- Composition and layout principles
- Mood board keywords

### 🖼️ Midjourney Prompts

The skill generates multiple prompt variations:

```
# Hero Section - Premium Fintech
"sleek digital interface, minimalist design, trust and innovation, 
futuristic minimalism, soft cyan and navy blue, 
high contrast, professional photography, --ar 16:9"

# Supporting Visual - Nature of Growth
"organic growth metaphor, financial plant sprouting coins, 
botanical illustration style, watercolor, soft greens and golds,
editorial illustration, --ar 1:1"
```

Plus fallback options and technical variations.

## Architecture

```
src/research-to-mj/
├── data/
│   ├── research_frameworks.csv       # Analysis frameworks and questions
│   ├── metaphor_database.csv         # 200+ metaphors across domains
│   ├── visual_styles.csv             # Style descriptions and keywords
│   ├── mj_templates.csv              # Prompt generation templates
│   └── historical_references.csv     # Historical context database
├── scripts/
│   ├── research.py                   # Main research analyzer
│   ├── metaphor_finder.py            # Metaphor extraction engine
│   ├── style_analyzer.py             # Visual style recommender
│   ├── mj_prompt_generator.py        # MJ prompt composer
│   └── report_generator.py           # Markdown report creation
└── templates/
    ├── research_report.md            # Research output template
    └── mj_prompts.md                 # Prompts template
```

## Example Research Output

### Input
```
Build a cybersecurity platform for gaming communities
```

### Output Structure

**1. Executive Summary**
- Core concept: Democratizing gaming security
- Target: Gen Z gamers, streaming communities
- Innovation angle: Security without friction

**2. Historical Context**
- Evolution of gaming platforms (2000-2026)
- Security awareness in communities
- Precedent: Discord security features

**3. Metaphor Exploration**
- Guardian/Sentinel (protection concept)
- Firewall as protective barrier (tech domain)
- Fortress/Castle (security concept)
- Shield (universal protection symbol)

**4. Visual Style Recommendations**
- **Primary Style**: Neubrutalism meets gaming aesthetic
- **Mood**: Edgy, trustworthy, high-tech
- **Colors**: Deep purple, neon green, dark backgrounds
- **Typography**: Bold sans-serif, tech-forward

**5. Midjourney Prompts**

```
1. "cybersecurity platform interface, gaming aesthetic, 
   neubrutalism design, neon green accents, dark theme,
   digital fortress, high-tech minimalism, --ar 16:9"

2. "gaming security metaphor, sentinel guardian, neon lighting,
   cyberpunk style, protective aura, digital art, --ar 1:1"

3. "hero section for gaming security app, sleek modern interface,
   trust and protection feeling, premium gaming aesthetic,
   --ar 16:9 --q 2"

4. "abstract cybersecurity concept, glowing network protection,
   fortress of light, digital art, gaming inspired,
   dark background with neon, --ar 2:1"

5. "community gaming platform security, diverse gamers,
   protected space, digital community, heroic feeling,
   cinematic lighting, --ar 16:9"
```

## How It Works

```
┌─────────────────────────────────────────────────────────────┐
│  USER INPUT: Technical Brief or Product Description          │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  RESEARCH ANALYZER (5 parallel analyses)                     │
│  • Concept extraction & refinement                          │
│  • Historical timeline matching                             │
│  • Semantic field analysis                                   │
│  • Cultural reference discovery                             │
│  • Emotional & psychological mapping                        │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  METAPHOR ENGINE                                             │
│  • Cross-domain semantic matching                           │
│  • Metaphor relevance scoring                               │
│  • Emotional weight assessment                              │
│  • Historical precedent linking                             │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  VISUAL STYLE INTELLIGENCE                                  │
│  • Style recommendations based on concept                   │
│  • Mood & emotional palette mapping                         │
│  • Color psychology application                             │
│  • Composition principles                                    │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  MIDJOURNEY PROMPT GENERATOR                                │
│  • Template matching based on research                       │
│  • Style parameter insertion                                 │
│  • Multiple variation generation                            │
│  • Technical optimization                                    │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  OUTPUT: Complete Research Document + MJ Prompts            │
│  • Markdown research report                                  │
│  • 5-10 optimized Midjourney prompts                         │
│  • Style recommendations                                     │
│  • Source references                                         │
└─────────────────────────────────────────────────────────────┘
```

## Research Data Files

### research_frameworks.csv

Structured research questions and frameworks:

```csv
domain|framework|key_questions|areas
concept|Five Whys|Why does this exist? Who needs it?|Purpose,Value,Impact,Uniqueness
history|Timeline Analysis|What came before? What's the evolution?|Origins,Movements,Trends,Current State
metaphor|Domain Mapping|What is this like? What does it remind us of?|Nature,Tech,Art,History,Psychology
cultural|Reference Discovery|What cultural moments does this connect to?|Movements,Periods,Symbols,Archetypes
visual|Style Matching|How should this look and feel?|Mood,Era,Aesthetic,Color,Form
```

### metaphor_database.csv

Rich metaphor library with semantic relationships:

```csv
metaphor|source_domain|target_domain|description|emotional_weight|strength
lighthouse|nature|guidance|illuminating path through darkness|hope,trust,clarity|strong
fortress|architecture|protection|secure stronghold against threats|safety,strength,control|strong
garden|nature|growth|cultivated space for flourishing|peace,abundance,nurture|medium
river|nature|flow|constant movement and change|progress,freedom,inevitability|medium
```

### mj_templates.csv

Intelligent prompt templates:

```csv
category|template|key_parameters|weight|context
style|"[concept], [visual_style], [mood], [era], [lighting]"|visual_style,mood,era|high|primary
composition|"[layout], [perspective], [focus], [depth]"|layout,perspective|medium|supporting
emotion|"[emotional_tone], [atmosphere], [feeling]"|emotional_tone|medium|supporting
technical|"[quality], [aspect_ratio], [style_modifiers]"|quality,aspect_ratio|low|optimization
```

## Integration with Claude

The skill auto-activates when you:
- Ask for research on an idea or product
- Request metaphor discovery
- Need visual style recommendations
- Want Midjourney prompts

Works seamlessly with Claude Code, Cursor, Windsurf, and other AI assistants.

## For Developers

See [CLAUDE.md](CLAUDE.md) for detailed architecture, data formats, and development guidelines.

### Contributing

1. Create a branch: `git checkout -b feat/feature-name`
2. Make your changes
3. Commit: `git commit -m "feat: description"`
4. Push: `git push -u origin feat/feature-name`
5. Create a PR

## Data Sources

Research data draws from:
- Historical design and art movements
- Cultural and psychological research
- Semantic and metaphor studies
- Visual design principles
- Linguistic pattern analysis

## License

MIT License - see [LICENSE](LICENSE) file

## Support

For issues, suggestions, or contributions, please open an issue or PR on GitHub.

---

**Made for creatives, researchers, and teams using Midjourney** 🎨✨
