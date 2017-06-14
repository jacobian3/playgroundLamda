values = [6, 1, 3, 2, 4, 5]

length = len(values)

s_val = sorted(values)

r_ndex  = length // 2

l_ndex = r_ndex - 1

median = ( s_val[l_ndex] + s_val[r_ndex] ) / 2

print(median)


