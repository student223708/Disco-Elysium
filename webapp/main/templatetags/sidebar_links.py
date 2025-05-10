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
        'name': 'Contact',
        'href': '/contact',
        'icon': 'fa-paper-plane',
    }, {
        'name': 'About',
        'href': '/about',
        'icon': 'fa-address-card',
    },{
        'name': 'Revachol Courier',
        'href': '/news/',
        'icon': 'fa-newspaper',
    },{
        'name': 'Add news',
        'href': '/news/create',
        'icon': 'fa-plus',
    },{
        'name': 'Forum',
        'href': '/forum',
        'icon': 'fa-comment',
    }]
    