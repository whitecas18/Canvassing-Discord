import requests
import json

class CanvasCourse:

  def __init__(self, institution=None, auth_token=None, class_code=None):
    #'13605~tyg7VFRxKn0BmCdQUK5gzgte5Sy8H4lgYCwFfPz3Bbb5sU6k3nD5l46WORwS4AEF'
    #'13605~emUlcabJaZL40QOMJMF39mUzIpOnRGMzI4c6fI9ZIVgRa6cswtXTCMLO8WTL9O60'
    self.auth_token = auth_token
    self.institution = institution
    self.class_code = class_code
    self.session = requests.session()
    if institution is not None:
     self.headers = {
        'Authorization': 'Bearer {}'.format(self.auth_token),
      }
     self.session.headers.update(self.headers)
    if  auth_token is not None:
      self.initial_url = 'https://{}.instructure.com/api/v1/'.format(self.institution)
    else:
      self.headers = None
      self.initial_url = None



  #date is in the format 'YYYY-MM-DD'
  #returns all announcements for self.class_code with a starting date of start_date
  #and an ending date of end_date
  def getAnnouncements(self):
    return self.session.get(
      self.initial_url + 'announcements?context_codes[]=course_' + self.class_code).json()

  
  #returns all assignments along with the due dates for the course
  def getAssignments(self):
    return self.session.get(
      self.initial_url + "courses/" + self.class_code + "/assignments").json

  def setAuth(self, auth):
    self.auth_token = auth
    self.headers = {
        'Authorization': 'Bearer {}'.format(self.auth_token),
      }
    print(self.headers)
    self.session.headers.update(self.headers)

  def setInst(self, inst):
    self.institution = inst
    self.initial_url = 'https://{}.instructure.com/api/v1/'.format(self.institution)

  def setCCode(self, code):
    self.class_code = code

  def getSession(self):
    return session

#   def get_info(self):
#   	headers = {
#     'Authorization': 'Bearer {}'.format(self.auth_token),
#    }

# 	session = requests.Session()
# 	session.headers.update(headers)


# 	courses = session.get('https://canvas.instructure.com/api/v1/courses').json()

# 	data = []
# 	for course in courses:
# 	  course_id = course['id']
# 	  course_quizzes = session.get('https://canvas.instructure.com/api/v1/courses/{}/quizzes'.format(course_id)).json()
# 	  course_assignments = session.get('https://canvas.instructure.com/api/v1/courses/{}/assignments'.format(course_id)).json()
# 	  data.append({
# 	    "course": course_id,
# 	    "assignments": course_assignments,
# 	    "quizzes": course_quizzes
# 	  }
# 	  )

# 	print(data)

# 	announ_response = session.get('https://canvas.instructure.com/api/v1/announcements') 
# 	announcements = announ_response.json()
# 	print(announcements)


# c = Canvas()
# c.get_info()
