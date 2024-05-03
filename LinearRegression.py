import csv
import copy

fileName = "It_buri.csv"


# Matnlarni float ga aylantiruvchi funksiya
def StrToFloat(ll):
    return [float(a) for a in ll]


# Ma'lumotlarni Min-Max normalizatsiyasi bilan to'g'rilash uchun funksiya
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


# Ikki ro'yxatning dot (nokta) ko'paytmasini hisoblash uchun funksiya
def DotProduct(w, x):
    n = len(x)
    s = 0
    for i in range(n):
        s += w[i] * x[i]
    return s


# Chiziqli regressiya to'xtatish sharti
def StopCriterion(x, w, y, eps):
    n = len(y)
    s = sum((DotProduct(w, x_i) - y_i) ** 2 for x_i, y_i in zip(x, y)) / n
    s *= 100
    print("Xato % :", s)
    print()
    return s < eps


# Yo'lda funksiya gradienti
def X_sum(x):
    s = 0
    for i in range(len(x)):
        s += x[i]
    return s
def LossGradient(w, x, y):
    x_sum = X_sum(x)
    w_sum = DotProduct(w, x)
    return 2 * (w_sum - y) * x_sum



# Chiziqli klassifikatsiya funksiyasi
def LinearClassification(x, w):
    return [classFunc(DotProduct(w, x_i)) for x_i in x]


# Klassifikatsiya funksiyasi
def classFunc(z):
    if z > 0:
        return 1.0
    return 0.0


# CSV fayldan ma'lumotlarni o'qish
obj_list = []
with open(fileName, "r", newline="") as f:
    reader = csv.reader(f)
    for r in reader:
        obj_list.append(StrToFloat(r))

# Ma'lumotlarni normalizatsiya qilish
Nomrirovka_Min_Max(obj_list)

# Xususiyatlarni (x) va belgilarni (y) ajratish
y = [a[-1] for a in obj_list]
x = [[1] + a[:-1] for a in obj_list]

# Og'irligi (w) boshlash
feature_count = len(obj_list[0]) - 1
w = [0] * (feature_count + 1)

# O'qitish parametrlari
n_iterations = 1000
learning_rate = 0.2
epsilon = 10

# O'qish tsikli
for iteration in range(n_iterations):
    print("Iteratsiya #", iteration)
    # Gradientni hisoblash
    gradient = LossGradient(w, x, y)
    # Og'irligini yangilash
    w = [w_j - learning_rate * grad_j for w_j, grad_j in zip(w, gradient)]
    # To'xtatish shartini tekshirish
    if StopCriterion(x, w, y, epsilon):
        break

# Klassifikatsiyani amalga oshirish
predictions = LinearClassification(x, w)

print("Og'irlar:", w)
print("Bashoratlar:", predictions)
