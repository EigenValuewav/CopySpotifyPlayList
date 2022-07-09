import requests as req
response = req.get("https://open.spotify.com/")
print(response.content)








# 쿼리스트링이란? 
# URL의 뒤에 입력 데이터를 함께 제공하는 가장 단순한 데이터 전달 방법이다. 
# 웹개발에서 데이터를 요청하는 방식 중 대표적인 것이 GET방식과 POST방식인데, 
# 주로 GET방식으로 데이터를 요청할 때 쓰이는 방법이다.