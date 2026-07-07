import math
import pandas as pd
import yfinance as yf


def load_stock_tickers(file_path):
    """
    Load stock tickers from a CSV file.

    The CSV file must contain a column named 'Ticker'.
    """
    stocks = pd.read_csv(file_path)
    return stocks["Ticker"].dropna().tolist()


def get_stock_data(ticker_list):
    """
    Fetch the latest closing price and market capitalization
    for each stock ticker using Yahoo Finance.
    """
    price_data = yf.download(
        ticker_list,
        period="1d",
        group_by="ticker",
        auto_adjust=False,
        progress=False
    )

    stock_records = []

    for ticker in ticker_list:
        try:
            latest_close_price = price_data[ticker]["Close"].iloc[-1]
            market_cap = yf.Ticker(ticker).info.get("marketCap", 0)

            stock_records.append({
                "Ticker": ticker,
                "Market Cap": market_cap,
                "Latest Price": latest_close_price
            })

        except Exception as error:
            print(f"Could not fetch data for {ticker}: {error}")

    return pd.DataFrame(stock_records)


def build_equal_weight_portfolio(stocks_df, portfolio_value, number_of_stocks=10):
    """
    Select the top stocks by market capitalization and calculate
    how many shares to buy for an equal-weight portfolio.
    """
    top_stocks = stocks_df.sort_values(
        by="Market Cap",
        ascending=False
    ).head(number_of_stocks)

    top_stocks = top_stocks.reset_index(drop=True)

    position_size = portfolio_value / len(top_stocks)

    top_stocks["Number of Shares to Buy"] = top_stocks["Latest Price"].apply(
        lambda price: math.floor(position_size / price)
    )

    return top_stocks


def main():
    """
    Main program execution.
    """
    tickers = load_stock_tickers("data/top_50_indian_stocks.csv")

    stocks_df = get_stock_data(tickers)

    portfolio_size = int(input("Enter the amount you want to invest: "))

    portfolio_df = build_equal_weight_portfolio(
        stocks_df,
        portfolio_size,
        number_of_stocks=10
    )

    print("\nEqual Weight Portfolio Recommendation:\n")
    print(portfolio_df)


if __name__ == "__main__":
    main()