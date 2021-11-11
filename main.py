WORDS = []
def load_data():
    print('loading...')
    with open('words_bank.txt','r') as f:
        big_text = f.read()
        lines = big_text.split('\n')
        for i in range(0,len(lines),2):
            WORDS.append({'english':lines[i] ,'persion': lines[i+1]})

def add():
    n_eng = input('enter english word :')
    n_fa = input('enter persian meaning:')
    f = open('words_bank.txt','w')
    WORDS.append({'english':n_eng ,'persion': n_fa})
    f = open('words_bank.txt','a')
    f.write(WORDS)

def translat_eng2fa(input_txt):
    user_words = user_text.split(' ')
    output_txt = ""
    for user_word in user_words:
        for WORD in WORDS:
            if user_word == WORD['english']:
                output_txt += WORD['persion'] + " "
                break
        else:
            output_txt += user_word + " "

    return output_txt

def translat_fa2eng(input_txt):
    user_words = user_text.split(' ')
    output_txt = ""
    for user_word in user_words:
        for WORD in WORDS:
            if user_word == WORD['persion']:
                output_txt += WORD['english'] + " "
                break
        else:
            output_txt += user_word + " "

    return output_txt

while (True):
    load_data()
    print('enter your choice:\n1- english to farsi\n2- farsi to english\n3-add new word\4-exit')
    choice = int(input("input here :"))
    if choice == 1:
        user_text = input("please write your text : ")
        output_txt = translat_eng2fa(user_text)
        print(output_txt)
    elif choice == 2 :
        user_text = input("please write your text : ")
        output_txt = translat_fa2eng(user_text)
        print(output_txt)
    elif choice == 3 :
        add()
    elif choice == 4:
        exit()