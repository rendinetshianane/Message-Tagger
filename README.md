 # Intelligent Message Tagger — Proof of Concept

The **Intelligent Message Tagger** is a message classification system based on keywords that performs an analysis of a user message and then applies one or more tags such as Sales, Billing or Support according to the frequency of the keywords and the underlying scoring system. 

---

# Minimum Requirements
**Python:  Version 3.8 or later**

**Libraries: `json`, `os`, `typing`**

**Operating System: Works on Windows, macOS, or Linux**

**Editor (Optional):  VS Code, PyCharm, or any Python IDE**

# Installation Steps

1. Clone or download the repository
2. Open the project folder in your terminal
3. Then run the CLI tool:
```bash
python app_runner.py
```

# High-Level Implementation Details
**1. ConfigLoader**
Handles configuration management and loading of tag definitions from a JSON file.

- Loads tag_config.json

- Validates its structure

- Makes the tag–keyword dictionary available to the message analyzer

Example Config:

{

  "tags": {
  
    "SALES": ["buy", "quote", "plan"],
    
    "BILLING": ["payment", "refund", "invoice"],
    
    "ACCOUNT": ["register", "login", "signup"],

    "GENERAL_INQUIRY": [ "question", "ask", "information",]
    
  }
  
}

**2. MessageTagger**
The core engine that processes the message and assigns the two most relevant tags.

Process Overview:

- Firstly it tokenizes the message text from the user (e.g., "registration is failing" → ["registration", "is", "failing"])
- Matches the tokens to the keywords defined in each tag
- After that it scores each tag based on the number of keywords a certain tag contains in the user message
- Then finally it returns two tags, primary and secondary, primary is the tag with the highest score then secondary is second highest
- Example Flow:

Message: "I want to register for an account"
→ Match: "register" → ACCOUNT
→ Output: Primary Tag = ACCOUNT

**3. AppRunner**
- This file is the command-line interface for running the message tagger.
- Firstly it will load the configuration using ConfigLoader
- Then it will initialize the MessageTagger to start with tagging messages given by the user..
- User input messages will be accepted via the terminal.
- After a user writes their message, the message will be tagged with primary and secondary tags which will be displayed with their scores on the terminal
- Supports extra commands:
  - debug → shows all tags and keywords
  - quit / exit → exits the program

**4. How the Scoring Logic Works**

Each tag is scored based on how many of its keywords appear in the message.

Tokenization:

The message is split into lowercase words.

Example:

"Transacts are a pain" → ['I am not able to make a transaction']

Keyword Matching:

For each tag, the system counts how many defined keywords appear in the message.
Example:

BILLING keywords: [ 
                 "invoice", "payment", "charge", "refund", 
                 "subscription", "billing", "paid", "credit card", 
                 "transaction","receipt", "account", "balance", 
                 "overcharge", "transfer", "fee"
              ],

→ Match: "transaction" ≈ "transaction"

Scoring Formula:

score = matched_keywords / total_keywords

Example: BILLING = 1 / 15 = 0.06

Ranking:

- Tags are sorted by score.
  
- The top tag = Primary, and the next = Secondary.

Example Result:

Message: "Is a refund possible for the payment I made yesterday"

→ Primary Tag: BILLING (0.06)

→ Secondary Tag: None
 
# Acceptance Criteria
Test Case 1
- Input Message: "I want to register for an account"

- Expected Output Tags: ACCOUNT

- Description: Contains keyword “register” and "account"

Test Case 2
- Input Message: "I am unable to get an invoice"

- Expected Output Tags: BILLING

- Description: Contains keyword “invoice” 

Test Case 3
- Input Message: "Can I get a refund for my payment?"

- Expected Output Tags: BILLING

- Description: Contains keywords “refund” and “payment”


# Project Structure
message_tagger/

│

├── pycache            

├── app_runner.py            **# Tag and keyword definitions**

├── config_loader.py         **# Loads and validates configuration**

├── message_tagger.py        **# Core tag analysis logic**

├── tag_config.json          **# Command-line interface entry point**


# Example Usage
python
- from config_loader import ConfigLoader
- from message_tagger import MessageTagger

# Load tag configuration
- loader = ConfigLoader("tag_config.json")
- tag_config = loader.load()

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

# Future Enhancements
Add semantic matching using synonyms (WordNet)

Integrate TF-IDF or cosine similarity scoring

Extend with FastAPI REST endpoint for real-time tagging
