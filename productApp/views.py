from django.shortcuts import render

# Create your views here.

def homeView(request):
    firstname = 'Damilare'
    isAdmin = False
    
    contacts = [
        {
            "name": 'Jerry',
            'course': "Data Science",
            'bio': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Inventore amet corrupti ab odio, iusto unde magni cupiditate est ipsum beatae aut vel necessitatibus temporibus porro voluptate dolore similique adipisci suscipit!',
            'amount': 2000000,
            "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_t.png"
        },
        {
            "name": 'Jb',
            'course': "Data Science",
            'bio': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Inventore amet corrupti ab odio, iusto unde magni cupiditate est ipsum beatae aut vel necessitatibus temporibus porro voluptate dolore similique adipisci suscipit!',
            'amount': 2000000,
            "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_t.png"
        },
        {
            "name": 'Akin',
            'course': "Data Science",
            'bio': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Inventore amet corrupti ab odio, iusto unde magni cupiditate est ipsum beatae aut vel necessitatibus temporibus porro voluptate dolore similique adipisci suscipit!',
            'amount': 2000000,
            "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_t.png"
        },
    ]

    
    return render(
        request, 
        template_name='index.html', 
        context={
            'firstname':firstname, 
            "contacts":contacts,
            'isAdmin': isAdmin
        }
    )


def pricingView(request):
    
    return render(request, template_name='pricing.html')

