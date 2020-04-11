# 2015100902 김현균
# Algorithm for merge sort the list

def merge(h, m, Ulist, Vlist, Slist):
    i, j ,k = 0, 0, 0
    while i < h and j < m:      # 각 요소의 값을 비교하여 Slist에 추가 
        if Ulist[i] < Vlist[j]:
            Slist[k] = Ulist[i]
            i += 1
        else:
            Slist[k] = Vlist[j]
            j += 1
        k += 1

    if i >= h:                  # 한 리스트가 정리되면 정리되지 않은 리스트의 값을 전부 Slist로 이동
        while k < len(Slist):
            Slist[k] = Vlist[j]
            k += 1 
            j += 1
    else:
        while k < len(Slist):
            Slist[k] = Ulist[i]
            k += 1
            i += 1

    print('\nMerge\nSlist = {}'.format(Slist))      # Merge된 결과 출력

    return Slist


def mergesort(n, Slist):
    if n>1:
        h = n//2                # 왼쪽으로 분할될 개수
        m = n - h               # 오른쪽으로 분할될 개수

        Ulist = Slist[:h]       # 입력받은 Slist를 Slicing하여 Ulist에 할당
        Vlist = Slist[m:]       # 입력받은 Slist를 Slicing하여 Vlist에 할당

        print('\nDevide\nUlist : {}\nVlist : {}'.format(Ulist, Vlist))      # 분할된 결과 list 출력

        Ulist = mergesort(h, Ulist)
        Vlist = mergesort(m, Vlist)
        return merge(h, m, Ulist, Vlist, Slist)
    return Slist

import random                                       # 난수생성 라이브러리
InputList = [random.randint(0, 50) for _ in range(8)]
print('Input List : ', InputList)                   # sort될 list 출력

SortedList = mergesort(len(InputList), InputList)
print('Result : ', SortedList)                      # 최종 결과 list 출력