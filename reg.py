import csv
import copy

fileName = "data.csv"

def Nomrirovka_Min_Max(l):
    if type(l[0] == list):
        max_ = []
        min_ = []
        for obj in l[0]:
            max_.append(obj)
            min_.append(obj)
        for line in l:
            for i in range(len(line)):
                if line[i] > max_[i]:
                    max_[i] = line[i]
                if line[i] < min_[i]:
                    min_[i] = line[i]
        for line in l:
            for i in range(len(line)):
                line[i] = (line[i] - min_[i]) / (max_[i] - min_[i])

    else:
        max_ = max(l)
        min_ = min(l)
        for i in range(len(l)):
            l[i] = (l[i] - min_) / (max_ - min_)


# X_l = [[float(element) for element in row] for row in X_l]

def StrToFloat(ll):
    l = []
    for a in ll:
        l.append(float(a))
    return l


obj_list = []
with open(fileName, "r", newline="") as f:
    reader = csv.reader(f)
    for r in reader:
        obj_list.append(StrToFloat(r))

Nomrirovka_Min_Max(obj_list)


#  a<x,w> algoritm
def W_sum(w, x):
    n = len(x)
    s = 0
    for i in range(n):
        s += w[i] * x[i]
    return s


# x1=1 x2 x3 ... xn lar yig'indisi
def X_sum(x):
    s = 0
    for i in range(len(x)):
        s += x[i]
    return s


# Yo'qotish funksiyasi
# L(a,y)=(a-y)**2
def StopKrit(x, w, y, eps):
    n = len(y)
    s = 0
    for i in range(n):
        h_tetta = W_sum(w, x[i])
        s += (h_tetta - y[i]) ** 2
        print(y[i], "==>>", h_tetta)
    s /= n
    s *= 100
    print("Xatolik % :", s)
    print()
    if s < eps:
        return True
    return False


# &L(a,y)=2(a<x,w>-y)*<x>
def grad_L(w, x, y):
    x_sum = X_sum(x)
    w_sum = W_sum(w, x)
    return 2 * (w_sum - y) * x_sum


# y
y = [a[-1] for a in obj_list if a]
print(y)
# x
x = []
for obj in obj_list:
    xx = [1]
    for o in obj[:-1]:
        xx.append(o)
    x.append(xx)
    print(xx)
# w larga boshlang'ich qiymat berib olamiz
feature_count = len(obj_list[0]) - 1
w = []
for i in range(feature_count + 1):
    w.append(0)
print(w)

n_itenation = 1000
rate = 0.2

# W larni keyingi har bir itaratsiyadagi qiymatini hisoblaymiz
for iter in range(n_itenation):
    print("Iteratsiya #", iter)
    w1 = []
    for j in range(feature_count + 1):
        sum_ = 0
        for i in range(len(x)):
            s = 0
            s += x[i][j]
            sum_ += 2 * (W_sum(w, x[i]) - y[i]) * s
        sum_ /= len(x)
        w_ = w[j] - rate * sum_
        w1.append(w_)
    w = copy.deepcopy(w1)
    if StopKrit(x, w, y, eps=10):
        break

print(w)
