from django.shortcuts import render, render_to_response, RequestContext, HttpResponsePermanentRedirect
from django.contrib import messages
# from django.core.mail import send_mail
from haystack.views import SearchView
from django.conf import settings

from .forms import ContactForm

from itertools import chain

#===== Kreyol Pages ========#

def akey(request):

     return render_to_response("kr/akey.html",
                              locals(),
                              context_instance=RequestContext(request))


def ekip(request): #=====Paj Ekip la =======#

    return render_to_response("kr/ekip.html",
                              locals(),
                              context_instance=RequestContext(request))


def pwoje(request):

     return render_to_response("kr/pwoje.html",
                              locals(),
                              context_instance=RequestContext(request))


def kontak(request):

    form = ContactForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.success(request, 'Thank you for Joining')
        return HttpResponsePermanentRedirect('../')

    return render_to_response("kr/kontak.html",
                              locals(),
                              context_instance=RequestContext(request))


#===== English Pages ========#

def home(request):

     return render_to_response("en/kokray.html",
                              locals(),
                              context_instance=RequestContext(request))


def team(request): #=====Paj Ekip la =======#

    return render_to_response("en/team.html",
                              locals(),
                              context_instance=RequestContext(request))


def project(request):

     return render_to_response("en/project.html",
                              locals(),
                              context_instance=RequestContext(request))


def contact(request):

    form = ContactForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.success(request, 'Thank you for Joining')
        return HttpResponsePermanentRedirect('/thank-you/')


    return render_to_response("en/contact.html",
                              locals(),
                              context_instance=RequestContext(request))



def thankyou(request):

    return render_to_response("en/thankyou.html",
                              locals(),
                              context_instance=RequestContext(request))


#===== Search ========#

class MultilineSearchView(SearchView):
    def find_highlightable_words(self, text):
        # Use a set so we only do this once per unique word.
        word_positions = {}

        # Pre-compute the length.
        end_offset = len(text)
        lower_text_block = text.lower()

        for word in self.get_query().split(' '):
            if word.startswith('-'):
                continue
            if not word in word_positions:
                word_positions[word] = []

            start_offset = 0

            while start_offset < end_offset:
                next_offset = lower_text_block.find(word, start_offset, end_offset)

                # If we get a -1 out of find, it wasn't found. Bomb out and
                # start the next word.
                if next_offset == -1:
                    break

                word_positions[word].append(next_offset)
                start_offset = next_offset + len(word)

        return word_positions
        
    def get_parts(self, text):
        # Invert highlight_locations to a location -> term list
        highlight_locations = self.find_highlightable_words(text)

        term_list = []

        for term, locations in highlight_locations.items():
            term_list += [(loc, term) for loc in locations]

        loc_to_term = sorted(term_list)

        WORDS_AROUND = settings.HAYSTACK_WORDS_AROUND

        for cur, cur_str in loc_to_term:
            
            # This can be in a different case than cur_str
            actual_term = text[cur:cur + len(cur_str)]

            # Handle incorrect highlight_locations by first checking for the term
            if actual_term.lower() == cur_str:
                yield (
                        u' '.join(text[:cur].split()[-WORDS_AROUND:]),
                        actual_term,
                        u' '.join(text[cur:].split()[1:WORDS_AROUND+1]),
                        )

    def extra_context(self):
        return {'num_hits': self.num_hits}

    def get_results(self):
        results = super(MultilineSearchView, self).get_results()
        show_results = []
        for r in results:
            for parts in self.get_parts(r.text):
                show_results.append({'result': r, 'parts': parts})
        self.num_hits = len(show_results)
        return show_results
    
