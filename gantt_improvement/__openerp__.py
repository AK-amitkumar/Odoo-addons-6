{
    'name': "Gantt Improvement",
    'category': 'Project',
    'sequence': 1,
    'description': """
Gantt Improvement
=================
    """,
    'version': '0.3',
    'depends': ['web', 'web_gantt'],
    'js': ['static/src/js/gantt.js'], #Odoo V7.0
    'css': ['static/src/css/gantt.css'], #Odoo V7.0
    'qweb': ['static/src/xml/gantt.xml'],
    'data': [
        'static/src/xml/gantt_config.xml',
        #'views/web_gantt.xml', #Odoo V8.0
    ],
}
