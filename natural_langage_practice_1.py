#00. 文字列の逆順
string00 = "stressed"
string_split00 = list(string00)
reverse_string00 = ""
for i in reversed(string_split00):
    reverse_string00 += i
print("問題00")
print(reverse_string00)

#01「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
string01 = "パタトクカシーー"
string_split01 = list(string01)
ans_string01 = ""
for i in range(len(string_split01)):
    if i == 1 or i == 3 or i == 5 or i == 7:
        ans_string01 += string_split01[i]
print("問題01")
print(ans_string01)

# 02「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
string02 = "パトカー"
string_02 = "タクシー"
string_split02 = list(string02)
string_split_02 = list(string_02)
count02 = 0
ans_string02 = ""
for i in range(len(string_split02)):
    if count02 == i :
        ans_string02 += string_split02[i]
    for j in range(len(string_02)):
        if count02 == j:
            ans_string02 += string_split_02[j]
            count02 += 1
            break
print("問題02")
print(ans_string02)

# 03 "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
string03 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
string_split03 = string03.split(" ")
print("問題03")
for i in string_split03:
    print(len(list(i)))

# 04"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，
# 1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
string04 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can"
string_split04 = string04.split(" ")
get_first_chara_num_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
ans_dict = {}

"""
文字列の先頭の一文字を取得する関数
@param String string
@return string first_chara
"""
def getFirstChara(word):
    word_list = list(word)
    first_chara = word_list[0]
    return first_chara

"""
文字列の先頭の2文字を取得する関数
@param String string
@return string first_and_second_chara
"""
def getFirstAndSecondChara(word):
    word_list = list(word)
    first_and_second_chara = word_list[0] + word_list[1]
    return first_and_second_chara

for index, item in enumerate(string_split04):
    if index+1 in get_first_chara_num_list:
        value_string = getFirstChara(item)
    else:
        value_string = getFirstAndSecondChara(item)
    ans_dict[index + 1] = value_string
print("問題04")
print(ans_dict.items())