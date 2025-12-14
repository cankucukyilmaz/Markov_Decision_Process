from parameters import get_args
from mdp_logic import calculate_action_value

def main():
    args = get_args()
    
    print(f"\n--- Running Two-City Car Rental Optimization ---")
    print(f"Gamma:      {args.gamma}")
    print(f"Move Cost:  €{args.move_cost}")
    print(f"Revenues:   Same = €{args.rent_same}, OneWay = €{args.rent_other}")
    print(f"Stop when:  Delta < {args.theta}")
    print("------------------------------------------------")

    V = [0.0] * 21
    policy = [0] * 21
    iteration = 0

    print("Starting Value Iteration...")
    
    while True:
        iteration += 1
        delta = 0
        
        for s in range(21):
            old_v = V[s]
            best_val = -float('inf')
            best_action = 0
            
            min_action = -(20 - s)
            max_action = s
            
            for a in range(min_action, max_action + 1):
                val = calculate_action_value(s, a, V, args)
                
                if val > best_val:
                    best_val = val
                    best_action = a
            
            V[s] = best_val
            policy[s] = best_action
            
            diff = abs(old_v - V[s])
            if diff > delta:
                delta = diff
        
        print(f"Iteration {iteration}: Max change = {delta:.4f}")
        
        if delta < args.theta:
            print("\nConvergence achieved!")
            break

    print("\nOptimal Policy (Cars to move from City 1 -> City 2):")
    print("-" * 50)
    print(f"{'State (Cars in C1)':<20} | {'Action':<10}")
    print("-" * 50)
    for s in range(21):
        action_str = f"Move {policy[s]}"
        print(f"{s:<20} | {action_str:<10}")

if __name__ == "__main__":
    main()