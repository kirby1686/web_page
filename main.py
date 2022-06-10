import streamlit as st
import requests
import pprint

header = st.container()
body = st.container()
footer = st.container()

h_i = header.text_input('패스트푸드점 검색', placeholder='enter 키워드 입력')

h_b = header.button('enter')
if h_b:
    url = 'https://floating-harbor-78336.herokuapp.com/fastfood'
    r = requests.get(url, params={'searchKeyword': h_i})

    rjson = (r.json())
    body.write(f'총 {rjson["total"]}개의 패스트푸드점을 찾었습니다.')

    body.write(rjson)

    """rjson['total']
    rjson['list']"""


