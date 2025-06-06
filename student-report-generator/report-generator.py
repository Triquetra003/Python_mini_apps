import csv

students="<path-of-file>/students.csv"
marks="<path-of-file>/marks.csv"
reports=[]
names={} 
fieldnames=['id','name','total','percentage','status',"rank"]

# read students.csv 
with open(students,'r') as file:
    reader=csv.DictReader(file)
    for row in reader:
        names[int(row['id'])]=row['name']
    
# read marks.csv
with open(marks, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        #calcuate total, percentage and status(Pass or Fail)
        total=float(row['math'])+float(row['science'])+float(row['english'])
        percentage=(total/300)*100
        percentage=round(percentage,2)
        if percentage>=40:
            status="Pass"
        else:
            status="Fail"

        # add student report
        reports.append({
            "id":int(row['id']),
            "name":names[int(row['id'])],
            "total":total,
            "percentage":percentage,
            "status":status
        })
   
# sort reports by percentage to establish rank 
reports.sort(key=lambda x: x['percentage'], reverse=True)
rank=1
count=1 #position in list
prev_percentage=None
for student in reports:
    if student["status"]=="Fail":
        student["rank"]="-"
        continue
    if student["percentage"] == prev_percentage:
        student["rank"] = rank
    else:
        rank = count
        student["rank"] = rank
        prev_percentage = student["percentage"]
    count += 1 

with open('<path-of-file>/reports.csv',"w",newline='') as file:
    writer=csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(reports)
        