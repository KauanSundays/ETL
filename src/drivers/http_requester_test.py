from .http_requester import HttpRequester #importar o arquivo a ser testado

def test_request_from_page(): #sempre ter test no começo / nome da classe a ser testada
    http_requester = HttpRequester()
    http_requester.request_from_page()
