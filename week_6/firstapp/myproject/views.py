import json
from django.http import JsonResponse

store = []



def sayHello(request):
    # Do something here
    return JsonResponse({"message": "Hello, I am your backend application"})
    
    
def get_todos(request):
    # Do something here
    return JsonResponse({"message": "Get me,", "data": store})

def clubNames(request):
    # Do something here
    return JsonResponse({"message": "Premier league,", "club names": store})

def post_todo(request):
    if request.method == 'POST':
        incoming_data_from_client_application = request.body.decode()
        converting_to_dictionary_format = json.loads(incoming_data_from_client_application)

        # title = request.POST.get('title')
        # description = request.POST.get('description')

        # store data
        store.append(converting_to_dictionary_format)
        return JsonResponse({"message": "Post Request,"})
    else:
        return JsonResponse({"message": "The request is not a post request."})




def update_todo(request, index):
    if request.method == 'PUT':
        incoming_data_from_client_application = request.body.decode()
        converting_to_dictionary_format = json.loads(incoming_data_from_client_application)

        if index not in store:
            return JsonResponse({"message": "No such data exist in store."})

        store[index] = converting_to_dictionary_format

        return JsonResponse({"message": "Put request successful"})
    else:
        return JsonResponse({"message": "The request is not a put request."})
    

def delete_todo(request, index):
    if request.method == 'DELETE':
        del store[index]
        return JsonResponse({"message": "Delete request successful"})
    else:
        return JsonResponse({"message": "The request is not a delete request."})
    
    