
def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None,0
    else:

        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url =page[start_quote + 1:end_quote]
        return url #,end_quote
print (get_next_target('this is a <a href="http://udacity.com" will now go to spleep'))
print (get_next_target('this is a will now go to sleep'))