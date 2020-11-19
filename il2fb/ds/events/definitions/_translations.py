from pathlib import Path

from verboselib import Translations


__here__ = Path(__file__).absolute().parent


translations = Translations(
  domain="il2fb-ds-events",
  locale_dir_path=(__here__ / "locale"),
)


gettext       = translations.gettext
gettext_lazy  = translations.gettext_lazy

pgettext      = translations.pgettext
pgettext_lazy = translations.pgettext_lazy
