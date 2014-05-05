from providers import providers


def build_response(user, pw, base_provider):
    response_dict = {}
    if base_provider not in providers.keys():
        raise Exception("Couldn't find provider: " + str(base_provider))

    if not providers[base_provider]['login'](user, pw):
        response_dict[base_provider] = {}
        response_dict[base_provider]['same'] = False
        populate_row(response_dict, base_provider)
        return response_dict
    else:
        for provider in providers:
            response_dict[provider] = {}
            response_dict[provider]['same'] = providers[provider]['login'](user, pw)
            populate_row(response_dict, provider)
        return response_dict


def populate_row(d, provider):
    for k in providers[provider]:
        if k is not 'login':
            d[provider][k] = providers[provider][k]
