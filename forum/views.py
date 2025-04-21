from django.shortcuts import render, redirect
from . import forms, models
from django.contrib import messages 
from django.contrib.auth.decorators import login_required

def forum(request):
    posts = models.Post.objects.all()

    return render(request, 'forum/forum-template.html', {"posts": posts})

def post_detail(request, pk):
    post = models.Post.objects.get(pk=pk)
    comments = models.Comment.objects.filter(post=post)
    form = forms.CreateCommentForm()

    return render(request, 'forum/post-detail-template.html', {"post": post, "comments": comments, "form": form})

@login_required
def create_post_view(request):
    if request.method == "POST":
        form = forms.CreatePostForm(request.POST)

        if form.is_valid():
            short_description = form.cleaned_data["short_description"]
            content = form.cleaned_data["content"]
            author = request.user

            post = models.Post.objects.create(short_description=short_description, 
                                              content=content,
                                              author=author)
            
            post.save()

            return redirect('forum')
        else: 
            messages.error("Перевірте форму і повторіть спробу")
    else:
        form = forms.CreatePostForm()

    return render(request, 'forum/create-post-template.html', {"form": form})

@login_required
def edit_post_view(request, pk):
    post = models.Post.objects.get(pk=pk)

    if request.method == "POST":
        form = forms.EditPostForm(request.POST)

        if form.is_valid():
            short_description = form.cleaned_data["short_description"]
            content = form.cleaned_data["content"]

            post = models.Post.objects.get(pk=pk)

            if short_description:
                post.short_description = short_description
            
            if content:
                post.content = content

            post.save()

            return redirect('forum')
        else:
            messages.error("Перевірте форму і повторіть спробу")
    else:
        form = forms.EditPostForm()
    
    return render(request, 'forum/edit-post-template.html', {"form": form, "post": post})

@login_required
def delete_post_view(request, pk):
    post = models.Post.objects.get(pk=pk)

    if request.method == "POST":
        post.delete()

        return redirect('forum')
    
    return render(request, 'forum/delete-post-template.html', {"post": post})

@login_required
def create_comment_view(request, pk):
    if request.method == "POST":
        form = forms.CreateCommentForm(request.POST)

        if form.is_valid():
            content = form.cleaned_data["content"]
            author = request.user

            post = models.Post.objects.get(pk=pk)

            comment = models.Comment.objects.create(content=content, 
                                                    author=author,
                                                    post=post)
            
            comment.save()

            return redirect('post-detail', pk=pk)
        else:
            messages.error("Перевірте форму і повторіть спробу")
    else:
        form = forms.CreateCommentForm()

    return render(request, 'forum/create-comment-template.html', {"form": form})

@login_required
def edit_comment_view(request, pk):
    comment = models.Comment.objects.get(pk=pk)

    if request.method == "POST":
        form = forms.EditCommentForm(request.POST)

        if form.is_valid():
            content = form.cleaned_data["content"]

            comment = models.Comment.objects.get(pk=pk)

            if content:
                comment.content = content

            comment.save()

            return redirect('post-detail', pk=comment.post.pk)
        else:
            messages.error("Перевірте форму і повторіть спробу")
    else:
        form = forms.EditCommentForm()
    
    return render(request, 'forum/edit-comment-template.html', {"form": form, "comment": comment})

@login_required
def delete_comment_view(request, pk):
    comment = models.Comment.objects.get(pk=pk)

    if request.method == "POST":
        comment.delete()

        return redirect('post-detail', pk=comment.post.pk)
    
    return render(request, 'forum/delete-comment-template.html', {"comment": comment})
