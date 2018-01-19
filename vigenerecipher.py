alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

frequencySortedAlpha = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 'U', 'M', 'W', 'F', 'G', 'Y', 'P',
                        'B', 'V', 'K', 'J', 'X', 'Z', 'Q']


def encode(plaintext, key):
    plaintext = removeNonLetters(plaintext)
    count = 0
    klength = len(key)
    ciphertext = ""
    for c in plaintext:
        charASCII = ord(c) + int(key[count % klength])
        if charASCII >= 91:
            charASCII = (charASCII % 91) + 65
        ciphertext += chr(charASCII)
        count += 1
    print(ciphertext)

def checkFreqSimilarity(freqList):
    count = 0
    samefreqletters = 0
    freqList = freqList[:-20]
    for letter in freqList:
        if letter in frequencySortedAlpha[:-20]:
            samefreqletters += 1
        count += 1
    return samefreqletters


def shift(shiftval, text, Substitution):
    shiftedtext = ""
    if(Substitution):
        for c in text:
            charASCII = ord(c) - shiftval
            if charASCII < 65:
                charASCII = 91 - (65 - charASCII)
            shiftedtext += chr(charASCII)
    else:
        for c in text:
            charASCII = ord(c) + shiftval
            if charASCII >= 91:
                charASCII = (charASCII % 91) + 65
            shiftedtext += chr(charASCII)
    return shiftedtext


def isInAlphabet(c):
    for l in alphabet:
        if c == l:
            return True
    return False


def removeNonLetters(ciphertext):
    ciphertext = ciphertext.upper()
    for c in ciphertext:
        if not isInAlphabet(c):
            ciphertext = ciphertext.replace(c, '')
    return ciphertext


def getLetterCount(ciphertext):
    # Returns a dictionary with keys of single letters and values of the
    # count of how many times they appear in the message parameter.
    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0,
                   'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0,
                   'Y': 0, 'Z': 0}
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for letter in ciphertext:
        if letter in LETTERS:
            letterCount[letter] += 1

    return letterCount


def checkCoincidence(shiftval, ciphertext):  # To use, give a shift value and a string as function arguements.
    # Returns the number of coincidences between a text and its shifted version.
    coinCount = 0
    count = 0
    while count < len(ciphertext) - shiftval:
        if ciphertext[count] == ciphertext[count + shiftval]:
            coinCount += 1
        count += 1
    return coinCount


def obtainsubtext(startletter, shiftval, ciphertext):
    count = startletter
    subtext = ""
    while count < len(ciphertext):
        subtext += ciphertext[count]
        count += shiftval
    return subtext


def findKeyLenghts(ciphertext):
    keyLenghts = {}
    r = max(20, len(ciphertext) // 20)
    for i in range(2, r + 1):
        keyLenghts[i] = checkCoincidence(i, ciphertext)
    sortedlengths = list(sorted(keyLenghts, key=keyLenghts.__getitem__, reverse=True))
    return keyLenghts, sortedlengths


def freqanalysis(ckeylength, ciphertext):    #Takes candidate key length and ciphertext.
    key = []
    for i in range(0, ckeylength):
        maxsim = 0  # maximum similarity
        kmaxsim = 0  # key resulting in maximum frequency similarity.
        subtext = obtainsubtext(i, ckeylength, ciphertext)
        lc = getLetterCount(subtext)
        mostfreqletter = list(sorted(lc, key=lc.__getitem__, reverse=True))[0]
        for l in ['E', 'T', 'A']:
            k = ( ord(mostfreqletter) - ord(l) ) % 26
            shiftedstext = shift(k, subtext,Substitution=True)
            slc = getLetterCount(shiftedstext)
            freqlist = list(sorted(slc, key=slc.__getitem__, reverse=True))
            sim = checkFreqSimilarity(freqlist)
            if sim > maxsim:
                maxsim = sim
                kmaxsim = k
        key.append(kmaxsim)
    keyword = ""
    for l in key:
        keyword += alphabet[l]
    print("Key is " + str(key) + " = " + keyword)
    return key

def decodewithkey(ciphertext, key):

    ctext = removeNonLetters(ciphertext)
    ctext = ctext.upper()
    count = 0
    klength = len(key)
    plaintext = ""
    print(ciphertext)
    for c in ctext:
        charASCII = ord(c) - key[count % klength]
        if charASCII < 65:
            charASCII = 91 - (65 - charASCII)
        plaintext += chr(charASCII)
        count += 1
    print("Key Length " + str(len(key)) + ": ")
    print(plaintext)
    print("---------------------------------------------------------------------------------------------------------")
    return plaintext

def decodewithkeylength(ciphertext, keylength):
    ctext = removeNonLetters(ciphertext)
    key = freqanalysis(keylength, ctext)
    plaintext = decodewithkey(ctext, key)

def decode(ciphertext):
    ctext = removeNonLetters(ciphertext)  # Remove non letter characters from the ciphertext.
    klengths, sortedlengths = findKeyLenghts(ctext)
    maxcoincidence = klengths[sortedlengths[0]]
    i = 0

    numOfKeysToTest = max (5,len(ciphertext) // 50)

    while (klengths[sortedlengths[i]] == maxcoincidence ) or (i < numOfKeysToTest) :
        key = freqanalysis(sortedlengths[i], ctext)
        plaintext = decodewithkey(ctext, key)
        i += 1


