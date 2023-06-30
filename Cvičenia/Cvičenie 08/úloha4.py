import csv

source = "movies1.csv"

def movies_by_year(year):
    with open(source, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if str(year) == row["Year"]:
                print(row["Rank"], row["Title"])
                          

movies_by_year(1941)

 