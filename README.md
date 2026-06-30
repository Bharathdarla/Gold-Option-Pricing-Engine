# My Gold Option Pricing Playground 🪙

Hey there! Welcome to my little project where I'm diving into the fascinating world of option pricing, starting with gold. This isn't some fancy institutional software; it's my personal learning journey to understand how options are valued, built with Python and a dash of Streamlit magic.

## What's This All About?

I've always been curious about financial derivatives, and options are particularly intriguing. This project is my attempt to build a basic **Option Pricing Engine** specifically for **Gold (XAU/USD)**. I'm kicking things off with the classic **Black-Scholes-Merton (BSM) model** because it's foundational, even if it has its limitations in the real world.

### Current Features (My First Steps!)

*   **Black-Scholes Model:** I've implemented the math for European Call and Put options on gold. It's a great way to see the theoretical price.
*   **Live Gold Price Fetcher:** I've hooked it up to the Alpha Vantage API to pull in real-time XAU/USD spot prices. Getting live data was a fun challenge!
*   **Interactive Web UI:** Thanks to Streamlit, I've got a simple web interface where you can tweak parameters and see the option prices update. Super handy for experimenting!
*   **Modular Code:** I'm trying to keep the code clean and organized, separating the pricing logic from data fetching and the UI. Future me will thank me for this!

## Getting Started (Join My Journey!)

Want to play around with it yourself? Here's how to get this little engine running on your machine.

### What You'll Need

*   **Python 3.9+:** My code is written in Python, so make sure you have a recent version.
*   **An Alpha Vantage API Key:** You can get one for free from [alphavantage.co](https://www.alphavantage.co/support/#api-key). This is crucial for fetching live gold prices.

### Setup Steps

1.  **Clone this repository:**
    ```bash
    git clone https://github.com/Bharathdarla/Gold-Option-Pricing-Engine.git
    cd Gold-Option-Pricing-Engine
    ```

2.  **Create and activate a virtual environment:**
    It's good practice to keep project dependencies isolated. I learned this the hard way!
    ```bash
    python -m venv venv
    # On macOS/Linux:
    source venv/bin/activate
    # On Windows:
    .\venv\Scripts\activate
    ```

3.  **Install all the necessary Python libraries:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set your Alpha Vantage API Key:**
    The app needs your API key to talk to Alpha Vantage. I've set it up to read from an environment variable, which is safer than hardcoding it.
    
    *   **On macOS/Linux (for your current terminal session):**
        ```bash
        export ALPHA_VANTAGE_API_KEY="YOUR_ALPHA_VANTAGE_API_KEY"
        ```
    *   **On Windows (Command Prompt - for your current session):**
        ```bash
        set ALPHA_VANTAGE_API_KEY="YOUR_ALPHA_VANTAGE_API_KEY"
        ```
    *   **On Windows (PowerShell - for your current session):**
        ```powershell
        $env:ALPHA_VANTAGE_API_KEY="YOUR_ALPHA_VANTAGE_API_KEY"
        ```
    **Remember to replace `"YOUR_ALPHA_VANTAGE_API_KEY"` with your actual key!** For persistent setting, you might need to add this to your shell's profile file (`.bashrc`, `.zshrc`, `environment variables` on Windows).

### Running the Application

1.  **Make sure your virtual environment is active.**
2.  **Fire up the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

    This command should automatically open the application in your default web browser. If not, it'll give you a local URL to copy-paste.

## My Project Structure (Keeping Things Tidy)

```
Gold-Option-Pricing-Engine/
├── app.py
├── pricing_models.py
├── data_handler.py
├── requirements.txt
├── README.md
└── .gitignore
```

*   `app.py`: This is the heart of the user interface, built with Streamlit.
*   `pricing_models.py`: Where all the mathematical magic happens for option pricing (starting with Black-Scholes).
*   `data_handler.py`: My little helper for fetching live market data, specifically gold prices.
*   `requirements.txt`: Lists all the Python libraries this project needs.
*   `README.md`: You're reading it! My project overview and instructions.
*   `.gitignore`: Tells Git what files to ignore (like my virtual environment).

## What's Next? (My To-Do List!)

This is just the beginning! Here are some ideas I have for future improvements:

*   **More Models!** I really want to implement the Binomial Tree model (especially for American options, which BSM can't handle) and maybe even Monte Carlo simulations for more complex scenarios.
*   **Other Assets:** Expanding to Forex and Cryptocurrency options would be super cool, but each has its own quirks.
*   **Greeks, Please!** Calculating and displaying the 
Greeks (Delta, Gamma, Theta, Vega, Rho) would be a huge step for understanding option sensitivities.
*   **Better Volatility:** Estimating volatility is a beast! I want to explore more sophisticated methods beyond simple historical volatility.
*   **Historical Data & SQLite:** Storing historical data locally in an SQLite database would make analysis much faster and reduce API calls.
*   **Charts and Visualizations:** Who doesn't love a good chart? Visualizing price paths, implied volatility surfaces, or option payoffs would be awesome.

## Disclaimer (The Serious Bit)

Just a friendly reminder: **This project is purely for educational purposes and my personal learning.** Please, **DO NOT** use this for actual financial trading or making real investment decisions. Option pricing models are theoretical, and the real market is way more complex and unpredictable. Always do your own thorough research and, if you're dealing with real money, talk to a qualified financial professional!

Happy coding and happy learning! ✨
