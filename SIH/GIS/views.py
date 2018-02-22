from django.shortcuts import render
from django.http import HttpResponse
from json import dumps
from .models import *
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import RequestSerializer
from . serializers import ControlCenterLogINSerializer
from geopy.distance import vincenty



class RequestList(APIView):
    def get(self, request):
        request1 = Request.objects.all()
        serializer = RequestSerializer(request1, many = True)
        return Response(serializer.data)

    def post(self, request):
        robj = RequestSerializer(data = request.data)
        print(robj)
        if robj.is_valid():
            robj.save()
        return Response()


class ControlCenterLogINList(APIView):
    def get(self, request):
        login1 = ControlCenterLogIN.objects.all()
        serializer = ControlCenterLogINSerializer(login1, many = True)
        return Response(serializer.data)

    def post(self, request):
        pass
        # lobj = ControlCenterLogINSerializer(data = request.data)
        # print(lobj)
        # if lobj.is_valid():
        #     lobj.save()
        # return Response()



from django.views.decorators.csrf import csrf_exempt

def getNearest(request_latlon):
    computed_distance = []
    all_stns = Stations.objects.all()
    if len(all_stns) == 0:
        return None
    for i in all_stns:
        stn_latlon = (float(i.Latitude),float(i.Longitude))
        computed_distance.append(vincenty(request_latlon, stn_latlon).miles)
    idx = computed_distance.index(min(computed_distance))
    return all_stns[idx]

@csrf_exempt
def User_Request(request):
    if request.method == "POST":
        RequestID = request.POST.get('RequestID')
        IncidentType = request.POST.get('IncidentType')
        image = request.POST.get('image')
        Latitude = request.POST.get('Latitude')
        Longitude = request.POST.get('Longitude')
        r=Request(
        RequestID = RequestID,
        IncidentType = IncidentType,
        image = image,
        Latitude = Latitude,
        Longitude = Longitude
        )
        r.save()
        return HttpResponse('Successfully Inserted records')
    elif request.method == "GET":
        rid = request.GET.get('rid')
        lat = request.GET.get('lat')
        lon = request.GET.get('lon')
        response_json = {}
        response_json['data'] = {}
        if rid is None:
            return HttpResponse('RequestID parameter not given')
        try:
            robj = Request.objects.get(RequestID__exact=rid)
            request_latlon = (float(robj.Latitude), float(robj.Longitude))
            res_stn = getNearest(request_latlon)
            # write some logic to send the robj to the res_stn's asssociated Socket ID
            # Error codes
            # NF-404
            # SOE-404
            # OK-200
            response_json['code'] = 'OK-200'
            response_json['data']['StationID'] = res_stn.StationID
            response_json['data']['StationName'] = res_stn.StationName
            response_json['data']['StationArea'] = res_stn.StationArea
        except Request.DoesNotExist:
            response_json['code'] = 'NF-404'
        except:
            response_json['code'] = 'SOE-404'
        return HttpResponse(dumps(response_json), content_type = 'application/json')
    else:
        return HttpResponse('')


@csrf_exempt
def Web_Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        l = ControlCenterLogIN(
        username = username,
        password = password
        )
        return HttpResponse('Successfully Inserted records')
    else:
        return HttpResponse('')
