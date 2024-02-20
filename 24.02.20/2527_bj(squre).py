for tc in range(4) :
    x1_s, y1_s, x1_e, y1_e, x2_s, y2_s, x2_e, y2_e = map(int, input().split())
    ans = ''

    # 만나지 않을 때, 'd'일 때이다.
    if x1_e < x2_s or x2_e < x1_s or y2_e < y1_s or y1_e < y2_s :
        ans = 'd'

    else :

        # 점만 만날 때, 'c'일 때이다.
        if (x1_s == x2_e and y1_s == y2_e) or (x1_e == x2_s and y1_e == y2_s) or (x1_e == x2_s and y1_s == y2_e) or (x1_s == x2_e and y1_e == y2_s) :
            ans = 'c'

        # 선이 만날 때, 'b'일 때이다.
        elif (y1_s == y2_e and (x1_s < x2_s < x1_e or x1_s < x2_e < x1_e)) or (y1_e == y2_s and (x1_s < x2_s < x1_e or x1_s < x2_e < x1_e)) or (x1_s == x2_e and (y1_s < y2_s < y1_e or y1_s < y2_e < y1_e)) or (x1_e == x2_s and (y1_s < y2_s < y1_e or y1_s < y2_e < y1_e)) :
            ans = 'b'
        # elif (y1_s == y2_e) or (y1_e == y2_s) or (x1_s == x2_e) or (x1_e == x2_s) :
        #     ans = 'b'

        else :
            ans = 'a'

    print(ans)