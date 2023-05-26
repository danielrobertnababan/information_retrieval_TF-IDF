docA = '90% data yang ada di dunia, dibuat hanya dalam dua tahun terakhir'
docB = 'Suhu tubuh merupakan contoh dari data kontinu'
docC = 'Dalam era revolusi industri 4.0 ini, data menjadi mata uang baru'
docD = 'Data scientist bertugas menganalisis berbagai macam data dalam jumlah besar'
docE = 'Indexing atau pengindeksan merupakan suatu proses penting dalam IR'
docF = 'Informasi adalah data yang disimpan, diproses, atau ditransmisikan'

bowA = docA.split(" ")
bowB = docB.split(" ")
bowC = docC.split(" ")
bowD = docD.split(" ")
bowE = docE.split(" ")
bowF = docF.split(" ")

bowF

wordSet = set().union(bowA, bowB, bowC, bowD, bowE, bowF)

wordSet

wordDictA = dict.fromkeys(wordSet, 0) 
for word in bowA:
    wordDictA[word]+=1
wordDictB = dict.fromkeys(wordSet, 0) 
for word in bowB:
    wordDictB[word]+=1
wordDictC = dict.fromkeys(wordSet, 0) 
for word in bowC:
    wordDictC[word]+=1
wordDictD = dict.fromkeys(wordSet, 0) 
for word in bowD:
    wordDictD[word]+=1
wordDictE = dict.fromkeys(wordSet, 0) 
for word in bowE:
    wordDictE[word]+=1
wordDictF = dict.fromkeys(wordSet, 0) 
for word in bowF:
    wordDictF[word]+=1
    
wordDictF

import pandas as pd
pd.set_option('display.max_columns', None)
pd.DataFrame([wordDictA, wordDictB, wordDictC, wordDictD, wordDictE, wordDictF])

1)Term Frequency

def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(bow)
    for word, count in wordDict.items():
        tfDict[word] = count/float(bowCount)
    return tfDict
    
tfBowA = computeTF(wordDictA, bowA)
tfBowB = computeTF(wordDictB, bowB)
tfBowC = computeTF(wordDictC, bowC)
tfBowD = computeTF(wordDictD, bowD)
tfBowE = computeTF(wordDictE, bowE)
tfBowF = computeTF(wordDictF, bowF)

tfBowF

2)Inverse Data Frequency
def computeIDF(docList):
    import math
    idfDict = {}
    N = len(docList)
    
    idfDict = dict.fromkeys(docList[0].keys(), 0)
    for doc in docList:
        for word, val in doc.items():
            if val >= 0:
                idfDict[word] += 1
    
    for word, val in idfDict.items():
        idfDict[word] = math.log10(N / float(val))
        
    return idfDict    
    
    idfs = computeIDF([wordDictA, wordDictB, wordDictC, wordDictD, wordDictE, wordDictF])
    
3)TF-IDF
def computeTFIDF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.items():
        tfidf[word] = val*idfs[word]
    return tfidf
    
tfidfBowA = computeTFIDF(tfBowA, idfs)
tfidfBowB = computeTFIDF(tfBowB, idfs)
tfidfBowC = computeTFIDF(tfBowC, idfs)
tfidfBowD = computeTFIDF(tfBowD, idfs)
tfidfBowE = computeTFIDF(tfBowE, idfs)
tfidfBowF = computeTFIDF(tfBowF, idfs)

import pandas as pd
pd.DataFrame([tfidfBowA, tfidfBowB, tfidfBowC, tfidfBowD, tfidfBowE, tfidfBowF])
