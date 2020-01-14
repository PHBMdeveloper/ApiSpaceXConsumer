from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import ProximosLancamento, LancamentosPassado


@admin.register(ProximosLancamento, LancamentosPassado)
class PersonAdmin(ImportExportModelAdmin):
    list_display = [
        field.attname for field in LancamentosPassado._meta.fields]
    readonly_fields = [
        field.attname for field in LancamentosPassado._meta.fields]
