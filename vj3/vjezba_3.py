#!C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\IDE\Extensions\Microsoft\Python\Miniconda\Miniconda3-x64\python.exe
import cgi


print("""
<!DOCTYPE html>

<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="utf-8" />
    <title></title>
</head>
<body>

    <form action="2.forma.py" method="post">
        Ime:<br>
        <input type="text" name="ime">
        <br>
        Lozinka:
        <br>
        <input type="password" name="lozinka" value="" required>
        <br>
        Potvrdena lozinka:<br>
        <input type="password" name="potvrdena_lozinka" value="" required>
        <br>
        <input type="submit" value="Next" >
    </form>
    

</body>
</html>

""")



