import sqlite3

def check_credentials(username, password):

 conn = sqlite3.connect('db.sqlite3')

 cursor = conn.cursor()
 #cursor.execute("""CREATE TABLE members_member (
 #   member_name NULL,
 # gender integer,
  #  member_id varchar(8)
 #)""")

 cursor.execute("Select member_id, member_name FROM members_member where member_id = {username} AND member_name = {password}" , (username, password))
 
 result = cursor.fetchone()

 print(result)
 
 conn.commit()


 cursor.close
 conn.close()
 
 if result == username and password:
     return True
 else :
     return False
 
username = "MK-936"
password = "Shivam Kumar Singh"

print(check_credentials(username, password))


     
     
 
 