from django.contrib import admin
from .models import FollowersCount, Profile,Post,LikePost,Comment


admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(FollowersCount)
admin.site.register(Comment)
