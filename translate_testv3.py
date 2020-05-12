#from google.cloud import translate
from google.cloud import translate_v3beta1 as translate
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/root/gcp_credentials/My_First_Project-3199b3086600.json"

#def sample_translate_text(text, target_language, project_id):
#    """
#    Translating Text
#
#    Args:
#      text The content to translate in string format
#      target_language Required. The BCP-47 language code to use for translation.
#    """

client = translate.TranslationServiceClient()

# TODO(developer): Uncomment and set the following variables
text = "I'm a human glacier, wrist full of frozen water"
target_language = 'ja-JP'
project_id = 'fluted-arcadia-270206'
contents = [text]
parent = client.location_path(project_id, "global")

response = client.translate_text(
    parent=parent,
    contents=contents,
    mime_type='text/plain',  # mime types: text/plain, text/html
    source_language_code='en-US',
    target_language_code=target_language)
# Display the translation for each input text provided
for translation in response.translations:
    print(format(translation.translated_text))
