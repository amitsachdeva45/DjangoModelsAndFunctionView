from django.http import HttpResponse, HttpResponseRedirect

#Functional Views
#Video 1
def normal_request(request):
    print(request)
    print(dir(request))
    print(request.get_full_path())
    return HttpResponse('<h1>Hello</h1>')

#Video 2
def normal_response(request):
    response = HttpResponse(content_type="text/html") # type of content we want to send to response
    response.write("Hello") #To write normal text
    response.content = "<h1>Hanji</h1>" #It is entire content
    response.status_code = 404
    return response

def redirect_views(request):
    return HttpResponseRedirect('/some/path') # https://www.google.com