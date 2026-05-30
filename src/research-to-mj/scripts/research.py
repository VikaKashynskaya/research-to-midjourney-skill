import csv
import json
from typing import List, Dict, Any
from pathlib import Path

class ResearchAnalyzer:
    """Main research analyzer for concept exploration and idea generation."""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.frameworks = self._load_csv("research_frameworks.csv")
        self.metaphors = self._load_csv("metaphor_database.csv")
        self.styles = self._load_csv("visual_styles.csv")
        self.mj_templates = self._load_csv("mj_templates.csv")
    
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
    
    def analyze_concept(self, brief: str) -> Dict[str, Any]:
        """
        Analyze the core concept from a technical brief.
        
        Args:
            brief: Technical brief or product description
            
        Returns:
            Dictionary with concept analysis
        """
        return {
            "brief": brief,
            "analysis": {
                "purpose": self._extract_purpose(brief),
                "values": self._extract_values(brief),
                "target_audience": self._extract_audience(brief),
                "innovation_angle": self._extract_innovation(brief)
            }
        }
    
    def find_historical_context(self, brief: str) -> Dict[str, Any]:
        """
        Find historical context and precedents.
        
        Args:
            brief: Technical brief
            
        Returns:
            Dictionary with historical analysis
        """
        return {
            "historical_precedents": self._match_frameworks(brief, "history"),
            "relevant_periods": self._extract_periods(brief),
            "evolution_timeline": self._build_timeline(brief)
        }
    
    def discover_metaphors(self, concept: str, sources: List[str] = None) -> Dict[str, Any]:
        """
        Discover metaphors across multiple domains.
        
        Args:
            concept: Core concept to find metaphors for
            sources: List of domains (nature, tech, art, history, psychology)
            
        Returns:
            Dictionary with metaphor suggestions
        """
        if sources is None:
            sources = ["nature", "technology", "art", "history", "psychology"]
        
        metaphors_found = []
        for metaphor in self.metaphors:
            if any(source.lower() in metaphor.get("source_domain", "").lower() 
                   for source in sources):
                metaphors_found.append(metaphor)
        
        return {
            "concept": concept,
            "metaphors": metaphors_found,
            "sources": sources
        }
    
    def analyze_visual_style(self, concept: str, mood: str = None) -> Dict[str, Any]:
        """
        Analyze and recommend visual styles.
        
        Args:
            concept: Core concept
            mood: Optional mood/emotion filter
            
        Returns:
            Dictionary with style recommendations
        """
        recommendations = []
        
        for style in self.styles:
            if mood and mood.lower() not in style.get("mood", "").lower():
                continue
            recommendations.append(style)
        
        return {
            "concept": concept,
            "mood": mood,
            "recommended_styles": recommendations,
            "mood_keywords": self._extract_mood_keywords(recommendations)
        }
    
    def generate_mj_prompts(self, research: Dict[str, Any], variations: int = 5) -> List[str]:
        """
        Generate Midjourney prompts based on research.
        
        Args:
            research: Research analysis dictionary
            variations: Number of prompt variations to generate
            
        Returns:
            List of MJ prompts
        """
        prompts = []
        
        for i in range(variations):
            template = self.mj_templates[i % len(self.mj_templates)] if self.mj_templates else {}
            
            # Build prompt from template and research
            prompt = self._build_prompt(research, template)
            prompts.append(prompt)
        
        return prompts
    
    # Private helper methods
    def _extract_purpose(self, brief: str) -> str:
        """Extract purpose from brief."""
        # Simple keyword matching - can be enhanced with NLP
        keywords = ["purpose", "goal", "aim", "objective", "mission"]
        for keyword in keywords:
            if keyword.lower() in brief.lower():
                return brief  # Placeholder
        return "Undefined purpose"
    
    def _extract_values(self, brief: str) -> List[str]:
        """Extract core values."""
        value_keywords = ["trust", "innovation", "reliability", "creativity", "sustainability", 
                         "security", "accessibility", "quality", "transparency", "community"]
        found_values = []
        for value in value_keywords:
            if value.lower() in brief.lower():
                found_values.append(value)
        return found_values
    
    def _extract_audience(self, brief: str) -> str:
        """Extract target audience."""
        return "Target audience analysis"
    
    def _extract_innovation(self, brief: str) -> str:
        """Extract innovation angle."""
        return "Innovation analysis"
    
    def _match_frameworks(self, brief: str, domain: str) -> List[Dict]:
        """Match analysis frameworks."""
        return [f for f in self.frameworks if f.get("domain", "").lower() == domain.lower()]
    
    def _extract_periods(self, brief: str) -> List[str]:
        """Extract relevant historical periods."""
        periods = ["Renaissance", "Industrial Revolution", "Digital Age", "Post-Modern", "Contemporary"]
        return [p for p in periods if any(word in brief for word in brief.split())]
    
    def _build_timeline(self, brief: str) -> Dict[str, str]:
        """Build evolution timeline."""
        return {
            "origin": "Historical origin",
            "evolution": "How concept evolved",
            "current_state": "Current manifestation"
        }
    
    def _extract_mood_keywords(self, styles: List[Dict]) -> List[str]:
        """Extract mood keywords from styles."""
        keywords = []
        for style in styles:
            if "mood" in style:
                keywords.extend(style["mood"].split(","))
        return list(set(keywords))
    
    def _build_prompt(self, research: Dict[str, Any], template: Dict[str, str]) -> str:
        """Build MJ prompt from template and research."""
        # Placeholder prompt building
        return f"Research-based prompt for concept: {research}"


def main():
    """Example usage of ResearchAnalyzer."""
    analyzer = ResearchAnalyzer()
    
    # Example brief
    brief = "Build a modern fintech app for Gen Z users with focus on trust and innovation"
    
    # Run analysis
    concept = analyzer.analyze_concept(brief)
    history = analyzer.find_historical_context(brief)
    metaphors = analyzer.discover_metaphors("fintech innovation")
    style = analyzer.analyze_visual_style("modern fintech", mood="trust")
    prompts = analyzer.generate_mj_prompts({"brief": brief}, variations=5)
    
    print("=== RESEARCH ANALYSIS ===")
    print(json.dumps(concept, indent=2))
    print("\n=== HISTORICAL CONTEXT ===")
    print(json.dumps(history, indent=2))
    print("\n=== METAPHORS ===")
    print(json.dumps(metaphors, indent=2))
    print("\n=== VISUAL STYLE ===")
    print(json.dumps(style, indent=2))
    print("\n=== MIDJOURNEY PROMPTS ===")
    for i, prompt in enumerate(prompts, 1):
        print(f"{i}. {prompt}")


if __name__ == "__main__":
    main()
