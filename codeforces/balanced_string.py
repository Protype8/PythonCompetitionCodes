# Python3 program to find number of
# balanced parentheses sub strings

# Function to find number of
# balanced parentheses sub strings
def Balanced_Substring(s, n):
    # To store required answer
    ans = 0;

    # Vector to stores the number of
    # balanced brackets at each depth.
    arr = [0] * (int(n / 2) + 1);

    # d stores checks the depth of our sequence
    # For example level of () is 1
    # and that of (()) is 2.
    d = 0;
    for i in range(n):

        # If open bracket
        # increase depth
        if (s[i] == '('):
            d += 1;

        # If closing bracket
        else:
            if (d == 1):
                j = 2
                while (j <= n // 2 + 1 and arr[j] != 0):
                    arr[j] = 0
            ans += 1;
            ans += arr[d];
            arr[d] += 1;
            d -= 1;

    # Return the required answer
    return ans;


# Driver code
s = "()()()()()(";
n = len(s);

# Function call
print(Balanced_Substring(s, n));