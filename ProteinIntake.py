print('\'Protein Intake Calculator\' by Andrew')
#Collecting Data
print('')
print('--Your Details--')
kg = float(input('Weight(kg): '))
cal = float(input('Calories Intake/day(cal): '))

#Calculations
print('')
grams_perkg = str(0.8 * kg) + 'g/day'
Calories_Intake = str(0.25 * cal) + 'cal/day'
print('Results:')
print('Protein to take(g)                     : ',grams_perkg)
print('Protein to take(cal) by Calories Intake: ',Calories_Intake)

#Citation
print('')
print('Source: https://www.acsm.org/docs/default-source/files-for-resource-library/protein-intake-for-optimal-muscle-maintenance.pdf')