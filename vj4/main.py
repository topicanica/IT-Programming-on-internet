#!C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\python.exe

import cgi
import os
import subjects
import base
import session

params=cgi.FieldStorage()
if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    session.add_to_session(params)
    
session_data = session.get_session_data()
print()
base.start_html()
base.table_style()
print ('''
    <form action="" method="post">
''')
for years, year_id in subjects.year_ids.items():
    print ('<input type="submit" name="year" value="'+ years +'">')

print ('<input type="submit" name="year" value="upis">')

print ('''
''')
in_total=0
first_year=0
current_year = params.getvalue('year')
if current_year=='upis':
    base.start_table_upisi()
    for sub, stat_name in session_data.items():
        if(subjects.subjects.get(sub)!=None):
            print_subjects=subjects.subjects.get(sub)
            print('<tr>')
            print('<td>'+print_subjects['name']+'</td>')
            print('<td>'+subjects.status_names[stat_name]+'</td>')
            print('<td>'+str(print_subjects['ects'])+'</td>')
            print('</tr>')
            if stat_name=='pass':
                in_total+=print_subjects['ects']
            if stat_name=='pass' and print_subjects['year']==1:
                first_year+=1
        else:
            continue
    print('<tr><td></td><td>In total:</td><td>'+str(in_total)+'</td></tr>')
    print('<tr><td></td><td>First year:</td><td>'+str(first_year)+'</td></tr>')
    print('</table>')
else:
    base.start_table_yearly(current_year)
    for key, value in subjects.subjects.items():
        year=subjects.year_names.get(value['year'])
        if year==current_year:
            print('<tr>')
            print('<td>'+value['name']+'</td>')
            print('<td>'+str(value['ects'])+'</td>')
            print('<td>')
            current_stat = session_data.get(key, 'not') # spremi u current stat trenutni status, a ako ga nema onda not
            for stat, stat_name in subjects.status_names.items():
                if current_stat == stat:
                    print('<input type="radio" name="' + key + '" value="' + stat + '" checked > ' + stat_name)
                else:
                    print('<input type="radio" name="' + key + '" value="' + stat + '" > ' + stat_name)
                
            print('</td>')
            print('</tr>')
    
    print('</table>')

print('''
    </form>
''')
base.finish_html()
