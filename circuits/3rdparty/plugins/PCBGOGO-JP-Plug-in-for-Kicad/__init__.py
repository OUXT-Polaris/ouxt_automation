try:
    from .plugin import PCBGOGOPlugin
    plugin = PCBGOGOPlugin()
    plugin.register()
except Exception as e:
    import logging
    root = logging.getLogger()
    root.debug(repr(e))
