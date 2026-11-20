num=int(input())
for i in range(1,num+1):
    for j in range(i):
        print(i,end=" ")
    print("")




def print_pattern(n, current=1):
    # Base condition: current value 'n'-a vida periyasaana stop panirum
    if current > n:
        return
    
    # Antha line-ah print panrom
    print((str(current) + " ") * current)
    
    # Adutha number-ku function-a thirumba call panrom
    print_pattern(n, current + 1)

# Input vaangi function-a call panrom
num = int(input())
print_pattern(num)