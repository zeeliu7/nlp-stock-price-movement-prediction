"""
Generate a dummy financial news dataset for testing the price prediction model.

This script creates a dataset with 12 price change categories using word-aligned vocabulary
for better machine translation performance. News headlines use vocabulary that matches the
output adjectives to facilitate word-to-word learning.

Categories:
- 5 levels of gains (slightly, modestly, moderately, strongly, sharply)
- 5 levels of declines (slightly, modestly, moderately, strongly, sharply)
- 2 levels of stable (edges up slightly, edges down slightly)

Output format: "{ticker} gains sharply." (includes ticker and period)

Usage:
    python generate_dummy_dataset.py
"""

import csv
import random

# Stock tickers to use
TICKERS = [
    "NVDA", "AAPL", "GOOG", "MSFT", "TSLA", "AMZN", "META", "JPM", "V", "UNH",
    "NFLX", "AMD", "INTC", "CSCO", "ORCL", "IBM", "CRM", "ADBE", "PYPL", "QCOM",
    "BA", "CAT", "DIS", "GE", "GM", "F", "WMT", "TGT", "HD", "LOW"
]

# News templates for each category
# Key insight: Use the SAME adjective/verb in news that appears in the output
NEWS_TEMPLATES = {
    # Gains categories - word alignment with output adjectives
    "Gains slightly": [
        "{ticker} edges up slightly on neutral trading session",
        "{ticker} rises slightly after minor positive news",
        "{ticker} advances slightly on low volume trading",
        "{ticker} climbs slightly following small upgrade",
        "{ticker} moves up slightly in quiet session",
    ],
    "Gains modestly": [
        "{ticker} gains modestly on encouraging earnings data",
        "{ticker} rises modestly after positive analyst comment",
        "{ticker} advances modestly following good news",
        "{ticker} climbs modestly on sector strength",
        "{ticker} improves modestly after upbeat guidance",
    ],
    "Gains moderately": [
        "{ticker} gains moderately on strong earnings beat",
        "{ticker} rises moderately after partnership announcement",
        "{ticker} advances moderately following revenue growth",
        "{ticker} climbs moderately on positive outlook",
        "{ticker} rallies moderately after analyst upgrade",
    ],
    "Gains strongly": [
        "{ticker} gains strongly on exceptional quarterly results",
        "{ticker} surges strongly after major deal announcement",
        "{ticker} advances strongly following breakthrough news",
        "{ticker} rallies strongly on impressive profit margins",
        "{ticker} climbs strongly after securing key contract",
    ],
    "Gains sharply": [
        "{ticker} gains sharply on blockbuster earnings surprise",
        "{ticker} surges sharply after transformative acquisition",
        "{ticker} soars sharply following game-changing innovation",
        "{ticker} rallies sharply on explosive revenue growth",
        "{ticker} jumps sharply after landmark partnership deal",
    ],

    # Declines categories - word alignment with output adjectives
    "Declines slightly": [
        "{ticker} edges down slightly on profit-taking",
        "{ticker} dips slightly in light trading session",
        "{ticker} falls slightly on minor concerns",
        "{ticker} slips slightly after neutral news",
        "{ticker} drops slightly on low volume",
    ],
    "Declines modestly": [
        "{ticker} declines modestly on mixed earnings report",
        "{ticker} falls modestly after cautious analyst note",
        "{ticker} drops modestly following weak guidance",
        "{ticker} slips modestly on sector weakness",
        "{ticker} retreats modestly after disappointing data",
    ],
    "Declines moderately": [
        "{ticker} declines moderately on earnings miss",
        "{ticker} falls moderately after analyst downgrade",
        "{ticker} drops moderately following revenue shortfall",
        "{ticker} slides moderately on regulatory concerns",
        "{ticker} weakens moderately after guidance cut",
    ],
    "Declines strongly": [
        "{ticker} declines strongly on major earnings disappointment",
        "{ticker} falls strongly after losing key customer",
        "{ticker} drops strongly following weak outlook",
        "{ticker} slides strongly on significant concerns",
        "{ticker} tumbles strongly after unexpected bad news",
    ],
    "Declines sharply": [
        "{ticker} declines sharply on catastrophic earnings miss",
        "{ticker} plunges sharply after scandal revelation",
        "{ticker} falls sharply following CEO resignation",
        "{ticker} crashes sharply on regulatory probe announcement",
        "{ticker} tumbles sharply after product recall",
    ],

    # Stable categories - minimal movement
    "Edges up slightly": [
        "{ticker} edges up slightly as market remains cautious",
        "{ticker} inches up slightly on mixed sentiment",
        "{ticker} ticks up slightly in range-bound trading",
        "{ticker} rises fractionally in quiet session",
        "{ticker} advances marginally on low volatility",
    ],
    "Edges down slightly": [
        "{ticker} edges down slightly as investors take pause",
        "{ticker} inches down slightly on uncertainty",
        "{ticker} ticks down slightly in sideways trading",
        "{ticker} falls fractionally in quiet session",
        "{ticker} declines marginally on profit-taking",
    ],
}

def generate_dataset(num_samples=1200, output_file="dummy_financial_news.csv"):
    """
    Generate a balanced dummy dataset with financial news and price changes.

    Args:
        num_samples: Total number of examples to generate
        output_file: Output CSV filename
    """
    # Calculate samples per category (balanced distribution)
    categories = list(NEWS_TEMPLATES.keys())
    samples_per_category = num_samples // len(categories)

    data = []

    for category in categories:
        templates = NEWS_TEMPLATES[category]

        for i in range(samples_per_category):
            # Randomly select ticker and template
            ticker = random.choice(TICKERS)
            template = random.choice(templates)

            # Generate news by filling in the ticker and add period
            news = template.format(ticker=ticker) + "."

            # Create the output: "{ticker} {category}." (with period)
            # This matches machine translation format: full sentence in, full sentence out
            change = f"{category}."

            data.append({
                "ticker": ticker,
                "news": news,
                "change": change
            })

    # Shuffle to mix categories
    random.shuffle(data)

    # Write to CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['ticker', 'news', 'change']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"Generated {len(data)} examples in {output_file}")
    print(f"\nCategory distribution (12 categories):")
    for category in categories:
        count = sum(1 for d in data if category in d['change'])
        print(f"  {category}: {count} examples")

    # Show some examples
    print(f"\nSample examples:")
    for i in range(3):
        ex = data[i]
        print(f"\n  News:   {ex['news']}")
        print(f"  Output: {ex['change']}")

if __name__ == "__main__":
    random.seed(42)  # For reproducibility
    generate_dataset(num_samples=1200, output_file="dummy_financial_news_no_ticker.csv")
