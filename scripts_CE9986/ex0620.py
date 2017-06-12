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

for key in site_pages:
    print(key)
    for site in site_pages[key]:
        print('\t{}'.format(site))
