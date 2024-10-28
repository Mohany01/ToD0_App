{
    'name' : 'To_Do App' ,
    'version' :'12.0.1.0.0',
    'category':'Extra Tools',
    'summary':'second module',
    'author':'Mohammed Hany',
    'depends':['base','mail',],
    'data':[
        'views/root_menu.xml',
        'views/all_tasks_view.xml',
        'security/ir.model.access.csv',

    ],

    'installable':True,
    'application':True,

}