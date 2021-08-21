import random
from django.conf                import settings
from rest_framework             import status
from rest_framework.response    import Response
from rest_framework.views       import APIView
from .models                    import ColorSpace


class ColorSpaceAPIView(APIView):

    def get(self, request, *args, **kwargs):
        color_ids = list(ColorSpace.objects.all().values_list('id', flat=True))
        result = []
        if not color_ids:
            return Response(result, status=status.HTTP_200_OK)
        for i in range(settings.DEFAULT_SWATCHES_SET):
            color = ColorSpace.objects.get(id=random.choice(color_ids))
            res = {'type': color.name}
            for r in color.ranges.all():
                res[r.name] = '%(value)s%(suffix)s' % {'value': random.randint(r.range_start, r.range_stop), 'suffix': r.suffix}
            result.append(res)
        return Response(result, status=status.HTTP_200_OK)
