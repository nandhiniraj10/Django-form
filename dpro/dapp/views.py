from django.shortcuts import render, redirect
from .forms import PersonForm

def create_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PersonForm()

    return render(request, 'create_person.html', {'form': form})

def success(request):
    return render(request, 'success.html')

# from django.shortcuts import render  
# from .forms import StudentForm  
  
# def index(request):  
#     student = StudentForm()  
#     return render(request,"index.html",{'form':student})  

# from django.contrib.auth.models import User
# from django.contrib.auth.tokens import default_token_generator
# from django.shortcuts import render
# from django.http import HttpResponse

# def generate_and_view_token(request, user_id):
#     try:
#         user = User.objects.get(pk=user_id)
#     except User.DoesNotExist:
#         return HttpResponse("User not found.")

#     # Generate a token (for example, a password reset token)
#     token = default_token_generator.make_token(user)

#     # Render the template with the user and token information
#     return render(request, 'view_token.html', {'user': user, 'token': token})

