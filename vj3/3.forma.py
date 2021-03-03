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
    <form action="4.forma.py" method="post">
        Napomene:
        <br/>
        <textarea name="napomena"></textarea>
        <br />
        <input type="submit" name="next" value="Next" ''')

print ('<input type="hidden" name="ime" value="' + params.getvalue("ime") + '">')
print ('<input type="hidden" name="email" value="' + params.getvalue('email') + '">')
print ('<input type="hidden" name="smjer_studija" value="' + params.getvalue('smjer_studija') + '">')
print ('<input type="hidden" name="studij" value="' + params.getvalue("studij") + '">')
print ('<input type="hidden" name="zavrsni_rad" value="' + params.getvalue("zavrsni_rad") + '">')
print('''
        
    </form>
</body>
</html>''')
 