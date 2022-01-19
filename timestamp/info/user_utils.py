"""
docs: request.META (содержит http headers added by user's browser == dict (keys= header's names)
request.META.get('REMOTE_ADDR') => ip address
"""


def get_user_ip(request):
    """
    if x_forward present return it;
    otherwise remote_addr or empty string

    """
    try:
        real_ip = request.META.get('HTTP_X_FORWARDED_FOR')
        # HTTP_X_FORWARDED_FOR can be a comma-separated list of IPs.
        if real_ip:
            return request.META.get('HTTP_X_FORWARDED_FOR').split(',')[0].strip()
        else:
            return request.META.get('REMOTE_ADDR')
    except Exception as e:
        print('exception',e)
        return ''
