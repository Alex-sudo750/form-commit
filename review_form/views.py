from .forms import FormReviewForm
import requests
import json
from django.shortcuts import render
import pymysql
from .config import DB_NAME,USER, PASSWORD, HOST

#
# try:
#     connection = pymysql.connect(
#         host=HOST,
#         port=3306,
#         user=USER,
#         password=PASSWORD,
#         database=DB_NAME,
#         cursorclass=pymysql.cursors.DictCursor)
#
#     print("Succesful connected....")
#     try:
#         with connection.cursor() as cursor:
#             select_all_column = f'SELECT docId_user FROM drive.review_form_reviewform WHERE docId_user={inf}'
#             cursor.execute(select_all_column)
#             column = cursor.fetchall()
#             for columns in column:
#                 doc_id = (columns["docId_user"])
#                 print(doc_id)
#             print("#" * 20)
#     finally:
#         connection.close()
# except Exception as ex:
#     print("Connction refused..")
#     print(ex)


def showform(request):
    form = FormReviewForm(request.POST or None)
    info = request.GET.get("docId")
    all_info = get_json(token=get_token(), id_Dock=info)
    dictData = json.dumps(all_info)
    data = json.loads(dictData)
    docId_user = (data["docId"])
    docType_user = (data["docType"]["value"])
    docOper_user = (data["docOper"]["value"])
    department_user = (data["department"]["value"])
    lastUpdateDate_user = (data["lastUpdateDate"])
    region = (department_user.split('МВС')[1])
    department_output = ''
    for c in department_user:
        if c not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            department_output = department_output + c

    nnn = int(''.join(filter(str.isdigit, department_user)))

    if form.is_valid():
        form.save()
    else:
        print("Error")


    return render(request, 'contactform.html',{'form': form, 'currentUrl': info,
                                               'doc_Id': docId_user, 'docType': docType_user, 'docOper': docOper_user, 'lastUpdateDate': lastUpdateDate_user,
                                               'department': department_output, 'region': region, 'nnn': nnn,
                                               })

def get_token():
    data = {'grant_type': 'password',
            'username': 'internal',
            'password': 'internal'}

    client_id = 'inter_id'
    client_secret = 'inter_sec'

    token = requests.post('http://mainapi.hsc.gov.ua/auth-server/oauth/token', data=data,
                              auth=(client_id, client_secret)).json()
    # headers = {'Authorization': 'Bearer ' + token['access_token'],
    #            'Content-Type': 'application/json'}
    # #equest.session['main_api_token'] = headers
    return 'Bearer ' + token['access_token']


def get_json(token, id_Dock):
    headers = {"Authorization": token}
    res = requests.get(url=f'http://mainapi.hsc.gov.ua/oper-service/opers/{id_Dock}', headers=headers).json()
    return res


