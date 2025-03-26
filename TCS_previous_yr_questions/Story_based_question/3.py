# Q3. At a fun fair, a street vendor is selling different colours of balloons. He sells N number of
# different colours of balloons (B[]). The task is to find the colour (odd) of the balloon which is
# present odd number of times in the bunch of balloons.
# Note: If there is more than one colour which is odd in number, then the first colour in the
# array which is present odd number of times is displayed. The colours of the balloons can all
# be either upper case or lower case in the array. If all the inputs are even in number, display
# the message “All are even”.
# Example 1: 7 -> Value of N [r,g,b,b,g,y,y] -> B[] Elements B[0] to B[N-1], where each input
# element is sepārated by ṉew line.
# Output : r -> [r,g,b,b,g,y,y] -> “r” colour balloon is present odd number of times in the bunch.
# Explanation:
# From the input array above: r: 1 balloon g: 2 balloons b: 2 balloons y : 2 balloons Hence , r is
# only the balloon which is odd in number.




#Method-1
# from collections import Counter


# def find_odd_balloon(balloons):
#     count_map=Counter(balloons)
    
#     for color in balloons:
#         if count_map[color]%2!=0:
#             return color
    
#     return "All are even"


# balloons = ['r', 'r', 'b', 'b', 'g', 'y', 'y']
# print(find_odd_balloon(balloons))  # Output: r


def find_odd_balloon(balloons):
    
    counter_map={}
    
    for color in balloons:
        if color in counter_map:
            counter_map[color]+=1
        else:
            counter_map[color]=1
    
    # Step 2: Find the first odd-occurrence balloon
    for color in balloons:
        if counter_map[color] % 2 != 0:
            return color  # Return first odd occurring balloon
    
    return "All are even"  # If no odd occurr
    

balloons = ['r', 'g', 'b', 'b', 'g', 'y', 'y']
print(find_odd_balloon(balloons))  # Output: r
            
        