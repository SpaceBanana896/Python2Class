# import random module\n
import random
# Print multiline instruction



while True:    
	print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n")    
	
	# take the input from user use the variable choice\n\n\n    
	choice = input()
	
	# OR is the short-circuit operator\n    
	# if any one of the condition is true\n    
	# then it return True value\n    
	# looping until user enter invalid input\n    
	while choice > 3 or choice < 1:       
		choice = int(input("enter valid input: "))    


	# initialize value of choice_name variable   
	choice_name = "" 
	# corresponding to the choice value\n    
	if choice == 1:       
		choice_name = "Rock"
	elif choice == 2:
		choice_name = "Paper"
	elif choice == 3:
		choice_name = "Scissor"
	
	
	# print user choice\n\n\n    
	print(choice_name)
	
	# Computer chooses randomly any number\n    
	# among 1 , 2 and 3. Using randint method\n    
	# Use comp_choice as variable name\n\n\n    
	
	
	# looping until comp_choice value   
	# is equal to the choice value  
	while comp_choice == choice:       
		comp_choice = random.randint(1, 3) 
		
	# initialize value of comp_choice_name\n    
	# variable corresponding to the comp choice value\n    
	if comp_choice == 1:       
		comp_choice_name = 'Rock'    
		
	# Print comp_choice_name using string concatenation\n\n    
	
	# Print comp_choice_name VS choice_nmae using string concatenation\n\n\n    
	
	
	# condition for winning\n\n\n    
	
	
	# Printing either user or computer wins\n\n\n    
	
	#Ask whether user wants to play again\n    
	print("Do you want to play again? (Y/N)")  
	ans = input()   
	
	# if user input n or N then condition is True\n    
	if ans == 'n' or ans == 'N':        
		break

# after coming out of the while loop\n
# we print thanks for playing\n
print("Thanks for playing")
