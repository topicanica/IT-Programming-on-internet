#!C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\IDE\Extensions\Microsoft\Python\Miniconda\Miniconda3-x64\python.exe

import cgi
params=cgi.FieldStorage()
ime=params.getvalue("ime")
print('''

<!DOCTYPE html>

<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="utf-8" />
    <title></title>
</head>
<body>
    <h2>Uneseni podatci</h2>
''')

print(' Ime:', params.getvalue("ime") )
print("<br>")
print('Smjer:',params.getvalue("smjer_studija") )
print("<br>")
print('Status:',params.getvalue("studij"))   
print("<br>")
print('Zavrsni rad:',params.getvalue("zavrsni_rad"))
print("<br>")
print('Napomene:',params.getvalue("napomena"))

print('''
    </br>
    <button onclick="window.location.href='/test/vjezba_3.py'">Vrati na pocetak</button>
</body>
</html>
''')