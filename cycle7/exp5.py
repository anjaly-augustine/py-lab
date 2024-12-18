import csv

def write_dict_to_csv(filename, data):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def read_csv_file(filename):
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)

# Example usage
dict_data = [
    {'Name': 'Tris', 'Age': 20, 'City': 'Chicago'},
    {'Name': 'Thobit', 'Age': 22, 'City': 'Downtown'},
    {'Name': 'Merkle', 'Age': 45, 'City': 'Wales'}
]

csv_filename = "output.csv"
write_dict_to_csv(csv_filename, dict_data)
print("CSV file content:")
read_csv_file(csv_filename)




