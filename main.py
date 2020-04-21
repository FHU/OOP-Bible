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
* Law = 1
* History = 2 
* Wisdom = 3
* Prophecy = 4
* Gospel = 5
* Epistle = 6
* Apocalypse = 7

TestamentType (enum)
* OldTestament
* NewTestament
* None

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

    

