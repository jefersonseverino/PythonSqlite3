import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

logged = False

print('Welcome to our login base')
print('Do you have an account?')
resp = str(input('S/N: ')).upper().strip()[0]

if resp == 'N':
    user = str(input('Username: '))
    password = str(input('Password: '))
    print('Confirm your password')
    p2 = str(input(''))
    if p2 != password:
        while True:
            print('Confirm your password')
            p2 = str(input(''))
            if p2 == password:
                break
    cur.execute('''INSERT INTO Counts (user,password) VALUES (?,?)''',(user,password))

else:
    while not logged:
        user = str(input('Username: '))
        password = str(input('Password: '))
        for row in cur.execute('SELECT * FROM Counts'):
            if (user,password) == row:
                print('Login efetuado com sucesso')
                logged = True
                break
            
conn.commit()

conn.close()