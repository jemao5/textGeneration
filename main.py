def generateTable(data,k=4):

    T = {}
    for i in range(len(data)-k):
        X = data[i:i+k]
        Y = data[i+k]
        #print("X  %s and Y %s  "%(X,Y))

        if T.get(X) is None:
            T[X] = {}
            T[X][Y] = 1
        else:
            if T[X].get(Y) is None:
                T[X][Y] = 1
            else:
                T[X][Y] += 1

    return T

T = generateTable("my name is Tejas and I am a car who is very new")
#print(T)

def convertFreqIntoProb(T):
    for kx in T.keys():
        s = float(sum(T[kx].values()))
        for k in T[kx].keys():
            T[kx][k] = T[kx][k]/s

    return T

T = convertFreqIntoProb(T)
print(T)

text_path = "stateoftheunion.txt"
def load_text(filename):
    with open(filename,encoding='utf8') as f:
        return f.read().lower()

text = load_text(text_path)
print('Loaded the dataset.')

def MarkovChain(text,k=4):
    T = generateTable(text,k)
    T = convertFreqIntoProb(T)
    return T

model = MarkovChain(text)
print('Model Created Successfully!')
