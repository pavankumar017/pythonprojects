dict = {
    "name" : "Pavan",
    "age" : 27

}

for i in dict:
    print(dict.get(i))


print (dict.get("DOB" , "1/1/2011"))  #so here DOB key is not present in dict hence - the default value is displayed which was added

dict["DOB"] = "17/08/1996"  #ADDING A NEW VALUE TO DICT

print (dict.get("DOB" , "1/1/2011"))
dict["name"] = "Pavan Kumar"  #modifying the dict
dict["emoty"] = 0

print(dict) 
print(dict.items())
print(dict.values())
print(dict.keys())