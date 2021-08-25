import os
import csv

csvpath=os.path.join('Resources','budget_data.csv')

with open(csvpath) as csvfile:
	csvreader=csv.reader(csvfile, delimiter=',') #CSV FUNCTION
	#print(csvreader)
	
	csv_header=next(csvreader)
	
	sum = 0
	date_list=[]
	profit= 0
	loss = 0
	changes = 0
	lastmonth=0
	change=0
	diff_list=[]
	diff_list2=[]
	
	for row in csvreader:  
		#print(row)	
		#store the data in a variable
		total = row[1]
		date = row[0]

		#add up the value 
		sum= sum+float(total)
	
		#loop through the row and add them into variable, First change first row it will be zero 
		currentmonth = float(row[1])
		
		#firstloop take in the initial value of zero because there is nothing to compare	
		if lastmonth==0:
			change=0	#Set the change to zero		
			diff_list.append(change)  #add this result into a new list
			lastmonth=currentmonth	  #this month figures will be updated as last month

			#GENERATE a new list with all the date and change in
			diff_list2.append(date)
			diff_list2.append(change)
		else:	
			#as long as last month is not a zero, it will calculate the difference between last month and current month
	
			change=currentmonth-lastmonth
			change=float(change)
			diff_list.append(change)

			#GENERATE a new list with all the date and change in
			diff_list2.append(date)
			diff_list2.append(change)
			lastmonth=currentmonth
			
			
		
		#COUNT THE DATE by creating a list, append row[0] to the new list during each loop
		date_list.append(row[0])
		
		#loop through the list to store the data in a variable
		total1= row[1]
		#set conditional to store the data in profit or loss on condition
		if float(total1) > 0:
			#add up the value to get the final amount
			profit = profit+float(total1)
		else:
			#add up the value to get the final amount
			loss = loss+float(total1)
	
	print("Financial Analysis")
	print("-------------------------")
	
	#return the length of the list
	length=len(date_list)
	print(f'Total Month: {length}')

	#return the length of this list
	print(f'Total: $ {sum} ' )
	
	#average of the changes in profit and loss during the entire period
	#print(diff_list)
	sum=0
	for i in diff_list:
		sum=sum+i
		max_no = max(diff_list)
		min_no = min(diff_list)

	for a in diff_list2:
		if a == max_no:
			 Greatestindex = (diff_list2.index(a)-1)	
		if a == min_no:
			 Lowestindex = (diff_list2.index(a)-1)	
		
	IncreaseMonth = diff_list2[Greatestindex]
	DecreaseMonth = diff_list2[Lowestindex]	

	Averagechange = sum/(length-1)
	print(f'Average Change: $ {Averagechange}')
	print(f'Greatest Increase in Profits: {IncreaseMonth}  $( {max_no})')
	print(f'Greatest Decrease in Profits: {DecreaseMonth}  $( {min_no})')
	
output_path = os.path.join("Resources","analysis_result.txt")
with open(output_path,'w', newline='') as csvfile:
	csvwriter = csv.writer(csvfile, delimiter=' ')
	csvwriter.writerow("Financial Analysis")
	csvwriter.writerow("-------------------------------")
	csvwriter.writerow(f'Total Month:{length}') 
	csvwriter.writerow(f'Total: ${sum}')
	csvwriter.writerow(f'Average Change: ${Averagechange}')
	csvwriter.writerow(f'Greatest Increase in Profits: {IncreaseMonth}$({max_no})')
	csvwriter.writerow(f'Greatest Decrease in Profits: {DecreaseMonth}$({min_no})')
		
