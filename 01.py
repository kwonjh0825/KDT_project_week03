import requests, os
from dotenv import load_dotenv

def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  

    load_dotenv()
    api_key = os.environ.get('api_key')
    url = f'https://api.themoviedb.org/3/movie/popular?'
    params = {'api_key': api_key, 'langauge':'ko-KR', 'region': 'KR'}
    res = requests.get(url, params=params).json()
    data = res['results']
    
    return len(data)
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20