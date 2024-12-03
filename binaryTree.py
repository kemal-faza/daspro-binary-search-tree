from list_24060124120013 import *

# DEFINISI TYPE
# Type PohonBiner: <A: integer, L: PohonBiner, R: PohonBiner>
# Pohon Biner terdiri dari akar yang berupa elemen,
# L dan R adalah Pohon Biner yang merupakan sub pohon kiri dan sub pohon kanan


# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakePB: integer, 2 PohonBiner --> PohonBiner
# MakePB(A, L, R) membuat Pohon Biner yang terdiri dari akar yang berupa elemen,
# L dan R adalah Pohon Biner yang merupakan sub pohon kiri dan sub pohon kanan
# REALISASI


def MakePB(A, L, R):
    return [A, L, R]


# DEFINISI DAN SPESIFIKASI SELEKTOR
# Akar: PohonBiner --> integer
# Akar(P) mengembalikan akar dari sebuah PohonBiner
# REALISASI
def Akar(P):
    return P[0]


# Left: PohonBiner --> PohonBiner
# Left(P) mengembalikan subpohon kiri dari sebuah PohonBiner
# REALISASI
def Left(P):
    return P[1]


# Right: PohonBiner --> PohonBiner
# Right(P) mengembalikan subpohon kanan dari sebuah PohonBiner
# REALISASI
def Right(P):
    return P[2]


# IsTreeEmpty: PohonBiner --> boolean
# IsTreeEmpty(P) mengembalikan True jika P adalah pohon biner kosong
def IsTreeEmpty(P):
    return P == []


# isOneElmt: PohonBiner --> boolean
# isOneElmt(P) mengembalikan True jika P adalah pohon biner dengan satu elemen
def isOneElmt(P):
    return not IsTreeEmpty(P) and IsTreeEmpty(Left(P)) and IsTreeEmpty(Right(P))


# IsUnerLeft: PohonBiner --> boolean
# IsUnerLeft(P) mengembalikan True jika P adalah pohon biner dengan anak kiri
def IsUnerLeft(P):
    return not IsTreeEmpty(Left(P)) and IsTreeEmpty(Right(P))


# IsUnerRight: PohonBiner --> boolean
# IsUnerRight(P) mengembalikan True jika P adalah pohon biner dengan anak kanan
def IsUnerRight(P):
    return IsTreeEmpty(Left(P)) and not IsTreeEmpty(Right(P))


# IsBiner: PohonBiner --> boolean
# IsBiner(P) mengembalikan True jika P adalah pohon biner dengan anak kiri dan kanan
def IsBiner(P):
    return not IsTreeEmpty(Left(P)) and not IsTreeEmpty(Right(P))


# IsExistLeft: PohonBiner --> boolean
# IsExistLeft(P) mengembalikan True jika P memiliki anak kiri
def IsExistLeft(P):
    return not IsTreeEmpty(Left(P))


# IsExistRight: PohonBiner --> boolean
# IsExistRight(P) mengembalikan True jika P memiliki anak kanan
def IsExistRight(P):
    return not IsTreeEmpty(Right(P))


# NbElmt: PohonBiner --> integer
# NbElmt(P) mengembalikan jumlah elemen dalam P
def NbElmt(P):
    if IsTreeEmpty(P):
        return 0
    else:
        return NbElmt(Left(P)) + 1 + NbElmt(Right(P))


# NbElmt1: PohonBiner --> integer
# NbElmt1(P) mengembalikan jumlah elemen dalam P dengan rekursif
def NbElmt1(P):
    if isOneElmt(P):
        return 1
    elif IsBiner(P):
        return NbElmt1(Left(P)) + 1 + NbElmt1(Right(P))
    elif IsUnerLeft(P):
        return NbElmt1(Left(P)) + 1
    elif IsUnerRight(P):
        return 1 + NbElmt1(Right(P))


# NbDaun: PohonBiner --> integer
# NbDaun(P) mengembalikan jumlah daun dalam P

# NbDaun1: PohonBiner --> integer
# NbDaun1(P) mengembalikan jumlah daun dalam P dengan rekursif

# IsMember: PohonBiner, elemen --> boolean
# IsMember(P, X) mengembalikan True jika X adalah elemen dalam P, False otherwise

# IsSkewLeft: PohonBiner --> boolean
# IsSkewLeft(P) mengembalikan True jika P adalah pohon skew kiri, False otherwise

# IsSkewRight: PohonBiner --> boolean
# IsSkewRight(P) mengembalikan True jika P adalah pohon skew kanan, False otherwise

# max2: integer, integer --> integer
# max2(a, b) mengembalikan nilai maksimum antara a dan b

# Level: PohonBiner, elemen, integer --> integer
# Level(P, X, lvl) mengembalikan level dari elemen X dalam P

# LevelOfX: PohonBiner, elemen --> integer
# LevelOfX(P, X) mengembalikan level dari elemen X dalam P

# AddDaunTerkiri: PohonBiner, elemen --> PohonBiner
# AddDaunTerkiri(P, X) menambahkan elemen X sebagai daun terakhir dalam P

