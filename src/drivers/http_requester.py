import requests

class HttpRequester:
    #onde estiver self esta no mesmo contexto
    def __init__(self) -> None:
        self.__url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm'
        # privado

    def request_from_page(self): 
        response = requests.get(self.__url)
        print(response)