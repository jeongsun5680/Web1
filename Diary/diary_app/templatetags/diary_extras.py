from django import template
from django.template.defaultfilters import stringfilter

register = template . Library ()

#템플릿 사용자 정의 필터
#아래꺼 사용 안하게 됐음.. ㅎㅎ 공부용으로 두자 ㅎㅎ
@register . filter
@stringfilter
def myfilter ( value ):
    print("before : "+value)
    value = value.replace("'","\\")
    value = value.replace('"','\\')
    print("after : "+value)
    return value