"""
This is the main application file for my Gold Option Pricing Engine!
I'm using Streamlit to create a simple, interactive web interface.
It's pretty cool how quickly you can get a UI up and running with Streamlit.

My goal here is to make it easy for anyone (including myself!) to play around
with the Black-Scholes model for gold options and see how different inputs
affect the price. Eventually, I want to add more models and maybe even some charts!
"""

import streamlit as st
import os
from pricing_models import black_scholes_gold
from data_handler import get_gold_price, get_risk_free_rate

# Basic page configuration - just making it look a bit nicer.
st.set_page_config(page_title="My Gold Option Pricing Playground", layout="centered")

st.title("🪙 My Gold Option Pricing Playground")
st.markdown("--- ")

# --- API Key Input (Super Important for Live Data!) ---
st.sidebar.header("Configuration")
alpha_vantage_api_key = st.sidebar.text_input(
    "Alpha Vantage API Key", 
    type="password", 
    help="Grab your free API key from alphavantage.co. It's essential for live gold prices!"
)

# --- Live Market Data Section ---
st.header("Live Gold Price & Market Data")
st.write("Let's get the latest gold price! This uses Alpha Vantage, so your API key is needed.")

# Using a button to fetch data, so it doesn't hit the API on every little change.
if st.button("Fetch Latest Gold Price"): 
    if alpha_vantage_api_key:
        with st.spinner("Fetching gold price... this might take a second."):
            live_gold_price = get_gold_price(alpha_vantage_api_key)
            if live_gold_price:
                st.session_state["gold_price"] = live_gold_price # Storing in session_state so it persists!
                st.success(f"Got it! Live Gold Price: ${live_gold_price:.2f}")
            else:
                st.error("Couldn't fetch live gold price. Double-check your API key or internet connection!")
    else:
        st.warning("Hey, don't forget to enter your Alpha Vantage API Key in the sidebar to fetch live data!")

# Displaying the gold price. If we fetched it, it'll show that; otherwise, a default.
# Users can also manually override it, which is handy for testing different scenarios.
default_gold_price = st.session_state.get("gold_price", 2350.0) # Starting with a reasonable default.
current_gold_price = st.number_input(
    "Current Gold Price (XAU/USD)", 
    min_value=0.01, 
    value=default_gold_price, 
    step=1.0,
    format="%.2f",
    help="This is the current price of gold. You can fetch it live or enter it manually."
)

# The risk-free rate is hardcoded for now, but I'd love to make this dynamic later.
risk_free_rate = get_risk_free_rate()
st.info(f"Risk-Free Rate (Currently a placeholder): {risk_free_rate*100:.2f}%")

st.markdown("--- ")

# --- Option Parameters Section ---
st.header("Set Your Option Parameters")
st.write("Time to define the option you want to price!")

strike_price = st.number_input(
    "Strike Price (K)", 
    min_value=0.01, 
    value=current_gold_price, # Defaulting to current gold price is a good starting point.
    step=1.0,
    format="%.2f",
    help="The price at which the option holder can buy (call) or sell (put) the underlying gold."
)

time_to_expiry_days = st.number_input(
    "Time to Expiration (in Days)", 
    min_value=1, 
    value=30, 
    step=1,
    help="How many days until the option expires? (Converted to years for the model)"
)
time_to_expiry_years = time_to_expiry_days / 365.0 # Black-Scholes needs years, not days!

volatility = st.slider(
    "Volatility (Sigma)", 
    min_value=0.01, 
    max_value=1.0, 
    value=0.15, 
    step=0.01,
    format="%.2f",
    help="This is the tricky part! It's the expected fluctuation of gold's price. 0.15 means 15% annual volatility."
)

option_type = st.radio(
    "Option Type", 
    ("Call", "Put"), 
    index=0,
    help="Call gives the right to buy, Put gives the right to sell."
).lower()

st.markdown("--- ")

# --- Calculate Option Price Section ---
st.header("Calculate & See the Results!")
st.write("Hit the button to crunch the numbers using the Black-Scholes model.")

if st.button("Calculate Option Price"): 
    try:
        # Calling my pricing model function from pricing_models.py
        call_premium = black_scholes_gold(
            current_gold_price, 
            strike_price, 
            time_to_expiry_years, 
            risk_free_rate, 
            volatility, 
            'call'
        )
        put_premium = black_scholes_gold(
            current_gold_price, 
            strike_price, 
            time_to_expiry_years, 
            risk_free_rate, 
            volatility, 
            'put'
        )

        st.subheader("Black-Scholes Model Says...")
        st.write(f"**Theoretical Call Option Price:** ${call_premium:.2f}")
        st.write(f"**Theoretical Put Option Price:** ${put_premium:.2f}")

        # Highlighting the selected option type's price.
        if option_type == 'call':
            st.success(f"Your selected **{option_type.capitalize()} Option Price:** ${call_premium:.2f}")
        else:
            st.success(f"Your selected **{option_type.capitalize()} Option Price:** ${put_premium:.2f}")

    except ValueError as e:
        st.error(f"Calculation Error: {e}. Make sure all your inputs are valid!")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}. This is why we test! :(")

st.markdown("--- ")
st.caption("**Important Note:** This is a personal learning project and a simplified model. Please don't use this for actual trading decisions! Always do your own research and consult with financial pros. Options are complex!")
