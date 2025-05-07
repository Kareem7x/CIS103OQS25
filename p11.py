import os

def main():
    input_file_name = "C:/Users/nodys/Downloads/points.txt"

    grades_file_name = "grades.txt"
    error_file_name = "error.txt"

    records_read = 0
    good_records = 0
    error_records = 0

    try:
        input_file = open(input_file_name, "r")
        grades_file = open(grades_file_name, "w")
        error_file = open(error_file_name, "w")
    except FileNotFoundError:
        print("Error: One or more files not found.")
        return

    line = input_file.readline()
    while line != "":
        records_read += 1
        line = line.strip()
        fields = line.split(",")

        if len(fields) != 3:
            error_message = "Invalid number of fields"
        else:
            id_number, name, points_str = fields
            if not points_str.isdigit():
                error_message = "Points must be numeric"
            else:
                points = int(points_str)
                if points < 0 or points > 1000:
                    error_message = "Points must be between 0 and 1000"
                else:
                    if(1000<=points):
                      grade = 'A'
                    elif(900<=points < 1000):
                      grade = 'B'
                    elif(800<= points < 900):
                      grade = 'C'
                    elif(600<= points < 800):
                      grade = 'D'
                    else:
                      grade = 'F'

                    grades_file.write(f"{id_number},{name},{points},{grade}\n")
                    good_records += 1
                    error_message = None

        if error_message:
            error_file.write(f"{id_number},{name},{points_str},{error_message}\n")
            error_records += 1

        line = input_file.readline()

    input_file.close()
    grades_file.close()
    error_file.close()

    print("Records read:", records_read)
    print("Good records:", good_records)
    print("Error records:", error_records)

main()