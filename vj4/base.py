#!C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\python.exe

def start_html():
    print ("""<!DOCTYPE html>
    <html>
    <body>""")

def finish_html():
    print ("""</body>
    </html>""")

def start_table_upisi():
    print('''<table> 
    <tr>
    <th>Predmet</th>
    <th>Status</th>
    <th>Bodovi</th>
    </tr>''')
def start_table_yearly(year):
    print('''<table>
    <tr>
    <th>'''+year+'''</th>
    <th>Bodovi</th>
    <th>Status</th>
    </tr> ''')

def table_style():
    print('''<style>
table, th, td {
  border: 2px solid black;
  border-color:gray;
}
</style>''')