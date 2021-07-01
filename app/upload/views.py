from django.shortcuts import render, redirect
from .forms import PostForm, PlayerForm, CardForm
from .models import Post
from django.views.generic import CreateView



def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

#プレイヤーと同時に複数のセットを登録する試み
class CreatePlayerSetView(CreateView):
   form_class =PlayerForm
   form_class2 =CardForm

   template_name = 'post_list'

   def get_context_data(self, **kwargs):
       context= CreateView.get_context_data(self, **kwargs)
       form2 = self.form_class2(self.request.GET or None)
       context.update({'form2':form2})


       return context

   def form_valid(self, form):
       form2 = self.form_class2(self.request.POST or None)

       if form2.is_valid():
           with transaction.atomic():
               form.save()
               form2.save() 
       else:
           self.form_invalid(form)


       return HttpResponseRedirect(self.get_success_url())

   def get_success_url(self):
       return reverse_lazy('player:create_playerset')

create_player_setview = CreatePlayerSetView.as_view()