#00. 文字列の逆順
string00 = "stressed"
string_split00 = list(string00)
reverse_string00 = ""
for i in reversed(string_split00):
    reverse_string00 += i
print(reverse_string00)

#01「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
string01 = "パタトクカシーー"
string_split01 = list(string01)
ans_string01 = ""
for i in range(len(string_split01)):
    if i == 1 or i == 3 or i == 5 or i == 7:
        ans_string01 += string_split01[i]
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
print(ans_string02)

# 03 "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
string03 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
string_split03 = string03.split(" ")
print(string_split03)
for i in string_split03:
    print(len(list(i)))