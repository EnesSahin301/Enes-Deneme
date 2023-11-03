import string
alfabe= list(string.ascii_uppercase)

def encoder(text,runningKey):
   anahtar= createKey(runningKey.upper())
   mesaj = list(text.upper())
   keyCounter = 0
   for i in range(0,len(text)):
    k = 0
    while k < 26:
        if text[i] not in alfabe:
            break
        if keyCounter == len(runningKey):
            keyCounter = 0
        if mesaj[i] == anahtar[keyCounter][k]:
           mesaj[i] = alfabe[k]
           keyCounter+=1
           break
        k+=1
   return "".join(text)

def createKey(runningKey):
    i = 0
    key = []
    while i < len(runningKey):
      w = alfabe[alfabe.index(f"{runningKey[i]}"):]
      w.extend(alfabe[:alfabe.index(f"{runningKey[i]}")])
      key.append(w)
      i+=1
    return key
print(encoder("Wml, Haexrv scl Zettt! Opwclvr ztzr. Me rcevwcbyc dxdvry xv glw nmnv 1883, scl V las bumk amgxwg qa lgemf xzpb vx odcyh gcm qeq gmngz nwh.(M ydb glw xlre xgwz xzt ubzat Zrxmgv Oeuzenvvh bb xzt Xnwl Ponmf 3,Ipvgz xa eiijqeiv Kqraaco ssj Iqzi sriqien neikwurr) Qdc'ii hgwoetag tsl p tbx gu yhikiqbrk, pvq exime xzt miifia bj Otqeheporhvdv,zef,X lbrl qtnqw nwh!","PINES"))