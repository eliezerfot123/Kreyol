from django.shortcuts import render, render_to_response, RequestContext, HttpResponsePermanentRedirect
from django.contrib import messages
# from django.core.mail import send_mail


from .forms import ContactForm

# Create your views here.

def home(request):

     return render_to_response("kokray.html",
                              locals(),
                              context_instance=RequestContext(request))


def about(request):

     return render_to_response("about.html",
                              locals(),
                              context_instance=RequestContext(request))


def contact(request):

    form = ContactForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.success(request, 'Thank you for Joining')
        return HttpResponsePermanentRedirect('/thank-you/')


    return render_to_response("contact.html",
                              locals(),
                              context_instance=RequestContext(request))

def corpus(request):

    #========== Search Extention goes here ===========#

    return render_to_response("corpus.html",
                              locals(),
                              context_instance=RequestContext(request))


def thankyou(request):

    return render_to_response("thankyou.html",
                              locals(),
                              context_instance=RequestContext(request))