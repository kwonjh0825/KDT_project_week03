import requests, os
from dotenv import load_dotenv
from pprint import pprint


def search_movie(title):
    pass
    # 여기에 코드를 작성합니다.
    load_dotenv()
    api_key = os.environ.get('api_key')
    base_url = f'https://api.themoviedb.org/3/'
    search_url = f'search/movie?api_key={api_key}&language=ko-KR&query={title}&region=KR'
    res = requests.get(base_url+search_url).json()
    data = res['results']
    if len(data) < 1:
        return None
    return data[0]['id']


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id 반환
    검색한 결과 영화가 없다면 None을 반환
    """
    print(search_movie('기생충'))
    # 496243
    print(search_movie('그래비티'))
    # 959101
    print(search_movie('검색할 수 없는 영화'))
    # None
