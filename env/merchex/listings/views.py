from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from listings.models import Band
from listings.forms import ContactUsForm, BandForm
from django.shortcuts import redirect

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', {'bands': bands})

def about(request):
    return render(request,
                  'listings/about.html')
    #return HttpResponse('<h1>A propos</h1> <p>Nous sommes sur une nouvelle page !</p>')

def band_list(request):  # renommer la fonction de vue
   bands = Band.objects.all()
   return render(request,
           'listings/band_list.html',  # pointe vers le nouveau nom de modèle
           {'bands': bands})

def band_detail(request, id):
    #L'id commence à 4 et termine à 7
  band = Band.objects.get(id=id)  # nous insérons cette ligne pour obtenir le Band avec cet id
  return render(request,
          'listings/band_detail.html',
          {'band': band}) # nous mettons à jour cette ligne pour passer le groupe au gabarit

def contact(request):
    if request.method == 'POST':
        #Création d'une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us from',
                      message=form.cleaned_data['message'],
                      from_email=form.cleaned_data['email'],
                      recipient_list=['admin@merchex.xyz'])
        return redirect('email-sent')
            #Si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
            #Ci-dessous et afficher à nouveau formulaire (avec des erreurs).
    else:
        #Requete GET, création d'un formulaire vide
        form = ContactUsForm()
    return render(request,
          'listings/contact.html',
          {'form': form})  # passe ce formulaire au gabarit

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # Créer une nouvelle "Band" et la sauvegarder dans la db
            band = form.save()
            # Redirige vers la page de détail du groupe que nous venos de créer
            # Nous pouvons fournir les arguments du motif URL comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)
    else:
        form = BandForm()
    return render(request,
                  'listings/band_create.html',
                  {'form': form})

def band_update(request, id):
    band = Band.objects.get(id=id)
    form = BandForm(instance=band) #On pré remplie le formulaire avec un groupe existant
    return render(request,
                  'listings/band_update.html',
                  {'form': form})