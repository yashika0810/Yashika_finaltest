from django.shortcuts import render,redirect
from .forms import Userproform
from .models import fullname
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import fullnameSerializer

# Create your views here.
def userpro(request):
    temp_name = fullname.objects.latest('id')
    return render(request, 'user.html',{'use':temp_name})


def userprofile(request,id):
    user_objects=fullname.objects.get(id=id)
    return render(request, 'user.html',{'user':user_objects})

def create(request):
    if request.method == "POST":
        form = Userproform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('index')
            except:
                pass
    else:
        form = Userproform()
    return render(request,'edit.html',{'form':form})




class view_data(APIView):
    def get(self,request):
        values=fullname.objects.all()
        Serializer=fullnameSerializer(values,many=True)
        return Response(Serializer.data)
        
