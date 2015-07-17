# __author__ = 'sree'
import urllib2
from lxml import html
import requests

def get_page_tree(url=None):
    page = requests.get(url=url, verify=False)
    return html.fromstring(page.text)

def get_title(url=None):
    tree = get_page_tree(url=url)
    return tree.xpath('//title//text()')[0].strip()

def find_other_news_sources(url=None, title=None):
    # Google forwards the url using <google_domain>/url?q=<actual_link>. This might change over time
    forwarding_identifier = '/url?q='
    if not title:
        title = get_title(url=url)
    google_news_search_url = 'http://www.google.com/search?q=' + urllib2.quote(title) + '&tbm=nws'
    google_news_search_tree = get_page_tree(url=google_news_search_url)
    other_news_sources_links = [a_link.replace(forwarding_identifier, '') for a_link in
                                google_news_search_tree.xpath('//a//@href') if forwarding_identifier in a_link]
    return other_news_sources_links
