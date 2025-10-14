from django import template

register = template.Library()

@register.filter
def get_attr(obj, field):
    return getattr(obj, field)

@register.filter
def format_value(value):
    
    if value is None:
        return ""
    if isinstance(value, bool):
        return "✅" if value else "❌"
    if hasattr(value, "strftime"):  # Date or DateTime
        return value.strftime("%Y-%m-%d")
    if isinstance(value, float):
        return f"{value:.2f}"
    return str(value)