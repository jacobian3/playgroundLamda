def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user. """
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last 
    for key, value in user_info.items():
        profile[key] = value
    return profile

def main():
    user_profile = build_profile('Trex', 'Higram',
                                 location ='Charlston',
                                 field='Economics')
    print(user_profile)

if __name__ == "__main__":
    main()
