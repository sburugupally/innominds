"""
import csv
fp=open ('myfile.csv','w',newline='')
writer = csv.writer(fp)
writer.writerow(['spam','hello','bye','hi'])
writer.writerow(['spam','hello','bye','hi'])
row.deleterow()
fp.close()

"""
import csv
myData = [["first_name", "second_name", "Grade"],
          ['Alex', 'Brian', 'A'],
          ['Tom', 'Smith', 'B']]
myFile = open('example2.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)
print("Writing complete")