
def areSimilar(a, b):
    cnt = 0
    if sorted(a) != sorted(b):
        return False

    else:
        for i in range(len(a)):
            if a[i] != b[i]:
                cnt += 1
        return cnt < 3 
         # 다른 것의 개수가 3보다 크면 한번 swap해도 같아질 수 없다 
         