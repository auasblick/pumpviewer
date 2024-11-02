# this script is dedicated to the extraction of characteristic
# pump curve information


# import numpy as np
import os


class GenerateCollection:
    # source properties
    source_n = int(0)  # number of sources
    locationlist = []  # location array
    sourcenamelist = []  # name array of source files
    sourcetypelist = []  # type array of source files
    # image properties
    img_size = [0, 0]
    img_rgb = [(0, 0, 0)]

    def addsource(self, sourcelocation):
        self.source_n += 1
        print("S Len: ", self.source_n)
        self.locationlist.append(sourcelocation)
        _, snl = os.path.split(sourcelocation)
        self.sourcenamelist.append(snl)
        _, ext = os.path.splitext(sourcelocation)
        self.sourcetypelist.append(ext.lower())
        if self.sourcetypelist[self.source_n - 1] == ".png":
            self.addpng(sourcelocation)

    def addpng(self, pnglocation):
        pass
        # reader = png.Reader(filename=pnglocation)
        # self.img_size[0], self.img_size[1], self.img_rgb, img_info = reader.read_flat()
        # print("png file read")
        # print(pnglocation)

    def addpdf(self):
        print("pdf needs to be added")
        print(self.sourcetypelist[self.source_n])

    def isempty(self):
        return self.source_n == 0

    def get_rgb(self):
        return self.img_rgb


geninfo = GenerateCollection()


def import_source():
    file = filedialog.askopenfilename(filetypes=(("PNG images", "*.png"), ("JPEG images", "*.jpg"),
                                                 ("PDF files", "*.pdf")))
    geninfo.addsource(file)
    rgb = geninfo.get_rgb()


def isempty():
    return geninfo.isempty()


