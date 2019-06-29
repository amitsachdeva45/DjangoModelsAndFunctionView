from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import PostModel
from .forms import PostModelForm
from django.contrib import messages
from django.db.models import Q

#Delete View
def post_model_delete_view(request, id):
        obj = get_object_or_404(PostModel, id=id)
        if request.method == "POST":
            obj.delete()
            messages.success(request, "Deleted successfully")
            return HttpResponseRedirect("/blog/list")
        context = {
            "object": obj,
        }
        template = "blog/delete_view.html"
        return render(request, template, context)


#Update View
def post_model_update_view(request, id = None):
    obj = get_object_or_404(PostModel, id=id)
    form_a = PostModelForm(request.POST or None, instance = obj)  # View Form
    context = {
        "object": obj,
        "form": form_a  # Template Context
    }
    if form_a.is_valid():
        obj = form_a.save(commit=False)
        obj.save()
        messages.success(request, "Updated")
        context = {
            "form": PostModelForm()  # To refresh the form
        }
        return HttpResponseRedirect("/blog/detail/{num}".format(num = obj.id))

    template = "blog/update_view.html"
    return render(request, template, context)


#Create View
def post_model_create_view(request):
    # if request.method == "POST":
    #     print(request.POST)
    #     form = PostModelForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit=False)
    #         print(form.cleaned_data)

    form_a = PostModelForm(request.POST or None) #View Form

    context = {
        "form": form_a  # Template Context
    }
    if form_a.is_valid():
        obj = form_a.save(commit = False)
        obj.save()
        messages.success(request,"Jai mata di")
        context = {
            "form": PostModelForm() # To refresh the form
        }
        #return HttpResponseRedirect("/blog/detail/{num}".format(num = obj.id))


    template = "blog/create_view.html"
    return render(request, template, context)


#Detail view
def post_model_detail_view(request, id):
    #### Three ways of retreving data using id

    ### Exception Handling
    # try:
    #     obj = PostModel.objects.get(id = 1)
    # except:
    #     raise 404

    ### How to check if item exist if yes get the item
    ### It is useful to filter the data and check if it exists
    # qs = PostModel.objects.filter(id = 100)
    # obj = None
    # if not qs.exists() and qs.count() != 1:
    #     raise Http404
    # else:
    #     obj = qs.first()

    #####Get object or 404
    obj = get_object_or_404(PostModel, id=id)
    context = {
        "object" : obj,
    }
    template = "blog/detail_view.html"
    return render(request,template, context)


#Listing the data
def post_model_list_view(request):
    qs = PostModel.objects.all()
    query1 = request.GET.get('query')
    if query1 is not None:
        qs = qs.filter(
            Q(title__icontains = query1) |
            Q(content__icontains=query1)
        ) # For multiple Filters
        #qs = qs.filter(title__icontains = query1) #Single Search
    print(request.user)
    context_dicitionary = {
        "object_list": qs,
        "normal_data": "Paras Sachdeva",
        "normal_array": [12, 13, 14],
        "num": 12,
        "boolean_value": True
    }
    template_path = "blog/list_view.html"
    return render(request, template_path, context_dicitionary)

#Login Required
@login_required(login_url="/login/")
def login_required_view(request):
    qs = PostModel.objects.all()
    print(request.user)
    context_dicitionary = {
        "object_list": qs,
    }
    if request.user.is_authenticated():
        template_path = "blog/list_view.html"
    else:
        template_path = "blog/login.html"
        raise Http404
        return HttpResponseRedirect('/login')

    return render(request, template_path, context_dicitionary)