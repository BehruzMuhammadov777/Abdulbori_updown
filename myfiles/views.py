import datetime

from django.db.models import Q
from django.shortcuts import render
from myfiles.models import *
# Create your views here.

def index(malumot):
    if malumot.method =="POST":
        text = malumot.POST.get('matn')
        soz = str(text).strip()
        qidirish = Q(nomi__contains=soz) | Q(eski_narxi__contains=soz) | Q(yangi_narxi__contains=soz) | \
                   Q(manzil__contains=soz) | Q(xonalar__contains=soz) | Q(yuvinish_xonasi__contains=soz) | Q(maydon__contains=soz)

        servislar = Service.objects.filter(qidirish)
        d = Q(ismi__contains=soz) | Q(fami__contains=soz) | Q(lavozimi__contains=soz)
        agens = Agents.objects.filter(d)



        servislar = Service.objects.filter(qidirish)
        r = Q(ismi__contains=soz) | Q(fam__contains=soz) | Q(lavozimi__contains=soz) | Q(malumot__contains=soz)
        clients = Clients.objects.filter(r)

        servislar = Service.objects.filter(qidirish)
        f = Q(nomi__contains=soz) | Q(maydoni__contains=soz) | Q(malumot__contains=soz)
        blogs = Blogs.objects.filter(f)
        content = {
            "service": servislar,
            "agen": agens,
            "client": clients,
            "blog": blogs
        }
        return render(malumot, 'index.html', content, )

    else:

        servislar = Service.objects.all().order_by('-vaqt')[:3]
        agens = Agents.objects.all().order_by('-lavozimi')[:3]
        clients = Clients.objects.all().order_by('-id')[:3]
        blogs = Blogs.objects.all().order_by('-vaqt')[:3]
        content = {
            "service":servislar,
            "agen":agens,
            "client":clients,
            "blog":blogs
        }
        return render(malumot, 'index.html', content,)



def agent(malumot):
    if malumot.method =="POST":
        text = malumot.POST.get('matn')
        soz = str(text).strip()
        v = Q(ismi__contains=soz) | Q(fami__contains=soz) | Q(lavozimi__contains=soz)
        hodim = Agents.objects.filter(v)
        hodm = {
            "agentlar":hodim
        }
        return render(malumot, 'agent.html', hodm)

    else:
        hodim = Agents.objects.all()
        hodm = {
            "agentlar": hodim
        }
        return render(malumot, 'agent.html', hodm)


def contact(malumot):
    if malumot.method == "POST":
        ism = malumot.POST.get('ism')
        gmail = malumot.POST.get('adres')
        informatsiya = malumot.POST.get('malumot')
        xabar = malumot.POST.get('messege')
        vaqt = datetime.datetime.now()
        Murojat(name=ism, mail=gmail, subject=informatsiya, messege=xabar, vaqt=vaqt).save()
    return render(malumot, 'contact.html')


def properties(malumot):
    if malumot.method =="POST":
        text = malumot.POST.get('matn')
        soz = str(text).strip()
        d = Q(nomi__contains=soz) | Q(eski_narxi__contains=soz) | Q(yangi_narxi__contains=soz) | \
                   Q(manzil__contains=soz) | Q(xonalar__contains=soz) | Q(yuvinish_xonasi__contains=soz) | Q(maydon__contains=soz)
        narsa = Service.objects.filter(d)
        nusxa = {
            "ishlarimiz":narsa
        }
        return render(malumot, 'properties.html', nusxa)

    else:
        narsa = Service.objects.all()
        nusxa = {
            "ishlarimiz": narsa
        }
        return render(malumot, 'properties.html', nusxa)
