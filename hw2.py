from scipy import stats

def calculate_power(lst): #sum of x^2/y^2
    sum = 0
    for num in lst:
        sum += num*num
    return sum

def calculate_sum(lst): #sum of x/y
    sum = 0
    for num in lst:
        sum += num
    return sum

def calculate_mul(lst1,lst2): #sum of x*y
    sum = 0
    for i in range (len(lst1)):
        sum += lst1[i]*lst2[i]
    return sum

def calculate_sxx_syy(n,lst,avarage):
    sum = 0
    for i in range(n):
        sum += pow(lst[i]-avarage,2)
    return sum

def calculate_sse(sxx,syy,b1):
    return syy-(pow(b1,2)*sxx)

def calculate_t_stat(n, alpha):
    return stats.t.ppf(1-(alpha/2),n-2)

def calculate_Confidence_Interval(b,t_stat,Sb):
    left = b - (t_stat * Sb)
    right = b + (t_stat * Sb)
    return left, right


def calculate_t_star(b, Sb):
    return abs(b/Sb)

def reject_or_accept(t_star_forB, t_stat):
    if t_star_forB <= t_stat :
        print("t* <= t_stat")
        print(str(t_star_forB)+" <= "+str(t_stat)
              + "\nwe accept the H0")
    else:
        print("t* > t_stat")
        print(str(t_star_forB)+" > "+str(t_stat) + "\nwe reject the H0")
    return

def calculate_pvalue(t_stat, df):
    return stats.t.sf(t_stat, df)*2


lstx = [40, 20, 25, 20, 30, 50, 40, 20, 50, 40, 25, 50]
lsty = [385, 400, 395, 365, 475, 440, 490, 420, 560, 525, 480, 510]

print("#################################")
xPower = calculate_power(lstx)
print ("segma x^2: "+ str(xPower))

yPower = calculate_power(lsty)
print ("segma y^2: "+str(yPower))

x = calculate_sum(lstx)
print ("segma x: "+str(x))

y = calculate_sum(lsty)
print ("segma y: "+str(y))

mulXY = calculate_mul(lstx, lsty)
print ("segma x*y: "+str(mulXY))

avarage_x = calculate_sum(lstx)/len(lstx)
print ("avarage x: "+str(avarage_x))

avarage_y = calculate_sum(lsty)/len(lsty)
print("avarage y: "+str(avarage_y))
print("#################################")
n = len(lstx)
b1 = ((n*mulXY)-(x*y))/((n*xPower)-(x*x))
print ("b1: "+ str(b1))

b0 = avarage_y-(b1*avarage_x)
print ("b0: "+ str(b0))
print("#################################")
syy = calculate_sxx_syy(n, lsty, avarage_y)
print ("Syy: "+str(syy))

sxx = calculate_sxx_syy(n, lstx, avarage_x)
print ("Sxx: "+str(sxx))
print("#################################")
sse = calculate_sse(sxx, syy, b1)
print ("SSE: "+str(sse))

mse = sse/(n-2)
print ("MSE: "+str(mse))
print("#################################")
Sb1 = pow(mse/sxx, 0.5)
print ("S(b1): "+str(Sb1))

Sb0 = pow((xPower/(n*sxx))*mse, 0.5)
print ("S(b0): "+str(Sb0))
print("#################################")

t_stat = calculate_t_stat(n, 0.05)
print("t_stat: "+str(t_stat))

print("#################################")
leftB1, rightB1 = calculate_Confidence_Interval(b1, t_stat, Sb1)
print("P( " + str(leftB1) + " <= B1 <= " + str(rightB1) + " ) = 0.95")

leftB0, rightB0 = calculate_Confidence_Interval(b0, t_stat, Sb0)
print("P( " + str(leftB0) + " <= B0 <= " + str(rightB0) + " ) = 0.95")
print("#################################")
print("Hypothesis test for B1 :\nH0: B1=0\nH1: B1!=0")
t_star_forB1 = calculate_t_star(b1,Sb1)
print("t*_B1 == " + str(t_star_forB1)+"\n")
reject_or_accept(t_star_forB1,t_stat)
p_value_B1 = calculate_pvalue(t_star_forB1, n-2)
print("p-value is : " + str(p_value_B1))
print("#################################")
print("Hypothesis test for B0 :\nH0: B0=0\nH1: B0!=0")
t_star_forB0 = calculate_t_star(b0, Sb0)
print("t*_B0 == " + str(t_star_forB0)+"\n")
reject_or_accept(t_star_forB0, t_stat)
p_value_B0 = calculate_pvalue(t_star_forB0, n-2)
print("p-value is : " + str(p_value_B0))