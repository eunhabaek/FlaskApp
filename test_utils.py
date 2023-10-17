from utils import get_movie_info

def test_get_movie_info():
    test_url="https://m.search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%9D%B8%EA%B0%84%2C+%EA%B3%B5%EA%B0%84%2C+%EC%8B%9C%EA%B0%84+%EA%B7%B8%EB%A6%AC%EA%B3%A0+%EC%9D%B8%EA%B0%84&x_csa=%7B%22mv_id%22%3A%22163379%22%7D&pkid=68"

    title, image, desc = get_movie_info(test_url)
    print(title)
    print(image)
    print(desc)

    assert title =='인간, 공간, 시간 그리고 인간'