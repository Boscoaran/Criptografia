from os import replace


def calcFrecPrinc(cfr,desc):
    frecabs = [0]*26
    n=0
    for carac in cfr:
        ind = ord(carac)
        if ind>=65 and ind<=90:
            ind = ind-65
        elif ind>=97 and ind<=122:
            ind = ind-97
        else:
            ind=28
        if ind<28:        
            frecabs[ind] = frecabs[ind]+1
            n=n+1       
    frec=frecabs
    for i in range(0, 26):
        frec[i]=frecabs[i]/n
        i = i+1
    let_e=0
    let_a=0
    x=0
    for i in range(0, 26):
        if x<frecabs[i]:
            x=frecabs[i]
            let_a=let_e
            let_e=i    
    desc[0]=chr(let_a+65)
    desc[4]=chr(let_e+65)
          
    return(desc)
              
def descifrar(txt,desc):
    txt=list(txt)
    for i in range(0, 26):
        l=chr(i+97)
        if desc[i]=='':
            None
        elif ord(desc[i])>=65 and ord(desc[i])<=90:
            for c in range (0, len(txt)):
                if txt[c]==desc[i]:
                    txt[c]=l
    txt=convert_str(txt)
    return(txt)          

def convert_str(s):
    nueva_str = ""
    for x in s:
        nueva_str += x 
    return nueva_str

def buscar_coincidencias(txt,coincidencia):
    list_txt=list(txt)
    list_coinc=list(coincidencia)
    enc=False
    c=0
    descubierta=''
    while c<len(list_txt) and enc==False:
        if list_txt[c]==list_coinc[0]:
            i=1
            c=c+1
            error=False
            while i<len(list_coinc) and not error:
                if list_txt[c]==list_coinc[i]:
                    i=i+1
                    c=c+1
                elif list_coinc[i]=='?' and list_txt[c]!=' ' and ord(list_txt[c])<97:
                    i=i+1
                    descubierta=list_txt[c]
                    c=c+1
                else:
                    error=True
        c=c+1
    return(descubierta)

def eliminar_desc(desc):
    for i in range (0, 26):
        if desc[i]!='':
            if ord(desc[i])<97:
                desc[i]=chr(ord(desc[i])+32)
    return(desc)                    

def buscar_rr(txt):
    list_txt=list(txt)
    c1=''
    c2=0
    doble_r=False
    while c2<len(list_txt) and not doble_r: 
        if list_txt[c2]==c1 and ord(c1)<97:
            doble_r=True
            desc=c1
            c2=len(list_txt)
            return desc
        else:
            c1=list_txt[c2]
            c2=c2+1    

def palabras_rep(txt):
    lista_txt=[""]
    pal=""
    for c in txt:
        if c.isalpha():
            pal=pal+c
        if c.isascii and not c.isalpha() and pal!="":
            lista_txt.append(pal)
            pal=""
    lista_txt.remove("")
    rep=[]
    for p1 in lista_txt:
        n=0
        for p2 in lista_txt:
            if p1==p2:
                n=n+1
                lista_txt.remove(p1)
        rep.append((p1,n))
    return(rep) 

def calc_frec_pal(rep):
    n=0
    for p in rep:
        n=n+p[1]
    for i in range (0, len(rep)):
        x=rep[i][1]
        p=rep[i][0]
        rep[i]=(p,x/n)      

def pal_mas_rep(rep):
    n1=0
    n2=0
    n3=0
    p1=""
    p2=""
    p3=""
    for p in rep:
        if p[1]>n1:
            p3=p2
            n3=n2
            p2=p1
            n2=n1
            p1=p[0]
            n1=p[1]
        elif p[1]>n2:
            p3=p2
            n3=n2
            p2=p[0]
            n2=p[1]
        elif p[1]>n3:
            p3=p[0]
            n3=p[1]     
    top_pal=[(p1,n1),(p2,n2),(p3,n3)]
    return(top_pal)

def sust_por_pal_princ(txt,top_pal):
    p1=top_pal[0][0]
    p1=list(p1)
    p2=top_pal[1][0]
    p2=list(p2)
    p3=top_pal[2][0]
    p3=list(p3)
    #estadísticamente el que más aparece es "de". Es muy improbable que "en" sea el más repetido
    if p1[1]==p2[0]:    #de - en - la:
        txt=txt.replace(p1[0],'d')
        txt=txt.replace(p1[1],'e')
        txt=txt.replace(p2[0],'e')
        txt=txt.replace(p2[1],'n')
        txt=txt.replace(p3[0],'l')
        txt=txt.replace(p3[1],'a')
    elif p1[1]==p3[0]:  #de - la - en
        txt=txt.replace(p1[0],'d')
        txt=txt.replace(p1[1],'e')
        txt=txt.replace(p2[0],'l')
        txt=txt.replace(p2[1],'a')
        txt=txt.replace(p3[0],'e')
        txt=txt.replace(p3[1],'n')
    else:               #la - de - en
        txt=txt.replace(p1[0],'l')
        txt=txt.replace(p1[1],'a')
        txt=txt.replace(p2[0],'d')
        txt=txt.replace(p2[1],'e')
        txt=txt.replace(p3[0],'e')
        txt=txt.replace(p3[1],'n')    
    return(txt)

with open('texto.txt','r') as f: 
    txt=f.read()       
desc=['']*26

#usando la frecuencia de letras 'e' 'a'
desc=calcFrecPrinc(txt, desc)
txt=descifrar(txt,desc)
desc=eliminar_desc(desc)

#usando la frecuencia de palabras más repetidas "de" "en" "la" (e/a/n/d/l)
'''rep=palabras_rep(txt)
top_pal=pal_mas_rep(rep)
txt=sust_por_pal_princ(txt,top_pal)
desc=eliminar_desc(desc)'''

#buscar l (a la)
nuevo_desc=buscar_coincidencias(txt, " a ?a ")
desc[11]=nuevo_desc
txt=descifrar(txt,desc)
desc=eliminar_desc(desc)

#buscar n (en el)
nuevo_desc=buscar_coincidencias(txt, " e? el ")
desc[13]=nuevo_desc
txt=descifrar(txt,desc)
desc=eliminar_desc(desc)

#buscar o (no)
nuevo_desc=buscar_coincidencias(txt, " n? ")
desc[14]=nuevo_desc
txt=descifrar(txt,desc)
desc=eliminar_desc(desc)

#buscar s (las)
nuevo_desc=buscar_coincidencias(txt, " la? ")
desc[18]=nuevo_desc
txt=descifrar(txt,desc)
desc=eliminar_desc(desc)

#Buscar r (rr)
nuevo_desc=buscar_rr(txt)
desc[17]=nuevo_desc
txt=descifrar(txt,desc)
desc=eliminar_desc(desc)

#Buscar i (sin)
nuevo_desc=buscar_coincidencias(txt," s?n " )
desc[8]=nuevo_desc
txt=descifrar(txt,desc)
desc=eliminar_desc(desc)

#Buscar u (a su)
nuevo_desc=buscar_coincidencias(txt," a s? " )
desc[20]=nuevo_desc
txt=descifrar(txt,desc)
desc=eliminar_desc(desc)

print(desc)
print(txt)