# AddDaun: PohonBiner, elemen, elemen, boolean --> PohonBiner
# AddDaun(P, X, Y, Kiri) menambahkan elemen Y sebagai anak kiri atau kanan dari elemen X dalam P

# DelDaunTerkiri: PohonBiner --> PohonBiner
# DelDaunTerkiri(P) menghapus daun terakhir dalam P

# DelDaun: PohonBiner, elemen --> PohonBiner
# DelDaun(P, X) menghapus elemen X dalam P

# MakeListDaun: PohonBiner --> list
# MakeListDaun(P) mengembalikan list daun dalam P

# MakeListPreOrder: PohonBiner --> list
# MakeListPreOrder(P) mengembalikan list elemen dalam P dengan traversal pre-order

# MakeListPostOrder: PohonBiner --> list
# MakeListPostOrder(P) mengembalikan list elemen dalam P dengan traversal post-order

# MakeListInOrder: PohonBiner --> list
# MakeListInOrder(P) mengembalikan list elemen dalam P dengan traversal in-order

# MakeListLevel: PohonBiner, integer --> list
# MakeListLevel(P, N) mengembalikan list elemen dalam P pada level N

# Left: PohonBiner --> PohonBiner
# Left(P) mengembalikan subpohon kiri dari P

# Right: PohonBiner --> PohonBiner
# Right(P) mengembalikan subpohon kanan dari P

# Akar: PohonBiner --> elemen
# Akar(P) mengembalikan elemen akar dari P

# MakePB: elemen, PohonB ```python
# MakePB(X, L, R) mengembalikan pohon biner baru dengan elemen X sebagai akar, L sebagai subpohon kiri, dan R sebagai subpohon kanan


def NbDaun(P):
    if IsTreeEmpty(P):
        return 0
    else:
        return NbDaun1(P)


def NbDaun1(P):
    if isOneElmt(P):
        return 1
    elif IsBiner(P):
        return NbDaun1(Left(P)) + NbDaun1(Right(P))
    elif IsUnerLeft(P):
        return NbDaun1(Left(P))
    elif IsUnerRight(P):
        return NbDaun1(Right(P))


def IsMember(P, X):
    if isOneElmt(P):
        return Akar(P) == X
    elif Akar(P) == X:
        return True
    elif IsBiner(P):
        return IsMember(Left(P), X) or IsMember(Right(P), X)
    elif IsUnerLeft(P):
        return IsMember(Left(P), X)
    elif IsUnerRight(P):
        return IsMember(Right(P), X)


def IsSkewLeft(P):
    if isOneElmt(P):
        return True
    else:
        return IsUnerLeft(P)


def IsSkewRight(P):
    if isOneElmt(P):
        return True
    else:
        return IsUnerRight(P)


def max2(a, b):
    return a if a > b else b


def Level(P, X, lvl):
    if IsTreeEmpty(P):
        return 0
    elif Akar(P) == X:
        return lvl
    else:
        return max2(Level(Left(P), X, lvl + 1), Level(Right(P), X, lvl + 1))


def LevelOfX(P, X):
    if IsTreeEmpty(P):
        return 0
    elif Akar(P) == X:
        return 0
    else:
        return Level(P, X, 0)


def AddDaunTerkiri(P, X):
    if IsTreeEmpty(P):
        return MakePB(X, [], [])
    elif IsUnerRight(P):
        return MakePB(Akar(P), Left(P), AddDaunTerkiri(Right(P), X))
    else:
        return MakePB(Akar(P), AddDaunTerkiri(Left(P), X), Right(P))


def AddDaun(P, X, Y, Kiri):
    if IsTreeEmpty(P):
        return P
    elif Akar(P) == X:
        if Kiri:
            return MakePB(X, MakePB(Y, [], []), Right(P))
        else:
            return MakePB(X, Left(P), MakePB(Y, [], []))
    else:
        return MakePB(
            Akar(P), AddDaun(Left(P), X, Y, Kiri), AddDaun(Right(P), X, Y, Kiri)
        )


def DelDaunTerkiri(P):
    if isOneElmt(P):
        return []
    elif IsUnerRight(P):
        return MakePB(Akar(P), Left(P), DelDaunTerkiri(Right(P)))
    else:
        return MakePB(Akar(P), DelDaunTerkiri(Left(P)), Right(P))


def DelDaun(P, X):
    if IsTreeEmpty(P):
        return P
    elif Akar(P) == X:
        return []
    else:
        return MakePB(Akar(P), DelDaun(Left(P), X), DelDaun(Right(P), X))


def MakeListDaun(P):
    if IsTreeEmpty(P):
        return []
    elif isOneElmt(P):
        return [Akar(P)]
    else:
        return MakeListDaun(Left(P)) + MakeListDaun(Right(P))


def MakeListPreOrder(P):
    if IsTreeEmpty(P):
        return []
    else:
        return [Akar(P)] + MakeListPreOrder(Left(P)) + MakeListPreOrder(Right(P))


