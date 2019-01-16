#Admin methods to access REST endpoints of  prcessmaker, written referring to:
#https://wiki.processmaker.com/index.php/ProcessMaker_API
import requests

#Application registration variables
api_server = ''
client_id = ''
client_secret = ''


class Admin:
  def __init__(self, username, password):
    self.username = username
    self.password = password


  def login(self, workspace):
    url = api_server+'/'+workspace+'/oauth2/token'
    payload ={'grant_type':'password','scope': '*',
        'client_id': client_id,
        'client_secret':client_secret,
        'username':self.username, 'password': self.password}
    r = requests.post(url, data=payload)
    self.accesstoken = 'Bearer '+r.json()['access_token']
    return (r.json()['token_type'], r.json()['access_token'])


#Users###########################################################
    
  def users(self, workspace): #gets all users
    headers = {'Authorization': self.accesstoken}
    url = api_server+'/api/1.0/'+workspace+'/users'
    r = requests.get(url,headers=headers)  
    print(r.status_code)
    print(r.text)

  def user_info(self, usr_uid): #gets a users information
    headers = {'Authorization': self.accesstoken}
    url = api_server+'/api/1.0/'+workspace+'/user/'+usr_uid
    r = requests.get(url,headers=headers)  
    print(r.status_code)
    print(r.text)
    

  def user(self, workspace, new_user): #creates a new user  
    payload = new_user
    headers = {'Authorization': self.accesstoken}
    #POST /api/1.0/{workspace}/user
    url = api_server+'/api/1.0/'+workspace+'/user/'
    r = requests.post(url, data=payload, headers=headers)
    print(r.status_code)
    print(r.text)

  def image_upload(self,workspace, usr_uid): #uploads user image 
    #POST /api/1.0/{workspace}/user/{usr_uid}/image-upload
    url = api_server+'/api/1.0/'+workspace+'/user/'+usr_uid+'/image-upload'
    imagelocation=r"C:\Users\MYPC\Pictures\processmaker\userimage.jpg"
    payload = {'USR_PHOTO': imagelocation} #need a location on the server. 
    headers = {'Authorization': self.accesstoken}
    r = requests.post(url, data=payload, headers=headers)
    print(r.status_code)
    print(r.text)

  def update_user(self, workspace, updated_user): #updates a user  
    payload = updated_user
    headers = {'Authorization': self.accesstoken}
    #PUT /api/1.0/{workspace}/user
    url = api_server+'/api/1.0/'+workspace+'/user/'
    r = requests.put(url, data=payload, headers=headers)
    print(r.status_code)
    print(r.text)
    
  def delete_user(self,workspace, usr_uid):#Delete a specified user
    #DELETE /api/1.0/{workspace}/user/{usr_uid}
    url = api_server+'/api/1.0/'+workspace+'/user/'+usr_uid
    headers = {'Authorization': self.accesstoken}
    r = requests.delete(url, headers=headers)
    print(r.status_code)
    print(r.text)

  #Groups###########################################################

  def groups(self, workspace):#Get a list of all the groups in the workspace.
    #GET /api/1.0/{workspace}/groups?filter={filter}&start={start}&limit={limit}
    headers = {'Authorization': self.accesstoken}
    url = api_server+'/api/1.0/'+workspace+'/groups'
    r = requests.get(url,headers=headers)  
    print(r.status_code)
    print(r.text)

  def group_info(self, workspace, grp_uid): #Get information about a specified group.
    #GET /api/1.0/{workspace}/group/{grp_uid}
    headers = {'Authorization': self.accesstoken}
    url = api_server+'/api/1.0/'+workspace+'/group/'+grp_uid
    r = requests.get(url,headers=headers)  
    print(r.status_code)
    print(r.text)

  def group(self, workspace, grp_title, grp_status): #creates a new group. 
    #POST /api/1.0/{workspace}/group
    payload = {'grp_title': grp_title, 'grp_status': grp_status}
    headers = {'Authorization': self.accesstoken}
    url = api_server+'/api/1.0/'+workspace+'/group/'
    r = requests.post(url, data=payload, headers=headers)
    print(r.status_code)
    print(r.text)

  def update_group(self, workspace, grp_uid, grp_title, grp_status): #Update information about a specified group. 
    #PUT /api/1.0/{workspace}/group/{grp_uid}
    payload = {'grp_title': grp_title, 'grp_status': grp_status}
    headers = {'Authorization': self.accesstoken}
    url = api_server+'/api/1.0/'+workspace+'/group/'+grp_uid
    r = requests.put(url, data=payload, headers=headers)
    print(r.status_code)
    print(r.text)

  def delete_group(self,workspace, grp_uid):#Delete a specified group
    #DELETE /api/1.0/{workspace}/group/{grp_uid}
    url = api_server+'/api/1.0/'+workspace+'/group/'+grp_uid
    headers = {'Authorization': self.accesstoken}
    r = requests.delete(url, headers=headers)
    print(r.status_code)
    print(r.text)

  def get_group_members(self,workspace, grp_uid):#List the assigned users to a specified group.
    #GET /api/1.0/{workspace}/group/{grp_uid}/users?filter={filter}&start={start}&limit={limit}
    url = api_server+'/api/1.0/'+workspace+'/group/'+grp_uid+'/users'
    #optional parameters. 
    #payload = {'filter': mfilter, 'start': start, 'limit': limit}
    headers = {'Authorization': self.accesstoken}
    r = requests.get(url, headers=headers)
    print(r.status_code)
    print(r.text)

  def available_group_users(self,workspace, grp_uid):#Get a list of available users, which can be assigned to a specified group.
    #GET /api/1.0/{workspace}/group/{grp_uid}/available-users?filter={filter}&start={start}&limit={limit}
    url = api_server+'/api/1.0/'+workspace+'/group/'+grp_uid+'/available-users'
    #optional parameters. 
    #payload = {'filter': mfilter, 'start': start, 'limit': limit}
    headers = {'Authorization': self.accesstoken}
    r = requests.get(url, headers=headers)
    print(r.status_code)
    print(r.text)

  def assign_to_group(self,workspace, grp_uid, usr_uid):#Assign a user to a specified group.
    #POST /api/1.0/{workspace}/group/{grp_uid}/user
    url = api_server+'/api/1.0/'+workspace+'/group/'+grp_uid+'/user'
    payload = {'usr_uid': usr_uid,}
    headers = {'Authorization': self.accesstoken}
    r = requests.post(url, headers=headers, data=payload)
    print(r.status_code)
    print(r.text)

  def unassign_from_group(self,workspace, grp_uid, usr_uid):#Unassign (remove) a user from a group so no longer a member of the group.
    #DELETE /api/1.0/{workspace}/group/{grp_uid}/user/{usr_uid}
    url = api_server+'/api/1.0/'+workspace+'/group/'+grp_uid+'/user/'+usr_uid
    headers = {'Authorization': self.accesstoken}
    r = requests.delete(url, headers=headers)
    print(r.status_code)
    print(r.text)

 #Departments###########################################################

  def departments(self, workspace):#Get a list of all the departments in the workspace.
    #GET /api/1.0/{workspace}/departments
    headers = {'Authorization': self.accesstoken}
    url = api_server+'/api/1.0/'+workspace+'/departments'
    r = requests.get(url,headers=headers)  
    print(r.status_code)
    print(r.text)

  def department_info(self, workspace, dep_uid): #Get information about a specified department.
    #GET /api/1.0/{workspace}/department/{dep_uid}
    headers = {'Authorization': self.accesstoken}
    url = api_server+'/api/1.0/'+workspace+'/department/'+dep_uid
    r = requests.get(url,headers=headers)  
    print(r.status_code)
    print(r.text)

  def update_department(self, workspace, dep_uid, departmentinfo): #Update information about a deparment 
    #PUT /api/1.0/{workspace}/department/{dep_uid}
    payload = departmentinfo
    headers = {'Authorization': self.accesstoken}
    url = api_server+'/api/1.0/'+workspace+'/department/'+dep_uid
    r = requests.put(url, data=payload, headers=headers)
    print(r.status_code)
    print(r.text)

  def delete_department(self,workspace, dep_uid):#Delete a specified department
    #DELETE /api/1.0/{workspace}/department/{dep_uid}
    url = api_server+'/api/1.0/'+workspace+'/department/'+dep_uid
    headers = {'Authorization': self.accesstoken}
    r = requests.delete(url, headers=headers)
    print(r.status_code)
    print(r.text)
    #Not tested

  def get_depart_mentmembers(self,workspace, dep_uid):#Get a list of the users assigned to a specified department.
    #GET /api/1.0/{workspace}/department/{dep_uid}/assigned-user
    url = api_server+'/api/1.0/'+workspace+'/department/'+dep_uid+'/assigned-user'
    headers = {'Authorization': self.accesstoken}
    r = requests.get(url, headers=headers)
    print(r.status_code)
    print(r.text)
    #print(r.json()[0]['usr_uid'])

  def available_dept_users(self,workspace, dep_uid):#Get a list of the available users, which can be assigned to a specified department. 
    #GET /api/1.0/{workspace}/department/{dep_uid}/available-user
    url = api_server+'/api/1.0/'+workspace+'/department/'+dep_uid+'/available-user'
    headers = {'Authorization': self.accesstoken}
    r = requests.get(url, headers=headers)
    print(r.status_code)
    print(r.text)

  def v28_assign_to_dept(self,workspace, dep_uid, usr_uid):#Assign a user to a specified department in version 2.8
    #PUT /api/1.0/{workspace}/department/{dep_uid}/assign-user/{usr_uid}
    url = api_server+'/api/1.0/'+workspace+'/department/'+dep_uid+'/assign-user/'+usr_uid
    headers = {'Authorization': self.accesstoken}
    r = requests.put(url, headers=headers)
    print(r.status_code)
    print(r.text)
    
  def v30_assign_to_dept(self,workspace, dep_uid, usr_uid):#Assign a user to a specified department in version 2.8
    #POST /api/1.0/{workspace}/department/{dep_uid}/assign-user
    url = api_server+'/api/1.0/'+workspace+'/department/'+dep_uid+'/assign-user'
    headers = {'Authorization': self.accesstoken}
    payload = {'usr_uid': usr_uid}
    r = requests.post(url, headers=headers, data=payload)
    print(r.status_code)
    print(r.text)
    
  def unassign_from_dept(self,workspace, dep_uid, usr_uid):#Unassign a user from a department
    #Doest work
    #PUT /api/1.0/{workspace}/department/{dep_uid}/unassign-user/{usr_uid}
    url = api_server+'/api/1.0/'+workspace+'/department/'+dep_uid+'/unassign-user/'+usr_uid
    headers = {'Authorization': self.accesstoken}
    r = requests.put(url, headers=headers)
    print(r.status_code)
    print(r.text)

  def set_manager(self,workspace, dep_uid, usr_uid):#Set a user to be the manager (supervisor) for a department.
    #PUT /api/1.0/{workspace}/department/{dep_uid}/set-manager/{usr_uid}  
    url = api_server+'/api/1.0/'+workspace+'/department/'+dep_uid+'/set-manager/'+usr_uid
    headers = {'Authorization': self.accesstoken}
    r = requests.put(url, headers=headers)
    print(r.status_code)
    print(r.text)


