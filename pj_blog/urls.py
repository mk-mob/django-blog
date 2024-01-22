
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import Group

admin.site.site_title = '匿名ブログ 内部管理サイト'
admin.site.site_header = '匿名ブログ 内部管理サイト'
admin.site.index_title = 'メニュー'
admin.site.unregister(Group)
admin.site.disable_action('delete_selected')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls")),
]
