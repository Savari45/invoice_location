{
    'name': "Invoice Location",
    'summary': "Display only in-stock products in sale order lines and show available on-hand quantity.",
    'description': """
        
    """,
    'version': '18.0.1.0.0',
    'category': 'Sales',
    'author': 'Alan Technologies',
    'maintainer': 'Alan Technologies',
    'company': 'Alan Technologies',
    'website': "https://alantechnologies.in/",
    'license': "AGPL-3",
    'depends': ['base', 'sale', 'account'],
    'data': [
         'views/inherit_account_move_views.xml',


    ],
    'images': ['static/description/banner.gif'],
    'installable': True,
    'application': False,
    'auto_install': False,
    'sequence': 1,
}
