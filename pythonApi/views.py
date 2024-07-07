from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.http import JsonResponse

import json

class ItemsView(APIView):
	def get(self, request):
		with open('data.json') as f:
			response = JsonResponse(json.load(f), status=200,safe=False);
			return response;
