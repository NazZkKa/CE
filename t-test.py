import csv
from scipy import stats

# Read data from CSV file
def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append([float(val) for val in row])
    return data

# Specify the filename
filename = "Untitled.csv"  # Replace with your CSV filename

# Read data from CSV
data = read_csv(filename)


# Extract data for two groups (assuming two columns)

# Group 1

group1 = []

for i in range(0, 30):
    group1.append(data[i][0])

# Group 2
group2 = []

for i in range(0, 30):
    group2.append(data[i][1])


# Perform t-test
t_statistic, p_value = stats.ttest_ind(group1, group2)

# Print results
print("T-Statistic:", t_statistic)
print("P-Value:", p_value)

# Interpret the results
alpha = 0.05
if p_value < alpha:
    print("Reject null hypothesis: There is a significant difference between the means.")
else:
    print("Fail to reject null hypothesis: There is no significant difference between the means.")
