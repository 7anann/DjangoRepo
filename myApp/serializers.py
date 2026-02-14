from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.Serializer):
    # You must redefine every field manually
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    content = serializers.CharField(style={"base_template": "textarea.html"})
    author_email = serializers.EmailField()

    # You MUST write the logic to save/update data manually
    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.save()
        return instance


class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "content", "author_email", "created_at"]
        # DRF automatically knows how to create() and update()!

        def validate_title(self, value):
            if "Django" not in value:
                raise serializers.ValidationError("Title must mention Django!")
            return value
