from rest_framework import serializers


class CgroupSerializer(serializers.Serializer):
    name = serializers.ReadOnlyField()
    cpu_limit = serializers.ReadOnlyField()
    memory_limit = serializers.ReadOnlyField()
    pids = serializers.ReadOnlyField()