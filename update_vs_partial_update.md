# Update vs Partial Update

In Django REST Framework (DRF), **partial update** and **update** are used 
to modify existing records through serializers, but they function slightly differently:

### 1. **Update (PUT Request)**:
- **Full Update**: Involves replacing the entire resource with the new data. If any fields are omitted, they will be set to `null` or their default values, essentially meaning that all fields must be provided during the update.
- **Usage**: When you send a `PUT` request to the server, you need to include all fields (even if some fields have not changed).
- **Example**:
  ```python
  # views.py
  def update(self, request, *args, **kwargs):
      instance = self.get_object()
      serializer = MySerializer(instance, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  ```

### 2. **Partial Update (PATCH Request)**:
- **Partial Update**: Only modifies the fields that are explicitly provided in the request data. If some fields are omitted, they remain unchanged.
- **Usage**: When you send a `PATCH` request, you only need to include the fields that you want to modify.
- **Example**:
  ```python
  # views.py
  def partial_update(self, request, *args, **kwargs):
      instance = self.get_object()
      serializer = MySerializer(instance, data=request.data, partial=True)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  ```

### Key Differences:
- **PUT (Update)**:
  - Requires the full payload of the object to be passed.
  - Omitted fields will be reset or defaulted.
  - Used when you want to completely replace an object.

- **PATCH (Partial Update)**:
  - Only requires the fields that need to be updated.
  - Omitted fields remain unchanged.
  - Used when you want to modify parts of an object.

### Example in Usage:
Given a `User` model with `name`, `email`, and `age` fields:

- **PUT request**:
  ```json
  {
      "name": "John Doe",
      "email": "john@example.com",
      "age": 25
  }
  ```
  If you omit `age`, it will be reset (e.g., to `null` or the default value).

- **PATCH request**:
  ```json
  {
      "email": "john.new@example.com"
  }
  ```
  Only the `email` field will be updated; `name` and `age` will remain unchanged.

### Conclusion:
- Use **PUT** for full updates when you want to replace an entire resource.
- Use **PATCH** for partial updates when you only want to update certain fields without affecting others.