#Roles###########################################################

  def roles(self, workspace, rfilter = '', start = 0, limit = 100):#Get a list of all the roles in the workspace.
    #GET /api/1.0/{workspace}/roles?filter={filter}&start={start}&limit={limit}
    headers = {'Authorization': self.accesstoken}
    payload = {'filter': rfilter, 'start': start, 'limit': limit}
    print(payload)
    url = api_server+'/api/1.0/'+workspace+'/roles'
    r = requests.get(url,headers=headers, params=payload)  
    print(r.status_code)
    print(r.text)

  def role_info(self, workspace, rol_uid): #Get information about a specified role.
    #GET /api/1.0/{workspace}/role/{rol_uid}
    headers = {'Authorization': self.accesstoken}
    url = api_server+'/api/1.0/'+workspace+'/role/'+rol_uid
    r = requests.get(url,headers=headers)  
    print(r.status_code)
    print(r.text)

  def role(self, workspace, rol_code, rol_name, rol_status): #Create a new role.
    #POST /api/1.0/{workspace}/role
    payload = {'rol_code': rol_code, 'rol_name':rol_name , 'rol_status':rol_status}
    headers = {'Authorization': self.accesstoken}
    url = api_server+'/api/1.0/'+workspace+'/role/'
    r = requests.post(url, data=payload, headers=headers)
    print(r.status_code)
    print(r.text)

  def update_role(self, workspace, rol_uid, rol_code='', rol_name='', rol_status=''): #Update information about a specified role.
    #Dosent work unless optional parameters are provided
    #PUT /api/1.0/{workspace}/role/{rol_uid}
    url = api_server+'/api/1.0/'+workspace+'/role/'+rol_uid
    payload = {'rol_code': rol_code, 'rol_name': rol_name, 'rol_status': rol_status}
    headers = {'Authorization': self.accesstoken}  
    r = requests.put(url, data=payload, headers=headers)
    print(r.status_code)
    print(r.text)

  def delete_role(self,workspace, rol_uid):#Delete a specified role. 
    #DELETE /api/1.0/{workspace}/role/{rol_uid}
    url = api_server+'/api/1.0/'+workspace+'/role/'+rol_uid
    headers = {'Authorization': self.accesstoken}
    r = requests.delete(url, headers=headers)
    print(r.status_code)
    print(r.text)

  def get_users_with_role(self,workspace, rol_uid, rfilter = '', start = 0, limit = 100000):#Get a list of the users assigned to a specified department.
    #GET /api/1.0/{workspace}/role/{rol_uid}/users
    url = api_server+'/api/1.0/'+workspace+'/role/'+rol_uid+'/users'
    headers = {'Authorization': self.accesstoken}
    payload = {'filter': rfilter, 'start': start, 'limit': limit}
    r = requests.get(url, headers=headers, params=payload)
    print(r.status_code)
    print(r.text)
    #print(r.json()[0]['usr_uid'])

  def available_role_users(self,workspace, rol_uid):#Get a list of the available users, which can be assigned to a specified department. 
    #GET /api/1.0/{workspace}/role/{rol_uid}/available-users
    url = api_server+'/api/1.0/'+workspace+'/role/'+rol_uid+'/available-users'
    headers = {'Authorization': self.accesstoken}
    r = requests.get(url, headers=headers)
    print(r.status_code)
    print(r.text)

  def assign_to_role(self,workspace, rol_uid, usr_uid):#Assign a user to a role.
    #POST /api/1.0/{workspace}/role/{rol_uid}/user
    url = api_server+'/api/1.0/'+workspace+'/role/'+rol_uid+'/user'
    headers = {'Authorization': self.accesstoken}
    payload = {'usr_uid': usr_uid}
    r = requests.post(url, headers=headers, data = payload)
    print(r.status_code)
    print(r.text)
    
  def unassign_from_role(self,workspace, rol_uid, usr_uid):#Unassign a user from a department
    #DELETE /api/1.0/{workspace}/role/{rol_uid}/user/{usr_uid}
    #Not tested
    url = api_server+'/api/1.0/'+workspace+'/role/'+rol_uid+'/user/'+usr_uid
    headers = {'Authorization': self.accesstoken}
    r = requests.delete(url, headers=headers)
    print(r.status_code)
    print(r.text)


    
#for testing
    newuser = {
          "usr_username":    "aravinda123",
          "usr_firstname":   "Aravinda",
          "usr_lastname":    "Silva",
          "usr_email":       "aravinda@example.com",
          "usr_due_date":    "2020-12-31",
          "usr_status":      "ACTIVE",
          "usr_role":        "PROCESSMAKER_OPERATOR",
          "usr_new_pass":    "123456",
          "usr_cnf_pass":    "123456",
          "usr_address":     "",#optional
          "usr_zip_code":    "46135",
          "usr_country":     "SL",
          "usr_city":        "CMB", #optional
          "usr_location":    "", #optional
          "usr_phone":       "1-765-653-4478", #optional
          "usr_position":    "Head Accountant", #optional
          "usr_create_date": "2015-02-12 17:27:06", #optional
          "usr_update_date": "2015-02-12 17:27:06", #optional
          "usr_replaced_by": "", #optional
          "usr_calendar":    "", #optional
        }
    
#examples
#a1 = Admin("admin", "123456")
#a1.login('workspace')
#a1.available_dept_users('workspace', '32143xxxx43243')



