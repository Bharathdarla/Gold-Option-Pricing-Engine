# Research Notes & Learning Log for Gold Option Pricing Engine

This document is a log of my thoughts, research findings, and challenges encountered while building this Gold Option Pricing Engine. It's a way for me to keep track of what I've learned and what I still need to figure out.

## Week 1-2: Diving into Black-Scholes and Python Basics

### Initial Thoughts:
*   **Options are complex!** Seriously, the terminology alone is a lot to take in. Call, Put, Strike, Expiration... it's like learning a new language.
*   **Black-Scholes-Merton (BSM) Model:** Everyone talks about it, so it seemed like the natural place to start. The formula looks intimidating at first, but breaking it down into `d1` and `d2` makes it more manageable. `numpy` and `scipy.stats.norm.cdf` are lifesaesavers for the math.
*   **Python for Finance:** Glad I chose Python. The libraries (`numpy`, `scipy`) are incredibly powerful for numerical stuff. It feels like I'm standing on the shoulders of giants.

### Challenges:
*   **Understanding `norm.cdf`:** Initially, I was a bit confused about how the cumulative normal distribution function ties into option pricing. Had to re-read a few articles to grasp its role in probability.
*   **Time to Expiration (T) Units:** Kept forgetting that `T` needs to be in *years*. My first few calculations were way off until I realized I was passing days directly. Simple mistake, but crucial!
*   **Volatility (Sigma):** This is the biggest mystery! BSM assumes constant volatility, which is totally unrealistic. How do people actually estimate this in the real world? Historical volatility is a start, but implied volatility seems like the holy grail. Need to research this more.

### Key Learnings:
*   The BSM model is elegant but has strong assumptions (European options only, constant volatility, no dividends, etc.).
*   Python's scientific stack makes implementing complex formulas relatively straightforward.
*   Error handling (like `T <= 0` in `pricing_models.py`) is important for robustness.

## Week 3-4: Data Fetching and Streamlit UI

### Initial Thoughts:
*   **Live Data is a Must:** A pricing engine without live data is just a calculator. I needed a way to get the current gold price.
*   **Alpha Vantage:** Found Alpha Vantage as a free API option. It's not perfect, but it's good enough for a personal project.
*   **Streamlit:** Heard about Streamlit for quick data apps. Decided to give it a shot instead of building a full Flask/Django app. It's incredibly fast to prototype with!

### Challenges:
*   **API Keys and Environment Variables:** Learning about `os.getenv()` and why it's important not to hardcode API keys. Security best practices, even for small projects!
*   **JSON Parsing:** Navigating the JSON response from Alpha Vantage took a bit of trial and error. Different APIs have different structures.
*   **Streamlit State Management:** Understanding `st.session_state` was key to making the 
UI feel responsive when fetching live data.
*   **Streamlit Layout:** Getting the `st.sidebar` and main content to look decent took some fiddling. Still learning the best practices for Streamlit UI design.

### Key Learnings:
*   Streamlit is fantastic for rapid prototyping of data applications. It lets me focus on the logic rather than complex web development.
*   API integration requires careful error handling (network issues, unexpected responses).
*   Environment variables are the way to go for sensitive information like API keys.

## Future Ideas & Open Questions:

*   **Binomial Tree Model:** This is next on my list. It handles American options, which BSM can't. It seems more intuitive to visualize the price paths.
*   **Monte Carlo Simulation:** For really complex options or if I want to model different price distributions, Monte Carlo seems powerful. But it's computationally intensive.
*   **Volatility Estimation:** How do professional traders get their volatility numbers? Implied volatility from option chains seems like the answer, but that's another layer of data fetching and calculation.
*   **Greeks:** Need to add Delta, Gamma, Theta, Vega, Rho calculations. These are crucial for understanding risk and sensitivity.
*   **Database:** For storing historical data and making the app faster, an SQLite database would be a good addition. Right now, it's all in memory or fetched live.
*   **Other Assets:** Gold was a good start, but Forex and Crypto options have their own unique challenges (e.g., Garman-Kohlhagen for Forex, high volatility and different market structures for Crypto).
*   **Testing:** Need to write more comprehensive unit and integration tests. My current tests are pretty basic.

This project is a continuous learning experience, and I'm excited to see where it goes next!
