
import os, html_sanitizer

def getList():
    sanitizer = html_sanitizer.Sanitizer()

    files = os.listdir('d_Turretinus_ko')
    list_Turretinus_ko = ''
    for item in files:
        sub_item=item.rstrip('.jpg')
        item=item
        list_Turretinus_ko = list_Turretinus_ko + '<li><a href="d_Turretinus_ko/{org_name}" target="content_ko">{name}</a></li>'.format(org_name=item, name=sub_item)
    return list_Turretinus_ko
