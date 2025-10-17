# message_tagger.py
import re
from typing import Dict, List, Tuple, Optional

class MessageTagger:
    """Analyzes messages and assigns relevant tags based on keyword scoring."""
    
    def __init__(self, tag_config: Dict[str, List[str]]):
        self.tag_config = tag_config
        self.tags = list(tag_config.keys())
    
    def analyze_message(self, message_text: str) -> Tuple[Optional[str], Optional[str]]:
        """Analyze a message and return the top 2 most relevant tags."""
        if not message_text or not message_text.strip():
            return (None, None)
        
        tokens = self._tokenize(message_text)
        scores = self._score_tags(tokens)
        
        ranked_tags = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        ranked_tags = [(tag, score) for tag, score in ranked_tags if score > 0]
        
        primary = ranked_tags[0][0] if len(ranked_tags) > 0 else None
        secondary = ranked_tags[1][0] if len(ranked_tags) > 1 else None
        
        return (primary, secondary)
    
    def _tokenize(self, text: str) -> List[str]:
        """Tokenize text into lowercase words."""
        text = text.lower()
        tokens = re.findall(r'\b\w+\b', text)
        return tokens
    
    def _score_tags(self, tokens: List[str]) -> Dict[str, float]:
        """Score each tag based on keyword matches in the tokens."""
        scores = {}
        
        for tag_name, keywords in self.tag_config.items():
            if not keywords:
                scores[tag_name] = 0.0
                continue
            
            matches = sum(1 for keyword in keywords if keyword.lower() in tokens)
            score = matches / len(keywords) if keywords else 0.0
            scores[tag_name] = score
        
        return scores
    
    def get_detailed_analysis(self, message_text: str) -> Dict[str, any]:
        """Get detailed analysis including all scores."""
        tokens = self._tokenize(message_text)
        scores = self._score_tags(tokens)
        primary, secondary = self.analyze_message(message_text)
        
        return {
            'tokens': tokens,
            'scores': scores,
            'primary_tag': primary,
            'secondary_tag': secondary
        }