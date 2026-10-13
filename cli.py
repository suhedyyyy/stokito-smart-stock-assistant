"""Argument-based command-line interface for STOKITO.

Examples:
  python3 cli.py add --name "Notebook" --stock 10 --selling-price 50 --purchase-price 30 --limit 3 --target 20
  python3 cli.py sell --name "Notebook" --quantity 2
  python3 cli.py restock --name "Notebook" --quantity 5
  python3 cli.py list
  python3 cli.py report
  python3 cli.py export --output reports/inventory.csv
"""
import argparse
from main import (
    add_product, export_stock_csv, list_products, load_data, products,
    restock_product, show_reports, sell_product
)


def make_parser():
    parser = argparse.ArgumentParser(description="Manage products, stock, sales, and restocking with STOKITO.")
    commands = parser.add_subparsers(dest="command", required=True)

    add = commands.add_parser("add", help="Register a new product.")
    add.add_argument("--name", required=True)
    add.add_argument("--stock", required=True, type=int)
    add.add_argument("--selling-price", required=True, type=float)
    add.add_argument("--purchase-price", required=True, type=float)
    add.add_argument("--limit", required=True, type=int)
    add.add_argument("--target", required=True, type=int)

    sell = commands.add_parser("sell", help="Sell units of an existing product.")
    sell.add_argument("--name", required=True)
    sell.add_argument("--quantity", required=True, type=int)

    restock = commands.add_parser("restock", help="Increase stock for an existing product.")
    restock.add_argument("--name", required=True)
    restock.add_argument("--quantity", required=True, type=int)

    commands.add_parser("list", help="List all registered products.")
    commands.add_parser("report", help="Show daily revenue and restocking report.")

    export = commands.add_parser("export", help="Export current stock to CSV.")
    export.add_argument("--output", default="reports/stock_report.csv")
    return parser


def main():
    parser = make_parser()
    args = parser.parse_args()
    load_data()
    try:
        if args.command == "add":
            add_product(args.name, args.stock, args.selling_price, args.purchase_price, args.limit, args.target)
            print(f"Added product: {args.name.strip().title()}")
        elif args.command == "sell":
            product, revenue = sell_product(args.name, args.quantity)
            print(f"Sale completed. Revenue: {revenue:.2f} TL. Remaining stock: {product['stock']}.")
        elif args.command == "restock":
            product, cost = restock_product(args.name, args.quantity)
            print(f"Restocked successfully. Added: {args.quantity}. New stock: {product['stock']}. Cost: {cost:.2f} TL.")
        elif args.command == "list":
            list_products()
        elif args.command == "report":
            show_reports()
        elif args.command == "export":
            print(f"Stock report exported to: {export_stock_csv(args.output)}")
    except (ValueError, OSError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
