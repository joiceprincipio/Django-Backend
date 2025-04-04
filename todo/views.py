from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import TaskSerializers

@api_view(['GET', 'POST'])
def todos(request):
    if request.method == 'GET':
        tasks = Todo.objects.all()
        serializer = TaskSerializers(tasks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TaskSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['PUT', 'DELETE'])
def update(request, pk):
    try:
        task = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response(status=404)

    if request.method == 'PUT':
        serializer = TaskSerializers(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=204)