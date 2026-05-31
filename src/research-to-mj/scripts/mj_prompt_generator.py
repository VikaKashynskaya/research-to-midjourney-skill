import csv
import random
from typing import List, Dict, Any
from pathlib import Path

class MJPromptGenerator:
    """Generate optimized Midjourney prompts based on research."""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.templates = self._load_csv("mj_templates.csv")
    
    def _load_csv(self, filename: str) -> List[Dict[str, str]]:
        """Load CSV data file."""
        filepath = self.data_dir / filename
        if not filepath.exists():
            return []
        data = []
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter='|')
            for row in reader:
                data.append(row)
        return data
    
    def generate_prompts(self, research: Dict[str, Any], variations: int = 5) -> List[str]:
        """Generate multiple Midjourney prompt variations."""
        prompts = []
        
        # Extract key info from research
        concept = research.get("concept", "")
        style = research.get("style", "")
        mood = research.get("mood", "")
        metaphors = research.get("metaphors", [])
        
        for i in range(variations):
            prompt = self._build_prompt(concept, style, mood, metaphors, i)
            prompts.append(prompt)
        
        return prompts
    
    def _build_prompt(self, concept: str, style: str, mood: str, metaphors: List[str], index: int) -> str:
        """Build individual MJ prompt."""
        # Base structure
        prompt_parts = []
        
        # Main subject
        prompt_parts.append(concept)
        
        # Style and mood
        if style:
            prompt_parts.append(style)
        if mood:
            prompt_parts.append(f"{mood} mood")
        
        # Add metaphor if available
        if metaphors and index < len(metaphors):
            prompt_parts.append(f"inspired by {metaphors[index]}")
        
        # Add quality parameters
        if index % 2 == 0:
            prompt_parts.append("--q 2")
        
        # Add aspect ratio
        aspect_ratios = ["--ar 16:9", "--ar 1:1", "--ar 2:1", "--ar 4:3"]
        prompt_parts.append(aspect_ratios[index % len(aspect_ratios)])
        
        return ", ".join(prompt_parts)
    
    def generate_hero_prompts(self, concept: str, style: str, mood: str) -> List[str]:
        """Generate hero section prompts."""
        hero_templates = [
            f"{concept}, {style} design, {mood} feeling, hero section, --ar 16:9 --q 2",
            f"premium {concept}, {style}, {mood}, cinematic hero, --ar 16:9 --q 2",
            f"{concept} showcase, {style} aesthetic, {mood} atmosphere, --ar 16:9"
        ]
        return hero_templates[:3]
    
    def generate_supporting_prompts(self, metaphors: List[str]) -> List[str]:
        """Generate supporting visual prompts based on metaphors."""
        prompts = []
        for metaphor in metaphors[:3]:
            prompt = f"{metaphor}, illustration style, editorial, --ar 1:1"
            prompts.append(prompt)
        return prompts
    
    def generate_with_fallbacks(self, concept: str, style: str) -> Dict[str, List[str]]:
        """Generate prompts with fallback options."""
        return {
            "primary": [f"{concept}, {style}, professional, --q 2 --ar 16:9"],
            "secondary": [f"{concept}, {style}, artistic, --ar 1:1"],
            "fallback": [f"{concept}, minimalist, clean design, --ar 16:9"]
        }
