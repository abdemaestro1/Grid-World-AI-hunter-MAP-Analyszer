#Creat a file 
milaf_tafribi=open("Title tajribi","w")

#Write inside the file 
milaf_tafribi.write("salamo3alikom xorfa dyana \n")
milaf_tafribi.write("thalaw fraskom o nodo dasliw rah weden dhor nodo t9awdo\n")

#Open the file first and Show it content 
milaf_tafribi=open("d","r")#Open the file content and look inside it 
mohtawa=milaf_tafribi.read()#read the file with read method after open it 
print(mohtawa)

#Close the file 
milaf_tafribi.close()