from django.shortcuts import render,redirect
from hospitalapp.models import Member,Message,users,ImageModel
from hospitalapp.forms import ImageUploadForm
def index(request):
  if request.method == 'POST':
      messages =Message(name=request.POST['name'],
                       email=request.POST['email'],
                       subject=request.POST['subject'],
                       message=request.POST['message'],)
      messages.save()
      return redirect('/')
  else:
      return render(request,'index.html'),

def index(request):
  if request.method == 'POST':
      Users =users (name=request.POST['Users'],
                    fulllname=request.POST['Fullname'],
                    username=request.POST['Username'],
                    email=request.POST['Email Address'],
                    password=request.POST['Password'],
                   age =request.POST['Age'],
                   yearofbirth=request.POST['Year of Birth'],

      )
      Users.save()

      return redirect('/')
  else:
      return render(request,'index.html')




def innerpage(request):
    return render(request,'inner-page.html')

def register(request):
    if request.method == 'POST':
# Create your views here.
        member = Member(username=request.POST['username'],
                        email=request.POST['email'],
                        password=request.POST['password'])
        member.save()
        return redirect('/login')

    else:
        return render(request,'register.html')


def login(request):
    return render(request,'login.html')

def upload(request):
    return render(request,'upload.html')

def Details(request):
    Details=Message.objects.all()
    return render(request,'Details.html',{'Details':Details})

def Details(request):
    Users=users.objects.all()
    return render(request,'Details.html',{'Users':Users})


def adminhome(request):
    if request.method=='POST':
        if Member.objects.filter(username=request.POST['username'],password=request.POST['password']).exists():
            member=Member.objects.get(username=request.POST['username'],
                                      password=request.POST['password'])
            return render(request,'adminhome.html',{'member':member})
        else:
            return render(request,'login.html')
    else:

        return render(request, 'login.html')


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'Upload.html', {'form': form})


def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'showimages.html', {'images': images})


def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/showimage')