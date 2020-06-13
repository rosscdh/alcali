from django.contrib import admin
from . models import (FindJobManager,
                      Jids,
                      SaltReturns,
                      SaltEvents,
                      Functions,
                      JobTemplate,
                      Minions,
                      Keys,
                      MinionsCustomFields,
                      Schedule,
                      UserSettings,
                      Conformity,)



@admin.register(FindJobManager)
class FindJobManagerAdmin(admin.ModelAdmin):
    pass

@admin.register(Jids)
class JidsAdmin(admin.ModelAdmin):
    pass

@admin.register(SaltReturns)
class SaltReturnsAdmin(admin.ModelAdmin):
    pass

@admin.register(SaltEvents)
class SaltEventsAdmin(admin.ModelAdmin):
    pass

@admin.register(Functions)
class FunctionsAdmin(admin.ModelAdmin):
    pass

@admin.register(JobTemplate)
class JobTemplateAdmin(admin.ModelAdmin):
    pass

@admin.register(Minions)
class MinionsAdmin(admin.ModelAdmin):
    pass

@admin.register(Keys)
class KeysAdmin(admin.ModelAdmin):
    pass

@admin.register(MinionsCustomFields)
class MinionsCustomFieldsAdmin(admin.ModelAdmin):
    pass

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    pass

@admin.register(UserSettings)
class UserSettingsAdmin(admin.ModelAdmin):
    pass

@admin.register(Conformity)
class ConformityAdmin(admin.ModelAdmin):
    pass