def MakeListPostOrder(P):
    if IsTreeEmpty(P):
        return []
    else:
        return MakeListPostOrder(Left(P)) + MakeListPostOrder(Right(P)) + [Akar(P)]


def MakeListInOrder(P):
    if IsTreeEmpty(P):
        return []
    else:
        return MakeListInOrder(Left(P)) + [Akar(P)] + MakeListInOrder(Right(P))


def MakeListLevel(P, N):
    if IsTreeEmpty(P):
        return []
    elif N == 0:
        return [Akar(P)]
    else:
        return MakeListLevel(Left(P), N - 1) + MakeListLevel(Right(P), N - 1)


# APLIKASI
print(
    f"NbElmt(P) => {NbElmt(MakePB(0, MakePB(1, MakePB(3, [], []), MakePB(4, [], [])), MakePB(2, MakePB(5, [], []), MakePB(6, [], []))))}"
)
print(
    f"NbElmt1(P) => {NbElmt1(MakePB(0, MakePB(1, MakePB(3, [], []), MakePB(4, [], [])), MakePB(2, MakePB(5, [], []), MakePB(6, [], []))))}"
)
print(
    f"NbDaun(P) => {NbDaun(MakePB(0, MakePB(1, MakePB(3, [], []), MakePB(4, [], [])), MakePB(2, MakePB(5, [], []), MakePB(6, [], []))))}"
)
print(
    f"NbDaun1(P) => {NbDaun1(MakePB(0, MakePB(1, MakePB(3, [], []), MakePB(4, [], [])), MakePB(2, MakePB(5, [], []), MakePB(6, [], []))))}"
)
print(
    f"IsMember(P, 5) => {IsMember(MakePB(0, MakePB(1, MakePB(3, [], []), MakePB(4, [], [])), MakePB(2, MakePB(5, [], []), MakePB(6, [], []))), 5)}"
)
print(
    f"IsSkewLeft(P) => {IsSkewLeft(MakePB(0, MakePB(1, MakePB(3, [], []), MakePB(4, [], [])), MakePB(2, MakePB(5, [], []), MakePB(6, [], []))))}"
)
print(
    f"IsSkewRight(P) => {IsSkewRight(MakePB(0, MakePB(1, MakePB(3, [], []), MakePB(4, [], [])), MakePB(2, MakePB(5, [], []), MakePB(6, [], []))))}"
)
print(
    f"LevelOfX(P, 5) => {LevelOfX(MakePB(0, MakePB(1, MakePB(3, [], []), MakePB(4, [], [])), MakePB(2, MakePB(5, [], []), MakePB(6, [], []))), 5)}"
)
print(
    f"AddDaunTerkiri(P, 7) => {AddDaunTerkiri(MakePB(0, MakePB(1, MakePB(3, [], []), MakePB(4, [], [])), MakePB(2, MakePB(5, [], []), MakePB(6, [], []))), 7)}"
)
print(
    f"AddDaun(P, 7, 5, True) => {AddDaun(MakePB(0, MakePB(1, MakePB(3, [], []), MakePB(4, [], [])), MakePB(2, MakePB(5, [], []), MakePB(6, [], []))), 7, 5, True)}"
)
print(
    f"DelDaunTerkiri(P) => {DelDaunTerkiri(MakePB(0, MakePB(1, MakePB(3, [], []), MakePB(4, [], [])), MakePB(2, MakePB(5, [], []), MakePB(6, [], []))))}"
)
print(
    f"DelDaun(P, 5) => {DelDaun(MakePB(0, MakePB(1, MakePB(3, [], []), MakePB(4, [], [])), MakePB(2, MakePB(5, [], []), MakePB(6, [], []))), 5)}"
)
print(
    f"MakeListDaun(P) => {MakeListDaun(MakePB(0, MakePB(1, MakePB(3, [], []), MakePB(4, [], [])), MakePB(2, MakePB(5, [], []), MakePB(6, [], []))))}"
)
print(
    f"MakeListPreOrder(P) => {MakeListPreOrder(MakePB(0, MakePB(1, MakePB(3, [], []), MakePB(4, [], [])), MakePB(2, MakePB(5, [], []), MakePB(6, [], []))))}"
)
print(
    f"MakeListPostOrder(P) => {MakeListPostOrder(MakePB(0, MakePB(1, MakePB(3, [], []), MakePB(4, [], [])), MakePB(2, MakePB(5, [], []), MakePB(6, [], []))))}"
)
print(
    f"MakeListInOrder(P) => {MakeListInOrder(MakePB(0, MakePB(1, MakePB(3, [], []), MakePB(4, [], [])), MakePB(2, MakePB(5, [], []), MakePB(6, [], []))))}"
)
print(
    f"MakeListLevel(P) => {MakeListLevel(MakePB(0, MakePB(1, MakePB(3, [], []), MakePB(4, [], [])), MakePB(2, MakePB(5, [], []), MakePB(6, [], []))), 1)}"
)
