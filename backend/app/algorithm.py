import numpy as np
import random
import pandas as pd
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split



def create_sample_data:
    n_companies = 100
    np.random.seed(42)  # For reproducibility
    # Simulate user decisions (Yes=1, No=0)
    # Will get the data from the website
    user_decisions = np.random.choice([0, 1], size=n_companies)
    real_startup_data = np.random.rand(10, len(variables)) * 100 
    return [user_decisions, real_startup_data]

def best_startups(user_decisions, real_startup_data):
    # Define bounds for each variable (min, max)
    n_companies = len(user_decisions)
    variable_bounds = {
        'sales_revenue': (0, 100),
        'sales_growth': (0, 50),
        'netprofit': (-10, 90),
        'netprofit_growth': (0, 60),
        'users_number': (1000, 10000),
        'users_growth': (0, 100),
        'costs': (10, 200),
        'cost_growth': (0, 50)
    }
    
    variables = list(variable_bounds.keys())
    random_data = np.zeros((n_companies, len(variables)))

    # Generate random data within specified bounds for each variable
    for i, var in enumerate(variables):
        min_val, max_val = variable_bounds[var]
        random_data[:, i] = np.random.rand(n_companies) * (max_val - min_val) + min_val
    
    # Training the model with generated data
    X_train, X_test, Y_train, Y_test = train_test_split(random_data, user_decisions, test_size=0.2, random_state=42)
    model = Perceptron(tol=1e-3, random_state=42)
    model.fit(X_train, Y_train)
    
    # Assuming 'real_startup_data' is your actual data you want to rank
    # Will get the data from the website
    real_startup_data = np.random.rand(10, len(variables)) * 100  # Example real data
    
    # Use decision_function to get the confidence scores of the predictions
    confidence_scores = model.decision_function(real_startup_data)
    
    # Rank the startups by their confidence scores
    # Higher scores indicate a better match according to the user's preferences
    ranking_indices = np.argsort(confidence_scores)[::-1]  # Sort in descending order
    
    positive_confidence_indices = [i for i, score in enumerate(confidence_scores) if score > 0]
    
    # Apply the filter to get the indices in the original dataset and their confidence scores
    positive_ranked_indices = ranking_indices[np.isin(ranking_indices, positive_confidence_indices)]
    positive_confidence_scores = confidence_scores[positive_ranked_indices]
    
    # Print ranked startups with positive confidence scores (or return this data for further use)
    
    return (positive_ranked_indices, positive_confidence_scores)
