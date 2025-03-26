# You are given a row of N cards, where each card has a certain number of points. Your task is to pick exactly K cards in a way that maximizes your total score. However, there's a restriction:

# You can only pick cards from either the beginning (left) or the end (right) of the row.
# Once a card is picked, it is removed, and you continue picking until you have exactly K cards.

def max_scores(cards,K):
    n=len(cards)
    
    current_sum=sum(cards[:K])
    max_sum=current_sum
    
    for i in range(1,K+1):
        current_sum=current_sum-cards[K-i]+cards[-i]
        max_sum=max(current_sum,max_sum)
    
    return max_sum


N = 6
cards = [1, 2, 3, 4, 5, 45]
K = 3
print(max_scores(cards, K))