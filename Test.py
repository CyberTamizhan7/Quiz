import random
import time
import mysql.connector
import datetime

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root")

cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS Python_Test")
cursor.execute("USE Python_Test;")
cursor.execute('''CREATE TABLE IF NOT EXISTS Vehicle_Number_Test(
                    SNo INT AUTO_INCREMENT PRIMARY KEY,
                    Name VARCHAR(255) NOT NULL,
                    Score INT NOT NULL,
                    Total_Questions INT NOT NULL,
                    Percentage FLOAT NOT NULL,
                    Time_Taken FLOAT NOT NULL,
                    Date DATE NOT NULL,
                    Time TIME NOT NULL)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Morse_Code_Test(
                    SNo INT AUTO_INCREMENT PRIMARY KEY,
                    Name VARCHAR(255) NOT NULL,
                    Score INT NOT NULL,
                    Total_Questions INT NOT NULL,
                    Percentage FLOAT NOT NULL,
                    Time_Taken FLOAT NOT NULL,
                    Date DATE NOT NULL,
                    Time TIME NOT NULL)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Atomic_Number_Test(
                    SNo INT AUTO_INCREMENT PRIMARY KEY,
                    Name VARCHAR(255) NOT NULL,
                    Score INT NOT NULL,
                    Total_Questions INT NOT NULL,
                    Percentage FLOAT NOT NULL,
                    Time_Taken FLOAT NOT NULL,
                    Date DATE NOT NULL,
                    Time TIME NOT NULL)''')

connection.commit()
               

d_vehicle_no = {"TN01":"Ayanavaram", "TN02":"Anna Nagar", "TN03":"Tondiarpet",
              "TN04":"Basin Bridge", "TN05":"Vyaasarpadi", "TN06":"Mandaveli",
              "TN07":"Tiruvanmiyur", "TN09":"K.K. Nagar", "TN10":"Valasarawakkam",
              "TN11":"Tambaram", "TN12":"Poonamalle", "TN13":"Ambattur",
              "TN14":"Sholinganallur", "TN15":"Ulundurpet", "TN16":"Tindivanam",
              "TN18":"Redhills", "TN18y":"Gummidipoondi", "TN19":"Chengalpattu",
              "TN19Y":"Thirukazhugundram", "TN19Z":"Madurantagam", "TN20":"Tiruvallur",
              "TN20X":"Thiruthani", "TN21":"Kancheepuram", "TN22":"Meenambakkam-Alandur",
              "TN23":"Vellore", "TN23T":"Gudiyatham", "TN24":"Krishnagiri"}

d_vehicle_no = {value:key for key, value in d_vehicle_no.items()}

d_morse_code = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..", 
    "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", 
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", 

    "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", 
    "9": "----.", "0": "-----", 

    ".": ".-.-.-", ",": "--..--", ":": "---...", ";": "-.-.-.", "?": "..--..", "'": ".----.", "-": "-....-", 
    "/": "-..-.", "(": "-.--.", ")": "-.--.-", "&": ".-...", "=": "-...-", "+": ".-.-.", "$": "...-..-", 
    "@": ".--.-.", " ": "/"
}


d_atomic_number = {
    "Hydrogen": 1, "Helium": 2, "Lithium": 3, "Beryllium": 4, "Boron": 5, "Carbon": 6, "Nitrogen": 7, "Oxygen": 8,
    "Fluorine": 9, "Neon": 10, "Sodium": 11, "Magnesium": 12, "Aluminium": 13, "Silicon": 14, "Phosphorus": 15,
    "Sulphur": 16, "Chlorine": 17, "Argon": 18, "Potassium": 19, "Calcium": 20, "Scandium": 21, "Titanium": 22,
    "Vanadium": 23, "Chromium": 24, "Manganese": 25, "Iron": 26, "Cobalt": 27, "Nickel": 28, "Copper": 29, "Zinc": 30,
    "Gallium": 31, "Germanium": 32, "Arsenic": 33, "Selenium": 34, "Bromine": 35, "Krypton": 36, "Rubidium": 37,
    "Strontium": 38, "Yttrium": 39, "Zirconium": 40, "Niobium": 41, "Molybdenum": 42, "Technetium": 43,
    "Ruthenium": 44, "Rhodium": 45, "Palladium": 46, "Silver": 47, "Cadmium": 48, "Indium": 49, "Tin": 50,
    "Antimony": 51, "Tellurium": 52, "Iodine": 53, "Xenon": 54, "Cesium": 55, "Barium": 56, "Lanthanum": 57,
    "Cerium": 58, "Praseodymium": 59, "Neodymium": 60, "Promethium": 61, "Samarium": 62, "Europium": 63,
    "Gadolinium": 64, "Terbium": 65, "Dysprosium": 66, "Holmium": 67, "Erbium": 68, "Thulium": 69,
    "Ytterbium": 70, "Lutetium": 71, "Hafnium": 72, "Tantalum": 73, "Wolfram": 74, "Rhenium": 75,
    "Osmium": 76, "Iridium": 77, "Platinum": 78, "Gold": 79, "Mercury": 80, "Thallium": 81, "Lead": 82,
    "Bismuth": 83, "Polonium": 84, "Astatine": 85, "Radon": 86, "Francium": 87, "Radium": 88,
    "Actinium": 89, "Thorium": 90, "Protactinium": 91, "Uranium": 92, "Neptunium": 93, "Plutonium": 94,
    "Americium": 95, "Curium": 96, "Berkelium": 97, "Californium": 98, "Einsteinium": 99, "Fermium": 100,
    "Mendelevium": 101, "Nobelium": 102, "Lawrencium": 103, "Rutherfordium": 104, "Dubnium": 105,
    "Seaborgium": 106, "Bohrium": 107, "Hassium": 108, "Meitnerium": 109, "Darmstadtium": 110,
    "Roentgenium": 111, "Copernicium": 112, "Nihonium": 113, "Flerovium": 114, "Moscovium": 115,
    "Livermorium": 116, "Tennessine": 117, "Oganesson": 118
}

