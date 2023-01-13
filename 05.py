import requests, os
from dotenv import load_dotenv
from pprint import pprint

def recommendation(title):
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
    else:
        movie_id = data[0]['id']
        recommend_url = f'movie/{movie_id}/recommendations?api_key={api_key}&language=ko-KR&region=KR'
        res = requests.get(base_url+recommend_url).json()
        data = res['results']
        movie_recommended = []
        for d in data:
            movie_recommended.append(d['title'])
        return movie_recommended

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
