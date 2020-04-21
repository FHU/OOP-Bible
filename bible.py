class Bible:

    def __init__(self):
        self.books = []
        self.translation = ""

    # TODO
    def __init__(self, file, separator):
        '''
        Initialize Bible from a text file containing 1 verse per line.

        Parameters:
            file (str): the path to the input file containing
            the bible text. 

            separator (str) : the string that separates the book, 
            chapter number, verse number, and verse text.
        '''
        self.translation = ""

        self.books = self.parse_from_file(file, separator)

    # TODO
    def parse_from_file(self, file, separator):
        '''
        Read in Bible from a text file containing 1 verse per line.
        Ignore all lines begining with the `#` character.

        Parameters:
            file (str): the path to the input file containing
            the bible text. 

            separator (str) : the string that separates the book, 
            chapter number, verse number, and verse text.

        Returns:
            A list of book objects (populated with chapters populated
            with verses) as listed in the file. 
        '''

        with open(file) as f:
            lines = f.readlines()

        print(lines)

        return []

    # TODO
    def search(self, search_string):
        ''' 
        Returns an unduplicated list of Reference objects 
        that contain the search_string.

        Parameters:
            search_string (str): the string to search for 
            in the verses in the chapters of the books of this
            bible object.

        Returns:
            A list of unique (non-duplicated) Reference objects
            with verses that contain the search string. 
        '''
        pass

