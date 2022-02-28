from lr1 import spaces, spaces_abs_freq, data, h
import pandas as pd
import numpy as np

df = pd.DataFrame()
df['Средние значения'] = list(
    map(lambda space: (space[0] + space[1]) / 2, spaces))
df['Частоты'] = spaces_abs_freq
C = df.iloc[4, 0]
df['Условные варианты'] = df['Средние значения'].apply(lambda x: (x - C) / h)

moments = []
for i in range(1, 5):
    col = 'УМ{}'.format(i)
    df[col] = df.iloc[:, 1:3].apply(lambda x: x[0] * x[1] ** i, axis=1)
    moments.append(df[col].sum() / len(df))

df['Проверка'] = df.iloc[:, 1:3].apply(lambda x: x[0] * ((x[1]+1)**4), axis=1)
print(df)

start_moment_1_usl = moments[0]*h + C
print('Начальный условный момент 1го порядка: ', start_moment_1_usl)

central_moment_2_usl = (moments[1] - moments[0]**2)*(h**2)
print('Центральный условный момент 2го порядка: ', central_moment_2_usl)

central_moment_3_usl = (moments[2] - 3*moments[1]
                        * moments[0] + 2*(moments[0]**3))*(h**3)
print('Центральный условный момент 3го порядка: ', central_moment_3_usl)

central_moment_4_usl = (moments[3] - 4*moments[2]*moments[0] +
                        6*moments[1]*(moments[0]**2) - 3*(moments[0]**4))*(h**4)
print('Центральный условный момент 3го порядка: ', central_moment_4_usl)

start_moment_1_emp = df.iloc[:, :2].apply(
    lambda x: x[0]*x[1], axis=1).sum() / len(df)
print('Начальный эмпирический момент 1го порядка: ', start_moment_1_emp)

central_moment_2_emp = df.iloc[:, :2].apply(lambda x: (
    (x[0] - start_moment_1_emp)**2)*x[1], axis=1).sum() / len(df)
print('Центральный эмпирический момент 2го порядка: ', central_moment_2_emp)

s = np.sqrt((len(df)/(len(df)-1)) * central_moment_2_emp)
asim = central_moment_3_usl / (s**3)
print('Асимметрия: ', asim)

ecs = central_moment_4_usl / (s**4) - 3
print('Эксцесс: ', ecs)

space_moda_index = np.argmax(spaces_abs_freq)
m2, m1, m3 = spaces_abs_freq[space_moda_index], 0, 0
if space_moda_index > 0:
    m1 = spaces_abs_freq[space_moda_index - 1]
if space_moda_index < len(spaces_abs_freq):
    m3 = spaces_abs_freq[space_moda_index + 1]
moda = spaces[space_moda_index][0] + h * ((m2 - m1) / (2 * m2 - m1 - m3))
print("Мода:", moda)

median_index = 4
median_lower_freqs = np.sum(spaces_abs_freq[:median_index])
median = \
    spaces[median_index][0] \
    + h * ((0.5 * len(data) - median_lower_freqs) /
           spaces_abs_freq[median_index])
print("Медиана:", median)
