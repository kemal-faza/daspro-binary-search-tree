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


# def isOneElmt(P):
#     return not IsTreeEmpty(P) and IsTreeEmpty(Left(P)) and IsTreeEmpty(Right(P))


# def IsUnerLeft(P):
#     return not IsTreeEmpty(Left(P)) and IsTreeEmpty(Right(P))


# def IsUnerRight(P):
#     return IsTreeEmpty(Left(P)) and not IsTreeEmpty(Right(P))


# def IsBiner(P):
#     return not IsTreeEmpty(Left(P)) and not IsTreeEmpty(Right(P))


# def IsExistLeft(P):
#     return not IsTreeEmpty(Left(P))


# def IsExistRight(P):
#     return not IsTreeEmpty(Right(P))


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


# print(BSearchX(MakeBST(MakeBST([], 1, []), 8, MakeBST([], 10, [])), 1))


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


# print(AddX(MakeBST(MakeBST([], 2, []), 5, MakeBST([], 6, [])), 1))


def MakeBinSearchTree(L):
    if IsTreeEmpty(L):
        return []
    else:
        return AddX(MakeBinSearchTree(Tail(L)), FirstElmnt(L))
        # return AddX(MakeBinSearchTree(Head(L)), LastElmnt(L))


print(MakeBinSearchTree([5, 3, 8, 1, 4]))


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


# print(DelBTree(MakeBST(MakeBST([], 2, MakeBST([], 5, [])), 3, MakeBST([], 4, [])), 2))
