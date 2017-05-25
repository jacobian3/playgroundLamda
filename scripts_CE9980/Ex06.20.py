site_pages = {
    'example.com':  [
                        'index.html',
                        'about_us.html',
                        'contact_us.html',
                    ],        
    'something.com':  [
                        'index2.html',
                        'prizes.html',
                        'puppies.html',
                    ],        
    'whateva.com':  [
                        'main.html',
                        'getting.html',
                        'setting.html',
                    ],        
}

# produce keys; looping through a dict => keys
for site in site_pages:
    print(site)
    #use keys to access the dictionary values( the inner list)
    #use the page created, to loop through the list
    # of pages
    for page in site_pages[site]:
        print("  ",page)
