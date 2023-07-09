"""
6841 I Speak TXTMSG
"""

Translator = {"CU":"see you", ":-)":"I’m happy", ":-(":"I’m unhappy",
             ";-)":"wink",":-P":"stick out my tongue","(~.~)":"sleepy",
            "TA":"totally awesome","CCC":"Canadian Computing Competition",
            "CUZ":"because","TY":"thank-you","YW":"you’re welcome",
             "TTYL":"talk to you later"}

while True:
    try:
        text = input()
        if text in Translator:
            print(Translator[text])
        else:
            print(text)
    except:
        break
