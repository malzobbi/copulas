import pandas as pd
import time
from copulas.multivariate import GaussianMultivariate
t0= time.time()
# Load your original data from a CSV file
data = pd.read_csv('E:/Australian Institute/Capstone Master/copulas_theory/original_data2.csv')

# Remove any rows with missing values
data.dropna(inplace=True)

# Initialize a Gaussian copula object
copula = GaussianMultivariate()

# Fit the copula to your original data
copula.fit(data)

# Generate synthetic data using the copula
synthetic_data = copula.sample(len(data))

# Print the synthetic data
#print(synthetic_data)
file = open("E:/Australian Institute/Capstone Master/copulas_theory/synthetic_cop.csv","w") 
 
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)       
file.write(str(synthetic_data))   
file.close() 
t1 = time.time() - t0
print("Time elapsed: ", t1)  