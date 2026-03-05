from rest_framework import viewsets
from .models import Team, User, Activity, Workout, Leaderboard
from .serializers import TeamSerializer, UserSerializer, ActivitySerializer, WorkoutSerializer, LeaderboardSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

@api_view(['GET'])
def api_root(request):
    return Response({
        'teams': '/teams/',
        'users': '/users/',
        'activities': '/activities/',
        'workouts': '/workouts/',
        'leaderboard': '/leaderboard/',
    })
