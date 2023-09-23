from rest_framework.pagination import PageNumberPagination
from rest_framework.throttling import UserRateThrottle

class SimplePaginationClass(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 1000
    
class MyUserRateThrottleClass(UserRateThrottle):
    rate = '5/hour' # min/hour/day