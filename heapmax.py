
# coding: utf-8

# In[ ]:


heapvalues = 30*[None]
proximopai = 1
ultimoindice = 1


# In[ ]:


def subir(indice):
    indice_pai = indice//2 
    if(heapvalues[indice] is not None and heapvalues[indice_pai] is not None):
        if(heapvalues[indice] > heapvalues[indice_pai]):
            aux = heapvalues[indice_pai]
            heapvalues[indice_pai] = heapvalues[indice]
            heapvalues[indice] = aux
            subir(indice_pai)

def descer(indice):
    if(heapvalues[indice*2] is not None and heapvalues[indice*2+1] is not None):
        if(heapvalues[indice*2] > heapvalues[2*indice+1]):
            filhomaior = indice*2
        else:
            filhomaior = indice*2 +1
    elif(heapvalues[indice*2] is not None and heapvalues[indice*2+1] is not None):
        filhomaior = indice*2
    else:
        filhomaior = indice
    if(heapvalues[filhomaior] > heapvalues[indice]):
        aux = heapvalues[filhomaior]
        heapvalues[filhomaior] = heapvalues[indice]
        heapvalues[indice] = aux
        descer(filhomaior)



def inserir(num):
    global proximopai
    global heapvalues
    if(heapvalues[2*proximopai] is  None):
        heapvalues [2*proximopai] =  num   
        return 2*proximopai
    if(heapvalues[2*proximopai+1] is  None):
        heapvalues [2*proximopai+1] =  num
        aux = proximopai
        proximopai = proximopai+1
        return 2*aux+1

def removermax():
    global proximopai
    global ultimoindice
    aux = heapvalues[1]
    heapvalues[1] = heapvalues[ultimoindice]
    heapvalues[ultimoindice] = None
    descer(1)
    ultimoindice = ultimoindice -1
def remover(indice):
    global proximopai
    global ultimoindice
    aux = heapvalues[indice]
    heapvalues[indice] = heapvalues[ultimoindice]
    heapvalues[ultimoindice] = None
    descer(indice)
    ultimoindice = ultimoindice -1

def inserirHeap(num):
    global proximopai
    global heapvalues
    if(heapvalues[1] is not None):
        global ultimoindice
        indice = inserir(num)
        ultimoindice = indice
        print("entrou aqui "+ str(indice)+" "+str(num))
        if(indice is not None):
            subir(indice)
    else:
        heapvalues.insert(1,num)


inserirHeap(90)
inserirHeap(89)
inserirHeap(70)
inserirHeap(36)
inserirHeap(75)
inserirHeap(63)
inserirHeap(65)
inserirHeap(21)
inserirHeap(18)
inserirHeap(15)
inserirHeap(12)
inserirHeap(72)
print(heapvalues)
remover(1)
print(heapvalues)





