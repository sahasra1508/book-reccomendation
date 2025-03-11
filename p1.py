data = [
    {'A': 1, 'B': 5, 'C': 9},
    {'A': 2, 'B': 6, 'C': 10},
    {'A': 3, 'B': 7, 'C': 11},
    {'A': 4, 'B': 8, 'C': 12}
]
filtered_data = [row for row in data if row['A'] > 2 and row['B'] < 8]
print(filtered_data)