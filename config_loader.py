# config_loader.py
import json
import os
from typing import Dict, List, Any

class ConfigLoader:
    """Loads and validates tag configuration from a JSON file."""
    
    def __init__(self, config_path: str = "tag_config.json"):
        self.config_path = config_path
        self.config = None
    
    def load(self) -> Dict[str, List[str]]:
        """Load configuration from JSON file."""
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")
        
        with open(self.config_path, 'r', encoding='utf-8') as f:
            raw_config = json.load(f)
        
        if not self.validate_config(raw_config):
            raise ValueError("Invalid configuration structure")
        
        self.config = raw_config.get('tags', {})
        return self.config
    
    def validate_config(self, config: Dict[str, Any]) -> bool:
        """Validate configuration structure."""
        if not isinstance(config, dict):
            return False
        
        if 'tags' not in config:
            return False
        
        tags = config['tags']
        if not isinstance(tags, dict):
            return False
        
        for tag_name, keywords in tags.items():
            if not isinstance(tag_name, str):  # Now actually using tag_name
                return False
            if not isinstance(keywords, list):
                return False
            if not all(isinstance(kw, str) for kw in keywords):
                return False
        
        return True
    
    def get_tags(self) -> List[str]:
        """Get list of available tag names."""
        if self.config is None:
            raise RuntimeError("Configuration not loaded. Call load() first.")
        return list(self.config.keys())