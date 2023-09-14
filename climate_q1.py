import sqlite3
import matplotlib.pyplot as plt


db_file_path = 'Documents\GitHub\s5302699_quiz_week_8\climate.db' 

try:
    # Connect to the SQLite database using the absolute file path
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()

    # Fetch data from the "ClimateData" table
    cursor.execute("SELECT Year, CO2, Temperature FROM ClimateData")
    data = cursor.fetchall()

    # Separate the fetched data into separate lists
    years = [row[0] for row in data]
    co2 = [row[1] for row in data]
    temp = [row[2] for row in data]

    # Close the database connection
    conn.close()

    plt.subplot(2, 1, 1)
    plt.plot(years, co2, 'b--')
    plt.title("CO2 Data")
    plt.ylabel("[CO2]")
    plt.xlabel("Year")

    plt.subplot(2, 1, 2)
    plt.plot(years, temp, 'r*-')
    plt.title("Temperature Data")
    plt.ylabel("Temp (C)")
    plt.xlabel("Year")

    plt.tight_layout()
    plt.show()

except sqlite3.Error as e:
    print(f"SQLite error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")