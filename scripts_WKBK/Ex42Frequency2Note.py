#PROGRAM Ex42.py3

#SET values of know frequencies
C4_FREQ = 261.63
D4_FREQ = 293.66
E4_FREQ = 329.63
F4_FREQ = 349.23
G4_FREQ = 392.00
A4_FREQ = 440.00
B4_FREQ = 493.88

#READ frequency from user
frequency = float(input("Enter frequency: "))

#COMPUTE match for frequency and note
#IF frequency is in range +- 1 Hz of C4 THEN
if frequency <= ( C4_FREQ + 1 ) and \
    frequency >= ( C4_FREQ - 1 ) :
        #SET name of note
        note = 'C4'
        print("the frequency is between:%s & %s." % (C4_FREQ - 1, C4_FREQ + 1))

#IF frequency is in range +- 1 Hz of D4 THEN
elif frequency <= ( D4_FREQ + 1 ) and \
    frequency >= ( D4_FREQ - 1 ) :
        #SET name of note
        note = 'D4'
        print("the frequency is between:%s & %s." % (D4_FREQ - 1, D4_FREQ + 1))

#IF frequency is in range +- 1 Hz of E4 THEN
elif frequency <= ( E4_FREQ + 1 ) and \
    frequency >= ( E4_FREQ - 1 ) :
        #SET name of note
        note = 'E4'
        print("the frequency is between:%s & %s." % (E4_FREQ - 1, E4_FREQ + 1))

#IF frequency is in range +- 1 Hz of F4 THEN
elif frequency <= ( F4_FREQ + 1 ) and \
    frequency >= ( F4_FREQ - 1 ) :
        #SET name of note
        note = 'F4'
        print("the frequency is between:%s & %s." % (F4_FREQ - 1, F4_FREQ + 1))

#IF frequency is in range +- 1 Hz of G4 THEN
elif frequency <= ( G4_FREQ + 1 ) and \
    frequency >= ( G4_FREQ - 1 ) :
        #SET name of note
        note = 'G4'
        print("the frequency is between:%s & %s." % (G4_FREQ - 1, G4_FREQ + 1))

#IF frequency is in range +- 1 Hz of A4 THEN
elif frequency <= ( A4_FREQ + 1 ) and \
    frequency >= ( A4_FREQ - 1 ) :
        #SET name of note
        note = 'A4'
        print("the frequency is between:%s & %s." % (A4_FREQ - 1, A4_FREQ + 1))
        
#IF frequency is in range +- 1 Hz of B4 THEN
elif frequency <= ( B4_FREQ + 1 ) and \
    frequency >= ( B4_FREQ - 1 ) :
        #SET name of note
        note = 'B4'
        print("the frequency is between:%s & %s." % (B4_FREQ - 1, B4_FREQ + 1))

#ELSE
else:
    #SET note to 'no value within range'
    note = 'no value within range'
#END-IF    

#WRITE frequency corresponds to note
print("frequency %s corresonds to %s." % (frequency, note))

#END 
