from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
	# Fetch bank details
	# url(r'^api/v1/fetch/bank/(\w{11})/?$', csrf_exempt(fetch_bank), name="api.fetch_bank"),

]