from flask import request
import requests
from shared.portfolio_error import PortfolioError
from shared.stock_service import get_current_stock_price

def register_routes(app):
    @app.route('/capital-gains', methods=['GET'])
    def capital_gains():
        try:
            query_params = request.args.to_dict()
            valid_args = {'numsharesgt', 'numshareslt'}
            provided_args = set(query_params.keys())
            if not provided_args.issubset(valid_args) or len(provided_args) > 2:
                return PortfolioError.malformed_data()

            numshares_gt = int(query_params['numsharesgt']) if 'numsharesgt' in query_params else None
            numshares_lt = int(query_params['numshareslt']) if 'numshareslt' in query_params else None
            
            # use the service name for internal communication
            stocks_service_url = "http://stocks:8000/stocks"

            try:
                response = requests.get(stocks_service_url)
                if response.status_code != 200:
                    return PortfolioError.server_error("Failed to fetch data from stocks service")
                stocks = response.json()
            except requests.RequestException as e:
                return PortfolioError.server_error(f"Failed to connect to stocks service: {e}")
    
            if not isinstance(stocks, list):
                return PortfolioError.server_error("Invalid data format from stocks service")

            filtered_stocks = []
            for stock in stocks:
                if not isinstance(stock, dict):
                    return PortfolioError.server_error(f"Invalid stock format in data. Expected dict but got {type(stock).__name__}")
                shares = stock.get("shares", 0)
                if (numshares_gt is not None and shares <= numshares_gt):
                    continue  
                if (numshares_lt is not None and shares >= numshares_lt):
                    continue
                filtered_stocks.append(stock)
            
            total_gain = calculate_capital_gains(filtered_stocks)
            return str(round(total_gain, 2)), 200

        except Exception as e:
            return PortfolioError.server_error(e)

    def calculate_capital_gains(stocks):
        try:
            total_gain = 0.0
            for stock in stocks:
                try:
                    share_price = get_current_stock_price(stock["symbol"])
                    stock_value = stock["shares"] * share_price
                    purchase_stock_value = stock["shares"] * stock["purchase price"]
                    capital_gain = round(stock_value - purchase_stock_value, 2)
                    total_gain += capital_gain
                except KeyError as ke:
                    raise PortfolioError(f"Missing key in stock data: {ke}", 400, "malformed data")
                except Exception as e:
                    raise PortfolioError(f"Error processing stock {stock.get('symbol', 'unknown')}: {e}", 500,
                                         "server error")
            return total_gain
        except Exception as e:
            raise PortfolioError(f"Unexpected error in capital gains calculation: {e}", 500, "server error")