from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from blog.models import Category, blogComment, post
from django.contrib import messages # this is for session message
from blog.templatetags import extras 
from django.core.paginator import Paginator # For pagination part 

# Create your views here.
def bloghome(request):
	all_data 	= post.objects.all().order_by('-timestamp') # Descending er samne - dilet hoy. ascending er name likley hy.
	paginator  	= Paginator(all_data, 3) # Pagination part, Show 3 post per page.
	page_number = request.GET.get('page') # Pagination, this 'page' come form template page
	page_obj 	= paginator.get_page(page_number) # Pagination part, good site= https://www.ordinarycoders.com/blog/article/django-pagination
	
	most_view 	= post.objects.all().order_by('-views') # Most view part	
	cat 	 	= Category.objects.all() # for categorys show
	# print(cat)

	context ={
		'blog_all':page_obj, # All data and Pagination part 
		'categorys':cat,
		'mView':most_view # Most view part	
	}

	return render(request, 'blog/blog.html', context)



def category_list(request, category_slug=None):
    categories 	= get_object_or_404(Category, slug=category_slug) # match category_slug

    produc 	 	= post.objects.filter(category=categories) # match post category & category_slug
    paginator  	= Paginator(produc, 3) # Pagination part, Show 3 post per page.
    page_number = request.GET.get('page') # Pagination get page
    page_obj 	= paginator.get_page(page_number) # Pagination part, good site= https://www.ordinarycoders.com/blog/article/django-pagination
	
    cat 	 	= Category.objects.all() # for categorys name show
    most_view 	= post.objects.all().order_by('-views') # Most view part
    all_data 	= post.objects.all().order_by('-timestamp') # all post view
    
    context = {
        'category': categories,
        'products': page_obj, # get all post details
        'cat_name':cat, # category name show
        'blog_all':all_data,# for resent post, get all post details
        'mView':most_view, # Most view part
    }
    return render(request, 'blog/category.html', context)


def blogpost(request, slug):
	most_view 	= post.objects.all().order_by('-views') # Most view part
	all_data 	= post.objects.all().order_by('-timestamp') # Data view for template
	data 		= get_object_or_404(post, slug=slug)	# Data save for DB
	data.views  += 1	# Total view count with save
	data.save()

	cat 	 	= Category.objects.all() # for categorys show	
	commentData = blogComment.objects.filter(post=data, parent=None) #for comment part
	replys 		= blogComment.objects.filter(post=data).exclude(parent=None) #for reply part
	replyDict = {}
	for reply in replys:
		if reply.parent.sno not in replyDict.keys():
			replyDict[reply.parent.sno] = [reply]
		else:
			replyDict[reply.parent.sno].append(reply)

	context = {
		'mView':most_view, # Most view part
		'blog_all':all_data, # for category & resent post
		'post':data,
		'comment':commentData,
		'categoryItem':cat,
		'replyDict':replyDict
	}
	return render(request, 'blog/blog_details.html', context)



def postcomment(request):
	if request.method == "POST":
		comment 	= request.POST.get("comment")
		user 		= request.user
		postSno		= request.POST.get("postSno")
		Post 		= post.objects.get(sno=postSno)

		parentSno 	= request.POST.get("parentSno") # Reply insert ID
		# print(comment, user, Post, parentSno)
		if parentSno=="": # if parent ID=0 then reply will be save [reply save part]
			comment = blogComment(comment=comment, user=user, post=Post)
			comment.save()
		else: # comment save part
			Parent 	= blogComment.objects.get(sno=parentSno)
			# print(Parent)
			comment = blogComment(comment=comment, user=user, post=Post, parent=Parent)
			comment.save()

	return redirect(f"/blog/{Post.slug}")