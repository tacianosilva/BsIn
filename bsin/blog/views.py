from django.views import generic
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import CommentForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CadastroUsuarioForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required, permission_required

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 2 #paginação


def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


class PostCreate(generic.CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy('home')


class PostUpdate(generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy('home')

class PostDelete(generic.DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')



def cadastrar_user(request):
    if request.method == "POST":
        form_usuario = CadastroUsuarioForm(request.POST)
        if form_usuario.is_valid():
            try:
                criar_usuario(request, form_usuario)
                messages.success(request, 'Usuário cadastrado com sucesso.')
                return redirect('login/login.html')
            except ValidationError as e:
                form_usuario.add_error(None, e)
        else:
            messages.error(request, 'O formulário contém dados inválidos!')
    else:
        form_usuario = CadastroUsuarioForm()
    return render(request, 'cadastro/cadastro.html', {'form_usuario': form_usuario})


def check_email(request, form_usuario):
    email = form_usuario.cleaned_data.get('email')
    if User.objects.filter(email=email).exists():
        msg = 'O e-mail informado já foi cadastrado!'
        messages.error(request, msg)
        form_usuario.add_error('email', msg)
        raise ValidationError("Email já existe!")

def criar_usuario(request, form_usuario):
    usuario = form_usuario.save(commit=False)
    check_email(request, form_usuario)
    usuario.save()



def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            messages.success(request, 'Usuário logado com sucesso.')
            return redirect('home')
        else:
            messages.error(request, 'Erro ao logar usuário.')
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'login/login.html', {'form_login': form_login})

@login_required(login_url='/blog/templates/login/login.html')
def deslogar_usuario(request):
    logout(request)
    messages.success(request, 'Usuário deslogado com sucesso.')
    return redirect('index')


def index(request):
    return render(request, 'templates/index.html')


class PostSearch(generic.ListView):
    model = Post
    template_name = 'search_results.html'
    paginate_by = 5 #paginação     

    def get_queryset(self): # new
        query = self.request.GET.get('search')
        object_list = Post.objects.filter(title__icontains=query).order_by('-created_on')
                
        return object_list

    