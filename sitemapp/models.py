from django.db import models


class TimeFields(models.Model):
    mobile_list_time = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    article_list_time = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    common_list_time = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    earwear_list_time = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    headphone_list_time = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)


