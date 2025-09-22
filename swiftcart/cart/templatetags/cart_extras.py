from django import template

register = template.Library()

@register.filter
def cart_total(items):
    """
    Calculate total price for a queryset of CartItems
    """
    total = 0
    for item in items:
        total += item.product.pPrice * item.quantity
    return total
