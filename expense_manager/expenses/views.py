from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Sum
from .models import User, Expense
from .serializers import UserSerializer, ExpenseSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    @action(detail=False, methods=['get'])
    def list_by_date_range(self, request):
        user_id = request.query_params.get('user_id')
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        expenses = Expense.objects.filter(
            user_id=user_id,
            date__range=[start_date, end_date]
        )
        serializer = self.get_serializer(expenses, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def category_summary(self, request):
        user_id = request.query_params.get('user_id')
        month = request.query_params.get('month')

        expenses = Expense.objects.filter(
            user_id=user_id,
            date__month=month
        ).values('category').annotate(total=Sum('amount'))

        return Response(expenses)
