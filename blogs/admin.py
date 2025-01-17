from django.contrib import admin
from . import models


admin.site.register(models.BlogCategoryModel)
admin.site.register(models.BlogCommentModel)
admin.site.register(models.BlogLikeModel)
admin.site.register(models.BlogTagModel)
admin.site.register(models.BlogModel)
admin.site.register(models.BlogContactModel)
