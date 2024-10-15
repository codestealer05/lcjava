import pandas  # Import the pandas module

# Read the CSV file and store it in the variable df, specifying dtype as object
df = pandas.read_csv("players_22.csv", dtype=object)

"""
# Reading the CSV file in different ways:
df = pandas.read_csv("players_22.csv")              # Basic CSV reading
df = pandas.read_csv("players_22.csv", sep=",")     # Specify comma as the delimiter
df = pandas.read_csv("players_22.csv", header=2)    # Use the third row as header (0-indexed)
df = pandas.read_csv("players_22.csv", encoding="ISO-8859-1")  # Specify encoding
print(df)  # Display the entire CSV content

# Accessing the shape and dimensions of the data:
print(df.shape)         # Print the shape (rows, columns) of the DataFrame
print(len(df.columns))  # Print the number of columns
print(len(df))          # Print the number of rows

# Accessing specific columns:
print(df["long_name"])  # Display the "long_name" column
print(df["club_name"])  # Display the "club_name" column

# Accessing specific rows:
print(df.iloc[2])  # Display the row with index 2 (Cristiano Ronaldo"s information)

# Accessing a range of rows:
print(df.iloc[2:5][["short_name", "club_name"]])  # Display rows 2 to 4, showing "short_name" and "club_name" columns

# Displaying the first few rows:
print(df.iloc[:5])  # Display the first 5 rows
print(df.head()[["short_name", "club_name"]])  # Display the first 5 rows with specific columns

# Displaying the last few rows:
print(df.iloc[-5:][["short_name", "overall", "age"]])  # Display the last 5 rows with specific columns
print(df.tail())  # Display the last 5 rows

# Accessing rows based on labels:
print(df.loc[2])  # Retrieve values from row labeled 2
"""

# Initialize data as a dictionary of lists
data = {"Name": ["Tom", "Jack", "Nick", "Juli"], "marks": [99, 58, 35, 40]}  # Sample data

# Create a pandas DataFrame from the data
createdf = pandas.DataFrame(data)  # Create a DataFrame from the dictionary
print(createdf)  # Display the created DataFrame

# Save the DataFrame to a CSV file
createdf.to_csv("file_name.csv")  # Save the DataFrame to "file_name.csv"

# Create a new row of data to be added to the DataFrame
new_row = {"Name": "Geo", "marks": 127}  # New data to be added as a row

# Add the new row to the DataFrame
createdf.loc[len(createdf)] = new_row  # Append the new row to the DataFrame

# Manually add a "Manual Grade" column to the DataFrame
createdf["Manual Grade"] = [66, 38, 23, 26, 84]  # Add manual grades for each student

# Automatically calculate and add an "Auto Grade" column based on "marks"
createdf["Auto Grade"] = ((createdf["marks"] / 150) * 100).astype("int")  # Calculate and add auto grades

# Add a "Pass/Fail" column based on the "Manual Grade" values
createdf["P/F"] = ["Fail" if score < 40 else "Pass" for score in createdf["Manual Grade"]]  # Pass/Fail criteria


# Function to assign letter grades based on "Auto Grade"
def assign_result(row):
    if row >= 85:
        result = "a"
    elif row >= 70:
        result = "b"
    elif row >= 55:
        result = "c"
    elif row >= 40:
        result = "d"
    elif row >= 25:
        result = "e"
    else:
        result = "f"
    return result


# Apply the "assign_result" function to the "Auto Grade" column to assign letter grades
createdf["Letter Grades"] = createdf["Auto Grade"].apply(assign_result)  # Add letter grades column
print(createdf)  # Display the updated DataFrame
