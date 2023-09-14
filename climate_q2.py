import matplotlib.pyplot as plt
import pandas as pd


csv_file_path = 'Documents\GitHub\s5302699_quiz_week_8\climate.csv'

# Load the data from the CSV file
df = pd.read_csv(csv_file_path)

# Extract the data into separate lists
years = df['Year']
co2 = df['CO2']
temp = df['Temperature']


plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 

plt.tight_layout()
plt.show()
plt.savefig("co2_temp_2.png")

