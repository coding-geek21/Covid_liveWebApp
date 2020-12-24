from django.shortcuts import render
import requests
import json


url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "016a8ebd47msh238fbaab7c5e0b8p155cb5jsn3737a347feb1",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

# Create your views here.
def helloworldview(request):
	#mylist=['item1','item2','item3']
	#string ="everyone"
	#context={'string':string}
	#context1={'mylist':mylist}
	list1=[]
	noofresults=int(response['results'])
	for i in range(0,noofresults):

	    list1.append(response['response'][i]['country'])

	if request.method=="POST":
		selectedCountry = request.POST['selectedCountry']
		noofresults = int(response['results'])
		for x in range(0,noofresults):
			if selectedCountry==response['response'][x]['country']:

				new=response['response'][x]['cases']['new']
				active=response['response'][x]['cases']['active']
				critical=response['response'][x]['cases']['critical']
				recovered=response['response'][x]['cases']['recovered']
				total=response['response'][x]['cases']['total']
				deaths=int(total)-int(active)-int(recovered)

		context={'selectedCountry':selectedCountry,'list1':list1,'new':new,'active':active,'critical':critical,'recovered':recovered,'total':total,'deaths':deaths}		
		return render(request,'helloworld.html',context)

	list1=[]
	noofresults=int(response['results'])
	for i in range(0,noofresults):
	    list1.append(response['response'][i]['country'])
	context={'list1':list1}
	return render(request,'helloworld.html',context)
	