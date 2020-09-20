import requests
import json

auth_token = '13605~tyg7VFRxKn0BmCdQUK5gzgte5Sy8H4lgYCwFfPz3Bbb5sU6k3nD5l46WORwS4AEF'
headers = {
    'Authorization': 'Bearer {}'.format(auth_token),
}

session = requests.Session()
session.headers.update(headers)


courses = session.get('https://canvas.instructure.com/api/v1/courses').json()

data = []
for course in courses:
  course_id = course['id']
  #course_quizzes = session.get('https://canvas.instructure.com/api/v1/courses/{}/quizzes'.format(course_id)).json()
  #course_assignments = session.get('https://canvas.instructure.com/api/v1/courses/{}/assignments'.format(course_id)).json()
  data.append({
    "course": course_id
   # "assignments": course_assignments,
   # "quizzes": course_quizzes
  }
  )

print(data)

announ_response = session.get('https://canvas.instructure.com/api/v1/announcements') 
announcements = announ_response.json()
print(announcements)
