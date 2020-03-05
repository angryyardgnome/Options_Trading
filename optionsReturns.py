def gayBears(op1, d1, g1, q1, op2, d2, g2, q2, delt):
    # delta is amount option price moves per $1 change in underlying
    # gamma is rate delta changes per $1 move in underlying
    # assumpiton is volatility stays the same which is impossible but also unpredictable\
    # delt is expected drop in underlying
    op1_I = op1*q1
    op2_I = op2*q2
    delta = list(range(1, delt+1))  # Count from 1 - 22 instead of 0 - 21
    for i in delta:
        if i == 1:
            op1 = op1 + d1  # initial 1 dollar change in underlying does not have gamma
            op2 = op2 + d2
        else:
            d1 += g1  # Delta is the speed, gamma is acceleration. as underlying decreases delta speeds up or increase by gamma
            d2 += g2
            op1 = op1 + d1
            op2 = op2 + d2
    op1_E = op1*q1
    op2_E = op2*q2
    print()
    print()
    print('Initial Value Option 1: {0:.2f}'.format(op1_I))
    print('Estimated Value Option 1: {0:.2f}'.format(op1_E))
    print('Initial Value Option 2: {0:.2f}'.format(op2_I))
    print('Estimated Value Option 2: {0:.2f}'.format(op2_E))
    print()
    print()


gayBears(1.66, .0549, .0017, 1, 0.37, 0.0130, 0.0004, 6, 22)
