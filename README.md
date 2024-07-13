# FanCode SDET Assignment

## Setup and Running

1. Clone the repository
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory
   ```
   cd SDET-Assignment-FanCode
   ```
3. Install dependencies
   ```
   pip install -r requirements.txt
   ```
4. Run the main script
   ```
   python main.py
   ```
5. Run tests
   ```
   python -m unittest discover tests
   ```

## Description

This project automates the scenario where users from the city `FanCode` should have more than half of their todos tasks completed.

### Main Script

- `main.py`: Fetches data from APIs and checks the completion percentage for users from `FanCode`.

### Tests

- `tests/test_main.py`: Contains unit tests for the main script.
