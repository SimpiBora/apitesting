# from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import CursorPagination
from rest_framework.response import Response

# from datetime import datetime

# class CustomCursorPagination(CursorPagination):
#     page_size = 10
#     page_size_query_param = "page_size"
#     max_page_size = 50
#     ordering = "-created_at"  # Use '-id' or '-created_at' for reverse chronological

#     def get_paginated_response(self, data):
#         return Response({
#             "next": self.get_next_link(),
#             "previous": self.get_previous_link(),
#             "has_next": self.get_next_link() is not None,
#             "has_previous": self.get_previous_link() is not None,
#             "results": data,
#         })


class CustomCursorPagination(CursorPagination):
    page_size = 10  # Default number of items per page
    page_size_query_param = "page_size"  # Allow client to specify page size
    max_page_size = 15  # Maximum page size allowed
    ordering = "created_at"  # Field for ordering (must be unique) # Use '-id' or '-created_at' for reverse chronological
    cursor_query_param = "cursor"  # Query parameter for cursor

    def get_paginated_response(self, data):
        return Response(
            {
                "next": self.get_next_link(),  # URL for the next page
                "previous": self.get_previous_link(),  # URL for the previous page
                "page_size": len(data),  # Number of items in the current page
                "has_next": self.get_next_link()
                is not None,  # True if there is a next page
                # True if there is a previous page
                "has_previous": self.get_previous_link() is not None,
                "results": data,  # The paginated data
            }
        )


# class CustomPageNumberPagination(PageNumberPagination):
#     page_size = 10  # Default number of items per page
#     page_query_param = "page"  # Query parameter for the page number
#     page_size_query_param = "page_size"  # Allows clients to control the page size
#     max_page_size = 50  # Set an upper limit for page size to prevent abuse

#     def get_paginated_response(self, data):
#         """
#         Returns a custom paginated response.
#         Includes metadata like total pages, count, and links to navigate.
#         """
#         return Response(
#             {
#                 "pagination": {
#                     "current_page": self.page.number,
#                     "total_pages": self.page.paginator.num_pages,
#                     "total_count": self.page.paginator.count,
#                     "page_size": self.page_size,  # Actual page size in use
#                     "next_link": self.get_next_link(),
#                     "previous_link": self.get_previous_link(),
#                 },
#                 "results": data,  # The actual data for the current page
#             }
#         )
