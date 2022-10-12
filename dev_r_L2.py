# Name: Riya Dev
# Date: 11/11/2020

import random

def check_complete(assignment, csp_table):
   if assignment.find('.') != -1: return False
   for hexa in csp_table:
      if len(set([assignment[i] for i in hexa])) != 6: return False
   return True
   
def select_unassigned_var(assignment, csp_table):
   """ your code goes here """
   return random.choice([x for x in range(0, len(assignment)) if assignment[x] == "."]) #forward checking
   """
   # pseudocode
   for x in range len(assignment):
      if assignment[x] == '.'
         [ x ...]
   random.choice ([x ...])
   """
      
def isValid(value, var_index, assignment, csp_table):
   """ your code goes here """
   # value is consistent with assignment
   assignment = assignment[:var_index] + str(value) + assignment[var_index+1:]
   for x in csp_table: # [[0, 1, 2, 6, 7, 8], [2, 3, 4, 8, 9, 10], [5, 6, 7, 12, 13, 14], [7, 8, 9, 14, 15, 16], [9, 10, 11, 16, 17, 18], [13, 14, 15, 19, 20, 21], [15, 16, 17, 21, 22, 23]] 
      if var_index in x:
         for y in x: # [0, 1, 2, 6, 7, 8]
            if (not y == var_index) and (assignment[y] == assignment[var_index]): return False
               # print("Is Valid:", y, var_index, assignment[y], assignment[var_index])
   return True

def backtracking_search(input, csp_table): 
   return recursive_backtracking(input, csp_table)

def recursive_backtracking(assignment, csp_table):
   """ your code goes here """
   if check_complete(assignment, csp_table): return assignment
   var_index = select_unassigned_var(assignment, csp_table)
   
   for value in range(1, 7): # csp_table[var_index]: #number
      #print(assignment, '\t', var_index, '\t', value)
      if isValid(value, var_index, assignment, csp_table):                  
         assignmentcopy = assignment[:var_index] + str(value) + assignment[var_index+1:]
         csp_tablecopy = csp_table
         result = recursive_backtracking(assignmentcopy, csp_tablecopy)
         if result != None: return result
   return None

def display(solution):
   result = ""
   for i in range(len(solution)):
      if i == 0: result += "  "
      if i == 5: result += "\n"
      if i == 12: result += "\n"
      if i == 19: result += "\n  "
      result += solution[i] + " "
   return result

def main():
   csp_table = [[0, 1, 2, 6, 7, 8], [2, 3, 4, 8, 9, 10], [5, 6, 7, 12, 13, 14], [7, 8, 9, 14, 15, 16], [9, 10, 11, 16, 17, 18], [13, 14, 15, 19, 20, 21], [15, 16, 17, 21, 22, 23]] 
   solution = backtracking_search(input("24-char(. and 1-6) input: "), csp_table)
   if solution != None:
      print (display(solution))
      print ('\n'+ solution)
      print (check_complete(solution, csp_table))
   else: print ("It's not solvable.")

if __name__ == '__main__':
   main()
   
"""
Sample Output 1:
24-char(. and 1-6) input: ........................
  1 2 3 1 2 
1 4 5 6 4 5 1 
2 6 3 1 2 3 6 
  2 4 5 4 6 

123121456451263123624546
True

Sample Output 2:
24-char(. and 1-6) input: 6.....34...1.....2..4...
  6 1 2 1 3 
1 3 4 5 6 4 1 
5 6 2 1 3 2 5 
  3 4 5 4 6 

612131345641562132534546
True
"""