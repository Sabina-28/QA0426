import csv

def read_csv_data(file_path):
    """
    Reads a CSV file and returns its content as a list of dictionaries.
    """
    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            data = [row for row in csv_reader]
        return data
    except FileNotFoundError:
        print("Error: The specified file was not found.")
        return []

def main():
    print("==========================")
    print("Disneyland Review Analyser")
    print("==========================\n")

    # File path to the CSV file
    csv_file = 'disneyland_reviews.csv'  # Replace with your actual file path

    # Read data from the CSV file
    print("Reading data from the CSV file...\n")
    data = read_csv_data(csv_file)

    if data:
        print(f"Dataset successfully read. Total rows: {len(data)}\n")
    else:
        print("Failed to load the dataset.\n")

if __name__ == "__main__":
    main()

# Menu that runs continuously
while True:
   # Display menu
    print("Please enter the letter which corresponds with your desired menu choice:")
    print("   [A] View Data")
    print("   [B] Visualise Data")
    print("   [X] Exit")

   # Ask user input
    choice = input()

   # Store the choice in a variable and display
    if choice == 'A':
     print("You have chosen option A - View Data")
    elif choice == 'B':
     print("You have chosen option B - Visualise Data")
    elif choice == 'X':
     print("You have chosen option X - Exit")
     break # Exit the loop
    else:
     print("Invalid choice. Please select a valid option from the menu.")










