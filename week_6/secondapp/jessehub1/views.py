import json
from django.http import JsonResponse


blogs = []


def get_blog(request):
    # Do something here
    return JsonResponse({"message": "Get request data,", "data": blogs})

def post_blog(request):
     if request.method == 'POST':
        incoming_data_from_client_application = request.body.decode()
        converting_to_dictionary_format = json.loads(incoming_data_from_client_application)
      
        blogs.append(converting_to_dictionary_format)
        return JsonResponse({"message": "Blog created successfully", "data": converting_to_dictionary_format})
     else:
        return JsonResponse({"message": "Invalid request method"})
     
def delete_blog(request, index):
    if request.method == 'DELETE':
        del blogs[index]
        return JsonResponse({"message": "Delete request successful"})
    else:
        return JsonResponse({"message": "The request is not a delete request"})