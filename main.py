import fpgrowth 
import time

# '''simple data'''
# simDat = fpgrowth.loadSimpDat()
# initSet = fpgrowth.createInitSet(simDat)
# myFPtree, myHeaderTab = fpgrowth.createFPtree(initSet, 3)
# myFPtree.disp()

# print fpgrowth.findPrefixPath('z', myHeaderTab)
# print fpgrowth.findPrefixPath('r', myHeaderTab)
# print fpgrowth.findPrefixPath('t', myHeaderTab)

# freqItems = []
# fpgrowth.mineFPtree(myFPtree, myHeaderTab, 3, set([]), freqItems)
# for x in freqItems:
#     print x

'''kosarak data'''
start = time.time()
n = 100000
with open("./data/kosarak.dat", "rb") as f:
    parsedDat = [line.split() for line in f.readlines()]
initSet = fpgrowth.createInitSet(parsedDat)
myFPtree, myHeaderTab = fpgrowth.createFPtree(initSet, n)
freqItems = []
fpgrowth.mineFPtree(myFPtree, myHeaderTab, n, set([]), freqItems)
for x in freqItems:
    print x
print time.time()-start, 'sec'
