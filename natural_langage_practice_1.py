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

# 05 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
string05 = "I am an NLPer"

"""
n-gram関数
@param word
@param n_num
@return n_gram_string_list
"""
def N_Gram(word, n_num):
    string_split05 = list(word)
    n_gram_string = ""
    n_gram_string_list = []
    for i in range(len(string_split05)):
        if len(string_split05) >= n_num:
            for j in range(n_num):
                n_gram_string += string_split05[j]
            n_gram_string_list.append(n_gram_string)
            n_gram_string = ""
        string_split05.pop(0)
    return n_gram_string_list

print("問題05")
print(N_Gram(string05, 2))

# 06 "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ
string06 = "paraparaparadise"
string_06 = "paragraph"
string06_bi_gram = set(N_Gram(string06, 2))
string_06_bi_gram = set(N_Gram(string_06, 2))
print(string06_bi_gram)
print(string_06_bi_gram)
print("問題06")

s_06_union = string06_bi_gram | string_06_bi_gram
print("和集合")
print(s_06_union)

s_intersection = string_06_bi_gram.intersection(string06_bi_gram)
print("積集合")
print(s_intersection)

s_diff = string06_bi_gram.difference(string_06_bi_gram)
print("差集合")
print(s_diff)

#07. テンプレートによる文生成
#引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
def formatTemplate(x, y, z):
    temp07 = "{0}時の{1}は{2}".format(x, y, z)
    return temp07
print("問題07")
print(formatTemplate(12, "気温", 22.4))
