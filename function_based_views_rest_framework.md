# Function-Based Views (FBVs) in Django REST Framework with `@api_view`

Django REST Framework (DRF) provides the `@api_view` decorator to transform function-based views (FBVs) into API views. 
This allows you to handle different HTTP methods in a simple, straightforward way without needing to use class-based views (CBVs).

Here's how you can handle common use cases—list, detail, create, update, and delete—using `@api_view`.

---

#### 1. **List View (GET Request)**

This view retrieves and displays a list of all objects.

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MyModel
from .serializers import MyModelSerializer

@api_view(['GET'])
def mymodel_list(request):
    queryset = MyModel.objects.all()
    serializer = MyModelSerializer(queryset, many=True)
    return Response(serializer.data)
```

- **Purpose**: Lists all objects from the database.
- **HTTP Method**: `GET`
- **Decorator**: `@api_view(['GET'])` restricts the view to handle only GET requests.

---

#### 2. **Detail View (GET Request with ID)**

This view retrieves a specific object based on its primary key (ID).

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import MyModel
from .serializers import MyModelSerializer

@api_view(['GET'])
def mymodel_detail(request, pk):
    obj = get_object_or_404(MyModel, pk=pk)
    serializer = MyModelSerializer(obj)
    return Response(serializer.data)
```

- **Purpose**: Retrieves details of a single object by its ID.
- **HTTP Method**: `GET`
- **Decorator**: `@api_view(['GET'])`

---

#### 3. **Create View (POST Request)**

This view allows for the creation of a new object in the database.

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import MyModel
from .serializers import MyModelSerializer

@api_view(['POST'])
def mymodel_create(request):
    serializer = MyModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

- **Purpose**: Creates a new object.
- **HTTP Method**: `POST`
- **Decorator**: `@api_view(['POST'])`

---

#### 4. **Update View (PUT Request)**

This view updates an existing object based on its ID.

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import MyModel
from .serializers import MyModelSerializer

@api_view(['PUT'])
def mymodel_update(request, pk):
    obj = get_object_or_404(MyModel, pk=pk)
    serializer = MyModelSerializer(obj, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

- **Purpose**: Updates an existing object.
- **HTTP Method**: `PUT`
- **Decorator**: `@api_view(['PUT'])`

---

#### 5. **Partial Update View (PATCH Request)**

This view allows for the partial update of an object.

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import MyModel
from .serializers import MyModelSerializer

@api_view(['PATCH'])
def mymodel_partial_update(request, pk):
    obj = get_object_or_404(MyModel, pk=pk)
    serializer = MyModelSerializer(obj, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

- **Purpose**: Partially updates fields of an existing object.
- **HTTP Method**: `PATCH`
- **Decorator**: `@api_view(['PATCH'])`

---

#### 6. **Delete View (DELETE Request)**

This view deletes an object based on its ID.

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import MyModel

@api_view(['DELETE'])
def mymodel_delete(request, pk):
    obj = get_object_or_404(MyModel, pk=pk)
    obj.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
```

- **Purpose**: Deletes an object.
- **HTTP Method**: `DELETE`
- **Decorator**: `@api_view(['DELETE'])`

---

### URLs Configuration

To make these views accessible through specific URLs, you need to define the URL patterns:

```python
from django.urls import path
from .views import mymodel_list, mymodel_detail, mymodel_create, mymodel_update, mymodel_delete

urlpatterns = [
    path('mymodels/', mymodel_list, name='mymodel-list'),
    path('mymodels/<int:pk>/', mymodel_detail, name='mymodel-detail'),
    path('mymodels/create/', mymodel_create, name='mymodel-create'),
    path('mymodels/<int:pk>/update/', mymodel_update, name='mymodel-update'),
    path('mymodels/<int:pk>/partial_update/', mymodel_partial_update, name='mymodel-partial-update'),
    path('mymodels/<int:pk>/delete/', mymodel_delete, name='mymodel-delete'),
]
```

---

### Summary of `@api_view` Use Cases:

- **List View** (`GET /mymodels/`): Retrieves all objects.
- **Detail View** (`GET /mymodels/<pk>/`): Retrieves a single object by its primary key.
- **Create View** (`POST /mymodels/create/`): Creates a new object.
- **Update View** (`PUT /mymodels/<pk>/update/`): Updates an object.
- **Partial Update View** (`PATCH /mymodels/<pk>/partial_update/`): Partially updates an object.
- **Delete View** (`DELETE /mymodels/<pk>/delete/`): Deletes an object.

Using `@api_view` is a straightforward way to handle different HTTP methods in function-based views. 
It’s ideal for small or simple APIs where you don’t need the flexibility of class-based views.
