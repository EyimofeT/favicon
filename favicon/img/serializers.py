from rest_framework import serializers
from .models import ImageUpload



class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUpload
        # fields = ('first_name','last_name','username','email','password')
        fields = '__all__'
        # extra_kwargs = {
        #     'password':{'write_only': True}
        # }