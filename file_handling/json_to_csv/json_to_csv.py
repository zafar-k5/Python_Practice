import json
import csv
with open(r"C:\gitstuff\Python_Practice\file_handling\certifications.json","r") as jsonfile:
    all_file_content = json.load(jsonfile)
    all_json_content = all_file_content["certifications"]
    c=0
    df = open(r"C:\gitstuff\Python_Practice\file_handling\certifications.csv","w",newline="")
    csv_writer = csv.writer(df)
    for dict in all_json_content:
        if c == 0:
            csv_writer.writerow(dict.keys())
            c+=1
        csv_writer.writerow(dict.values())