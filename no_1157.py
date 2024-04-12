word = input().lower()      # 사용자로부터 단어를 입력받고 소문자로 변환합니다.
word_list = list(set(word)) # 입력된 단어에서 중복되지 않는 알파벳들의 리스트를 생성합니다.
cnt = []

# 각 알파벳의 등장 횟수를 세어서 리스트에 저장합니다.
for i in word_list:
    count = word.count(i)
    cnt.append(count)

# 가장 많이 등장하는 알파벳의 등장 횟수가 여러 개인지 확인합니다.
if cnt.count(max(cnt)) >= 2:
    print("?")  # 가장 많이 등장하는 알파벳이 여러 개인 경우 물음표를 출력합니다.
else:
    # 여러 개인 경우, 아무 알파벳이나 출력합니다.
    max_index = cnt.index(max(cnt)) # 가장 많이 등장하는 알파벳의 인덱스를 찾습니다.
    print(word_list[max_index].upper())  # 해당 알파벳을 대문자로 출력합니다.
