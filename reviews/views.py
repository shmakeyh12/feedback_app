from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

# Create your views here.
from .forms import review_form
from .models import ReviewTable

class ReviewView(CreateView):
    model = ReviewTable
    form_class= review_form
    template_name = "reviews/index.html"
    success_url= "/thank-page"
    
class ThankYou(TemplateView):
    template_name = "reviews/thanks.html"
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["message"] = "Finished!!"
        return context

class ListReviews(ListView):
    template_name= "reviews/listreviews.html"
    model = ReviewTable
    context_object_name = "reviews"
    
class SingleReview(DetailView):
    template_name= "reviews/singlereview.html"
    model = ReviewTable
    context_object_name = "review"
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        loaded_id = self.object.id 
        liked_id = self.request.session.get("liked_id")
        context["is_liked"] = str(loaded_id) == liked_id
        return context

class AddLikeView(View):
    def post(self, request):
        liked_id = request.POST['liked_id']
        request.session["liked_id"] = liked_id
        return HttpResponseRedirect("/list-reviews/"+liked_id)