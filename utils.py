import requests
from bs4 import BeautifulSoup

def get_movie_info(url_receive):
    headers={
        'User-Agent':"mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/118.0.0.0 safari/537.36"
    }
#html 읽어오기
    data=requests.get(url_receive,
                    headers=headers)
    soup=BeautifulSoup(data.text, 'html.parser' )

    #파싱
    title=soup.select_one('div.title_area._title_area > h2 > span > strong').get_text()
    image=soup.select_one('div.cm_content_area._cm_content_area_info > div > div.detail_info > a > img')['src']
    desc=soup.select_one('div > div.detail_info > div > span').get_text()

    return title, image, desc