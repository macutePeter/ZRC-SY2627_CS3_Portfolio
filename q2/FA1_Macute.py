class Publication:
    def __init__(self, title: str, author: str):
        self.__title = title
        self.__author = author

    def get_title(self) -> str:
        return self.__title

    def set_title(self, title: str):
        self.__title = title

    def get_author(self) -> str:
        return self.__author

    def set_author(self, author: str):
        self.__author = author

    def display_info(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")


class Book(Publication):
    def __init__(self, title: str, author: str, number_of_pages: int):
        super().__init__(title, author)
        self.__number_of_pages = 0
        self.set_number_of_pages(number_of_pages)

    
    def get_number_of_pages(self) -> int:
        return self.__number_of_pages

    def set_number_of_pages(self, number_of_pages: int):
        if number_of_pages > 0:
            self.__number_of_pages = number_of_pages
        else:
            print("Number of pages must be positive.")

    def display_info(self):
        super().display_info()
        print(f"Number of pages: {self.__number_of_pages}")


class Magazine(Publication):
    def __init__(self, title: str, author: str, issue_number: int):
        super().__init__(title, author)
        self.__issue_number = 0
        self.set_issue_number(issue_number)

    
    def get_issue_number(self) -> int:
        return self.__issue_number

    def set_issue_number(self, issue_number: int):
        if issue_number > 0:
            self.__issue_number = issue_number
        else:
            print("Issue number must be positive.")

    def display_info(self):
        super().display_info()
        print(f"Issue number: {self.__issue_number}")



if __name__ == "__main__":

    pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
    book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
    mag1 = Magazine("National Geographic", "Various Authors", 202)

    print("Publication Information (1):")
    pub1.display_info()

    print("\nBook Information (1):")
    book1.set_number_of_pages(-310)  
    book1.display_info()
    print(book1.get_number_of_pages())

    print("\nMagazine Information (1):")
    mag1.display_info()
    print(mag1.get_issue_number())

    print("\n" + "="*40 + "\n")

    pub2 = Publication("Nature", "Magdalena Skipper et al.")
    book2 = Book("Jujutsu Kaisen, Vol. 1", "Gege Akutami", 192)
    mag2 = Magazine("Rolling Stone: Nirvana Special Edition", "Rolling Stone Editors", 1024)

    print("Publication Information (2):")
    pub2.display_info()

    print("\nBook Information (2):")
    book2.display_info()

    print("\nMagazine Information (2):")
    mag2.display_info()