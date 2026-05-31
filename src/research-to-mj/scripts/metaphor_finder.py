import csv
from typing import List, Dict, Any
from pathlib import Path
from collections import defaultdict

class MetaphorFinder:
    """Discover and extract metaphors across multiple semantic domains."""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.metaphors = self._load_csv("metaphor_database.csv")
        self.semantic_map = self._build_semantic_map()
    
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
    
    def _build_semantic_map(self) -> Dict[str, List[str]]:
        """Build semantic relationship map."""
        semantic_map = defaultdict(list)
        for metaphor in self.metaphors:
            source = metaphor.get("source_domain", "").lower()
            target = metaphor.get("target_domain", "").lower()
            semantic_map[target].append(metaphor)
        return semantic_map
    
    def find_metaphors(self, concept: str, sources: List[str] = None) -> Dict[str, Any]:
        """Find metaphors for a concept across domains."""
        if sources is None:
            sources = ["nature", "technology", "art", "history", "psychology"]
        
        found = defaultdict(list)
        concept_lower = concept.lower()
        
        for metaphor in self.metaphors:
            source = metaphor.get("source_domain", "").lower()
            if not any(s.lower() in source for s in sources):
                continue
            if self._is_relevant(concept_lower, metaphor):
                found[source].append(metaphor)
        
        return {
            "concept": concept,
            "metaphors_by_domain": dict(found),
            "total_found": sum(len(v) for v in found.values()),
            "domains_searched": sources
        }
    
    def _is_relevant(self, concept: str, metaphor: Dict[str, str]) -> bool:
        """Check if metaphor is relevant to concept."""
        description = metaphor.get("description", "").lower()
        target = metaphor.get("target_domain", "").lower()
        concept_words = concept.split()
        return any(word.lower() in description or word.lower() in target for word in concept_words)
    
    def get_emotional_metaphors(self, emotion: str) -> List[Dict[str, str]]:
        """Find metaphors associated with specific emotions."""
        found = []
        emotion_lower = emotion.lower()
        for metaphor in self.metaphors:
            emotional_weight = metaphor.get("emotional_weight", "").lower()
            if emotion_lower in emotional_weight:
                found.append(metaphor)
        return found
    
    def get_metaphor_strength_ranking(self, concept: str) -> List[Dict[str, Any]]:
        """Get metaphors ranked by relevance strength."""
        relevant = self.find_metaphors(concept)
        all_metaphors = []
        for domain_metaphors in relevant["metaphors_by_domain"].values():
            all_metaphors.extend(domain_metaphors)
        
        strength_order = {"strong": 3, "medium": 2, "weak": 1}
        all_metaphors.sort(
            key=lambda m: strength_order.get(m.get("strength", "").lower(), 0),
            reverse=True
        )
        return all_metaphors
