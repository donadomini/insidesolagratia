
import os, html_sanitizer

def getList():
    sanitizer = html_sanitizer.Sanitizer()

    files = os.listdir('d_Calvinus_ko')
    list_Calvinus_ko = ''
    for item in files:
        sub_item=item.rstrip('.jpg')
        item=item
        list_Calvinus_ko = list_Calvinus_ko + '<li><a href="d_Calvinus_ko/{org_name}" target="content_ko">{name}</a></li>'.format(org_name=item, name=sub_item)
    return list_Calvinus_ko
