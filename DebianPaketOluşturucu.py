#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from tkinter import *
import tkinter.ttk as ttk
from tkinter.ttk import Combobox
from tkinter import filedialog

root = Tk()
root.title("Debian Paket Oluşturucu Programı")
root.resizable(width=FALSE ,height=FALSE)
img=PhotoImage(file='debian.png')
root.tk.call('wm','iconphoto',root._w,img)
mainframe = ttk.Frame(root,padding='3 3 12 12')
mainframe.grid(column=0, row=0)
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight =1)

folderPath = StringVar()

folder = folderPath.get()

py_file_Path = StringVar()

png_file_Path = StringVar()

SelectDebFiles = []

def olustur():
    folder = folderPath.get()
    f= os.path.split(folder)[1]
    
    folder1 = py_file_Path.get()
    py_file= os.path.split(folder1)[1]

    folder2 = png_file_Path.get()
    png_file= os.path.split(folder2)[1]

    for j in os.walk(folder):
        for sub in j[2]:
            SelectDebFiles.append(j[0]+'/'+sub)
            
    for source in SelectDebFiles:
        if (source[-4:] == '.png'):
            PngFile = os.path.split(source)[1]
            PngPath = '/usr/local/bin'+'/'+str(f)+'/'+PngFile
            
        if source[-3:] == '.py' :
            PyFile = os.path.split(source)[1]
            PyPath = '/usr/local/bin'+'/'+str(f)+'/'+PyFile
            
        if (os.path.split(source)[1].find('.desktop') is -1):
            target = str(folder)+'/'+str(f)+'/usr/local/bin/'+str(f)
         
        if (os.path.split(source)[1].find('.desktop') > -1):
            target = str(folder)+'/'+str(f)+'/usr/share/applications'
           
        if os.path.exists(target) is False:
            os.makedirs(target)
        
        os.system('cp -avr ' + source + ' ' + target)
    
    DebMakeString = ""
    DesktopMakeString = ""
    DebMakeFolder = str(folder)+'/'+str(f)+'/'+'DEBIAN'

    if os.path.isdir(DebMakeFolder) is False:
            os.makedirs(DebMakeFolder)
            
    os.system('touch '+DebMakeFolder+'/control')

    for makefile in zip([proje_klasoru.get(), versiyon.get(), section.get(),priority.get(), iletisim.get(), combo1.get(),aciklama.get()],
                        ['Package:', 'Version:', 'Section:', 'Priority:','Maintainer:', 'Architecture:', 'Description:']):
        DebMakeString = DebMakeString + makefile[1]+chr(32)+makefile[0] +'\n'
        
    with open(DebMakeFolder+'/control', 'w') as control:
        control.write(DebMakeString)

    folder = folderPath.get()
    f= os.path.split(folder)[1]

    folder1 = py_file_Path.get()
    py_file= os.path.split(folder1)[1]

    folder2 = png_file_Path.get()
    png_file= os.path.split(folder2)[1]
        
    for makefile in zip(['Version', 'Name', 'Encoding', 'Comment','Path', 'Exec', 'Icon', 'Terminal', 'Type', 'Categories'],
                        [combo1.get(), proje_klasoru.get(), 'UTF-8', aciklama.get(),'/usr/local/bin/'+f,'python3'+' '+'/usr/local/bin/'+f+'/'+py_file,
                         '/usr/local/bin/'+f+'/'+png_file,'false', 'Application',combo.get()+';']):
        
        DesktopMakeString = DesktopMakeString + str(makefile[0]+'='+makefile[1]) + '\n'
    
    with open(str(folder)+'/'+str(f)+'.desktop', 'w') as control:
        control.write('[Desktop Entry]\n'+DesktopMakeString)
        
    source1=str(folder)+'/'+str(f)+'.desktop'
    target1 = str(folder)+'/'+str(f)+'/usr/share/applications'

    if os.path.exists(target1) is False:
            os.makedirs(target1)
     
    os.system('cp -avr ' + source1 + ' ' + target1)

    os.remove(source1)

    os.system('dpkg-deb --build '+str(folder)+'/'+str(f))
   
    exit()

