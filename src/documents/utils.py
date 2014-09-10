from haystack.utils import Highlighter
from django.utils.html import strip_tags
from django.conf import settings


class MultilineHighlighter(Highlighter):
    '''Custom highligher for multi-line results'''

    def highlight(self, text_block):
        self.text_block = strip_tags(text_block)
        highlight_locations = self.find_highlightable_words()
        return self.render_html(highlight_locations)


    def render_html(self, highlight_locations):
        '''Basically rewriten Highlighter.render_html with some changes'''
        # Start by chopping the block down to the proper window.
        text = self.text_block

        # Invert highlight_locations to a location -> term list
        term_list = []

        for term, locations in highlight_locations.items():
            term_list += [(loc - start_offset, term) for loc in locations]

        loc_to_term = sorted(term_list)

        # Prepare the highlight template
        if self.css_class:
            hl_start = '<%s class="%s">' % (self.html_tag, self.css_class)
        else:
            hl_start = '<%s>' % (self.html_tag)

        hl_end = '</%s>' % self.html_tag

        # Copy the part from the start of the string to the first match,
        # and there replace the match with a highlighted version.
        highlighted_result = ''
        matched_so_far = 0
        padding = settings.HAYSTACK_HIGHLIGHTED_SYMBOLS

        for cur, cur_str in loc_to_term:
            
            # This can be in a different case than cur_str
            actual_term = text[cur:cur + len(cur_str)]

            # Handle incorrect highlight_locations by first checking for the term
            if actual_term.lower() == cur_str:
                symbols_start = cur - padding
                if symbols_start < 0:
                    symbols_start = 0
                after_term_idx = cur + len(actual_term)
                highlighted_result += ('<div>' + text[symbols_start:cur] +
                        hl_start + actual_term + hl_end +
                        text[after_term_idx:after_term_idx + padding] +
                        '</div>')
                # Keep track of how far we've copied so far, for the last step
                matched_so_far = cur + len(actual_term)

        # Don't forget the chunk after the last term

        if start_offset > 0:
            highlighted_result = '...%s...' % highlighted_result

        return highlighted_result