vehicle_no_keys = list(d_vehicle_no.keys())
morse_code_keys = list(d_morse_code.keys())
atomic_number_keys = list(d_atomic_number.keys())
random.shuffle(vehicle_no_keys)
random.shuffle(morse_code_keys)
random.shuffle(atomic_number_keys)
d_vehicle_no_sh = {key:d_vehicle_no[key] for key in vehicle_no_keys}
d_morse_code_sh = {key:d_morse_code[key] for key in morse_code_keys}
d_atomic_number_sh = {key:d_atomic_number[key] for key in atomic_number_keys}

def vehicle_no_test():

    start_time = time.time()

    print("\nVehicle Number Test\n\n")

    name = input("Name : ")
    
    score = 0
    for i, key in enumerate(d_vehicle_no_sh):

        q = input(f"{i+1}. {key} : ")
        
        if q.lower().strip() == d_vehicle_no[key].lower():
            score += 1
        else:
            print(f"Wrong Answer:\nCorrect Answer : {d_vehicle_no[key]}")

    end_time = time.time()

    time_taken = end_time - start_time
    total_questions = len(vehicle_no_keys)
    percentage = (score*100)/total_questions

    cursor.execute('''INSERT INTO Vehicle_Number_Test (Name, Score, Total_Questions, Percentage, Time_Taken, Date, Time)
                           VALUES (%s, %s, %s, %s, %s, %s, %s)''', (name, score, total_questions, percentage, time_taken, datetime.date.today(), datetime.datetime.now().strftime("%H:%M:%S")))
    connection.commit()
    
    print(f"\nScore : {score}/{total_questions}")
    print(f"Percentage : {percentage:.2f}%")
    print(f"Time Taken : {time_taken:.2f} seconds\n\n\n\n\n")

def morse_code_test():
    
    start_time = time.time()

    print("\nMorse Code Test\n\n")

    name = input("Name : ")
    
    score = 0
    for i, key in enumerate(d_morse_code_sh):

        q = input(f"{i+1}. {key} : ")

        if q.strip() == d_morse_code[key]:
            score += 1
        else:
            print(f"Wrong Answer:\nCorrect Answer : {d_morse_code[key]}")
            
    end_time = time.time()

    time_taken = end_time - start_time
    total_questions = len(morse_code_keys)
    percentage = (score*100)/total_questions

    cursor.execute('''INSERT INTO Morse_Code_Test (Name, Score, Total_Questions, Percentage, Time_Taken, Date, Time)
                           VALUES (%s, %s, %s, %s, %s, %s, %s)''', (name, score, total_questions, percentage, time_taken, datetime.date.today(), datetime.datetime.now().strftime("%H:%M:%S")))
    connection.commit()

    print(f"\nScore : {score}/{total_questions}")
    print(f"Percentage : {percentage:.2f}%")
    print(f"Time Taken : {time_taken:.2f} seconds\n\n\n\n\n")

def atomic_number_test():

    start_time = time.time()

    print("\nAtomic Number Test\n\n")

    name = input("Name : ")
    
    score = 0
    for i, key in enumerate(d_atomic_number_sh):

        q = input(f"{i+1}. {key} : ")

        if q.strip() == d_atomic_number[key]:
            score += 1
        else:
            print(f"Wrong Answer:\nCorrect Answer : {d_atomic_number[key]}")
            
    end_time = time.time()

    time_taken = end_time - start_time
    total_questions = len(atomic_number_keys)
    percentage = (score*100)/total_questions

    cursor.execute('''INSERT INTO Atomic_Number_Test (Name, Score, Total_Questions, Percentage, Time_Taken, Date, Time)
                           VALUES (%s, %s, %s, %s, %s, %s, %s)''', (name, score, total_questions, percentage, time_taken, datetime.date.today(), datetime.datetime.now().strftime("%H:%M:%S")))
    connection.commit()

    print(f"\nScore : {score}/{total_questions}")
    print(f"Percentage : {percentage:.2f}%")
    print(f"Time Taken : {time_taken:.2f} seconds\n\n\n\n\n")

def main():
    thodar = True
    while thodar:
        print("\nTest\n")
        print("1. Vehicle Number Test")
        print("2. Morse Code Test")
        print("3. Atomic Number Test")
        print("4. Exit\n")

        try:
            test = int(input("Enter an integer option : "))
        except ValueError:
            print("Enter an integer brov?!")
            continue
        
        if test == 1:
            vehicle_no_test()

        elif test == 2:
            morse_code_test()

        elif test == 3:
            atomic_number_test()

        elif test == 4:
            thodar = False
            print("Program Terminated..")
            
        else:
            print("Invalid Option!")

main()

cursor.close()
connection.close()
