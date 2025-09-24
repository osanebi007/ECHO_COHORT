import json
from django.http import JsonResponse
from .models import Todo

store = []

# Create your views here.
def get_store(request):
    return JsonResponse({"message": "Get request successful", "data": []})    



def get_todos(request):
    # Do something here
    todos = Todo.objects.all().values()  # Fetch all Todo objects from the database
    return JsonResponse({"message": "Get me,", "data": list(todos)})

def clubNames(request):
    # Do something here
    return JsonResponse({"message": "Premier league,", "club names": store})

def post_todo(request):
    if request.method == 'POST':
        incoming_data_from_client_application = request.body.decode()
        converting_to_dictionary_format = json.loads(incoming_data_from_client_application)

        title = converting_to_dictionary_format.get('title')
        description = converting_to_dictionary_format.get('description')

        # store data
        todo = Todo.objects.create(
            title = converting_to_dictionary_format["title"],
            description = converting_to_dictionary_format["description"]

            
        )

        todo.save()
        # store.append(converting_to_dictionary_format)
        return JsonResponse({"message": "Post Request,"})
    else:
        return JsonResponse({"message": "The request is not a post request."})


# Todo functions

def update_todo(request, index):
    if request.method == 'PUT':
        incoming_data_from_client_application = request.body.decode()
        converting_to_dictionary_format = json.loads(incoming_data_from_client_application)

        try:
            todo = Todo.objects.get(id=index)
        except Todo.DoesNotExist:
            return JsonResponse({"message": "The requested data does not exist."})
        
        todo.title = converting_to_dictionary_format["title"]
        todo.description = converting_to_dictionary_format["description"]
        todo.save()
        

        if index not in store:
            return JsonResponse({"message": "No such data exist in store."})

        store[index] = converting_to_dictionary_format

        return JsonResponse({"message": "Put request successful"})
    else:
        return JsonResponse({"message": "The request is not a put request."})

def patch_todo(request, index):
    if request.method == 'PATCH':
        incoming_data_from_client_application = request.body.decode()
        converting_to_dictionary_format = json.loads(incoming_data_from_client_application)

        try:
            todo = Todo.objects.get(id=index)
        except Todo.DoesNotExist:
            return JsonResponse({"message": "The requested data does not exist."})
        
        todo.title = converting_to_dictionary_format.get("title", todo.title)
        todo.description = converting_to_dictionary_format.get("description", todo.description)
        todo.save()
        

        if index not in store:
            return JsonResponse({"message": "No such data exist in store."})

        store[index] = converting_to_dictionary_format

        return JsonResponse({"message": "Patch request successful"})
    else:
        return JsonResponse({"message": "The request is not a patch request."})

def delete_todo(request, index):
    if request.method == 'DELETE':
        try:
            todo = Todo.objects.get(id=index)
            todo.delete()
        except Todo.DoesNotExist:
            return JsonResponse({"message": "The requested data does not exist."})
        
        todo.delete()

        del store[index]
        return JsonResponse({"message": "Delete request successful"})
    else:
        return JsonResponse({"message": "The request is not a delete request."})
    
  

    
