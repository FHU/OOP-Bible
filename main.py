from bible import Bible

'''
Bible
* translation (string)
* books (list of Book objects)

Book (e.g. Genesis, Exodus)
* name (string)
* testament (Testament enum)
* type (BookType enum)
* chapters (list of Chapter objects)

Chapter
* number (int)
* verses (list of Verse objects)

Verse
* number (int)
* note (string)
* text (string)

BookType (enum)
* LAW = 1
* HISTORY = 2 
* WISDOM = 3
* PROPHECY = 4
* GOSPEL = 5
* EPISTLE = 6
* APOCALYPSE = 7 

TestamentType (enum)
* OLD_TESTAMENT
* NEW_TESTAMENT
* NONE

'''


if __name__ == "__main__":
    
    kjv = Bible("data/kjv.txt", "|")

    # book
    gen = kjv.books[0]
    print(gen)

    # chapter 
    gen1 = gen.chapters[0]
    print(gen1)

    # verse 
    gen1_1 = gen1.verses[0]
    print(gen1_1)

    # search 
    refs = kjv.search("light")

    for ref in refs:
        print(ref)

    