def proje_klasor_sec():
    folder_selected = filedialog.askdirectory()
    folderPath.set(folder_selected)
    folder = folderPath.get()
    f= os.path.split(folder)[1]
    proje_klasoru.delete(0,END)
    proje_klasoru.insert(0,f)
    
def py_dosyasi_sec():
    ftypes = [('Python code files', '*.py')]
    py_file_selected = filedialog.askopenfilename(filetypes=ftypes)
    py_file_Path.set(py_file_selected)
    folder = py_file_Path.get()
    py_file= os.path.split(folder)[1]
    py_dosyasi.delete(0,END)
    py_dosyasi.insert(0,py_file)

def simge_dosyasi_sec():
    ftypes = [('Image files', '*.png')]
    png_file_selected = filedialog.askopenfilename(filetypes=ftypes)
    png_file_Path.set(png_file_selected)
    folder = png_file_Path.get()
    png_file= os.path.split(folder)[1]
    simge_dosyası.delete(0,END)
    simge_dosyası.insert(0,png_file)

proje_klasoru = ttk.Entry(mainframe, width =40)
proje_klasoru.grid(column = 2, row = 0)

py_dosyasi = ttk.Entry(mainframe, width =40)
py_dosyasi.grid(column = 2, row = 1)

simge_dosyası = ttk.Entry(mainframe, width =40)
simge_dosyası.grid(column = 2, row = 2)

versiyon = ttk.Entry(mainframe, width =40)
versiyon.insert(0,'0.1')
versiyon.grid(column = 2, row = 3)

section = ttk.Entry(mainframe, width =40)
section.insert(0,'base')
section.grid(column = 2, row = 5)

priority = ttk.Entry(mainframe, width =40)
priority.insert(0,'optional')
priority.grid(column = 2, row = 6)

iletisim = ttk.Entry(mainframe, width =40)
iletisim.insert(0,'x@x.com')
iletisim.grid(column = 2, row = 7)

aciklama = ttk.Entry(mainframe, width =40)
aciklama.insert(0,'Masaüstü Uygulaması')
aciklama.grid(column = 2, row = 8)

ttk.Label(mainframe, text ='Proje Klasörünü Seçiniz').grid(column = 1, row = 0, sticky=W)
ttk.Label(mainframe, text ='py Uzantılı Python Dosyanızı Seçiniz').grid(column = 1, row = 1, sticky=W)
ttk.Label(mainframe, text ="png Uzantılı Simge Dosyasınızı Seçiniz").grid(column = 1, row = 2, sticky=W)
ttk.Label(mainframe, text ='Versiyonunuzu Yazınız').grid(column = 1, row = 3, sticky=W)
ttk.Label(mainframe, text ='Kategorinizi Seçiniz').grid(column = 1, row = 4, sticky=W)
ttk.Label(mainframe, text ='Section').grid(column = 1, row = 5, sticky=W)
ttk.Label(mainframe, text ='Priority').grid(column = 1, row = 6, sticky=W)
ttk.Label(mainframe, text ='İletişim').grid(column = 1, row = 7, sticky=W)
ttk.Label(mainframe, text ='Açıklama').grid(column = 1, row = 8, sticky=W)
ttk.Label(mainframe, text ='İşlemcinizi Seçiniz').grid(column = 1, row = 9, sticky=W)
ttk.Label(mainframe, text ='').grid(column = 1, row = 10, sticky=W)

kategori=["Development","Education","Office"]
combo=Combobox(mainframe,values=kategori, width =38,state='readonly')
combo.set("Development")
combo.grid(column = 2, row = 4)

islemciniz=["i386","amd64"]
combo1=Combobox(mainframe,values=islemciniz, width =38,state='readonly')
combo1.set("amd64")
combo1.grid(column = 2, row = 9)

ttk.Button(mainframe, text='Seç',command= proje_klasor_sec).grid(column=3, row=0)
ttk.Button(mainframe, text='Seç',command= py_dosyasi_sec).grid(column=3, row=1)
ttk.Button(mainframe, text='Seç',command= simge_dosyasi_sec).grid(column=3, row=2)
ttk.Button(mainframe, text='Oluştur',command= olustur).grid(column=2, row=11)

root.mainloop()    
