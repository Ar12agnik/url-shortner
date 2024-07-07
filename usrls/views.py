from django.shortcuts import render,redirect
from .models import url_hash
import shortner

# Create your views here.
def index(request,*args, **kwargs):
    
    return render(request,'index.html',context=kwargs)
def shoten(request):
    lower=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upper=[x.upper() for x in lower ]
    digits=[x for x in range(10)]
    url=request.POST.get("url")
    hash=shortner.choose_random(lower,upper,digits)
    url_obj=url_hash.objects.create(original_url=url,hash=hash)
    url_obj.save()
    unique_id=f"{hash}+{url_obj.id}"
    base_address = f"{request.scheme}://{request.get_host()}"
    full_address=f"{base_address}/{unique_id}"
    return index(request,unique=full_address)
def visit(request,url):
    base_address = f"{request.scheme}://{request.get_host()}"
    new_url=url.replace(base_address,'')
    oid=new_url.split("+")
    id=oid[1]
    hash=oid[0]
    try:
        url_object=url_hash.objects.get(id=id,hash=hash)
        if url_object:
            original_url=url_object.original_url
            return redirect(original_url)
        else:
            return index(request,error="invalid url")
    except:
        return index(request,error="invalid url")
    
