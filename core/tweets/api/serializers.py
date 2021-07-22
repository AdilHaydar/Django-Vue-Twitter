from ..models import Tweet #File

from rest_framework import serializers

# class FileSerializer(serializers.ModelSerializer):
#     #file = serializers.FileField()
#     #or file = serializers.ListField(child=serializers.FileField())
#     #https://stackoverflow.com/questions/39645410/how-to-upload-multiple-files-in-django-rest-framework mutli file upload işine şuaradan bir bak
#     class Meta:
#         model = File
#         fields = ('file',)

class TweetSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only = True)
    #files = FileSerializer(many=True, required=False, read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    file = serializers.FileField(required=False)

    class Meta:
        model = Tweet
        fields = [
            'id',
            'user',
            'content',
            'likes',
            'file',
        ]

    def get_likes(self, obj):
        return obj.likes.count()