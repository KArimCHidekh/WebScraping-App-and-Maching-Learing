from django.contrib import admin
from django.core import management
from django.shortcuts import redirect
# Register your models here.
from karim.models import Article, django_site

#admin.site.register(Question)
#admin.site.register(Choice)
admin.site.register(Article)






class MovieAdmin(admin.ModelAdmin):
    #@admin.site.register_view('import_movies_from_url', 'Import Movies from URL')
    def import_movies_from_url(request):
        print('import movies here')
        try:
            management.call_command('elwaten')
            message = 'successfully imported data from URL'

        except Exception as ex:
            message = 'Error importing from data from URL {}'.format(str(ex))

        admin.ModelAdmin.message_user(Article, request, message)
        return redirect('admin:index')


#admin.site.register(Article, MovieAdmin)