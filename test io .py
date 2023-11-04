print("Basic I/O programming")
print("***********************")
n = int(input("Enter the number of processes:"))
print("Number of processes=",n)
a_time = []
b_time = []
for x in range(n):
        print("Enter the Arrival time of processes p{}".format(x+1))
        a = int(input())
        a_time.append(a)
print("The arrival time of processes:",a_time)
for x in range(n):
        print("Enter the burst time of processes p{}".format(x+1))
        a = int(input())
        b_time.append(a)
print("The burst time of processes:",b_time)
print("PNo\t\t AT \t\t BT")
for i in range(n):
    
     print("p{}".format(i+1),"\t\t",a_time[i],"\t\t",b_time[i])
