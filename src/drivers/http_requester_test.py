from .http_requester import HttpRequester #importar o arquivo a ser testado

def test_request_from_page(requests_mock): #sempre ter test no começo / nome da classe a ser testada
    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm'
    requests_mock.get(url, status_code=200, text='alguma coisa')

    http_requester = HttpRequester()
    request_response = http_requester.request_from_page()
    print(request_response)