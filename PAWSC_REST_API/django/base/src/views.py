from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from base.src.serializers import UserSerializer, GroupSerializer
from rest_framework.views import APIView, Response
from base.src import constants
from base.src.PAWSCMessage import PawscJson

from .models import Scan_Device

SpecResp = {
		"apiKey": "xxxxxxxx-xxxx-Mxxx-Nxxx-xxxxxxxxxxxx",
		"type": "SPECTRUM_RESP",
		"version": "1.0",
		"deviceDesc": {
			"serialNumber": "asdad1748kopol",
			"typeApprovalId": "TA-2016/001",
			"modelId": "asdsa444",
			"deviceType": "fixed",
			"deviceCategory": "master",
			"emissionClass": "3",
			"rulesetIds": ["ICASATVWS-2018", "FccTvBandWhiteSpace-2010"]
		},
		"masterDeviceDesc":{
			"serialNumber": "ioig"
		},
		"deviceDescs":[{
			"serialNumber": "meraka",
			"typeApprovalId": "csir",
			"modelId": "wireless",
			"deviceType": "fixed",
			"deviceCategory": "Client",
			"emissionClass": "1",
			"rulesetIds": ["ICASATVWS-2018", "FccTvBandWhiteSpace-2010"]
		},
		{
			"serialNumber": "lpm",
			"typeApprovalId": "lpm",
			"modelId": "lpm",
			"deviceType": "fixed",
			"deviceCategory": "Client",
			"emissionClass": "5",
			"rulesetIds": ["ICASATVWS-2018", "FccTvBandWhiteSpace-2010"]
		}],
		"location": {
			"point": {
				"center": {
					"latitude": -25.752660,
					"longitude": 28.253984
				}
			},
			"confidence": 95
		},
		"locations": [
			{
				"point": {
					"center": {
						"latitude": -25.7,
						"longitude": 40.5
					}
				},
				"confidence": 95
			},
			{
			"point": {
				"center": {
					"latitude": -99.15,
					"longitude": 15.8
				}
			},
			"confidence": 95
		}
		],
		"antenna": {
			"height": 3.1,
			"heightType": "AGL"
		},
		"deviceOwner": {
			"owner": "[\"vcard\",[[\"version\",{},\"text\",\"4.0\"],[\"fn\",{},\"text\",\"Size Testing\"],[\"tel\",{\"type\":\"work\"},\"text\",\"(012) 841-4766\"],[\"email\",{\"type\":\"work\"},\"text\",\"djohnson@cs.uct.ac.za\"],[\"adr\",{\"type\":\"work\"},\"text\",[\"\",\"\",\"CSIR Meraka Institute\",\"Brummeria\",\"Pretoria\",\"0184\",\"RSA\"]],[\"prodid\",{},\"text\",\"ez-vcard ${version}\"]]]",
			"operator": "[\"vcard\",[[\"version\",{},\"text\",\"4.0\"],[\"fn\",{},\"text\",\"Size Testing\"],[\"tel\",{\"type\":\"work\"},\"text\",\"(012) 841-3028\"],[\"email\",{\"type\":\"work\"},\"text\",\"djohnson@cs.uct.ac.za\"],[\"adr\",{\"type\":\"work\"},\"text\",[\"\",\"\",\"CSIR Meraka Institute\",\"Brummeria\",\"Pretoria\",\"0184\",\"RSA\"]],[\"prodid\",{},\"text\",\"ez-vcard ${version}\"]]]"
		},
		"spectra": [{
			"resolutionBwHz": 8e6,
			"profiles": [[{
				"hz": 5.18e8,
				"dbm": 30.0
			},
			{
				"hz": 5.26e8,
				"dbm": 30.0
			}]]
		}]
	}

class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Group.objects.all()
	serializer_class = GroupSerializer



class InitViewSet(APIView):

	def Method_Init_Req(self,params):
		print('Received INIT_REQ')
		return {"type": "INIT_RESP"}
	
	def Method_Spec_Req(self,params):
		print('Received SPEC_REQ')
		return SpecResp

	def Unknown_Req(self,params):
		print('Received Unknown Method: ', params)
		return {'code': 'xxx', 'message': 'Unknown Method: ' + params, 'data': 'zzz'}
	  
	def Malformed_Req(self):
		print('Received Malformed Request')
		return {'code': 'xxx', 'message': 'MALFORMED_REQUEST', 'data': 'zzz'}
   
	def Method_Init_Scan_Req(self,params):
		print('Received INIT_SCAN_REQ')
		


	def get(self, request, format=None):
	  return Response('GET NOT IMPLMENTED')

	   
	def post(self, request, format=None):
		
		PostString = request.data
		print(PostString)
		
		RD = PawscJson('2.0')
		if ('id' in PostString):
			JsonID = PostString['id']
			RD.IDSet(JsonID)
	
			if (('method' in PostString) and ('params' in PostString)):
				PAWSCMethod = PostString['method']
				PAWSCParams = PostString['params']
				print('Received: ', PAWSCMethod, PAWSCParams)

				if (PAWSCMethod == constants.MethodNameInit):
					Result = self.Method_Init_Req(PAWSCParams)
					RD.MethodSet(constants.MethodNameInit)
					RD.ParamSet(Result)

				elif (PAWSCMethod == constants.MethodNameAvailableSpectrum):
					Result = self.Method_Spec_Req(PAWSCParams)
					RD.MethodSet(constants.MethodNameAvailableSpectrum)
					RD.ParamSet(Result)

				# Add more methods here




				# Case for method not known
				else:
					Result = self.Unknown_Req(PAWSCMethod)
					RD.ErrorSet(constants.ExceptionMessageInvalidMethod)
					RD.ParamSet(Result)

			# Case fo malformed request
			else:
				Result = self.Malformed_Req()
				RD.ErrorSet(constants.ExceptionMessageParametersRequired)
				RD.ParamSet(Result)

		# Case fo malformed request
		else:
			Result = self.Malformed_Req()
			RD.ErrorSet(constants.ExceptionMessageParametersRequired)
			RD.ParamSet(Result)

		print(RD.Get())
		return Response(RD.Get())
