from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer

@api_view(['GET', 'POST', 'PATCH'])
def profile_create_or_update(request):
    if request.method == 'GET':
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    if request.method == 'PATCH':
        try:
            profile = Profile.objects.get(pk=request.data['id'])
        except Profile.DoesNotExist:
            return Response({'message': 'Profile not found'}, status=404)
        
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

