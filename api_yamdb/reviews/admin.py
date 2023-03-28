from django.contrib import admin
from import_export import resources
from import_export.fields import Field
from import_export.admin import ImportExportModelAdmin

from reviews.models import Category, Genre, Title, TitleGenre, Review, Comment


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'slug',
        )


class CategoryAdmin(ImportExportModelAdmin):
    resource_classes = (CategoryResource,)
    list_display = (
        'id',
        'name',
        'slug',
    )


class GenreResource(resources.ModelResource):
    class Meta:
        model = Genre
        fields = (
            'id',
            'name',
            'slug',
        )


class GenreAdmin(ImportExportModelAdmin):
    resource_classes = (GenreResource,)
    list_display = (
        'id',
        'name',
        'slug',
    )


class TitleResource(resources.ModelResource):
    class Meta:
        model = Title
        fields = (
            'id',
            'name',
            'year',
            'category'
        )


class TitleAdmin(ImportExportModelAdmin):
    resource_classes = (TitleResource,)
    list_display = (
        'id',
        'name',
        'year',
        'category'
    )


class TitleGenreResource(resources.ModelResource):
    title = Field(attribute='title_id', column_name='title_id')
    genre = Field(attribute='genre_id', column_name='genre_id')

    class Meta:
        model = TitleGenre
        fields = (
            'id',
            'title',
            'genre',
        )


class TitleGenreAdmin(ImportExportModelAdmin):
    resource_classes = (TitleGenreResource,)
    list_display = (
        'id',
        'title',
        'genre',
    )


class ReviewResource(resources.ModelResource):
    title = Field(attribute='title_id', column_name='title_id')

    class Meta:
        model = Review
        fields = (
            'id',
            'title',
            'text',
            'author',
            'score',
            'pub_date',
        )


class ReviewAdmin(ImportExportModelAdmin):
    resource_classes = (ReviewResource,)
    list_display = (
        'id',
        'title',
        'text',
        'author',
        'score',
        'pub_date',
    )


class CommentResource(resources.ModelResource):
    review = Field(attribute='review_id', column_name='review_id')

    class Meta:
        model = Comment
        fields = (
            'id',
            'review',
            'text',
            'author',
            'pub_date',
        )


class CommentAdmin(ImportExportModelAdmin):
    resource_classes = (CommentResource,)
    list_display = (
        'id',
        'review',
        'text',
        'author',
        'pub_date',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(TitleGenre, TitleGenreAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
