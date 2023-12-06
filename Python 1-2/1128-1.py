def printStep(arr, val) :
    print("  Step %2d = " % val, end='')
    print(arr)

def insertion_sort(A) :
    n = len(A)
    for i in range(1, n) : # 1부터 시작하는 이유는 key 값을 1번째 값부터 시작 하기 때문
        key = A[i]
        j = i-1
        while j>=0 and A[j] > key :
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
        printStep(A, i)

def bubble_sort(A) :
    n = len(A)
    for i in range(n-1, 0, -1) :
        bChanged = False
        for j in range (i) :
            if (A[j]>A[j+1]) :
                A[j], A[j+1] = A[j+1], A[j] 
                bChanged = True

        if not bChanged: break;			# 교환이 없으면 종료
        printStep(A, n - i);			# 중간 과정 출력용 문장


if __name__ == "__main__":
    org = [ 8,3,4,9,7]
    data = list(org)
    print(" Original =",data)
    bubble_sort(data)
    print("Selection =",data)

    # print(" Original =",data)
    # insertion_sort(data)
    # print("Selection =",data)
