values = [6, 1, 3, 2, 4, 5]

# sorts the values; median calculation only take sorted
sval = sorted(values) 

# take the length; div by 2 and covert to integer index val
index_val = int( len(sval) / 2 ) # finds the rsval_index as '4'

#using sorted values find the left an right 
rval = sval[index_val] #find rval of midpoint
lval = sval[index_val - 1] # finds lval of midpoint

median = ( rval + lval ) / 2 # finds the average

print(median)

