def toLowerCase(text):
    return text.lower()


def removeSpaces(text):
    newText = ""
    for i in text:
        if i == " ":
            continue
        else:
            newText = newText + i
    return newText
def Diagraph(text):
    Diagraph = []
    group = 0
    for i in range(2, len(text), 2):
        Diagraph.append(text[group:i])

        group = i
    Diagraph.append(text[group:])
    return Diagraph

def FillerLetter(text):
    k = len(text)
    if k % 2 == 0:
        for i in range(0, k, 2):
            if text[i] == text[i + 1]:
                new_word = text[0:i + 1] + str('x') + text[i + 1:]
                new_word = FillerLetter(new_word)
                break
            else:
                new_word = text
    else:
        for i in range(0, k - 1, 2):
            if text[i] == text[i + 1]:
                new_word = text[0:i + 1] + str('x') + text[i + 1:]
                new_word = FillerLetter(new_word)
                break
            else:
                new_word = text
    return new_word

def encrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    char1 = matr[e1r][e2c]

    char2 = ''
    char2 = matr[e2r][e1c]

    return char1, char2
def decrypt_search(mat, element):
    for i in range(5):
        for j in range(5):
            if (mat[i][j] == element):
                return i, j


def decrypt_RowRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1c == 0:
        char1 = matr[e1r][4]
    else:
        char1 = matr[e1r][e1c - 1]

    char2 = ''
    if e2c == 0:
        char2 = matr[e2r][4]
    else:
        char2 = matr[e2r][e2c - 1]

    return char1, char2


def decrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1r == 0:
        char1 = matr[4][e1c]
    else:
        char1 = matr[e1r - 1][e1c]

    char2 = ''
    if e2r == 0:
        char2 = matr[4][e2c]
    else:
        char2 = matr[e2r - 1][e2c]

    return char1, char2


def decrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    char1 = matr[e1r][e2c]

    char2 = ''
    char2 = matr[e2r][e1c]

    return char1, char2


def decryptByPlayfairCipher(Matrix, cipherlist):
    plainText = []
    for i in range(0, len(cipherlist)):
        c1 = 0
        c2 = 0
        ele1_x, ele1_y = decrypt_search(Matrix, cipherlist[i][0])
        ele2_x, ele2_y = decrypt_search(Matrix, cipherlist[i][1])

        if ele1_x == ele2_x:
            c1, c2 = decrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)

        elif ele1_y == ele2_y:
            c1, c2 = decrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        else:
            c1, c2 = encrypt_RectangleRule(
                Matrix, ele1_x, ele1_y, ele2_x, ele2_y)

        cipher = c1 + c2
        plainText.append(cipher)
    return plainText

def decryptt(ciphertext,matrix,text_Plain):
    text_Plain = removeSpaces(toLowerCase(text_Plain))
    CipherTextList = Diagraph(FillerLetter(ciphertext))
    plaintext = decryptByPlayfairCipher(matrix, CipherTextList)
    PlainText = ""
    for i in plaintext:
        PlainText += i
    if (len(text_Plain) % 2) != 0:
        PlainText = PlainText[:-1]
    return PlainText