import arrow

utc = arrow.utcnow()
print(utc)

#Some datetime operations

print(arrow.now())

print(arrow.get('2023-11-02 12:30:45', 'YYYY-MM-DD HH:mm:ss'))

print(arrow.get('Januka was born in May 1997', 'MMMM YYYY'))
print("\n\n")

arw = arrow.utcnow()
print(arw.shift(weeks=+3))
print(arw.replace(tzinfo='US/Pacific'))
print("\n\n")

print(arrow.utcnow().format('YYYY-MM-DD HH:mm:ss ZZ'))

print(utc.to('Asia/Baku'))