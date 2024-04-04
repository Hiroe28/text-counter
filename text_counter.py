import streamlit as st

# タイトルの設定
st.title('文字数カウンター')

# ユーザー入力のテキストエリアを作成
user_input = st.text_area('テキストを入力してください', '')

# 「文字カウント」ボタン
if st.button('文字カウント'):
    # スペースを含む文字数をカウント
    count_with_spaces = len(user_input)

    # スペースを除いた文字数をカウント
    count_without_spaces = len(user_input.replace(' ', ''))

    # 結果の表示
    st.write('スペース込みの文字数:', count_with_spaces)
    st.write('スペースなしの文字数:', count_without_spaces)
else:
    st.write('スペース込みの文字数:', 0)
    st.write('スペースなしの文字数:', 0)