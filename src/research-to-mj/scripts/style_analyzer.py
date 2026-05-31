import csv
from typing import List, Dict, Any
from pathlib import Path

class StyleAnalyzer:
    """Analyze and recommend visual styles based on concepts."""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.styles = self._load_csv("visual_styles.csv")
        self.historical_refs = self._load_csv("historical_references.csv")
    
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
    
    def analyze_style(self, concept: str, mood: str = None) -> Dict[str, Any]:
        """Analyze and recommend visual styles."""
        recommendations = []
        for style in self.styles:
            if mood and mood.lower() not in style.get("mood", "").lower():
                continue
            if self._is_relevant(concept, style):
                recommendations.append(style)
        
        return {
            "concept": concept,
            "mood": mood,
            "recommended_styles": recommendations[:5],
            "mood_keywords": self._extract_keywords(recommendations),
            "color_suggestions": self._extract_colors(recommendations),
            "typography_mood": self._extract_typography(recommendations)
        }
    
    def _is_relevant(self, concept: str, style: Dict[str, str]) -> bool:
        """Check if style is relevant."""
        description = style.get("description", "").lower()
        best_for = style.get("best_for", "").lower()
        return any(word in description or word in best_for for word in concept.lower().split())
    
    def _extract_keywords(self, styles: List[Dict]) -> List[str]:
        """Extract mood keywords."""
        keywords = []
        for style in styles:
            if "keywords" in style:
                keywords.extend(style["keywords"].split(","))
        return list(set(keywords))[:10]
    
    def _extract_colors(self, styles: List[Dict]) -> List[str]:
        """Extract color suggestions."""
        colors = []
        for style in styles:
            if "colors" in style:
                colors.extend(style["colors"].split(","))
        return list(set(colors))[:5]
    
    def _extract_typography(self, styles: List[Dict]) -> str:
        """Extract typography mood."""
        if styles and "typography_mood" in styles[0]:
            return styles[0]["typography_mood"]
        return "Modern, clean, professional"
    
    def get_historical_references(self, style: str) -> List[Dict[str, str]]:
        """Get historical references for a style."""
        return [ref for ref in self.historical_refs if style.lower() in ref.get("style", "").lower()]
