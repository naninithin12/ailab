#9ai.py
import numpy as np
from hmmlearn import hmm

# Generate some example stock prices
stock_prices = [100, 110,107,95,102,115,120]

# Create the HMM model
model = hmm.GaussianHMM(n_components=2, covariance_type="diag")

# Train the HMM model on the stock prices
reshaped_prices = np.array(stock_prices).reshape(-1, 1)
model.fit(reshaped_prices)

# Generate predictions using the trained HMM model
predicted_prices = model.sample(len(stock_prices))[0]

# Print the predicted stock prices
print("Predicted Stock Prices:", *predicted_prices[:3])

