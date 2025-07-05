from rest_framework import serializers
from django.utils.text import slugify

from blog.models import Post
from core.models import Company
from core.serializers.user_serializer import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(read_only=True)
    company_id = serializers.IntegerField(read_only=True)
    created_by = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'company_id',
            'title',
            'slug',
            'content',
            'created_at',
            'created_by',
            'updated_at',
            'updated_by',
        )

    def create(self, validated_data):
        company_pk= self.context['company_pk']
        current_user = self.context['user']
        validated_data['slug'] = slugify(validated_data['title'])
        return Post.objects.create(**validated_data, company_id=company_pk, created_by=current_user, updated_by=current_user)


    def update(self, instance, validated_data):
        company_pk = self.context['company_pk']
        current_user = self.context['user']
        validated_data['slug'] = slugify(validated_data['title'])
        instance.title = validated_data.get('title')
        instance.slug = validated_data['slug']
        instance.content = validated_data.get('content')
        instance.save()
        return instance
