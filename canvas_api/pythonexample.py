import requests

headers = {
    'Authorization': 'Bearer 13605~tyg7VFRxKn0BmCdQUK5gzgte5Sy8H4lgYCwFfPz3Bbb5sU6k3nD5l46WORwS4AEF',
}

response = requests.get('https://canvas.instructure.com/api/v1/courses', headers=headers)

print(response.content)
