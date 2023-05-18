from django.contrib import admin

from .models import Tweet, Reaction, ReactionType, TweetImages, Reply


@admin.display(description='Short Text')
def get_short_text(obj):
    return f'{obj.text[:10]}...'


class TweetImagesInline(admin.TabularInline):
    model = TweetImages
    extra = 1


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    actions_on_bottom = True
    actions_on_top = False
    empty_value_display = '-empty-'
    # exclude = ['profile', 'image']
    # fields = ['text']
    fields = (('text', 'profile'), 'image')
    list_display = ['id', 'get_profile_fullname', get_short_text, 'get_reactions_str', 'image', 'created_at']
    list_display_links = [get_short_text, 'id']
    list_editable = ['image', ]
    list_filter = ['created_at', ]
    list_per_page = 2
    save_as = True
    search_fields = ['text', 'profile__user__username']
    sortable_by = ['created_at', 'id']
    inlines = [TweetImagesInline]

    @admin.display(description='Fullname')
    def get_profile_fullname(self, obj):
        return obj.profile.user.get_full_name()


@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    pass


@admin.register(ReactionType)
class ReactionTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    actions_on_bottom = True
    actions_on_top = False
    empty_value_display = '-'
    list_editable = ['text', 'profile']
    list_display = ['tweet', 'text', 'profile', 'get_profile_fullname', get_short_text, 'get_reactions_str', 'created_at']
    search_fields = ['text', 'profile__user__username']
    list_display_links = [get_short_text, 'tweet']
    sortable_by = ['created_at', 'id']
    fields = [('text', 'profile'), 'tweet']

    @admin.display(description='Fullname')
    def get_profile_fullname(self, obj):
        return obj.profile.user.get_full_name()

