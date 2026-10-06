from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest, HttpResponse
from .models import Post
from django.http import Http404
from django.core.paginator import PageNotAnInteger, EmptyPage,Paginator 
from django.views.generic import ListView
from .forms import EmalIPostForm 
# Create your views here.

class PostListView(ListView):
   
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = 'blog/html/list.html' 



def post_share(request, post_id)>
    post = get_object_or_404(
        Post,
        id=post_id,
        status = Post.Status.PUBLISHED
    )

    if request.method == "POST":

        form = EmalIPostForm(request.POST)
        if form.is_valid():

            cd = form.cleaned_data
    else:
        form = EmalIPostForm()

    return render(
        request,
        "blog/post/share.html",
        {
            "post": post,
            "form": form
            
        }
    )
def tela_inicial(request):
    return render(request, "blog/html/telaHome.html")

def post_list(request):
    posts_list = Post.published.all()

    paginator = Paginator(posts_list,3)
    page_number = request.GET.get("page", 1)
    try:
        posts = paginator.page(page_number)

    except PageNotAnInteger: 
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request,
                  "blog/html/list.html",
                  {"post":posts}
                  )

def post_detail(request, year, month,day, post):
    post = get_object_or_404(
                             Post,
                             id = id,
                             status= Post.Status.PUBLISHED,
                             slug=post,
                             publish__year= year,
                             publish__month=month,
                             publish__day=day 
    )
    
    return render(request,
                  "blog/html/detail.html",
                  {"post": post}
    )