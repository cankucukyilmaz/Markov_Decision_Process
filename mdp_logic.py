f1 = [0.00, 0.09, 0.09, 0.09, 0.09, 0.09, 0.09, 0.09, 0.09, 0.09, 0.09, 0.10]
f2 = [0.00, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.45]
g1 = [0.00, 0.01, 0.04, 0.07, 0.10, 0.13, 0.30, 0.13, 0.10, 0.07, 0.04, 0.01]
g2 = [0.00, 0.20, 0.60, 0.20, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]

def calculate_action_value(state, action, V, args):
    """
    Calculates value using parameters from 'args' object (args.gamma, args.move_cost, etc.)
    """
    cost = abs(action) * args.move_cost
    
    avail_1 = state - max(0, action)
    avail_2 = (20 - state) - max(0, -action)

    total_expected_return = -cost

    for d1_same in range(1, 12):
        for d1_other in range(1, 12):
            for d2_same in range(1, 12):
                for d2_other in range(1, 12):

                    prob = f1[d1_same] * g1[d1_other] * f2[d2_same] * g2[d2_other]
                    
                    if prob == 0:
                        continue

                    real_rent_1_same = min(d1_same, avail_1)
                    avail_for_oneway_1 = avail_1 - real_rent_1_same
                    real_rent_1_other = min(d1_other, avail_for_oneway_1)

                    real_rent_2_same = min(d2_same, avail_2)
                    avail_for_oneway_2 = avail_2 - real_rent_2_same
                    real_rent_2_other = min(d2_other, avail_for_oneway_2)

                    revenue = args.rent_same * (real_rent_1_same + real_rent_2_same) + \
                              args.rent_other * (real_rent_1_other + real_rent_2_other)

                    cars_staying_in_1 = avail_1 - real_rent_1_other
                    cars_coming_from_2_rentals = real_rent_2_other
                    cars_coming_from_2_moves = max(0, -action)
                    
                    s_prime = cars_staying_in_1 + cars_coming_from_2_rentals + cars_coming_from_2_moves

                    if s_prime > 20:
                        s_prime = 20
                        
                    if s_prime < 0:
                        s_prime = 0

                    total_expected_return += prob * (revenue + args.gamma * V[int(s_prime)])
    
    return total_expected_return