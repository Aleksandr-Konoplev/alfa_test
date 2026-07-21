from rest_framework.pagination import PageNumberPagination


class CategoryPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 30
    page_query_param = 'cat_page'


class SubcategoryPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 30
    page_query_param = 'subcat_page'


class ProductPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 50
    page_query_param = 'prod_page'


class NestedSubcategoryPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'sub_page_size'
    max_page_size = 10
    page_query_param = 'subcat_page'
