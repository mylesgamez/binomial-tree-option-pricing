# Binomial Tree Option Pricing

This Python script calculates the option price using the Binomial Tree method. The Binomial Tree model provides a discrete-time approximation for option pricing based on various input parameters.

## Usage

1. Make sure you have Python and NumPy installed on your system.
2. Run the script in your terminal or Python environment.
3. Enter the required parameters such as stock price, strike price, time to expiration, risk-free interest rate, volatility, option type (call or put), and the number of time steps in the Binomial Tree.
4. The script will calculate and display the option price.

## Parameters

- `S`: Current stock price.
- `K`: Strike price.
- `T`: Time to expiration (in years).
- `r`: Risk-free interest rate.
- `sigma`: Volatility of the underlying asset.
- `option_type`: Type of option ('call' for call option, 'put' for put option).
- `num_steps`: Number of time steps in the Binomial Tree (default is 1,000).

## Example

Here's an example of how to use the script:

```python
python binomial_tree_option_pricing.py
Enter current stock price: 100
Enter strike price: 110
Enter time to expiration (in years): 1
Enter risk-free interest rate: 0.05
Enter volatility: 0.2
Enter option type (call/put): call
Enter number of time steps: 1000
Option Price: 8.07
```

## License
MIT
