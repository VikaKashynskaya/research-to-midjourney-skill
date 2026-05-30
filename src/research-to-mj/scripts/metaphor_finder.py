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
        """
        Find metaphors for a given concept across domains.
        
        Args:
            concept: The concept to find metaphors for
            sources: List of source domains (nature, technology, art, history, psychology)
                    If None, searches all domains
            
        Returns:
            Dictionary with matched metaphors organized by domain
        """
        if sources is None:
            sources = ["nature", "technology", "art", "history", "psychology"]
        
        found = defaultdict(list)
        concept_lower = concept.lower()
        
        for metaphor in self.metaphors:
            source = metaphor.get("source_domain", "").lower()
            
            # Check if this source domain is in our search list
            if not any(s.lower() in source for s in sources):
                continue
            
            # Check if metaphor relates to the concept
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
        # Check description and target domain
        description = metaphor.get("description", "").lower()
        target = metaphor.get("target_domain", "").lower()
        
        # Simple keyword matching - can be enhanced with NLP
        concept_words = concept.split()
        return any(word.lower() in description or word.lower() in target 
                  for word in concept_words)
    
    def get_emotional_metaphors(self, emotion: str) -> List[Dict[str, str]]:
        """
        Find metaphors associated with specific emotions.
        
        Args:
            emotion: Emotion type (e.g., 'trust', 'innovation', 'security')
            
        Returns:
            List of metaphors matching the emotion
        """
        found = []
        emotion_lower = emotion.lower()
        
        for metaphor in self.metaphors:
            emotional_weight = metaphor.get("emotional_weight", "").lower()
            if emotion_lower in emotional_weight:
                found.append(metaphor)
        
        return found
    
    def get_cross_domain_metaphors(self, concept: str, domain: str) -> List[Dict[str, str]]:
        """
        Find metaphors that link a concept to a specific domain.
        
        Args:
            concept: The concept to map
            domain: Target domain for metaphor mapping
            
        Returns:
            List of metaphors bridging concept to domain
        """
        return [m for m in self.metaphors 
                if domain.lower() in m.get("source_domain", "").lower()]
    
    def get_metaphor_strength_ranking(self, concept: str) -> List[Dict[str, Any]]:
        """
        Get metaphors ranked by relevance strength.
        
        Args:
            concept: The concept to rank metaphors for
            
        Returns:
            List of metaphors sorted by strength
        """
        relevant = self.find_metaphors(concept)
        all_metaphors = []
        
        for domain_metaphors in relevant["metaphors_by_domain"].values():
            all_metaphors.extend(domain_metaphors)
        
        # Sort by strength if available
        strength_order = {"strong": 3, "medium": 2, "weak": 1}
        all_metaphors.sort(
            key=lambda m: strength_order.get(m.get("strength", "").lower(), 0),
            reverse=True
        )
        
        return all_metaphors
    
    def build_metaphor_narrative(self, concept: str, metaphors: List[Dict[str, str]]) -> str:
        """
        Build a narrative description using metaphors.
        
        Args:
            concept: The core concept
            metaphors: List of metaphors to use
            
        Returns:
            Narrative text using metaphors
        """
        if not metaphors:
            return f"The concept of {concept} remains undefined."
        
        narrative = f"The essence of {concept}:\n\n"
        
        for i, metaphor in enumerate(metaphors[:5], 1):
            description = metaphor.get("description", "")
            narrative += f"{i}. {description}\n"
        
        return narrative
    
    def get_metaphor_combinations(self, concept: str, num_combinations: int = 3) -> List[List[Dict]]:
        """
        Generate combinations of metaphors for richer conceptualization.
        
        Args:
            concept: The concept
            num_combinations: Number of combinations to generate
            
        Returns:
            List of metaphor combinations
        """
        all_metaphors = self.get_metaphor_strength_ranking(concept)
        combinations = []
        
        # Create combinations of complementary metaphors
        for i in range(min(num_combinations, len(all_metaphors))):
            combination = []
            
            # Pick one from each domain if possible
            domains_used = set()
            for metaphor in all_metaphors:
                domain = metaphor.get("source_domain", "").lower()
                if domain not in domains_used:
                    combination.append(metaphor)
                    domains_used.add(domain)
                    if len(combination) >= 3:
                        break
            
            if combination:
                combinations.append(combination)
        
        return combinations


def main():
    """Example usage of MetaphorFinder."""
    finder = MetaphorFinder()
    
    # Example: Find metaphors for "fintech innovation"
    print("=== METAPHOR DISCOVERY ===\n")
    
    concept = "fintech innovation"
    print(f"Finding metaphors for: {concept}\n")
    
    # Find metaphors across domains
    result = finder.find_metaphors(concept, sources=["nature", "technology", "history"])
    print(f"Total metaphors found: {result['total_found']}\n")
    
    for domain, metaphors in result["metaphors_by_domain"].items():
        print(f"Domain: {domain.upper()}")
        for metaphor in metaphors:
            print(f"  - {metaphor.get('metaphor', 'N/A')}: {metaphor.get('description', 'N/A')}")
        print()
    
    # Find emotional metaphors
    print("=== EMOTIONAL METAPHORS ===\n")
    emotions = ["trust", "innovation", "security"]
    for emotion in emotions:
        emotional_meta = finder.get_emotional_metaphors(emotion)
        if emotional_meta:
            print(f"{emotion.upper()}:")
            for m in emotional_meta[:2]:
                print(f"  - {m.get('metaphor', 'N/A')}")
            print()
    
    # Get ranked metaphors
    print("=== RANKED METAPHORS (by strength) ===\n")
    ranked = finder.get_metaphor_strength_ranking(concept)
    for i, metaphor in enumerate(ranked[:5], 1):
        strength = metaphor.get("strength", "unknown").upper()
        print(f"{i}. [{strength}] {metaphor.get('metaphor', 'N/A')}")
    print()
    
    # Build narrative
    print("=== METAPHOR NARRATIVE ===\n")
    narrative = finder.build_metaphor_narrative(concept, ranked)
    print(narrative)
    
    # Metaphor combinations
    print("=== METAPHOR COMBINATIONS ===\n")
    combinations = finder.get_metaphor_combinations(concept)
    for i, combo in enumerate(combinations, 1):
        print(f"Combination {i}:")
        for metaphor in combo:
            print(f"  - {metaphor.get('metaphor', 'N/A')} ({metaphor.get('source_domain', 'N/A')})")
        print()


if __name__ == "__main__":
    main()
