import csv

# Step 1 Total months - equal Number of Raws
prevRev = 0
totalNumMonths = 0
totalRev = 0
gretestIncrease = 0
MonthofGretestIncrease =''
greatestDecrease = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
MonthofGretestDecrease =''





fileLoc= "../budget_data.csv"

with open(fileLoc) as raw_data:

   
   
   raw_data_read = csv.reader(raw_data)
   next(raw_data_read)
   
   for row in raw_data_read:
       #print(totalNumMonths)
       totalNumMonths+=1
       
       
       thisMonth = row[0]
       
       thisRev = int(row[1])
       
       #print(thisMonth)
       #print(thisRev)
       
       
       RevChange = thisRev - prevRev

       #RevChange.append(RevChange)
       
       
       if RevChange > gretestIncrease:
           
           MonthofGretestIncrease = thisMonth
           gretestIncrease = RevChange
           
       if RevChange < greatestDecrease:
           
           MonthofGretestDecrease = thisMonth
           greatestDecrease = RevChange
       
       
       prevRev = thisRev
       
       totalRev += thisRev
AvgRev = totalRev / totalNumMonths


print("######################")      
print(f'Total Number of Months: {totalNumMonths} Months')
print(f'Total Rev: ${totalRev}')
print(f"Greatest Increase: ${gretestIncrease}")
print(f"Greatest increase Month: {MonthofGretestIncrease}")
print(f'Greatest Decrease : ${greatestDecrease}')
print(f'Greatest Decares Month{MonthofGretestDecrease}')
print("######################")

file_to_output = "/budget_data.txt"
# Generate Output Summary
output = (

   f"\nFinancial Analysis\n"
   f"----------------------------\n"
   f"Total Months:  {totalNumMonths} Months\n"
   f"Total Revenu: ${totalRev}\n"
   f"Greatest Increase: ${gretestIncrease}")

# Print the output (to terminal)
print(output)

# Export the results to text file
with open(file_to_output, "w") as txt_file:
   txt_file.write(file_to_output)
   txt_file.write()