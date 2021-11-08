from django.contrib import admin
# from navbar1.models import register_table

# Register your models here.
from navbar1.models import detail_matches,update_matches,submitted_detail,submitted_ans,results_update_final





admin.site.register(detail_matches)
admin.site.register(update_matches)
admin.site.register(submitted_detail)
admin.site.register(submitted_ans)
admin.site.register(results_update_final)
