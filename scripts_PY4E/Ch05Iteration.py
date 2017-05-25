#(5.2) WHAT IS THE FLOW OF EXECUTION FOR A WHILE STATEMENT?
# 1. Eval  condition truth, 2. if false exit while;continue
# at next statement. 3. If true, execute body and go back to 1.
# each time through the body is an iteration
# body of loop should change value of vars so that conditions is false
#(5.3) otherwise situation is an infinite loop: no iteration var

#(5.4) HOW TO ESCAPE INFINITE LOOPS? BECAUSE CONDITION IS ALWAYS TRUE,
# use break to to go to the next statement outside of the loop
# or use continue to skip remainder of body and return to condition
# evaluation

#(5.4) WHY USE THE USE OF BREAK COMMON? AN IF STATEMENT, USED IN THIS WAY, 
# allows check of condition anywhere in the loop; not just the top.
# i.e. stop when(affirmative/anywhere) vs repeat until(neg/end) or 
# While/do (neutra/begin)

#(5.5) WHY USE A CONTINUE?
# if in the middle of an iteration and you want to skip to the next iteration
# continue imediately skips to the next iteration

#(5.1)?HOW DOES AN ACCUMULATOR WORK?
#(5.1)get the current value, add the distance and accumulate it by 
#storing inside of perimeter
#(5.1) before you can update the variable you must have already
#initialized it; see top of program
