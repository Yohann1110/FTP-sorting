# ------------------------------------------------------------------------
#                         Different function :
# ------------------------------------------------------------------------

#check if there is an extension 
def findpoint_(myString):
    point="."
    for letter in myString:
        if letter == point:
            return True
    return False

#remove the folder from my dirList
def removeFolderFromList(myList):
    if 'image' in myList: 
        myList.remove('image')
        myList.remove('document')
        myList.remove('note')
        myList.remove('erreur')
        myList.remove('divers')
    return myList

