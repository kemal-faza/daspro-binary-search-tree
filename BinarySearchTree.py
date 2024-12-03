from list_24060124120013 import *


def MakeBST(L, A, R):
    return [L, A, R]


def Akar(P):
    return P[1]


def Left(P):
    return P[0]


def Right(P):
    return P[2]


def IsTreeEmpty(P):
    return P == []


# BSearchX : BinSearchTree, elemen --> boolean
# BSearchX(P, X) mengirimkan true jika ada node dari BinSearchTree P bernilai X, mengirimkan false jika tidak ada
def BSearchX(P, X):
    if IsTreeEmpty(P):
        return False
    elif Akar(P) == X:
        return True
    else:
        if X < Akar(P):
            return BSearchX(Left(P), X)
        else:
            return BSearchX(Right(P), X)


print(
    f"BSearchX(P, X) => {BSearchX(MakeBST(MakeBST([], 1, []), 8, MakeBST([], 10, [])), 1)}"
)


# AddX : BinSearchTree, elemen --> PohonBiner
# Add(P, X) menghasilkan sebuah BinSearchTree P dengan tambahan simpul X. Belum ada simpul P yang bernilai X
def AddX(P, X):
    if IsTreeEmpty(P):
        return MakeBST([], X, [])
    elif Akar(P) == X:
        return P
    else:
        if X < Akar(P):
            return MakeBST(AddX(Left(P), X), Akar(P), Right(P))
        else:
            return MakeBST(Left(P), Akar(P), AddX(Right(P), X))


print(f"AddX(P, X) => {AddX(MakeBST(MakeBST([], 2, []), 5, MakeBST([], 6, [])), 1)}")


# MakeBinSearchTree : list of elemen --> PohonBiner
# MakeBinSearchTree(L) menghasilkan sebuah BinSearchTree P yang elemennya berasal dari elemen list L yang dijamin unik
def MakeBinSearchTree(L):
    if IsTreeEmpty(L):
        return []
    else:
        return AddX(MakeBinSearchTree(Tail(L)), FirstElmnt(L))


print(f"MakeBinSearchTree(L) => {MakeBinSearchTree([5, 3, 8, 1, 4])}")


# DelBTree : BinSearchTree tidak kosong, elemen --> PohonBiner
# DelBTree(P, X) menghasilkansebuah BinSearchTree P tanpa node yang bernilai X. X pasti ada sebagai salah satu node BinSearchTree. Menghasilkan BinSearchTree yang "kosong" jika P hanya terdiri dari X
def DelBTree(P, X):
    if IsTreeEmpty(P):
        return P
    elif Akar(P) == X:
        return []
    else:
        if X < Akar(P):
            return MakeBST(DelBTree(Left(P), X), Akar(P), Right(P))
        else:
            return MakeBST(Left(P), Akar(P), DelBTree(Right(P), X))


print(
    f"DelBTree(P, X) => {DelBTree(MakeBST(MakeBST([], 2, MakeBST([], 5, [])), 3, MakeBST([], 4, [])), 2)}"
)
