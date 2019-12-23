##########################################
#Par Jérémy LARDENOIS RT2
#Réponse au challenge
#Décodage en 4 étapes:
#   - convertir romain -> base 10
#   - convertir base 10 -> base 16
#   - regrouper par tranche de 2 digits
#   - Afficher la corespondance ASCII
##########################################

def romtoascii(nbrom):
    #Entrée : chaine de caractère 'nbrom' représantant un nombre romain < 4000
    #Sortie : Entier 'nbdec' équivalent au nombre romain entré
    #Manque la soustraction...
    
    tabrom=['M','D','C','L','X','V','I']
    tabdec=[1000,500,100,50,10,5,1]
    nbdec=0
    previous=tabdec[tabrom.index(nbrom[0])]
    for i in range(len(nbrom)):   
        nbdec+=tabdec[tabrom.index(nbrom[i])]
        if (previous < tabdec[tabrom.index(nbrom[i])]):
            nbdec-=2*previous
        previous=tabdec[tabrom.index(nbrom[i])]
   
    return nbdec   
    

print(romtoascii('CMI')) #255
print(hex(romtoascii('CCLV'))[2:]) #255
