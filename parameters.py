import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Solve the Rental Car MDP.")
    
    parser.add_argument('--gamma', type=float, default=0.9, help='Discount factor')
    parser.add_argument('--move_cost', type=int, default=60, help='Cost to move one car')
    parser.add_argument('--rent_same', type=int, default=50, help='Revenue for same-city rental')
    parser.add_argument('--rent_other', type=int, default=45, help='Revenue for one-way rental')
    parser.add_argument('--theta', type=float, default=0.1, help='Convergence threshold')

    return parser.parse_args()