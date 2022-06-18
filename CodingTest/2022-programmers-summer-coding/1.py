def solution(atmos):
    day_count = 0
    onmask = 0

    for atmo in atmos:
        if atmo[0] >= 151 and atmo[1] >= 76:
            if day_count == 0:
                onmask += 1
            else: day_count = 0
        elif atmo[0] >= 81 or atmo[1] >= 36:
            if day_count == 0:
                day_count += 1
                onmask += 1
            elif day_count < 3:
                day_count += 1
            else:
                day_count = 0
        else:
            if day_count != 0: day_count += 1
        if day_count > 2: day_count = 0
        
    return onmask
