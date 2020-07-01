from django import forms
import requests
import re
from .models import Entity
# noinspection PyUnresolvedReferences
from xml.dom import minidom

# noinspection -> chyba v současné verzi PyCharm


class RecordForm(forms.ModelForm):
    class Meta:
        model = Entity
        fields = '__all__'

    def clean_ico(self):
        ico = self.cleaned_data['ico']

        if not re.match(r"\d{8}", ico):
            raise forms.ValidationError("ICO has to be in 8 digits format!")

        response = requests.get("https://wwwinfo.mfcr.cz/cgi-bin/ares/darv_std.cgi?ico={}".format(ico))
        if response.ok:
            tree = minidom.parseString(response.content)
            el = tree.getElementsByTagName('are:Pocet_zaznamu')
            if not (len(el) > 0 and int(el[0].firstChild.nodeValue) > 0):
                raise forms.ValidationError("Subject does not exist!")
        else:
            raise forms.ValidationError("Connection to mfcr API cannot be established!")

        return ico



