from hashlib import new
from posixpath import basename
from csv import *
import csv
import json
import yaml
import xmltodict
import dicttoxml

def recupfich(a):
    file=a
    a=basename(a)
    a=a.split(".")
    ext=str(a[-1])
    ext=ext.upper()
    if ext in["CSV","JSON","YAML","XML","yml"]:
        new_fichier=[] 
        fichier=open(file,'r',encoding="utf8")
        if (ext=="CSV"):
             csv_reader=DictReader(fichier)
             for row in csv_reader:
                new_fichier.append(row) 
             li=[new_fichier,a]
             return li
             #print(new_fichier)  
        elif(ext=="JSON"):
            with open(file,'r') as fichier:
                new_fichier = json.load(fichier)
            li=[new_fichier,a]
            return li
                #print(new_fichier)
        elif(ext=="YAML"):
            with open(file, 'r') as new_fichier:
                print(yaml.load(new_fichier))
        elif (ext == 'XML'):
            k = open(file, 'r')
            new_fichier = xmltodict.parse(k.read())
            print(fichier)
            li=[new_fichier,a]
            return li
    else:
        print("Le fichier est invalide")
        return False

def TransformCsv(myfile):
    for i in range(len(myfile)):
        elm=myfile[i]
        keys=list(elm.keys())
    with open("mynewfile.csv","w") as csv_out:
        writer=DictWriter(csv_out,fieldnames=keys)
        writer.writeheader()
        for data in myfile:
            writer.writerow(data)


def TransformJson(filejson):
    import json
    fjson= open('file.json', 'w')
    json.dump(filejson, fjson)
    print(fjson)
    return "True"

def TransformYaml(fileyaml):
    import yaml
    fyaml= open('file.yaml', 'w')
    yaml.dump(fileyaml, fyaml)
    print(fyaml)
    return "True"


def TransformXml(filexml):
    from dicttoxml import dicttoxml
    xml = dicttoxml(filexml)
    xmlfile = open("file.xml", "w")
    xmlfile.write(xml.decode())
    xmlfile.close()
    print(xmlfile)
    return "True"


