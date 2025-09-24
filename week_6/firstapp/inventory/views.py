import json
from django.http import JsonResponse
from .models import Product

store = []
# Create your views here.


def get_product(request):
    # Fetch all Product objects from the database
    product = Product.objects.all().values()  
    return JsonResponse({"message": "Get products successful", "data": list(product)})

def post_product(request):
    if request.method == 'POST':
        incoming_data_from_client_application = request.body.decode()
        converting_to_dictionary_format = json.loads(incoming_data_from_client_application)  

         
      
        # store data
        product = Product.objects.create(
            name = converting_to_dictionary_format['name'],
            description = converting_to_dictionary_format['description'],   
            price = converting_to_dictionary_format['price'],
            quantity = converting_to_dictionary_format['quantity']
        )       
        # store.append(converting_to_dictionary_format)
        return JsonResponse({"message": "Post Request successful"})
    else:
        return JsonResponse({"message": "The request is not a post request."})


# Todo functions

def update_product(request, index):
    if request.method == 'PUT':
        incoming_data_from_client_application = request.body.decode()
        converting_to_dictionary_format = json.loads(incoming_data_from_client_application)

        try:
            product = Product.objects.get(id=index)
        except Product.DoesNotExist:
            return JsonResponse({"message": "The requested product does not exist."})
        
        product.name = converting_to_dictionary_format["name"]
        product.description = converting_to_dictionary_format["description"]
        product.price = converting_to_dictionary_format["price"]
        product.quantity = converting_to_dictionary_format["quantity"]
        product.save()
        

        # if id not in store:
        #     return JsonResponse({"message": "Such product does not exist in store."})

        # store[id] = converting_to_dictionary_format

        return JsonResponse({"message": "Put request successful"})
    else:
        return JsonResponse({"message": "The request is not a product request."})



def patch_product(request, index):
    if request.method == 'PATCH':
        incoming_data_from_client_application = request.body.decode()
        converting_to_dictionary_format = json.loads(incoming_data_from_client_application)

        try:
            product = Product.objects.get(id=index)
        except Product.DoesNotExist:
            return JsonResponse({"message": "The requested product does not exist."})
        

        print(converting_to_dictionary_format.get("price"))

         # Update only the fields provided in the request
        
        product.name = converting_to_dictionary_format.get("name", product.name)
        product.description = converting_to_dictionary_format.get("description", product.description)
        product.price = converting_to_dictionary_format.get("price", product.price)
        product.quantity = converting_to_dictionary_format.get("quantity", product.quantity)
        product.save()
    

        return JsonResponse({"message": "Patch request successful"})
    else:
        return JsonResponse({"message": "The request is not a patch request."})

def delete_product(request, index):
    if request.method == 'DELETE':
        try:
            product = Product.objects.get(id=index)
            product.delete()
        except Product.DoesNotExist:
            return JsonResponse({"message": "The requested product does not exist."})
        
        product.delete()

        del store[index]
        return JsonResponse({"message": "Delete request successful"})
    else:
        return JsonResponse({"message": "The request is not a delete request."})
    
  

    
