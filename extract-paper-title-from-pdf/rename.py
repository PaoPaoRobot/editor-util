
# src_dir = '/mnt/c/Users/daiwe/OneDrive/Desktop/paper/'              
# des_dir = '/mnt/c/Users/daiwe/OneDrive/Desktop/paper/new/'            
# pyPdf available at http://pybrary.net/pyPdf/from pyPdf import PdfFileWriter, PdfFileReader
import os

for fileName in os.listdir('/mnt/c/Users/daiwe/OneDrive/Desktop/paper/'):
    actfile = file(fileName,"rb")
    try:
        if fileName.lower()[-3:] != "pdf": continue
        input1 = PdfFileReader(actfile)
        # print the title of document1.pdf
        print '##1', fileName, '##2', input1.getDocumentInfo().title()
    except:
        print '##1', fileName, '##2'
    
    try:
        trgtfilename = input1.getDocumentInfo().title + "_" + fileName
    except:
        print "\n## ERROR ## %s Title could not be extracted. PDF file may be encrypted!" % fileName
    continue
       
    del input1
    actfile.close()
    
    print 'Trying to rename from:', fileName, '\n to ', trgtfilename
    try:
        print fileName
		# os.rename(fileName,trgtfilename)
    except:
        print fileName, ' could not be renamed!'
        print '\n## ERROR ## Maybe the filename already exists or the document is already opened!'