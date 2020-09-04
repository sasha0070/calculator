import math

u_apr = int(input("Какой процент годовых сейчас? Целое число процентов "))
u_now = int(input("Какая начальная сумма сбережений? "))
u_goal = int(input("Какая финансовая цель? "))

apr = 1 + (u_apr/100)
deferecne = u_goal/u_now
time = int(math.log(deferecne, apr))
print('Понадобится ', round(time), " лет для достижения цели, если не увеличивать сумму начальных сбережений.")

u_more = float(input("А если увеличивать начальный капитал. Сколько ты хотел бы прибавлять в месяц? "))

year_count = [11, 23, 35, 47]  # выделение каждого нового года
now = u_now # отделяем пользовательский ввод и расчет.
for i in range(time*12):
    now = now + now*(apr-1)/12 + u_more
    if now >= u_goal:
        break
print(round((i+1)/12, 1), ' Года') 
print('Намного лучше! Если увеличивать начальный капитал на ', u_more, '$ в месяц, то понадобится ', round((i+1)/12, 1), "Года, что б накопить ", round(now), "$")

u_m_more = float(input("А на сколько процентов в год сможешь увеличивать сумму ежемесячных пополнений? "))

m_more = 1 + (u_m_more/100) # перевод из процентов в целое
more = u_more
again_now = u_now
for i in range(time):
    if i < 11:
        more_monthly = u_more
    again_now = again_now + again_now*(apr-1)/12 + more_monthly
    if i in year_count:
        more_monthly *= m_more
    if again_now > u_goal:
        break
print() 
print('И если повышать ежемесяный вклад, на', u_m_more, '%, то понадобится ', round((i+1)/12, 1), "Года, что б накопить ", round(again_now), "$")