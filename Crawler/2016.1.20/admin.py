from django.contrib import admin
from elife.models import Audio, User, UserAudioBehavior, Words


class User_Admin(admin.ModelAdmin):
    list_display = ('userId', 'userCorrectRate')
admin.site.register(User, User_Admin)


class Audio_Admin(admin.ModelAdmin):
    list_display = ('audioTitle', 'audioType', 'audioDate', 'audioId')
admin.site.register(Audio, Audio_Admin)


class UserAudioBehavior_Admin(admin.ModelAdmin):
    list_display = ('audioId', 'userId', 'audioCorrectRate')
admin.site.register(UserAudioBehavior, UserAudioBehavior_Admin)


class Words_Admin(admin.ModelAdmin):
    list_display = ('word', 'wordId')
admin.site.register(Words, Words_Admin)