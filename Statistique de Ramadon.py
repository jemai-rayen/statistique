from PyQt5.uic import loadUi
from PyQt5.QtWidgets import*
from pickle import *
from numpy import array
app=QApplication([])
w=loadUi("Statistique de Ramadon.ui")
def add():
    n=w.num.text()
    s=w.com.currentText()
    if len (n)!=8 :
        QMessageBox.critical(w,"erreur","le numero doit etre 8 chifres")
    else:
        f=open("avis.dat","ab")
        e=dict()
        e["telephone"]=n
        if w.fem.isChecked()==True:
            e["genre"]="femme"
        elif w.ho.isChecked()==True:
            e["genre"]="homme"
        else:
            QMessageBox.critical(w,"erreur","selection un genre")
        e["feuilleton"]=s
        dump(e,f)
        f.close()
def affi():
    f=open("avis.dat","rb")
    test=False
    w.tb.setRowCount(0)
    i=0
    while not test:
        try:
            e=load(f)
            w.tb.insertRow(i)
            w.tb.setItem(i,0,QTableWidgetItem(e["telephone"]))
            w.tb.setItem(i,1,QTableWidgetItem(e["genre"]))
            w.tb.setItem(i,2,QTableWidgetItem(e["feuilleton"]))
            i=i+1
        except:
            test=True
    f.close()
    teste=True
    f2=open("statistique.txt","r")
    ch=f2.readline()
    while ch!="":
        w.ls.addItem(ch+"\n")
        ch=f2.readline()
    f2.close()
def satist():
    ff=hf=fj=hj=fsa=hsa=fs=hs=0
    f = open("avis.dat", "rb")
    test = False
    while not test:
        try:
            e=load(f)
            feuill=e["feuilleton"]
            genre=e["genre"]
            if feuill =="FALLOUJAH" and genre=="femme":
                ff=ff+1
            elif feuill =="FALLOUJAH" and genre=="homme":
                hf=hf+1
            elif feuill =="JBAL LAHMAR" and genre=="femme":
                fj=fj+1
            elif feuill =="JBAL LAHMAR" and genre=="homme":
                hj=hj+1
            elif feuill =="SINDRELLA" and genre=="femme":
                fs=fs+1
            elif feuill =="SINDRELLA" and genre=="homme":
                hs=hs+1
            elif feuill =="SABEK EL KHIR" and genre=="femme":
                fsa=fsa+1
            elif feuill =="SABEK EL KHIR" and genre=="homme":
                hsa=hsa+1
        except:
            test=True
    f.close()
    total=ff+hf+fj+hj+fs+hs+fsa+hsa
    pff=(ff/total)*100
    phf=(hf/total)*100
    falouja=pff+phf
    pfj=(fj/total)*100
    phj=(hj/total)*100
    jbal=pfj+phj
    pfs=(fs/total)*100
    phs=(hs/total)*100
    sind=pfs+phs
    pfsa=(fsa/total)*100
    phsa=(hsa/total)*100
    sabek=pfsa+phsa
    f2=open("statistique.txt","w")
    f2.write("le feuilleton FALLOUJAH suivi par "+str(phf)+"% homme et "+str(pff)+"% femme\n")
    f2.write("le feuilleton FALLOUJAH suivi par "+str(falouja/total)+"% télèspectateur\n")
    f2.write("le feuilleton JBAL LAHMAR suivi par "+str(phj)+"% homme et "+str(pfj)+"% femme\n")
    f2.write("le feuilleton JBAL LAHMAR suivi par "+str(jbal/total)+"% télèspectateur\n")
    f2.write("le feuilleton SINDRELLA suivi par "+str(phs)+"% homme et "+str(pfs)+"% femme\n")
    f2.write("le feuilleton SINDRELLA suivi par "+str(sind/total)+"% télèspectateur\n")
    f2.write("le feuilleton SABEK EL KHIR suivi par "+str(phsa)+"% homme et "+str(pfsa)+"% femme\n")
    f2.write("le feuilleton SABEK EL KHIR par "+str(sabek/total)+"% télèspectateur\n")
w.stat.clicked.connect(satist)
w.cf.clicked.connect(add)
w.aff.clicked.connect(affi)
w.show()
app.exec_()