# Indian Stock Equal-Weight Portfolio Builder

A Python-based portfolio allocation tool that constructs an **equal-weight investment strategy** using the top Indian stocks by market capitalization.

The application reads stock tickers from a CSV file, retrieves real-time market data from Yahoo Finance, ranks companies by market capitalization, and calculates the number of shares to purchase for each selected stock based on a user-defined investment amount.

## Features

* Load stock tickers from a CSV dataset
* Retrieve the latest closing prices using Yahoo Finance
* Fetch market capitalization for each company
* Rank stocks by market capitalization
* Select the top 10 companies
* Allocate the investment amount equally across the selected stocks
* Calculate the number of shares to purchase using whole-share allocation
* Display the final portfolio in a clean tabular format

## Technologies Used

* Python 3
* Pandas
* NumPy
* yFinance


## Installation

```bash
python -m venv venv
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python equal_weight_portfolio.py
```
## Learning Objectives

This project demonstrates practical experience with:

* Python programming
* Data manipulation using Pandas
* Financial data retrieval with yFinance
* Working with CSV datasets
* Function-based program design
* Basic portfolio allocation strategies

## Acknowledgements

This project was inspired by a public YouTube tutorial on building an equal-weight stock portfolio. The implementation has been independently refactored with improved code organization, modular functions, documentation, comments, and project structure as part of my Python learning journey.