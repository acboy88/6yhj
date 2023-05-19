from django.contrib import admin
from django.urls import path, include
from peoms import views,tools,collect

from django.conf.urls.static import static
from django.conf import settings
#for sitemap
from django.contrib.sitemaps.views import sitemap
from .sitemaps import sitemaps

urlpatterns = [     
    path('robots.txt',views.robots,name='robots'),
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('category-<int:cateid>/',views.category,name='category'),   
    path('leku-p-<int:id>.html',views.post,name='post'),
    path('cate<int:cateid>-tag-<int:id>/', views.tagall),
    path('taglist-<int:id>/',views.taglist,name='tag'),
    

    #管理功能
    path('tools/',tools.home),
    path('loading/',tools.loading),
    path('tools/zidong/',tools.zidong),
    path('tools/word_replace/',tools.word_replace),
    path('tools/submit_bd/',tools.submit_bd),
    path('tools/one-to-three/',tools.one_to_three),
    path('tools/caiji/',collect.collect_p),
    path('tools/caiji_by_id/',collect.caiji_by_id),
    path('tools/webinfo/',tools.get_webinfo),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
    #sitemaps
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap'),  

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
