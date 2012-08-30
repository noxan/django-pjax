def _pjaxify_template_var(template_var):
    if isinstance(template_var, (list, tuple)):
        template_var = type(template_var)(_pjaxify_template_name(name) for name in template_var)
    elif isinstance(template_var, basestring):
        template_var = _pjaxify_template_name(template_var)
    return template_var


def _pjaxify_template_name(name):
    if "." in name:
        name = "%s-pjax.%s" % tuple(name.rsplit('.', 1))
    else:
        name += "-pjax"
    return name

