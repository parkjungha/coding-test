def solution(files):
    info = []
    
    for file in files:       
        head, number, tail = '', '', ''
        for i in range(len(file)):
            if file[i].isdigit(): # 처음 나오는 숫자를 기준으로 앞은 head, 뒤는 number+tail
                head = file[:i]
                number = file[i:]
                
                for j in range(len(number)): # 연속된 숫자가 끝날때 앞은 number, 뒤는 tail
                    if not number[j].isdigit():
                        tail = number[j:]
                        number = number[:j]
                        break
                        
                info.append([head, number, tail])
                head, number, tail = '', '', ''
                break

    # 1.head기준, 2. number기준 정렬, 둘다 같으면 원래 순서 유지
    info = sorted(info, key=lambda x:(x[0].lower(), int(x[1])))

    return [''.join(i) for i in info]
