from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Room
from .serializer import RoomSerialzer


@api_view(['GET'])
def endpoints(request):
    url_list = ['api/rooms']
    return Response(url_list)


@api_view(['GET', 'POST'])
def room_list(request):
    if request.method == 'GET':
        rooms = Room.objects.all()
        serialzer = RoomSerialzer(rooms, many=True)
        return Response(serialzer.data)

    if request.method == 'POST':
        code = request.data['code']
        host = request.data['host']
        guest_can_pause = request.data['guest_can_pause']
        votes_to_skip = request.data['votes_to_skip']

        Room.objects.create(
            code=code,
            host=host,
            guest_can_pause=guest_can_pause,
            votes_to_skip=votes_to_skip
        )

        return redirect('room-list')
