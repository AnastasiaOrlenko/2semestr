import urllib.request 
import re



Links = ['http://echo.msk.ru/news/1884974-echo.html', 
         'http://www.kp.ru/online/news/2588291/', 
         'https://regnum.ru/news/polit/2212909.html',
         'http://izvestia.ru/news/649093']




def fun_1(url_1):
 #   url = 'http://echo.msk.ru/news/1884974-echo.html'  # адрес страницы, которую мы хотим скачать
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'  # хотим притворяться браузером

    req_1 = urllib.request.Request('http://echo.msk.ru/news/1884974-echo.html', headers={'User-Agent':user_agent}) 
    
    with urllib.request.urlopen(req_1) as response:
        html_1 = response.read().decode('utf-8')
        return html_1
    
    
def fun_2(url_2):
 #   url = 'http://echo.msk.ru/news/1884974-echo.html'  # адрес страницы, которую мы хотим скачать
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'  # хотим притворяться браузером  

    req_2 = urllib.request.Request('http://tass.ru/politika/3835411', headers={'User-Agent':user_agent}) 
# добавили в запрос информацию о том, что мы браузер Мозилла
 
    with urllib.request.urlopen(req_2) as response:
        html_2 = response.read().decode('utf-8')
        return html_2

    
def download_1 (html_1):
    
    regPostTitleEcho = re.compile('<span class="_ga1_on_ include-relap-widget contextualizable">(.*?)</span>', re.DOTALL)
    titlesEcho = regPostTitleEcho.findall(html_1)
    
    return (titlesEcho)


def download_2 (html_2):
    
    regPostTitleKp = re.compile('<div class="b-material-text__l js-mediator-article">(.*?)<div class="extra-content">', re.DOTALL)
    titlesKp = regPostTitleKp.findall(html_2)
    
    return (titlesKp)
  
    
 

    
def pechat_1 (titlesEcho):
    for t in titlesEcho:
        print (t)

def pechat_2 (titlesKp):
    for l in titlesKp:
        print (l)   

def split_1 (titlesEcho):
    A = set(list(titlesEcho))
    print(A)
    

def main ():
    
    url_1 = 'http://echo.msk.ru/news/1884974-echo.html'
    url_2 = 'http://tass.ru/politika/3835411'
    
    htmlEcho = fun_1(url_1)
    htmlKp = fun_2(url_2)
    
    titlesEcho = download_1 (htmlEcho)
    pechat_1 (titlesEcho)
    print ("Zalupa")
    split_1(titlesEcho)
    print ("Zalupa")
    
    
    
    titlesKp = download_2 (htmlKp)
    pechat_2 (titlesKp)
    



if __name__ == '__main__' :
    main ()
