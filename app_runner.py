import sys
from config_loader import ConfigLoader
from message_tagger import MessageTagger

class AppRunner:
    """Command-line interface for the message tagging service."""
    
    def __init__(self, config_path: str = "tag_config.json"):
        self.config_path = config_path
        self.tagger = None
        self.config = None
    
    def initialize(self):
        """Load configuration and initialize the tagger service."""
        try:
            print("Loading configuration...")
            loader = ConfigLoader(self.config_path)
            self.config = loader.load()
            print(f"Loaded {len(self.config)} tags: {', '.join(self.config.keys())}")
            self.tagger = MessageTagger(self.config)
            print("✓ Initialization complete\n")
        except FileNotFoundError as e:
            print(f"Error: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Error loading configuration: {e}")
            sys.exit(1)
    
    def run(self):
        """Run the interactive CLI loop."""
        self.initialize()
        
        print("=" * 60)
        print(" Intelligent Chat Message Tagger")
        print("=" * 60)
        print("\nEnter a customer message to analyze.")
        print("Commands: 'debug' , 'quit' - exit\n")
        
        while True:
            try:
                message = input("Message: ").strip()
                
                if message.lower() in ['quit', 'exit', 'q']:
                    print("\nGoodbye!")
                    break
                elif message.lower() == 'debug':
                    self._show_debug_info()
                    continue
                
                if not message:
                    print("Please enter a message.\n")
                    continue
                
                self._analyze_and_display(message)
                print()
                
            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {e}\n")
    
    def _analyze_and_display(self, message: str):
        """Analyze a message and display the results."""
        primary, secondary = self.tagger.analyze_message(message)
        detailed = self.tagger.get_detailed_analysis(message)
        
        print("\n" + "-" * 60)
        print("Results:")
        print("-" * 60)
        print(f"Original Message: {message}")
        print(f"Lemmatized Tokens: {detailed['tokens']}")
        
        if primary:
            print(f" Primary Tag: {primary} (score: {detailed['scores'][primary]:.2f})")
        else:
            print(" Primary Tag: (No match found)")
        
        if secondary:
            print(f" Secondary Tag: {secondary} (score: {detailed['scores'][secondary]:.2f})")
        else:
            print(" Secondary Tag: (No match found)")
        
        print("-" * 60)
    
    def _show_debug_info(self):
        """Show lemmatized configuration for debugging."""
        loader = ConfigLoader(self.config_path)
        config = loader.load()
        print("\n" + "=" * 60)
        print("DEBUG: Lemmatized Configuration")
        print("=" * 60)
        for tag_name, keywords in config.items():
            print(f"\n{tag_name}:")
            print(f"  {keywords}")
        print("\n" + "=" * 60)

def main():
    """Entry point for the application."""
    runner = AppRunner()
    runner.run()

if __name__ == "__main__":
    main()