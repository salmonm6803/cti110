# Write a program that displays the percentage of males and females in the class
# September 26 2018
# CTI-110 P2HW2 - Male Female Percentage
# Matthew Salmon
#

# Ask the user for the number of males registered in the class
male_students = int(input("Enter the number of male students registered in" \
" your class: "))

# Ask the user for the number of females registered in the class
female_students = int(input("Enter the number of female students registered" \
" in your class: "))

# Find the total number of students in the class
total_students = int(male_students + female_students)

# Calculate the percent of male students in the class
percent_males = float(male_students / total_students)

# Calculate the percent of female students in the class
percent_females = float(female_students / total_students)

# Display the results
print("The percent of males in the class is", format(percent_males, '.0%' ) \
,", and the percent of females in the    class is", format(percent_females, \
'.0%' ))
