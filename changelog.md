
V1.0 (2023-03-16)
-----------------
- Initial release of ALICE.
- Simple keyword-based NLP bot that responds to greetings and farewells.

Change Log:

ALICE V1.0: Basic version with keyword-based responses for greetings and farewells.
ALICE V1.1: Added support for Q&A pairs from a JSON file.
ALICE V1.2: Suppressed download messages for the 'punkt' resource.
ALICE V1.3: Improved question matching in find_response function by tokenizing and comparing questions.
ALICE V2.0 Stable: Version with improved question matching and support for Q&A pairs from a JSON file.

# ALICE - Changelog

## [2.4] - 2023-03-16

### Added

- ALICE now reads from AC.json (user-provided knowledge) and uses it to respond to user queries.
- Improved response matching by adding a minimum threshold for common tokens between user input and existing questions.
- Added a check to prevent duplicate information from being added to AC.json.
- Debug messages to help identify issues during development.
- Updated README.md file.

## [2.3] - 2023-03-15

### Added

- Introduced a fallback response mechanism for greetings and farewells when the input doesn't match any existing Q&A pairs.
- Fixed a bug where ALICE was unable to save user explanations to AC.json.
- Updated the code to ALICE V2.3.

## [2.2] - 2023-03-14

### Added

- Implemented a threshold for response matching to prevent unrelated answers.
- Fixed bugs related to missing functions and variable references.
- Updated the code to ALICE V2.2.

## [2.1] - 2023-03-13

### Added

- Initial version of ALICE with basic functionality for responding to user input based on predefined Q&A pairs in SK.json.
- Ability to save user explanations to AC.json when ALICE doesn't understand an input.
