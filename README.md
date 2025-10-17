# 💬 Intelligent Message Tagger — Proof of Concept

A lightweight **keyword-based message classification system** that analyzes user messages and assigns relevant tags such as *Sales*, *Billing*, or *Support* based on keyword frequency and scoring.

---

## ⚙️ Minimum Requirements
**Python** | Version 3.8 or later |
**Libraries** | `nltk`, `json`, `os`, `typing` |
**Operating System** | Works on Windows, macOS, or Linux |
**Editor (Optional)** | VS Code, PyCharm, or any Python IDE |

### 🧩 Installation Steps

1. Clone or download the repository  
2. Open the project folder in your terminal  
3. Run:
   ```bash
   pip install nltk
Then run the CLI tool:
python app_runner.py

# # #🏗️ High-Level Implementation Details
**🗂️ 1. ConfigLoader**
Handles configuration management and loading of tag definitions from a JSON file.

Loads tag_config.json

Validates its structure

Makes the tag–keyword dictionary available to the message analyzer

Example Config:
{
  "tags": {
    "SALES": ["buy", "quote", "plan"],
    "BILLING": ["payment", "refund", "invoice"],
    "ACCOUNT": ["register", "login", "signup"]
  }
}

**💡 2. MessageTagger**
The core engine that processes the message and assigns the two most relevant tags.

Process Overview:

--Tokenizes message text (e.g., "registration is failing" → ["registration", "is", "failing"])
--Matches keywords defined for each tag
--Scores each tag based on number of keyword hits
--Returns Primary (highest score) and Secondary (next highest) tag
--Example Flow:

Message: "I want to register for an account"
→ Match: "register" → ACCOUNT
→ Output: Primary Tag = ACCOUNT
## #🧪 Acceptance Criteria
Test Case	Input Message	Expected Output Tags	Description
✅ 1	"I want to register for an account"	ACCOUNT	Contains keyword “register”
✅ 2	"Transacts are a pain in the ass"	BILLING	Contains keyword “transact” (related to billing)
✅ 3	"Can I get a refund for my payment?"	BILLING	Contains “refund” and “payment”

✔️ All three cases must return the correct Primary Tag for project completion.

## #📂 Project Structure
message_tagger/
│
├── tag_config.json          # Tag and keyword definitions
├── config_loader.py         # Loads and validates configuration
├── message_tagger.py        # Core tag analysis logic
├── cli_runner.py            # Command-line interface entry point
└── README.md                # Documentation (this file)

# 🚀 Example Usage
pythone
from config_loader import ConfigLoader
from message_tagger import MessageTagger

# Load tag configuration
loader = ConfigLoader("tag_config.json")
tag_config = loader.load()

# Initialize tagger
tagger = MessageTagger(tag_config)

# Analyze a message
message = "Registration is failing again"
primary, secondary = tagger.analyze_message(message)

print("Primary Tag:", primary)
print("Secondary Tag:", secondary)
Expected Output:

Primary Tag: ACCOUNT
Secondary Tag: None

# 🧩 Future Enhancements
🔍 Add semantic matching using synonyms (WordNet)

🧠 Integrate TF-IDF or cosine similarity scoring

⚙️ Extend with FastAPI REST endpoint for real-time tagging
