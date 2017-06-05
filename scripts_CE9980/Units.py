#SET conversion factors
FT_PER_YD = 3
FT_PER_IN = 1/12
IN_PER_CM = 1/2.54
CM_PER_M = 100
FT_PER_BOING744 = 200
FT_PER_RAILWAY_CAR = 50

#READ user input
print('Choose distance Units [ FT,YD,M ]')
distance_unit = input('What is the unit of your measurement? :')

#COMPUTE: Convert everyting to yds
print('','Conversion to know sized object')
if distance_unit == 'FT':
    dist2_targetN_FT = int( input('Distance to target in feet: ') )
    dist2_targetN_YD = dist2_targetN_FT * 1/FT_PER_YD

elif distance_unit == 'YD':
    dist2_targetN_YD = int( input('Distance to target in yards: ') )
else:
    dist2_targetN_M = int( input('Distance to target in meters: ') )
    #??? solve over 79chr limit problem
    dist2_targetN_YD = dist2_targetN_M * CM_PER_M * IN_PER_CM * FT_PER_IN * 1/FT_PER_YD 


#COMPUTE recognizable units
dist_in_boings = dist2_targetN_YD * FT_PER_YD * 1/FT_PER_BOING744
dist_in_railwaycars = dist2_targetN_YD * FT_PER_YD * 1/FT_PER_RAILWAY_CAR

#WRITE
print('The number of Boing 747 planes: {}'.format(dist_in_boings))
print('The number of railway cars: {}'.format(dist_in_railwaycars))
