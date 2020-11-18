tenThousandPos = 4
# 억 단위 자릿수
hundredMillionPos = 9
txtDigit = ['', '십', '백', '천', '만', '억']
txtNumber = ['', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
txtPoint = ' 점 '
txtEnglish = ' 영어다! '

#def texttrans(strNum):
    #resultStr = ''

def digit2txt(strNum):
    resultStr = ''
    digitCount = 0
    print(strNum)
    #자릿수 카운트

    #for ch in str:
        #if ch == 'a':
            #break
            #resultStr = txtEnglish

    for ch in strNum:
        # ',' 무시
        if ch == ',':
            continue
        #소숫점 까지
        elif ch == '.':
            break
        digitCount = digitCount + 1


    digitCount = digitCount-1
    index = 0

    while True:
        notShowDigit = False
        ch = strNum[index]
        #print(str(index) + ' ' + ch + ' ' +str(digitCount))
        # ',' 무시
        if ch == ',':
            index = index + 1
            if index >= len(strNum):
                break;
            continue
        

        ###
        if ch == 'a':
            resultStr = txtEnglish
            break;


        if ch == '.':
            resultStr = resultStr + txtPoint
        else:
            #자릿수가 2자리이고 1이면 '일'은 표시 안함.
            # 단 '만' '억'에서는 표시 함
            if(digitCount == 1) and int(ch) == 1:
                resultStr = resultStr + ''
            elif int(ch) == 0:
                resultStr = resultStr + ''
                # 단 '만' '억'에서는 표시 함
                if (digitCount != tenThousandPos) and  (digitCount != hundredMillionPos):
                    notShowDigit = True
            else:
                resultStr = resultStr + txtNumber[int(ch)]


        # 1억 이상
        if digitCount > hundredMillionPos:
            if not notShowDigit:
                resultStr = resultStr + txtDigit[digitCount-hundredMillionPos]
        # 1만 이상
        elif digitCount > tenThousandPos:
            if not notShowDigit:
                resultStr = resultStr + txtDigit[digitCount-tenThousandPos]
        else:
            if not notShowDigit:
                resultStr = resultStr + txtDigit[digitCount]

        if digitCount <= 0:
            digitCount = 0
        else:
            digitCount = digitCount - 1
        index = index + 1
        if index >= len(strNum):
            break;
    print(resultStr)


if __name__ == '__main__':

    digit2txt("21,560,000.83")
    digit2txt("14")
    digit2txt("1")
    digit2txt("267")
    digit2txt("2214.4")
    digit2txt("244")
    digit2txt("17.4")
    digit2txt("a")


    