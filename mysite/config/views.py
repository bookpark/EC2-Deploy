from django.http import HttpResponse


def index(request):
    return HttpResponse('<html>'
                        '<body>'
                        '<img src="/media/joy6.jpg" width=100%)'
                        '</body>'
                        '</html>'
                        )
