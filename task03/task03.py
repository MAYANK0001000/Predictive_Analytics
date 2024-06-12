import csv

def get_user_input():
    username = input("Please enter your username: ")
    age = int(input("Please enter your age: "))
    height = float(input("Please enter your height in meters: "))
    weight = float(input("Please enter your weight in kilograms: "))
    return username, age, height, weight

def compute_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def comment_on_bmi(bmi):
    if bmi < 18.5:
        return "You are underweight."
    elif bmi < 25:
        return "You are normal weight."
    elif bmi < 30:
        return "You are overweight."
    else:
        return "You are obese."

def append_to_csv(username, age, height, weight, bmi, comment):
    with open("data.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([username, age, height, weight, bmi, comment])

def view_collected_data():
    with open("data.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

def main():
    print("Welcome to the BMI calculator!")
    while True:
        print("1. Run a new data capture")
        print("2. View collected data")
        choice = input("Please enter your choice: ")
        if choice == "1":
            username, age, height, weight = get_user_input()
            bmi = compute_bmi(weight, height)
            comment = comment_on_bmi(bmi)
            append_to_csv(username, age, height, weight, bmi, comment)
            print("Data captured successfully!")
        elif choice == "2":
            view_collected_data()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()