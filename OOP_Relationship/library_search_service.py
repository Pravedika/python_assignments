class SearchService:
    def search(self, keyword):
        print("Searching for:", keyword)

class Library:
    def search_book(self, search_service, keyword):
        search_service.search(keyword)

Library().search_book(SearchService(), "Python")
