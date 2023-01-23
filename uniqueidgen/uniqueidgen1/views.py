from django.shortcuts import render

from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
import uuid
def generate_unique_number():
    unique_id = uuid.uuid4()
    unique_number = "RES" + str(unique_id)
    return unique_number


class UserRegistrationView(View):
    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.unique_number = generate_unique_number()
            user.save()
            return render(request, 'registration_success.html', {'unique_number': user.unique_number})
        else:
            return render(request, 'registration.html', {'form': form})
