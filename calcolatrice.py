x=int(input("inserisci il primo numero intero(x):"))
y=int(input("inserisci il secondo numero intero(y):"))
print("Scegli:")
print("1.Somma")
print("2.Sottrazione")
print("3.Moltiplicazione")
print("4.Divisione (intera)")
operazione = int(input(inserisci il numero corrispondente all'operazione desiderata:'))
risultato = 0
if operazione == 1:
    risultato = x+y
elif operazione ==2:
    risultato =x-y
elif operazione ==3:
risultato =x * y
elif operazione ==4:
risultato = x //y
else:
print("Operazione non valida!")
print("il risultato dell'operazione è:",risultato)