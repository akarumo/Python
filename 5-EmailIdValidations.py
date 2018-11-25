# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 09:47:44 2018

@author: aditya
"""

email_ids_list= ['abcdef@y.com','b@yabcd.com','abcdef@yahoo.com','123456@y.com', 'aditya@gmail.com',]
domains_list= ['com', 'net', 'co', 'in', 'org']

valid_emails= []

for i in email_ids_list:
    if(i.find('@') == 6) : # before @ only 6 chars 
        if(i[7:].find('@') == -1) : #  only 1 @
            if(i[7:].find('.') > -1 & i[:6].find('.') == -1) : # only . after @
                if(len(i[7:7+i[7:].find('.')]) >= 3) : # between @ and . at least 3 chars
                    for domain in domains_list : # after . only accept [com, net, co, in, org]
                        if(i[7+i[7:].find('.')+1:] == domain) :
                            valid_emails.append(i)
                        else:
                            continue
print('Valid emails from the input list: ', valid_emails)

