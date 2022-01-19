# from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from reviews.models import Review

from reviews.forms import ReviewForm


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'create_review.html'
    success_url = reverse_lazy('reviews:detail-review')

    def get_form_kwargs(self):
        """return kwargs for instantiating the form"""
        kwargs = super().get_form_kwargs()
        print('kwargs are', kwargs)  # initial:{},prefix,instance:review
        if self.request.user != kwargs['instance'].user:
            return self.handle_no_permission()
        return kwargs


class ReviewDetailView(DetailView):
    model = Review
    template_name = 'reviews/review-detail.html'


class ReviewCreateView(LoginRequiredMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy('reviews:detail-review')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReviewCreateView(LoginRequiredMixin, DeleteView):
    model = Review
    success_url = reverse_lazy('reviews:list-review')

    def post(self, *args, **kwargs):
        # here msg + TODO
        return super().post(*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != request.user:
            return self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(self.success_url)
