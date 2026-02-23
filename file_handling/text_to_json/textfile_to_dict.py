import json
with open(r"C:\gitstuff\Python_Practice\file_handling\input.txt","r") as textfile:
    my_dict = {}
    for line in textfile:
        key,value = line.strip().split(":",1)
        my_dict[key] = value.strip()

df = open(r"C:\gitstuff\Python_Practice\file_handling\input.json","w")
json.dump(my_dict,df,indent=4,sort_keys=True)
df.close()