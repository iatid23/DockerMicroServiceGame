from django.http import JsonResponse
import json
import jwt
import re

SECRET = "jjfkecmwKJMd_effje2rfk394rf_KFMdsckW34x_ckr"
USER_DB = {}

emailRegex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def login(request):
    if request.method != "POST":
            return JsonResponse({})
    # body_unicode = request.body.decode('utf-8')
    body_unicode = request.body
    body = json.loads(body_unicode)
    email = body['email']
    if email not in USER_DB:
        # Already singup
        return JsonResponse({'err':'USER NOT EXISTS'}, safe=False)
    jwtToken = jwt.encode({'email': email}, SECRET, algorithm='HS256')
    return JsonResponse({'jwt':jwtToken }, safe=False)

def signup(request):
    if request.method != "POST":
            return JsonResponse({})
   # body_unicode = request.body.decode('utf-8')
    body_unicode = request.body
    body = json.loads(body_unicode)
    email = body['email']
    if email in USER_DB:
        # Already singup
        return JsonResponse({'err':'USER ALREADY EXISTS'}, safe=False)
    # validate that email is valid address
    if not re.search(emailRegex,email):
        return JsonResponse({'err':'NOT A VALID EMAIL'}, safe=False)
    USER_DB[email] = True
    jwtToken = jwt.encode({'email': email}, SECRET, algorithm='HS256')
    return JsonResponse({'jwt':jwtToken }, safe=False)