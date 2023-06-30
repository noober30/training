import csv

tabulka = []
nova_tabulka = []

def add_year(file_path):
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rank = row["Rank"]
            percent = row["Rating"]
            title = row["Title"]
            year_start = title.rfind("(") 
            year_end = title.rfind(")") 
            if year_start != -1 and year_end != -1:
                year = title[year_start+1:year_end]     #s tymto if mi pomohol chatGPT
                print(rank, year)
            title = title[:year_start]
            nova_tabulka.append([rank, percent, title, year])
    
    
    file_path1 = file_path[:-4]+ "1.txt"
    
    with open(file_path1, "w") as file1:
        writer = csv.writer(file1)
        writer.writerow(["Rank", "Rating", "Title", "Year"])
        for riadok in nova_tabulka:
            writer.writerow(riadok)
            

    print("New file was created : ", file_path1)


add_year("movies.txt")