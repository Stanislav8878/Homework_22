from django.conf import settings
from django.core.mail import send_mail
from django.db.models import F
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
class PostListView(ListView):
    model = Post; template_name = 'blogs/post_list.html'; context_object_name = 'posts'
    def get_queryset(self): return Post.objects.filter(is_published=True)
class PostDetailView(DetailView):
    model = Post; template_name = 'blogs/post_detail.html'; context_object_name = 'post'
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        Post.objects.filter(pk=obj.pk).update(views=F('views') + 1)
        obj.refresh_from_db(fields=['views'])
        if obj.views == 100:
            try:
                send_mail('Поздравляем! 100 просмотров статьи', f'Статья "{obj.title}" достигла 100 просмотров.',
                          getattr(settings,'DEFAULT_FROM_EMAIL',None), [getattr(settings,'ADMIN_EMAIL','you@example.com')], fail_silently=True)
            except Exception: pass
        return obj
class PostCreateView(CreateView):
    model = Post; fields = ['title','content','preview','is_published']; template_name = 'blogs/post_form.html'; success_url = reverse_lazy('blogs:post_list')
class PostUpdateView(UpdateView):
    model = Post; fields = ['title','content','preview','is_published']; template_name = 'blogs/post_form.html'
    def get_success_url(self): return reverse('blogs:post_detail', kwargs={'pk': self.object.pk})
class PostDeleteView(DeleteView):
    model = Post; template_name = 'blogs/post_confirm_delete.html'; success_url = reverse_lazy('blogs:post_list')
