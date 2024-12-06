# Aritzia Outfit Matcher

A script to check size availability for Aritzia sweats and hoodies, matching items by color and size to help you create matching outfit combinations.

## Features
- Checks size availability for two types of sweats and two types of hoodies.
- Matches sweats and hoodies of the same color.
- Filters results by specified sizes.

## Prerequisites
- Python 3.x
- Required libraries:
  - `requests`
  - `beautifulsoup4`

Install dependencies:
```bash
pip install requests beautifulsoup4
 ```

## How to Use

1. Clone the repository:
    ```bash
    git clone https://github.com/achchala/aritzia-outfit-matcher.git
    ```

2. Navigate to the project directory:
    ```bash
    cd aritzia-outfit-matcher
    ```

3. Check and update the `sweats_urls` and `hoodies_urls` lists in the script with up-to-date Aritzia product URLs.

4. Run the script:
    ```bash
    python aritzia_outfit_matcher.py
    ```

5. View the results for matching sweats and hoodies by color and size.

## Output

- The script will display matching colors and sizes:
    ```yaml
    Matching items found:
    Color: Black, Sizes: S, M
    Color: Heather Grey, Sizes: L
    ```
