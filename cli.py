import argparse
import logging
from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_side, validate_order_type
from bot.logging_config import setup_logger

setup_logger()

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_side(args.side)
        validate_order_type(args.type)

        print("Placing order...")
        logging.info(f"Request: {args}")

        if args.type == "MARKET":
            res = place_market_order(args.symbol, args.side, args.quantity)
        else:
            if not args.price:
                raise ValueError("Price required for LIMIT order")
            res = place_limit_order(args.symbol, args.side, args.quantity, args.price)

        print("Order Success!")
        print(res)

        logging.info(f"Response: {res}")

    except Exception as e:
        print("Error:", e)
        logging.error(str(e))

if __name__ == "__main__":
    main()
