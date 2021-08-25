import os
import math
import csv


csvpath=os.path.join('Resources','election_data.csv')

with open(csvpath) as csvfile:
	csvreader=csv.reader(csvfile, delimiter=',')
	#print(csvreader)
	csvheader = next(csvreader)
	#print(f'CSV HEADER : {csvheader}')

	voterlist=[]	
	total1 = 0
	total2 = 0
	total3= 0 
	total4 = 0	
	Summarylist=[]
	#Loop through each row in the spreadsheet
	for row in csvreader:
		#append to a new list
		voterlist.append(row[0])
	
	#The total number of votes each candidate won
	#Name matches will add one count INTO a total variable for tracking
		candidate = row[2]
		
		if candidate == "Khan":
			total1 = total1+1
			candidate1 = candidate
		if candidate == "Correy":
			total2 = total2+1
			candidate2 = candidate
		if candidate == "Li":
			total3 = total3+1
			candidate3 = candidate
		if candidate == "O'Tooley":
			total4= total4+1
			candidate4 = candidate	
	
	Summarylist=[[candidate1,total1],[candidate2,total2],[candidate3,total3],[candidate4,total4]]
	#print(Summarylist)
	#The winner of the election based on popular vote
	#largest value is the winner
	previous = 0
	for r in Summarylist:
		winner = r[1]
		if previous < winner:
			final = r[0]
			previous=winner	
	
	#calculate the total of voter
	length=len(voterlist)	
	
	#The percentage of votes each candidate won, Use formula to divide by total votes (length)
	percentage1 = (total1/length)*100  #how can we convert to percentage?
	format_float1="{:.3f}".format(percentage1)
	
	percentage2 = (total2/length)*100  #how can we convert to percentage?
	format_float2="{:.3f}".format(percentage2)	
	
	percentage3 = (total3/length)*100  #how can we convert to percentage?
	format_float3="{:.3f}".format(percentage3)	
	
	percentage4 = (total4/length)*100  #how can we convert to percentage?
	format_float4="{:.3f}".format(percentage4)	
		

	print("Election Results")
	print("-------------------------------")	
	print(f'Total Votes: {length}') 
	print("-------------------------------")
	print(f'{candidate1}: {format_float1}% ({total1})')
	print(f'{candidate2}: {format_float2}% ({total2})')
	print(f'{candidate3}: {format_float3}% ({total3})')
	print(f'{candidate4}: {format_float4}% ({total4})')
	print("-------------------------------")
	print(f'Winner: {final}')
	print("-------------------------------")


output_path = os.path.join("Resources","analysis_result.txt")
with open(output_path,'w', newline='') as csvfile:
	csvwriter = csv.writer(csvfile, delimiter=' ')
	csvwriter.writerow("Election Results")
	csvwriter.writerow("-------------------------------")
	csvwriter.writerow(f'Total Votes: {length}') 
	csvwriter.writerow("-------------------------------")
	csvwriter.writerow(f'{candidate1}: {format_float1}% ({total1})')
	csvwriter.writerow(f'{candidate2}: {format_float2}% ({total2})')
	csvwriter.writerow(f'{candidate3}: {format_float3}% ({total3})')
	csvwriter.writerow(f'{candidate4}: {format_float4}% ({total4})')
	csvwriter.writerow("-------------------------------")
	csvwriter.writerow(f'Winner: {final}')
	csvwriter.writerow("-------------------------------")