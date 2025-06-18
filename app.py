import pandas as pd
import pickle

# Load the model
with open('model.pkl', 'rb') as file:
    model = pickle.load(files)

# Ask user to input values
size = int(input("Enter Size (in sqft): "))
bedrooms = int(input("Enter Number of Bedrooms: "))
bathrooms = int(input("Enter Number of Bathrooms: "))

# Location input
print("\nChoose Location:\n0 - Downtown\n1 - Outskirts\n2 - Suburb")
location = int(input("Enter Location Number (0/1/2): "))

# Make DataFrame
data = pd.DataFrame([[size, bedrooms, bathrooms, location]],
                    columns=['Size_sqft', 'Num_Bedrooms', 'Num_Bathrooms', 'Location'])

# Predict
predicted_rent = model.predict(data)[0]

# Show result
print(f"\nPredicted Monthly Rent: ₹ {round(predicted_rent, 2)}")
