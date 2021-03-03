#!C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\python.exe

import base
import os,cgi
import session
import user

params = cgi.FieldStorage()

data = session.get_session_data()
if data is None: # tko nema sessiju nije logiran. - idi na login
    print ("Location: login.py")
else:
	user_id = data.get("user_id", None)
	user_role = user.get_user_role(user_id)
	if user_role != "ADMIN":
		print ("Location: index.py")
	else:
		edit_id = params.getvalue("edit_id")
        #if not edit_id:
        #    print ("Location: users.py")
if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    user_id = params.getvalue("edit_id")
    username = params.getvalue("username")
    gender = params.getvalue("gender")
    role = params.getvalue("role")
    user.update_user(user_id, username, gender, role)
    print("Location: users.py")
print ()
base.start_html()
user_obj = user.get_user(edit_id)
role = user.get_user_role(edit_id)
print ('<form method="POST">')
print ('Username: <input type="text" name="username" value="'+ user_obj[1] +'"><br>')
print ('Gender: <input type="text" name="gender" value="'+ user_obj[3] +'"><br>')
print ('Role: <input type="text" name="role" value="'+ role +'"><br>')
print ('<input type="submit" value="Edit">')
print ('</form>')
base.finish_html()