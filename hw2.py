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
def calculate_Sxy(b1,Sxx):
    return b1*Sxx

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

def calculate_r(b1,Syy,Sxx):
    up = b1 * pow(Sxx,0.5)
    down = pow(Syy,0.5)
    return up/down

def calculate_SSR(b1,Sxx):
    return pow(b1,2)*Sxx

def calculate_MSR(SSR,df):
    return SSR/df

def calculate_SSTO(SSR, SSE):
    return SSR + SSE

def calculate_F_stat(MSR,MSE):
    return MSR/MSE
#Q1
# lstx = [40, 20, 25, 20, 30, 50, 40, 20, 50, 40, 25, 50]
# lsty = [385, 400, 395, 365, 475, 440, 490, 420, 560, 525, 480, 510]

#Q3
# lstx = [86,74,63,95,90,34,63,81,60,60]
# lsty = [570,497,433,623,593,246,431,520,401,386]

# #Q4
# lstx = [3 ,2, 2, 1 ,3 ,3 ,5 ,2 ,1 , 3]
# lsty = [3.8 , 2.6 ,2.1, 1.5,3.4,3.2,4.8,2.3,1.4,3.3]

#Q5
lstx = [113,112,35,102,73,50,60,89,51,71,92,148,51,160,112,69,51,33,39,61]
lsty = [70,70,20,60,50,40,40,60,40,40,60,90,30,90,60,40,40,30,20,40,]

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
Sxy = calculate_Sxy(b1,sxx)
print ("Sxy: "+str(Sxy))

print("#################################")
sse = calculate_sse(sxx, syy, b1)
print ("SSE: "+str(sse))

MSE = sse / (n - 2)
print ("MSE: " + str(MSE))
print("#################################")
Sb1 = pow(MSE / sxx, 0.5)
print ("S(b1): "+str(Sb1))

Sb0 = pow((xPower/(n*sxx)) * MSE, 0.5)
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
print("Hypothesis test for B1 :\nH0: B1 = 0\nH1: B1 != 0")
t_star_forB1 = calculate_t_star(b1,Sb1)
print("t*_B1 == " + str(t_star_forB1)+"\n")
reject_or_accept(t_star_forB1,t_stat)
p_value_B1 = calculate_pvalue(t_star_forB1, n-2)
print("p-value is : " + str(p_value_B1))
print("#################################")
print("Hypothesis test for B0 :\nH0: B0 = 0\nH1: B0 != 0")
t_star_forB0 = calculate_t_star(b0, Sb0)
print("t*_B0 == " + str(t_star_forB0)+"\n")
reject_or_accept(t_star_forB0, t_stat)
p_value_B0 = calculate_pvalue(t_star_forB0, n-2)
print("p-value is : " + str(p_value_B0))
print("#################################\n")

r = calculate_r(b1,syy,sxx)
print("r == " + str(r))
print("#################################\n")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ANOVA Table @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
SSR = calculate_SSR(b1, sxx)
MSR = calculate_MSR(SSR, 1)
SSTO = calculate_SSTO(SSR,sse)
F_stat = calculate_F_stat(MSR, MSE)
F_PValue = 1- stats.f.cdf(F_stat, 1, n-2)
str_ssr = str(SSR)
str_MSR = str(MSR)
str_F = str(F_stat)
str_MSE = str(MSE)
str_sse = str(sse)
str_SSTO = str(SSTO)
str_F_PValue = str(F_PValue)
ss = "        Sum of Squares          "
ms = "        Mean Square          "
d_f = "D.F  "
f_star = "        F_stat       "
f_p_value = "         P-Value         "
print("___________________________________________________________________________________________________________________________________________________")
print("||            ||          Sum of Squares          ||          Mean Square          ||  D.F  ||          F_stat       ||          P-Value         ||")
print("||-----------------------------------------------------------------------------------------------------------------------------------------------||")
print("|| Regression ||  " + str_ssr+" "*(len(ss)-len(str_ssr)) + "||  "+ str_MSR +" "*(len(ms)-len(str_MSR))+ "||  1    ||  "+str_F+" "*(len(f_star)-len(str_F))+"|| "+str_F_PValue+" "*(len(f_p_value)-len(str_F_PValue))+"||")
print("||-----------------------------------------------------------------------------------------------------------------------------------------------||")
print("|| Residual   ||  "+str_sse+ " "*(len(ss)-len(str_sse))+"||  "+str_MSE+" "*(len(ms)-len(str_MSE))+"||  "+str(n-2)+" "*(len(d_f)-len(str(n-2))) +"||          --           ||            --            ||")
print("||-----------------------------------------------------------------------------------------------------------------------------------------------||")
print("|| Total      ||  "+str_SSTO+" "*(len(ss)-len(str_SSTO))+"||              --               ||  "+str(n-1)+" "*(len(d_f)-len(str(n-1)))+"||          --           ||            --            ||")
print("---------------------------------------------------------------------------------------------------------------------------------------------------")

