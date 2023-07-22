#
#hello today I am publishing a code to correct errors, I allow you to use my code to create applications, 
#the code works in Russian and English layout for convenience, you can change languages, 
#Just replace the letters with your language, it works something like this:
 #   "Ghbdtn Fylhtq rfr ltkf" "Привет андрей как дела" or "Рш пгны рщц фку нщг" "Hi guys how are you"
#Have a good project!
ru = list("йцукенгшщзфывапролдячсмитьхъжэбю ")
en = list("qwertyuiopasdfghjklzxcvbnm[];',. ")
ru_en = {}
en_ru = {}
for i in range(len(ru)):
    ru_en[ru[i]] = en[i]
    en_ru[en[i]] = ru[i]
inp = input('Enter the text with confused layout:')
out = []
for i in inp:
    if i in en:
        out.append(en_ru[i])
    elif i in ru:
        out.append(ru_en[i])
print(''.join(out))
#and he does not translate dots either, because in Russian there are more letters than in English Buy-Buy!
