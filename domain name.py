#baily leary 05-10-22
#getting domain name from URLs


#def domain_name(url):
#    url = url.replace('http://', ".")       
#    url = url.replace('https://', ".")
#    url_items = url.split('.')
#    del url_items[-1]
#     
#    
#
#    return url_items[???]       #[0] or [1] or [-1] depending 
#                               on if there is a sub domain    

    
#def domain_name(url):
#
#
#       --- this attempt is silly, and probily a waste of time---
#               --- i thought of all this splitting and joining first---
#                ---and did not want to trash first attemp just in case---
#
#
#    url_items = url.split('.' )
#    if url_items[0][0] != 'h' or url_items[0][0] == 'w':
#        url_items = url_items[1]
#    else:
#        url_items = " ".join(url_items)    
#        url_items = url.split('//' )
#        url_items = " ".join(url_items)
#        url_items = url.split(' ' )
#        url_items = url_items[???]         #why does spliting and then joining put 
#                                               the strings which i had origioinally plit 
#                                               with back into it?
#    return url_items


def domain_name(url):
    url_items = url.split('.')

    #if url_items[0][0] == 'h' or url_items[0][0] == 'w':   #cant do this because, it will delete all instances without subdomain
    #    url_items.pop(0)                                
    
    if len(url_items) >=3:         #this doesnt work becouse of instances with two TDL's
        url_items.pop(0)           #
    print(url_items)               #debug code
    url_items = '.'.join(url_items)
    url_items.replace("http//", '')
    url_items = url_items.split('.')
    return url_items[0]





print(domain_name("1: http://www.google.com"), "should be google")
print(domain_name("2: www.google.com"), "should be google")
print(domain_name("3: http://www.google.com/stuff"), "should be google")
print(domain_name("4: http://co.google.uk.com"), "should be google")
print(domain_name("5: http://google.com"), "should be google")
print(domain_name("6: http://google.co.jp"), "should be google")
print(domain_name("7: www.xakep.ru"), "should be xakep")
print(domain_name("8: https://youtube.com"), "should be youtube")