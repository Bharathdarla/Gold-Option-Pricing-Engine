"""
This module contains the core option pricing models. Starting with the classic Black-Scholes.
Eventually, I want to add more complex models like Binomial Trees and Monte Carlo simulations.
"""

import numpy as np
from scipy.stats import norm

def black_scholes_gold(S, K, T, r, sigma, option_type='call'):
    """
    Calculates the Black-Scholes price for a European-style Gold Option.
    
    This is the foundational model, great for understanding the basics.
    It assumes a few things that aren't always true in real life (like constant volatility),
    but it's a solid starting point!

    Parameters:
    S (float): Current Gold Price (XAU/USD) - gotta get this live!
    K (float): Strike Price - the price we can buy/sell at.
    T (float): Time to Expiration (in years) - careful with units here, always convert days to years.
    r (float): Risk-free Interest Rate (e.g., 0.04 for 4%) - usually a government bond yield.
    sigma (float): Volatility of Gold (e.g., 0.15 for 15%) - this is a tricky one to estimate!
    option_type (str): 'call' or 'put' - determines if we're buying or selling the right.
    
    Returns:
    float: The theoretical option price.
    """
    
    # Handle options that are already expired or expiring today (T=0)
    # If T is zero or negative, the option's value is just its intrinsic value.
    if T <= 0:
        if option_type == 'call':
            return max(0, S - K)
        else:
            return max(0, K - S)

    # Calculate d1 and d2 - these are the core components of the BSM formula.
    # They represent probabilities in the normal distribution.
    # Had to double-check these formulas a few times to make sure they were right!
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    # Now, apply the actual Black-Scholes formula based on option type.
    # norm.cdf is the cumulative distribution function for a standard normal distribution.
    if option_type == 'call':
        price = (S * norm.cdf(d1)) - (K * np.exp(-r * T) * norm.cdf(d2))
    elif option_type == 'put':
        price = (K * np.exp(-r * T) * norm.cdf(-d2)) - (S * norm.cdf(-d1))
    else:
        # Basic error handling - good practice!
        raise ValueError("Oops! Invalid option type. Please use 'call' or 'put'.")
        
    return price

# TODO: Next up, implement the Binomial Tree model for American options!
# That one's a bit more involved with building a tree structure.
# Also, need to think about how to handle dividends for gold ETFs if I expand to those.
