from rest_framework import serializers
from blog.models import Essay, Tag, Comment
from user.models import Profile

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class EssaySerializers(serializers.ModelSerializer):
    owner = ProfileSerializers(many=False)
    tag = TagSerializers(many=True)
    comment = serializers.SerializerMethodField()
    class Meta:
        model = Essay
        fields = '__all__'

    def get_comment(self, obj):

        comment = obj.comment_set.all()
        serializers = CommentSerializers(comment, many=True)

        return serializers.data