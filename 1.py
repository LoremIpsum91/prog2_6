import gspread
from statsmodels.tsa.ar_model import AutoReg, ar_select_order

# подключаем таблицу
sa = gspread.service_account(filename='nth-suprstate-273909-a8b636151c70.json')
sh = sa.open('prog2_6_1')
wks = sh.worksheet('Sheet1')

# получение значений курса
data = wks.col_values(2)

# очищение значений от пустых и перевод во float
for n, i in enumerate(data):
    if not bool(i):
        data.pop(n)
for n, i in enumerate(data):
    data[n] = float(data[n])

mod = ar_select_order(data, maxlag=3, old_names=False)
model = AutoReg(data, lags=mod.ar_lags, old_names=False).fit()
pred = model.predict(start=len(data), end=len(data)+2)

print('prediction:', pred[0])