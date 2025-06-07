from django import template

register = template.Library();

@register.simple_tag
def get_links():
    return [{
        'name': 'Home',
        'href': '/',
        'icon': 'fa-house',
    }, {
        'name': 'Find your path',
        'href': '/skills',
        'icon': 'fa-brain',
    }, {
        'name': 'Buy now',
        'href': 'https://store.steampowered.com/app/632470/Disco_Elysium__The_Final_Cut/',
        'icon': 'fa-cart-shopping',
    }, {
        'name': 'Introduction',
        'href': '/about',
        'icon': 'fa-book',
    },{
        'name': 'Revachol Courier',
        'href': '/news/',
        'icon': 'fa-newspaper',
    },]
    