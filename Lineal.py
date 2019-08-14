import numpy as np
def gaussjordan1(a,b):
    n=len(b)
    c=np.concatenate([a,b],axis=1)
    for e in range(n):
        t=c[e,e]
        for j in range(e,n+1):
            c[e,j]=c[e,j]/t
        for i in range(n):
            if i!=e:
                t=c[i,e]
                for j in range(e,n+1):
                    c[i,j]=c[i,j]-t*c[e,j]
                    print (c)
    x=c[:,n]
    return x

def gaussjordan2(a,b):
    n=len(b)
    c=np.concatenate([a,b],axis=1)
    for e in range(n):
        c[e,e:]=c[e,e:]/c[e,e]
        for i in range(n):
            if i!=e:
                c[i,e:]=c[i,e:]-c[i,e]*c[e,e:]
    x=c[:,n]
    return x

#Funcion inversa

def inversa (a,b):
    n=len(b)
    c=np.concatenate([a,b],axis=1)
    for e in range(n):
        t=c[e,e]
        for j in range(e,n+1):
            c[e,j]=c[e,j]/t
        for i in range (n):
            if i!=e:
                t=c[i,e]
                for j in range (e,n+1):
                    c[i,j]=c[i,j]-t*c[e,j]
    x=c[:,n]
    return x

def jacobi(a,b,x):
    n=len(x)
    t=x.copy()
    for i in range(n):
        s=0
        for j in range(n):
            if i!=j:
                s=s+a[i,j]*t[j]
                x[i]=(b[i]-s)/a[i,i]
    return x

def jacobim(a,b,x,e,m):
    n=len(x)
    t=x.copy()
    for k in range(m):
        x=jacobi(a,b,x)
        d=np.linalg.norm(array(x)-array(t),inf)
        if d<e:
            return[x,k]
        else:
            t=x.copy()
            return[[],m]

def gausseidel(a,b,x):
    n=len(x)
    for i in range(n):
        s=0
        for j in range(n):
            if i!=j:
                s=s+a[i,j]*x[j]
        x[i]=(b[i]-s)/a[i,i]

    return x
