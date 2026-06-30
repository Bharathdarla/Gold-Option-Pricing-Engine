"""
This module is all about getting the data we need for our option pricing! 
Right now, it focuses on fetching live gold prices and providing a risk-free rate.
Getting reliable, free data is always a bit of a challenge, but Alpha Vantage is a good start.
"""

import requests
import os

def get_gold_price(api_key):
    """
    Tries to grab the latest spot price for Gold (XAU) using the Alpha Vantage API.
    
    Honestly, finding a good, free API for real-time gold prices was tougher than I thought!
    Alpha Vantage seems decent for personal projects, but gotta be mindful of their rate limits.

    Parameters:
    api_key (str): Your personal Alpha Vantage API key. Keep this secret!
    
    Returns:
    float: The current gold price in USD, or None if something goes wrong.
    """
    # Alpha Vantage uses 'XAU' for gold. Good to know!
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=XAU&apikey={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # This is super important to catch HTTP errors!
        data = response.json()
        
        # Navigating nested JSON can be a bit fiddly, but this seems to work for Alpha Vantage.
        if "Global Quote" in data and "05. price" in data["Global Quote"]:
            gold_price = float(data["Global Quote"]["05. price"])
            return gold_price
        else:
            # If the API doesn't return what we expect, it's good to print the full response for debugging.
            print(f"Error: Couldn't get the gold price. API response was a bit weird: {data}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Network or API error while fetching gold price: {e}")
        return None
    except ValueError as e:
        print(f"Problem converting the price to a number (maybe the API sent something unexpected?): {e}")
        return None

def get_risk_free_rate():
    """
    Returns a placeholder for the risk-free interest rate.
    
    Ideally, this would come from a live source like the FRED API for the 10-year Treasury yield.
    But for now, a hardcoded value is fine for testing. It's a simplification, but hey, it's a start!
    """
    # Using a slightly arbitrary value for now. Real-world would need more dynamic fetching.
    return 0.045 # Let's assume 4.5% for now. It changes, but this is a good average.


if __name__ == "__main__":
    # This block runs only when you execute data_handler.py directly.
    # Super useful for quick tests without running the whole Streamlit app.
    print("--- Testing Data Handler --- ")
    my_api_key = os.getenv("ALPHA_VANTAGE_API_KEY") 
    if not my_api_key:
        print("WARNING: ALPHA_VANTAGE_API_KEY environment variable not set. Live data fetching will fail.")
        print("Please set it up! (e.g., export ALPHA_VANTAGE_API_KEY=\"YOUR_KEY\")")
    else:
        print("Attempting to fetch live gold price...")
        current_gold_price = get_gold_price(my_api_key)
        if current_gold_price:
            print(f"Fetched Gold Price: ${current_gold_price:.2f}")
        else:
            print("Could not fetch live gold price. Using a dummy value for demonstration.")
            current_gold_price = 2300.0 # Fallback for testing
        
        rfr = get_risk_free_rate()
        print(f"Using Risk-Free Rate: {rfr*100:.2f}%")
    print("--- Data Handler Test Complete ---")
