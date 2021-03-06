from rest_framework import serializers

from openbook_common.models import Emoji, EmojiGroup


class EmojiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emoji

        fields = (
            'id',
            'keyword',
            'image',
            'created',
            'order',
        )


class EmojiGroupSerializer(serializers.ModelSerializer):
    emojis = serializers.SerializerMethodField()

    def get_emojis(self, obj):
        emojis = obj.emojis.all().order_by('order')

        request = self.context['request']
        return EmojiSerializer(emojis, many=True, context={'request': request}).data

    class Meta:
        model = EmojiGroup

        fields = (
            'id',
            'keyword',
            'color',
            'created',
            'order',
            'emojis',
        )
