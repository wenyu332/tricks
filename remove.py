# coding: utf-8
for dirpath,dirnames,filenames in os.walk("g:/Docker/PAN-Card-OCR-master/src/"):
    for filename in filenames:
        if os.path.splitext(filename)[1]==".png":
            filepath=os.path.join(dirpath,filename)
            print(filepath)
            os.remove(filepath)
            
