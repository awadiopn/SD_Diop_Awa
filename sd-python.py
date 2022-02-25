from fonctions import *
from ntpath import *
file=input("veulliez saisir l' adresse complet du fichier:")
nr=recupfich(file)
files=nr

extens=nr[1][1]
if (nr!=False):
    rep=True
    while rep:
        if extens=="csv":
            print("""
                    1:Format xml
                    2:Format yaml
                    3:Format json
            """)
            choix=input("Faites votes Choix: ")
            if choix=="1":
                TransformXml(files)
            elif choix=="2":
                TransformYaml(files)
            elif choix=="3":
                TransformJson(files)
        elif extens=="json":
            print("""
                    1:Format xml
                    2:Format yaml
                    3:Format csv
                    4.Quitter
            """)
            choix=input("Faites votes Choix: ")
            if choix=="1":
                TransformXml(files)
            elif choix=="2":
                TransformYaml(files)
            elif choix=="3":
                TransformCsv(files)
        elif extens=="xml":
            print("""
                    1:Format csv
                    2:Format yaml
                    3:Format json
                    4.Quitter
            """)
            choix=input("Faites votes Choix: ")
            if choix=="1":
                TransformCsv(files)
            elif choix=="2":
                TransformYaml(files)
            elif choix=="3":
                TransformJson(files)
        elif extens=="yaml" or extens=="yml":
            print("""
                    1:Format xml
                    2:Format csv
                    3:Format json
                    4.Quitter
            """)
            choix=input("Faites votes Choix: ")
            if choix=="1":
                TransformXml(files)
            elif choix=="2":
                TransformCsv(files)
            elif choix=="3":
                TransformJson(files)
    else: rep=False
# nb=int(input("Entrer un nombre"))
# if (nb==1):
#     print(TransformJson(filess)) 
# elif (nb==2):
#    print(TransformXml(files))
# elif (nb==3):
#     print(TransformYaml(files))
# elif (nb==4): 
#     print(TransformCsv(files))
    




