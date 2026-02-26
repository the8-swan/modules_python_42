import importlib
import sys


def create_data_report():
    import requests as rq
    import pandas as pd
    import matplotlib.pyplot as plt

    print("Fetching Matrix data from the network...")
    URL = (
        "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
        "?vs_currency=usd&days=7&interval=daily"
    )
    response = rq.get(URL)
    data = response.json()
    df = pd.DataFrame(data["prices"], columns=["timestamp", "price"])
    df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
    print(df[["date", "price"]])

    print("\nbasic data manipulation...")
    print("average price", df["price"].mean())
    print("average price", df["price"].max())
    print("lowest price", df["price"].min())

    print("Analysis complete!")
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

    print("Checking dependencies:")
    for module in modules:
        m = importlib.import_module(module)
        print(f"[OK] {module} ({m.__version__})")
    print("")
    create_data_report()
except ModuleNotFoundError:
    print("missing dependencies...\n")
    print("To install using pip:\npip install -r requirements.txt\n")
    print("To install using Poetry:\npoetry install\n")
