# fibonacci/views.py
from django.http import JsonResponse

def fibonacci(request):
    try:
        n = int(request.GET.get('n'))
        result = calculate_fibonacci(n)
        if result is None:
            return JsonResponse({'status': 400, 'message': 'Bad request.'}, status=400)
        else:
            return JsonResponse({'result': result}, status=200)
    except ValueError:
        return JsonResponse({'status': 400, 'message': 'Bad request.'}, status=400)

def calculate_fibonacci(n):
    if n <= 0:
        return None
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(3, n+1):
            a, b = b, a + b
        return b
