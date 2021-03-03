#!C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\IDE\Extensions\Microsoft\Python\Miniconda\Miniconda3-x64\python.exe

import cgi

params=cgi.FieldStorage()

print('''
<!DOCTYPE html>

<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="utf-8" />
    <title></title>
</head>
<body>
    <form action="3.forma.py" method="post">

        Status:<input type="radio" name="studij" value="izvanredni" checked> izvanredni studij
        <input type="radio" name="studij" value="redovni"> redovni studij
        <br/>
        E-mail:<input type="email" name="email" required>
        <br/>
        Odabir smjera:<select name="smjer_studija">
            <option value="programiranje">Programiranje</option>
            <option value="baze_podataka">Baze podataka</option>
            <option value="racunalne_mreze">Racunalne mreze</option>
            <option value="informacijski_sustavi">Informacijski sustavi</option>
        </select>
        <br/>
        <input type="hidden" name="zavrsni_rad" value="nema" />
        Zavrsni:<input type="checkbox" name="zavrsni_rad" value="zavrsni rad">
                
        <br/>''')
print ('<input type="hidden" name="ime" value="' + params.getvalue("ime") + '">')
print('''
        <input type="submit" name="next" value="Next">
    </form>
</body>
</html>''')

 