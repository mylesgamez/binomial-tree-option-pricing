def binomial_tree_option_price(S, K, T, r, sigma, option_type='call', num_steps=1000):
    """
    Calculate the option price using the Binomial Tree method.

    Parameters:
    S (float): Current stock price
    K (float): Strike price
    T (float): Time to expiration (in years)
    r (float): Risk-free interest rate
    sigma (float): Volatility of the underlying asset
    option_type (str): 'call' for call option, 'put' for put option
    num_steps (int): Number of time steps in the Binomial Tree

    Returns:
    option_price (float): Option price
    """
    
    dt = T / num_steps
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    p = (np.exp(r * dt) - d) / (u - d)
    
    option_prices = np.zeros(num_steps + 1)
    
    for i in range(num_steps + 1):
        S_T = S * (u ** (num_steps - i)) * (d ** i)
        
        if option_type == 'call':
            option_prices[i] = max(0, S_T - K)
        elif option_type == 'put':
            option_prices[i] = max(0, K - S_T)
    
    for step in range(num_steps - 1, -1, -1):
        for i in range(step + 1):
            option_prices[i] = np.exp(-r * dt) * (p * option_prices[i] + (1 - p) * option_prices[i + 1])
    
    option_price = option_prices[0]
    
    return option_price

if __name__ == "__main__":
    import numpy as np
    
    S0 = float(input("Enter current stock price: "))
    K = float(input("Enter strike price: "))
    T = float(input("Enter time to expiration (in years): "))
    r = float(input("Enter risk-free interest rate: "))
    sigma = float(input("Enter volatility: "))
    option_type = input("Enter option type (call/put): ").lower()
    
    option_price = binomial_tree_option_price(S0, K, T, r, sigma, option_type)
    
    print(f'Option Price: {option_price:.2f}')

