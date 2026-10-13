# STOKITO — Smart Stock Assistant

## Project overview
STOKITO is a Python command-line inventory assistant for small shops. It lets users register products, sell units, restock inventory, track daily sales revenue, identify low stock, calculate the cost of reaching target stock, and export inventory data to CSV.

## Features
- Add products with current stock, selling price, purchase cost, low-stock threshold, and target stock.
- Sell products while validating requested quantities against available stock.
- Restock products and calculate purchase cost.
- Show daily revenue and a per-product restocking report.
- List all registered products and show low-stock status.
- Export current inventory to CSV.
- Save product inventory between runs using JSON files.
- Provide both an interactive menu and an argument-based CLI.

## Requirements
- Python 3.10+ recommended
- No third-party packages required

## Project structure
```text
stokito-smart-stock-assistant/
├── main.py
├── cli.py
├── README.md
├── .gitignore
├── data/
│   ├── products.json
│   └── daily_revenue.json
├── reports/
│   └── .gitkeep
├── contributions/
│   ├── CONTRIBUTION_TEMPLATE.md
│   ├── SUHEDA_KARADAG_2409011037.md
│   ├── BERRA_VILDAN_ERSIN_2409011033.md
│   ├── IREM_TOSUN_2409111009.md
│   ├── EMRE_DEMIR_MUCAHITOGLU_2409011029.md
│   └── OZGUR_OZTURK_2409111041.md
└── tests/
    └── test_stokito.py
```

## Run the interactive menu
From a terminal opened in the project directory:
```bash
python3 main.py
```
On some systems, use `python` instead of `python3`.

## Run the argument-based CLI
Show available commands:
```bash
python3 cli.py --help
```

Add a product:
```bash
python3 cli.py add --name "Notebook" --stock 10 --selling-price 50 --purchase-price 30 --limit 3 --target 20
```

Sell two units:
```bash
python3 cli.py sell --name "Notebook" --quantity 2
```

Restock five units:
```bash
python3 cli.py restock --name "Notebook" --quantity 5
```

List products:
```bash
python3 cli.py list
```

Show the daily revenue and restocking report:
```bash
python3 cli.py report
```

Export inventory:
```bash
python3 cli.py export --output reports/inventory.csv
```

## Data storage
Products are saved in `data/products.json`. Daily revenue is saved with the date in `data/daily_revenue.json`; the revenue counter resets when a new calendar day is detected. The program creates these files when data is saved. CSV reports are saved under `reports/` by default.

## Main functions and technical concepts
- `load_data()` and `save_data()`: JSON persistence and file handling.
- `add_product()`: validates product data and registers a new product.
- `sell_product()`: checks available stock, reduces quantity, and updates revenue.
- `restock_product()`: increases stock and calculates purchase cost.
- `show_reports()`: calculates required restocking quantities and costs.
- `export_stock_csv()`: writes inventory rows using Python's `csv` module.
- `make_parser()` in `cli.py`: defines command-line commands and arguments using `argparse`.
- `try/except`: handles invalid user input and file errors.
- Dictionaries and loops: store and iterate through product records.

## Validation and limitations
The application rejects empty or duplicate product names, negative stock and price values, non-positive sale/restock quantities, and sales exceeding available stock. This is an educational prototype. It does not connect to a real point-of-sale system or database. Daily revenue is tracked for the current day only, not as a full historical sales ledger.

## Team contributions
Each team member must review their individual contribution file and replace the placeholder with their actual work. The template files are included to help standardize the format. Do not claim contributions that were not completed. The instructor's email asks for a public GitHub repository and a separate contribution file for every team member.
