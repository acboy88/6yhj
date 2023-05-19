from django.contrib.sitemaps import Sitemap
from peoms.models import Posts,Tags,Category
#from django.core.urlresolvers import reverse
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = 'always'
    protocol = 'https'
    
    def items(self):
        return ['home', ]
    
    def location(self, item):
        return reverse(item)


class ArticleSiteMap(Sitemap):
    changefreq = "daily"
    priority = "0.9"
    protocol = 'https'
    
    def items(self):
        return Posts.objects.all()
    
    def lastmod(self, obj):
        return obj.time
        
    def location(self, item):
        return reverse('post',kwargs={'id': item.id})

class CategorySiteMap(Sitemap):
    changefreq = "daily"
    priority = "0.6"
    protocol = 'https'
    
    
    def items(self):
        return Category.objects.all()
        
    def location(self, item):
        return reverse('category',kwargs={'cateid': item.id})
    


class TagSiteMap(Sitemap):
    changefreq = "daily"
    priority = "0.6"
    
    def items(self):
        return Tags.objects.all()
        
    def location(self, item):
        return reverse('tag',kwargs={'id': item.id})
    

sitemaps = {
    'static': StaticViewSitemap,
    'blog': ArticleSiteMap,
    'Category': CategorySiteMap,
    'Tag': TagSiteMap,
}
