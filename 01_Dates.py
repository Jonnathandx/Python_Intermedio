from datetime import datetime

def show_datefields(date: datetime):
    print(f'Año actual: {date.year}')
    print(f'Mes actual: {date.month}')
    print(f'Dia actual: {date.day}')
    print(f'Hora actual: {date.hour}')
    print(f'Minuto actual: {date.minute}')
    print(f'Segundo actual: {date.second}')
# marca de tiempo actual
actual_datetime = datetime.now()
print(actual_datetime)
show_datefields(actual_datetime)

# timestamp (Representacion unica de un tiempo)
timestamp = actual_datetime.timestamp()
print(timestamp)

# Definicion de marca de tiempo
date_1997 = datetime(1997, 8, 28, 11, 5, 6)
print(date_1997)

from datetime import time

# Definicion de tiempo
actual_time = time(hour=15, minute=3, second=45)
print(actual_time)

from datetime import date

# Definicion de fecha
actual_date =  date(2026, 8, 28)
print(actual_date)

from datetime import timedelta

init_timedelta = timedelta(5)
final_timedelta = timedelta(2)

print(init_timedelta - final_timedelta)