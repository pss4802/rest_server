from .models import Member
from rest_framework import serializers, viewsets



import logging

class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = '__all__'

class MemberViewSet(viewsets.ModelViewSet):
#settings.py 파일에서 설정된 로거를 취득함

    logger = logging.getLogger('filelogger')
    #age = self.kwargs['age']
    queryset = Member.objects.all()
    logger.debug('queryset: '+ repr(queryset.first().name) + ' / ' + str(queryset.query))
    serializer_class = MemberSerializer

