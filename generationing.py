# this script is dedicated to the extraction of characteristic
# pump curve information


# import numpy as np
from tkinter import filedialog
import os


class GenerateCollection:
    sourcenamelist = []
    sourcetypelist = []
    locationlist = []
    typelist = []
    sourcelength = 0
    media_dictionary = {}
    media_length = 0

    def addsource(self, sourcelocation):
        self.sourcelength += 1
        print("S Len: ", self.sourcelength)
        self.locationlist.append(sourcelocation)
        _, snl = os.path.split(sourcelocation)
        self.sourcenamelist.append(snl)
        _, ext = os.path.splitext(sourcelocation)
        self.sourcetypelist.append(ext.lower())
        if self.sourcetypelist[self.sourcelength - 1] == ".png":
            self.addpng(sourcelocation)

    def addpng(self, pdflocation):
        print("png needs to be added")
        print(self.media_length)
        print(pdflocation)

    def addpdf(self):
        print("pdf needs to be added")
        print(self.sourcetypelist[self.sourcelength])

    def isempty(self):
        return self.sourcelength == 0


geninfo = GenerateCollection()


def import_source():
    file = filedialog.askopenfilename(filetypes=(("PNG images", "*.png"), ("JPEG images", "*.jpg"),
                                                 ("PDF files", "*.pdf")))
    geninfo.addsource(file)


def isempty():
    return geninfo.isempty()


