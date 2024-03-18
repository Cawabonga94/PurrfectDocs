from cat.mad_hatter.decorators import hook

from .parsers import DOCXParser


@hook
def rabbithole_instantiates_parsers(file_handlers: dict, cat) -> dict:

    new_handlers = {
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document": DOCXParser(),
        "application/msword": DOCXParser(),
    }
      
    file_handlers = file_handlers | new_handlers
    return file_handlers