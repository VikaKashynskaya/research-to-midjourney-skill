from typing import Dict, List, Any
from pathlib import Path
from datetime import datetime
import json

class ReportGenerator:
    """Generate comprehensive markdown research reports."""
    
    def __init__(self):
        self.timestamp = datetime.now().isoformat()
    
    def generate_report(self, research: Dict[str, Any], filename: str = None) -> str:
        """Generate complete research report."""
        report = self._build_report(research)
        
        if filename:
            Path(filename).write_text(report, encoding='utf-8')
        
        return report
    
    def _build_report(self, research: Dict[str, Any]) -> str:
        """Build markdown report."""
        sections = []
        
        # Header
        sections.append(self._build_header(research))
        
        # Executive Summary
        if "concept" in research:
            sections.append(self._build_executive_summary(research["concept"]))
        
        # Midjourney Prompts
        if "prompts" in research:
            sections.append(self._build_prompts_section(research["prompts"]))
        
        # References
        sections.append(self._build_references_section())
        
        return "\n\n".join(sections)
    
    def _build_header(self, research: Dict) -> str:
        """Build report header."""
        title = research.get("title", "Creative Research Report")
        brief = research.get("brief", "")
        
        return f"""# {title}

**Research Date:** {self.timestamp}

**Brief:** {brief}

---"""
    
    def _build_executive_summary(self, concept: Dict) -> str:
        """Build executive summary."""
        return f"""## Executive Summary

### Core Concept
{concept.get('purpose', 'Undefined')}"""
    
    def _build_prompts_section(self, prompts: List[str]) -> str:
        """Build Midjourney prompts section."""
        content = "## Midjourney Prompts\n\n"
        for i, prompt in enumerate(prompts, 1):
            content += f"""### Variation {i}
```
{prompt}
```

"""
        return content
    
    def _build_references_section(self) -> str:
        """Build references section."""
        return """## References & Sources

- Historical design movements
- Semantic and metaphor research
- Visual design principles
- Cultural and psychological studies
- Creative industry best practices

---

**Report Generated:** Research to Midjourney Skill v1.0"""
