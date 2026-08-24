dsfsfddkj
dkıjlkjhkjgfd
glkdjlkgjhldgbdsg
dflkgjdflgfd
g
dfgdfgdfg
kjrgkfgddg
sdfgskjfgdjk
gddgdfg
dfgdsfgdfg
kjhdfbkjlsgsdf
dfkbjfgk
fddkjgbjdhg
afdsgksdfjhgkjdhfgda
fgdfgadfg
slkgjfklasjd
fdljghkjsdfgsa
dfgfljdghkdjgnadf
güadlfkjgnhdkajfgdaf
gadşlfghdkjfgdfg
dfgkjdfgkdfgd
afgdafjgdjfhgdfg
kfdbhkjfsd
dkhjkdjgd
fgdskfhgjdsfhgdf
gdkfhgjkdsfgdfg,dsfgdsf
gsdfgdfg
dsfgdsf
gdsfgdsfgdfg
dfgdsfgdfgdf
kdsljfnvkjdf
dfkjndsfkj
fldsfnvkdsjfnvds
fvdfkjvdfv
sdfkjsdfs
dfskdjfkjsdf
sdfksjdfsdf
vklfgjkgd
vsdflşvksdmfşkldsf
ldsfjkvdksfv
dfjdkfjgdkf
dfgldksfbkjfdgvsdfasdsad
sadadsadasd
kljvkljdsfv
dsfgobjdsfklgsdf
gsdfkjgdskfg
dsfgkdsfjgdsfg
ofıjslakfd
sgrfbvlsdknfaf
svadlnfklbndaşsvafdsvbldfs
dvdljfnkasdjf
asfdlgajsndfasdv


def bubble_sort(items):
    """Sort a list in ascending order using bubble sort. Returns a new list."""
    result = list(items)
    n = len(result)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result
