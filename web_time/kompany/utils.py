from .models import Contact, Brend, Network

# постоянные данные
def get_constanta():
    contact = Contact.objects.all()
    brends = Brend.objects.all()
    upNetwork = Network.objects.all()

    return {
        'contact': contact,
        'brends': brends,
        'upNetwork': upNetwork,
        }