from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import User,wareHouse,SessionAudit
from django.template import loader
from .forms import MySearch,ProxyForm,DocumentForm
from django.http import HttpResponseRedirect





def index(request):
    try:
        all_users  = User.objects.all()
        template =  loader.get_template('RBAC_app/index.html')
        context = {
            'all_users' :all_users,
        }
    except:
        #raise Http404("nothing exist")
        template =  loader.get_template('RBAC_app/error.html')
    return HttpResponse(template.render(context,request))
        

def userEntry(request, username):
    context={}
    try:
        username = User.objects.get(username = username)
        
        template =  loader.get_template('RBAC_app/userEntry.html')
        context = {
            'username' : username,
        }
    except:
        #raise Http404("nothing exist")
        template =  loader.get_template('RBAC_app/error.html')
   
    return HttpResponse(template.render(context,request))
    #return HttpResponse("<h1> This is the Users page "+str(username.username)+" </h1>")

def is_valid(user,param):
    if param!='' and param is not None:
        
        sessionAuditNew = SessionAudit.objects.create(username = user,keywordsAudit=param)
        print('username : '+sessionAuditNew.username)
        print('keyword : '+sessionAuditNew.keywordsAudit)
    
        sessionAuditNew.save()
        
        return True
    return False

def makeQuery(queryset,param,Filter):
    if param == 'claims':
        queryset = queryset.filter(claims__icontains = Filter)
    
    elif param == 'description':
        queryset = queryset.filter(description__icontains = Filter)
    
    elif param =='assigne':
        queryset = queryset.filter(assigne__icontains = Filter)
    
    else:
        queryset=wareHouse.objects.all()
    
    return queryset

def userID(request,username):
    
    print(request.method)
    username = User.objects.get(username = username)
    print(username.username)
    context = {'username':username.username}

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        print('form creations')
        form = MySearch(request.POST)
        
        context={'form' : form,
                }
        
        # check whether it's valid:

        if form.is_valid():
            #newqueryset =  wareHouse.objects.all()
            print('valid form')
            claims = form['claims'].value()
            description= form['description'].value()
            assigne= form['assigne'].value()



            queryset=makeQuery('','','')
            
            if is_valid(username.username,claims):
                
                print('claims '+form['claims'].value())
                queryset=makeQuery(queryset,'claims',claims)
                
                context['queryset'] = queryset


            if is_valid(username.username,description):
                print('description '+form['description'].value())
                queryset=makeQuery(queryset,'description',description)
                context['queryset'] = queryset


            if is_valid(username.username,assigne):
                
                print('assigne '+form['assigne'].value())
                queryset=makeQuery(queryset,'assigne',assigne)

                context['queryset'] = queryset
            
                
            #print('orderByDate '+form['Order_By_Date'].value())
            if form['Order_By_Date'].value()==2:
                queryset=queryset.order_by('-addDate')
                context['queryset'] = queryset
                print('2')
            else:
                queryset=queryset.order_by('addDate')
                context['queryset'] = queryset


            return render(request, 'RBAC_app/resources.html', context)
                    # if a GET (or any other method) we'll create a blank form
    
    else:
        form = MySearch()
        #proxyForm = ProxyForm()
    
                
    return render(request, 'RBAC_app/resources.html', {'form' : form,'username' : username.username})

def proximitySearch(request,username):
    print(request.method)
    username = User.objects.get(username = username)
    print(username.username)
    if request.method == 'POST':
        form = ProxyForm(request.POST)
          
        if form.is_valid():
            print('valid form Proxy')
            Proximity_String= form['Proximity_String'].value()
            Proximity_Range = form['Proximity_Range'].value()
            queryset=makeQuery('','','')
            context={'form' : form,
            'username':username.username
                    }
            if is_valid(username.username,Proximity_String) and is_valid(username.username,Proximity_Range):
                print('Everything is valid')
                #queryset = queryset.Proximity(Proximity_String,Proximity_Range)
                context['queryset'] = queryset

            else:
                print('invalid')
    
        
    else:
        form = ProxyForm()
        context={'form' : form,
        'username':username.username
                }
    return render(request, 'RBAC_app/proxyResult.html', context)


def model_form_upload(request,username):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'RBAC_app/model_form_upload.html',
            {'form' : form,'username':username})
    else:
        form = DocumentForm()
    return render(request, 'RBAC_app/model_form_upload.html', {
        'form': form,'username':username
    })

    
    