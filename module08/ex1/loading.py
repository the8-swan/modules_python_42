import importlib
import sys


def create_data_report():
    # importing here instead of the top of the file
    # so the program can check dependencies first before trying to use them
    import requests as rq
    import pandas as pd
    import matplotlib.pyplot as plt

    print("Fetching Matrix data from the network...")

    # the API returns bitcoin price history for the last 7 days in USD
    URL = (
        "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
        "?vs_currency=usd&days=7&interval=daily"
    )

    # send a GET request to the API and parse the JSON response into a dict
    response = rq.get(URL)
    data = response.json()

    # data["prices"] is a list of [timestamp_ms, price] pairs
    # we turn it into a DataFrame with two named columns
    df = pd.DataFrame(data["prices"], columns=["timestamp", "price"])

    # the timestamp is in milliseconds, we convert it to a readable date
    df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
    print(df[["date", "price"]])

    # basic pandas statistics on the price column
    print("\nbasic data manipulation...")
    print("average price", df["price"].mean())
    print("average price", df["price"].max())
    print("lowest price", df["price"].min())

    print("Analysis complete!")

    # plot the price over time and save it as a PNG file
    print("\nmatplotlib plot")
    plt.plot(df["date"], df["price"])
    plt.title("Bitcoin - Last 7 Days")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.savefig("matrix_analysis.png")
    print("Results saved to: matrix_analysis.png")


modules = ["pandas", "requests", "matplotlib", "numpy"]
try:
    print("LOADING STATUS: Loading programs...\n")

    # loop through each required module and try to import it
    # if it's found, print its version — if any one is missing we jump to except
    print("Checking dependencies:")
    for module in modules:
        m = importlib.import_module(module)
        print(f"[OK] {module} ({m.__version__})")
    print("")

    create_data_report()

except ModuleNotFoundError:
    # one or more packages are not installed, tell the user how to fix it
    print("missing dependencies...\n")
    print("To install using pip:\npip install -r requirements.txt\n")
    print("To install using Poetry:\npoetry install\n")