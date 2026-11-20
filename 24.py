import math

# 1-la irundhu 20 varaikkum irukkira numbers-oda LCM-a kandupudikka
ans = 1
for i in range(1, 21):
    # LCM formula: (a * b) / GCD(a, b)
    ans = (ans * i) // math.gcd(ans, i)

print("Smallest number divisible by 1 to 20:", ans)