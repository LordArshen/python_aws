# Python3.7  
# Coding: utf-8  
# Store the human preproinsulin sequence in a variable called preproinsulin:  
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  
# Store the remaining sequence elements of human insulin in variables:  
lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
insulin = bInsulin + aInsulin

# this aminoacids contribute to the net-change
pKR = {'y': 10.07,'c': 8.18,'k':10.53,'h':6.00,'r':12.48,'d':3.65,'e':4.25}
#count the aminoacids in insulin and return an dictionary with de info "y": cuantity 
seqCount = ({x: float(insulin.count(x)) for x in pKR.keys()})
pH = 0

while (pH <= 14):
    netCharge = (
    +( sum( {x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
    for x in ['k','h','r']}.values()))
    -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
    for x in ['y','c','d','e']}.values() )  )  )
    print('{0:.2f}'.format(pH), netCharge)
    pH +=1
    
# evalue the first positions of the cicle
pH = 0
print("--"*15)

positivo1 = (seqCount["k"]*(10**pKR["k"]))/((10**pH)+(10**pKR["k"]))
print(positivo1)
positivo2 = (seqCount["h"]*(10**pKR["h"]))/((10**pH)+(10**pKR["h"]))
print(positivo2)
positivo3 = (seqCount["r"]*(10**pKR["r"]))/((10**pH)+(10**pKR["r"]))
print(positivo3)

print("--"*15) 

netPositivo=positivo1+positivo2+positivo3
print( "suma positivos", netPositivo )
print("--"*15)
negativo1 = (seqCount["y"]*(10**pH))/((10**pH)+(10**pKR["y"]))
negativo2 = (seqCount["c"]*(10**pH))/((10**pH)+(10**pKR["c"]))
negativo3 = (seqCount["d"]*(10**pH))/((10**pH)+(10**pKR["d"]))
negativo4 = (seqCount["e"]*(10**pH))/((10**pH)+(10**pKR["e"]))
print (negativo1)
print (negativo2)
print (negativo3)
print (negativo4)
print("--"*15)
netNegativo = negativo1+negativo2+negativo3+negativo4
print("negativos ",netNegativo )
print("--"*15)
primerNet = netPositivo - netNegativo
print ("primer netCharge", primerNet )