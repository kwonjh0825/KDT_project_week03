import requests, os
from dotenv import load_dotenv
from pprint import pprint


def credits(title):
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
    movie_id = data[0]['id']
    credits_url = f'movie/{movie_id}/credits?api_key={api_key}&language=ko-KR&region=KR'
    res = requests.get(base_url+credits_url).json()
    casts = res['cast']
    crew = res['crew']
    result = {'cast' : [], 'crew' : []}
    result['cast'] = [x['name'] for x in casts if x['cast_id'] < 10]
    result['crew'] = [x['name'] for x in crew if x['department'] == 'Directing']

    return result
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록 반환
    영화 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
